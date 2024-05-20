<template>
  <q-page padding>
    <q-toolbar class="bg-grey-3 text-black">
      <q-toolbar-title>
        Sipariş geçmişi
      </q-toolbar-title>
      <q-space />
      <q-btn :loading="loading" @click="load({pagination: pagination})" flat round dense icon="fas fa-sync-alt">
        <q-tooltip>
          Yenile
        </q-tooltip>
      </q-btn>
    </q-toolbar>

    <q-table
      :data="data"
      :columns="cols"
      dense
      row-key="id"
      :pagination.sync="pagination"
      :loading="loading"
      binary-state-sort
      :visible-columns="visible"
      no-data-label="Sipariş bulunamadı!"
      :rows-per-page-options="[]"
      @request="load"
      >

      <template v-slot:top>
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

      <template #body-cell-order-number="props">
        <q-td :props="props">
          <span @click="display_order(props.row)" style="cursor:pointer;text-decoration:underline" class="text-blue">{{ props.row.order_number }}</span>
        </q-td>
      </template>

      <template #body-cell-internal_ref="props">
        <q-td :props="props">
          <template v-if="props.row.internal_ref">
            <span class='text-positive'>Aktarıldı ({{ props.row.internal_ref }})</span>
          </template>
          <template v-else>
            <span class='text-negative'>Aktarılamadı</span>
          </template>
        </q-td>
      </template>

      <template #body-cell-islem="props">
        <q-td :props="props">
          <q-btn v-if="!props.row.internal_ref" :disabled="transfers.includes(props.row.pk)" outline @click="resend(props.row)" size="sm" no-caps color="primary" icon="send">Yeniden dene</q-btn>
        </q-td>
      </template>

    </q-table>


    <q-dialog v-model="detail" persistent transition-show="rotate" transition-hide="rotate">
      <q-card class="q-ma-sm">
        <q-card-section class="row items-center">
          Sipariş detayları
        </q-card-section>
        <Order v-if="item" :item="item" />
        <q-card-actions align="right">
          <q-btn flat label="Kapat" color="black" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>

  </q-page>
</template>

<script>
import Service from 'boot/service'
import { common } from 'src/mixins/common'
import { date } from 'quasar'


export default {
  name: 'Log',
  mixins: [common],
  components: {
    'Order': () => import('./Order.vue')
  },
  data () {
    return {
      loading: false,
      data: [],
      cols: [
        { field: 'pk', label: 'ID', name: 'pk', sortable: false, align: 'left' },
        { field: 'order_number', label: 'Sipariş numarası', name: 'order_number', sortable: false, align: 'left' },
        {
            field: 'internal_ref',
            label: 'Aktarım',
            name: 'internal_ref',
            sortable: false,
            align: 'left'
        },
        {
            field: 'created',
            label: 'Tarih',
            name: 'created',
            sortable: true,
            align: 'left',
            format: (val, row) => date.formatDate(val, 'DD/MM/YY HH:mm:ss')
        },
        { field: 'islem', name: 'islem', sortable: false, align: 'right'}
      ],
      visible: ['order_number', 'internal_ref', 'created', 'islem'],
      pagination: {
        sortBy: 'desc',
        descending: false,
        page: 1,
        rowsPerPage: 3,
        rowsNumber: 10
      },
      detail: false,
      item: null,
      log: null,
      transfers: []
    }
  },
  mounted () {
    this.load({ pagination: this.pagination })
  },
  methods: {
    display_order(item) {
      this.$set(this, "log", item)
      this.$set(this, "item", JSON.parse(item.raw))
      this.$set(this, "detail", true)
    },
    resend(item) {
      this.transfers.push(item.pk)
      Service.post('trendyol/transfer', { id: item.pk })
      .then((response) => {
        if (response.data.status) {
          this.bm('Başarıyla aktarıldı!')
        } else {
          if (response.data.description) this.um(response.data.description)
          else this.um('Bilinmeyen bir hata oluştu!')
        }
      })
      .catch((error) => {
        this.um('Bir hata oluştu!' + error)
      })
      .finally(() => {
        this.$set(this, 'loading', false)
      })
    },
    load (sett) {
      let self = this
      this.$set(this, 'loading', true)
      this.$set(this, 'data', [])
      this.$set(this, 'transfers', [])
      const params = {
        page: sett.pagination.page,
        page_size: sett.pagination.rowsPerPage,
        ordering: sett.pagination.descending ? ('-' + sett.pagination.sortBy) : sett.pagination.sortBy
      }
      Service.get('trendyol/log', { params: params })
        .then((response) => {
          self.$set(self, 'data', response.data.results)
          self.pagination.rowsNumber = response.data.total
          self.pagination.page = response.data.current
          self.pagination.rowsPerPage = response.data.page_size
          self.pagination.descending = response.data.descending
          self.pagination.sortBy = response.data.ordering
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
