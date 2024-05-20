<template>
  <q-page padding>
    <q-toolbar class="bg-grey-3 text-black">
      <q-toolbar-title>
        Eşleşmeyen ürünler
      </q-toolbar-title>
      <q-space />

      <q-btn :loading="loading" @click="export_to_excel" flat rounde dense icon="fa fa-file-excel">
        <q-tooltip>
          Excel'e aktar
        </q-tooltip>
      </q-btn>

      <q-btn :loading="loading" @click="load({pagination: pagination})" flat round dense icon="fas fa-sync-alt">
        <q-tooltip>
          Yenile
        </q-tooltip>
      </q-btn>
    </q-toolbar>

    <q-table
      :data="items"
      :columns="cols"
      dense
      row-key="id"
      :loading="loading"
      :pagination.sync="pagination"
      binary-state-sort
      :visible-columns="visible"
      :filter="search"
      no-data-label="Kayıt bulunamadı!"
      @request="load"
      >

      <template v-slot:top>
        <q-input v-model="search">
          <template #append>
            <q-icon name="search" />
          </template>
        </q-input>

        <q-space />
        <q-select
          v-model="visible"
          multiple
          outlined
          dense
          options-dense
          :display-value="$q.lang.table.columns"
          emit-value
          map-options
          :options="cols"
          option-value="name"
          options-cover
          style="min-width: 150px">
        </q-select>
      </template>

      <template #body-cell-order="props">
        <q-td :props="props">
          <span @click="display_order(props.row)" style="cursor:pointer;text-decoration:underline" class="text-blue">{{ props.row.order }}</span>
        </q-td>
      </template>

      <template #body-cell-barcode="props">
        <q-td :props="props">
          {{ props.row.barcode }}
          <q-btn @click="display_match(props.row)" size="6px" round icon="add" outline color="primary" />
        </q-td>
      </template>

    </q-table>

    <q-dialog v-model="dialog" transition-show="rotate" transition-hide="rotate">
      <q-card class="q-ma-sm">
        <q-card-section class="row items-center">
          Sipariş detayları
        </q-card-section>
        <Order v-if="active" :item="active" />
        <q-card-actions align="right">
          <q-btn flat label="Kapat" color="black" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>

    <q-dialog v-model="match" transition-show="rotate" transition-hide="rotate">
      <q-card style="width: 700px; max-width: 80vw;">
        <q-card-section class="q-mb-none q-pb-none">
          Yeni ürün eşleme
        </q-card-section>

        <q-card-section>
          <q-form ref="form" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false">
            <q-input
              v-model="record.erp_code"
              label="ERP kodu"
              :rules="[ val => val && val.length > 0 || 'Lütfen ERP kodunu belirtin!']"
            />
            <q-input
              v-model="record.barcode"
              label="Trendyol barkod"
            />
            <q-input
              v-model="record.product_code"
              label="Trendyol ürün kodu"
            />
            <q-input
              v-model="record.merchant_sku"
              label="Trendyol merchant sku"
            />
          </q-form>


        </q-card-section>
        <q-card-actions align="right">
          <q-btn @click="save()" flat label="Tamam" color="black" />
          <q-btn flat label="İptal" color="black" v-close-popup />

        </q-card-actions>

      </q-card>
    </q-dialog>

  </q-page>
</template>

<script>
import Service from 'boot/service'
import { common } from 'src/mixins/common'
import { date } from 'quasar'
import XLSX from 'xlsx'


export default {
  name: 'Mismatch',
  mixins: [common],
  components: {
    Order: () => import('./Order.vue')
  },
  data () {
    return {
      loading: false,
      items: [],
      cols: [
        { field: 'id', label: 'ID', name: 'id', sortable: true, align: 'left' },
        { field: 'order', label: 'Sipariş', name: 'order', sortable: true, align: 'left' },
        { field: 'barcode', label: 'Barkod', name: 'barcode', sortable: true, align: 'left' },
        { field: 'product_code', label: 'Trendyol ürün kodu', name: 'product_code', sortable: true, align: 'left' },
        { field: 'merchant_sku', label: 'Trendyol merchant sku', name: 'merchant_sku', sortable: true, align: 'left' },

        {
            field: 'created',
            label: 'Tarih',
            name: 'created',
            sortable: true,
            align: 'left',
            format: (val, row) => date.formatDate(val, 'DD-MM-YY HH:mm:ss')
        }
      ],
      pagination: {
        rowsPerPage: 25
      },
      visible: ['order', 'barcode', 'product_code', 'merchant_sku', 'created'],
      active: null,
      dialog: false,
      search: "",
      match: false,
      record: {}
    }
  },
  mounted () {
    this.load({ pagination: this.pagination })
  },
  methods: {
    export_to_excel() {
      const name = 'Eşleşmeyen ürünler.xlsx'
      let data = this.items.map(o => ({erp_code: '', barcode: o.barcode, product_code: o.product_code, merchant_sku: o.merchant_sku}))
  		const ws = XLSX.utils.json_to_sheet(data)
  		const wb = XLSX.utils.book_new()
  		XLSX.utils.book_append_sheet(wb, ws, '')
  		XLSX.writeFile(wb, name)
    },
    save(){
      const self = this
      this.$refs.form.validate().then(success => {
        Service.post('trendyol/product_match', self.record)
          .then((response) => {
            if (response.data.status) {
              self.bm(response.data.description)
              self.$set(self, "record", {})
              self.$set(self, "match", false)
              self.load({ pagination: this.pagination })
            }else {
              self.um(response.data.description)
            }
          })
          .catch((error) => {
            self.um('Bilinmeyen bir hata oluştu! ' + error)
          })
      })
    },
    display_match(row) {
      this.$set(this, "record", {
        barcode: row.barcode,
        product_code: row.product_code,
        merchant_sku: row.merchant_sku
      })
      this.$set(this, "match", true)
    },
    display_order(row) {
      this.$set(this, "active", JSON.parse(row.body))
      this.$set(this, "dialog", true)
    },
    load (sett) {
      let self = this
      this.$set(this, 'loading', true)
      this.$set(this, 'items', [])
      Service.get('trendyol/mismatch')
        .then((response) => {
          self.$set(self, 'items', response.data.results)
        })
        .catch((error) => {
          this.um('Bir hata oluştu!' + error)
        })
        .finally(() => {
          this.$set(this, 'loading', false)
        })
    }
  }
}
</script>
