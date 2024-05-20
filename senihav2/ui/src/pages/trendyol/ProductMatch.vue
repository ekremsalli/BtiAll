<template>
  <q-page padding>
    <q-toolbar class="bg-grey-3 text-black">
      <q-toolbar-title>
        Ürün eşleme
      </q-toolbar-title>
      <q-space />

      <q-btn :loading="loading" @click="show_excel_dialog" flat rounde dense icon="fa fa-file-excel">
        <q-tooltip>
          Excel'den aktar
        </q-tooltip>
      </q-btn>

      <q-btn :loading="loading" @click="new_record" flat round dense icon="fa fa-plus">
        <q-tooltip>
          Yeni kayıt ekle
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
      selection="multiple"
      :pagination.sync="pagination"
      binary-state-sort
      :visible-columns="visible"
      :filter="search"
      :selected.sync="selected"
      no-data-label="Kayıt bulunamadı!"
      @request="load"
      @row-click="update_record"
      >

      <template v-slot:top>
        <div class="col-2">
          <q-btn @click="delete_confirm" size="sm" class="q-mt-sm" :disabled="selected.length == 0">Seçilen kayıtları sil</q-btn>
        </div>
        <div class="col-7">
          <q-input dense v-model="search">
            <template #append>
              <q-icon name="search" />
            </template>
          </q-input>
        </div>
        <div class="col-2 offset-1">
          <q-select
            v-model="visible"
            hide-details
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
        </div>
      </template>

      <template #body-cell-erp_code="props">
        <q-td :props="props">
          <template v-if="products[props.row.erp_code] !== undefined && products[props.row.erp_code] == 0">
            {{ props.row.erp_code }}
          </template>
          <template v-else>
            <span class='text-negative'>
              <q-icon name="fa fa-exclamation-triangle">
                <q-tooltip>
                  Geçersiz veya kullanım dışı malzeme!
                </q-tooltip>
              </q-icon>
              {{ props.row.erp_code }}
            </span>
          </template>
        </q-td>
      </template>
    </q-table>

    <q-dialog v-model="dialog" transition-show="rotate" transition-hide="rotate">
      <q-card style="width: 700px; max-width: 80vw;">
        <q-card-section class="q-mb-none q-pb-none">
          <span v-if="record.id">Ürün eşleme güncelleme</span><span v-else>Yeni ürün eşleme</span>
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

    <q-dialog v-model="confirm" persistent transition-show="rotate" transition-hide="rotate">
      <q-card >
        <q-card-section class="row items-center">
          <q-avatar icon="delete" color="black" text-color="white" />
          <span class="q-ml-sm">Bu ürün silinmek üzere, devam edilsin mi?</span>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="İptal" color="black" v-close-popup />
          <q-btn @click="delete_record" flat label="Evet" color="black" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>

    <q-dialog :loading="bulk_inserting" v-model="excel" persistent>
      <q-card style="width: 600px; max-width: 60vw;">
        <q-card-section>
          <div class="text-subtitle1">Excel'den aktar</div>
        </q-card-section>
        <div class="q-mx-md">
          <div class="row">
            <div class="col-12">
              <q-file :disable="bulk_inserting" :loading="reading" label="Dosya seçimi" accept=".xls, .xlsx" outlined v-model="file">
                <template v-slot:prepend>
                  <q-icon name="attach_file" />
                </template>
              </q-file>
            </div>
          </div>

          <template v-if="results.length > 0">
            Aktarım
            <q-table
              :data="results"
              />
          </template>

          <template v-if="excel_records.length > 0 && results.length == 0">
            <br />
            * Alanları eşleyin
            <div class="row">
              <div class="col-12">
                <q-select
                  :disable="bulk_inserting"
                  label="ERP Kodu"
                  v-model="record_keys.erp_code"
                  :options="excel_headers"
                  />
              </div>
            </div>

            <div class="row">
              <div class="col-12">
                <q-select
                  :disable="bulk_inserting"
                  label="Trendyol barkod"
                  v-model="record_keys.barcode"
                  :options="excel_headers"
                  />
              </div>
            </div>

            <div class="row">
              <div class="col-12">
                <q-select
                  :disable="bulk_inserting"
                  label="Trendyol ürün kodu"
                  v-model="record_keys.product_code"
                  :options="excel_headers"
                  />
              </div>
            </div>

            <div class="row">
              <div class="col-12">
                <q-select
                  :disable="bulk_inserting"
                  label="Trendyol merchant sku"
                  v-model="record_keys.merchant_sku"
                  :options="excel_headers"
                  />
              </div>
            </div>

          </template>
        </div>

        <q-card-actions align="right">
          <template v-if="bulk_inserting">
            <q-circular-progress
              indeterminate
              size="32px"
              :thickness="0.2"
              color="black"
              center-color="grey-8"
              track-color="transparent"
              class="q-ma-md"
            />
          </template>
          <template v-else>
            <q-btn :loading="reading" @click="reset_excel_dialog" flat label="Sıfırla" color="indigo" />
            <q-btn :loading="reading" v-if="excel_records.length == 0 && file" @click="import_excel" flat label="Oku" color="black" />
            <q-btn :loading="reading" v-if="excel_records.length > 0" @click="process_excel" flat label="Oluştur" color="primary" />
            <q-btn :loading="reading" flat label="İptal" color="black" v-close-popup />
          </template>
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
  name: 'ProductMatch',
  mixins: [common],
  data () {
    return {
      loading: false,
      items: [],
      cols: [
        { field: 'id', label: 'ID', name: 'id', sortable: true, align: 'left' },
        { field: 'erp_code', label: 'ERP ürün kodu', name: 'erp_code', sortable: true, align: 'left' },
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
      visible: ['erp_code', 'barcode', 'product_code', 'merchant_sku', 'created'],
      active: null,
      dialog: false,
      record: {},
      search: "",
      selected: [],
      products: {},
      confirm: false,
      excel: false,
      file: null,
      excel_records: [],
      reading: false,
      record_keys: {
        'erp_code': '',
        'barcode': '',
        'product_code': '',
        'merchant_sku': ''
      },
      bulk_inserting: false,
      results: []
    }
  },
  computed: {
    excel_headers () {
      if (this.excel_records && this.excel_records.length > 0) return Object.keys(this.excel_records[0])
      return []
    }
  },
  mounted () {
    this.load({ pagination: this.pagination })
  },
  methods: {
    process_excel(){
      // alanları set et!
      let self = this
      this.$set(this, 'bulk_inserting', true)
      let rk = this.record_keys
      let items = []
      if (rk.erp_code && (rk.barcode || rk.product_code || rk.merchant_sku)){
        this.excel_records.forEach(function(item){
          let temp = {
            'erp_code': item[rk.erp_code]
          }
          if (item[rk.barcode]) temp['barcode'] = item[rk.barcode]
          if (item[rk.product_code]) temp['product_code'] = item[rk.product_code]
          if (item[rk.merchant_sku]) temp['merchant_sku'] = item[rk.merchant_sku]

          items.push(temp)
        })
        Service.post('trendyol/product_match', items)
          .then((response) => {
            if (response.data) {
              self.$set(self, 'results', response.data.results)
            }else {
              self.um('Bilinmeyen bir hata oluştu!')
            }
          })
          .catch((error) => {
            console.log("error", error.response)
            self.um('Bilinmeyen bir hata oluştu! ' + error)
          })
          .finally(() => {
            self.$set(self, 'bulk_inserting', false)
          })

      } else {
        this.um('Lütfen erp alanını ve eşleşme için en az bir Trendyol alanı seçin!')
        self.$set(self, 'bulk_inserting', false)
      }
    },
    show_excel_dialog(){
      this.$set(this, "excel", true)
    },
    reset_excel_dialog(){
      this.$set(this, "excel_records", [])
      this.$set(this, "file", null)
      this.$set(this, 'record_keys', {
        'erp_code': '',
        'barcode': '',
        'product_code': '',
        'merchant_sku': ''
      })
      this.$set(this, 'bulk_inserting', false)
      this.$set(this, 'results', [])
    },
    import_excel() {
      let self = this

      var reader = new FileReader();
      console.log('importing...', this.file)
      this.$set(this, 'reading', true)
      reader.onload = function(e) {
        console.log('file ok!')
        var data = new Uint8Array(e.target.result);
        var workbook = XLSX.read(data, {type: 'array'});
        for (const wb in workbook.Sheets) {
          self.$set(self, 'excel_records', XLSX.utils.sheet_to_json(workbook.Sheets[wb]))
          break
        }
        self.$set(self, 'reading', false)
      };
      reader.readAsArrayBuffer(this.file);
    },
    save(){
      const self = this
      this.$refs.form.validate().then(success => {
        Service.post('trendyol/product_match', self.record)
          .then((response) => {
            if (response.data.status) {
              self.bm(response.data.description)
              self.$set(self, "record", {})
              self.$set(self, "dialog", false)
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
    update_record(){
      // not implemented!
    },
    delete_confirm(){
      this.confirm = true
    },
    delete_record(){
      let self = this
      let records = this.selected.map(o => o.id)
      this.$set(this, 'loading', true)
      Service.delete('trendyol/product_match', {records: records })
        .then((response) => {
          if (response.data.status) {
            self.load({ pagination: self.pagination })
            self.bm('Başarıyla silindi!')
          }else {
            self.um(response.data.description)
          }
        })
        .catch((error) => {
          self.um('Bilinmeyen bir hata oluştu! ' + error)
          self.$set(self, 'loading', false)
        })
    },
    new_record(){
      this.$set(this, 'record', {})
      this.$set(this, 'dialog', true)
    },
    load (sett) {
      let self = this
      this.$set(this, 'loading', true)
      this.$set(this, 'items', [])
      this.$set(this, 'products', {})
      Service.get('trendyol/product_match')
        .then((response) => {
          self.$set(self, 'items', response.data.results)
          response.data.items.forEach(function(item){
            self.$set(self.products, item.code, item.active)
          })
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
