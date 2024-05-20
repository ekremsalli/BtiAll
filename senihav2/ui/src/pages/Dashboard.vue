<template>
  <q-page padding>
    <q-toolbar class="bg-grey-3 text-black">
      <q-toolbar-title>
        Entegrasyon
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
      no-data-label="Kayıt bulunamadı!"
      :rows-per-page-options="[]"
      @request="load"
      @row-click="details"
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

      <template #body-cell-related="props">
        <q-td :props="props">
          {{ props.row.related_object }} <span v-if="props.row.internal_ref">({{ props.row.internal_ref }})</span>
        </q-td>
      </template>
    </q-table>

    <q-dialog v-model="dialog" transition-show="rotate" transition-hide="rotate">
      <q-card style="width: 700px; max-width: 80vw;" v-if="active">
        <q-card-section>
          <div class="text-subtitle1">{{ active_created }} tarihli <strong>{{ active.id }}</strong> nolu istek detayı</div>
        </q-card-section>


        <q-card-section style="height:60vh" class="scroll">
          <q-tabs v-model="tab" inline-label :breakpoint="0" align="justify">
            <q-tab name="bilgi" label="Bilgi" />
            <q-tab name="veri" label="Veri" />
            <q-tab name="istek" label="İstek" />
            <q-tab name="yanit" label="Yanıt" />
            <q-tab name="hata" label="Hata" />

          </q-tabs>

          <q-tab-panels v-model="tab" animated>
            <q-tab-panel name="bilgi">
              <q-list dense>
                <q-item :key="item.label" v-for="item in detail">
                  <q-item-section>{{ item.label }}</q-item-section>
                  <q-item-section>{{ active[item.prop] }}</q-item-section>
                </q-item>
              </q-list>
            </q-tab-panel>
            <q-tab-panel name="veri">
              <pre>{{ active.data | pretty }}</pre>
            </q-tab-panel>
            <q-tab-panel name="istek">
              <pre>{{ active.request | pretty }}</pre>

            </q-tab-panel>
            <q-tab-panel name="yanit">
              <pre>{{ active.response | pretty }}</pre>
            </q-tab-panel>
            <q-tab-panel name="hata">
              <div v-if="active.exception">{{ active.exception }}</div>
              <div class='text-center' v-else>Hata yok!</div>
            </q-tab-panel>


          </q-tab-panels>
          </q-tabs>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="Tamam" color="black" v-close-popup />
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
  name: 'Dashboard',
  mixins: [common],
  computed: {
    active_created(){
      if (this.active) return date.formatDate(this.active.created, 'DD MMMM YYYY HH:mm:ss')
      return ''
    }
  },
  data () {
    return {
      loading: false,
      data: [],
      cols: [
        { field: 'id', label: 'ID', name: 'id', sortable: false, align: 'left' },
        { field: 'company', label: 'Firma', name: 'company', sortable: false, align: 'left' },
        { field: 'period', label: 'Dönem', name: 'period', sortable: false, align: 'left' },
        { field: 'user', label: 'Kullanıcı', name: 'user', sortable: false, align: 'left' },
        {
            field: 'created',
            label: 'Tarih',
            name: 'created',
            sortable: true,
            align: 'left',
            format: (val, row) => date.formatDate(val, 'DD-MM-YY HH:mm:ss')
        },
        { field: 'handler', label: 'İşleyici', name: 'handler', sortable: false, align: 'left' },
        { field: 'method', label: 'Yöntem', name: 'method', sortable: false, align: 'left' },
        { field: 'related', label: 'İlgili obje', name: 'related', sortable: false, align: 'left' },
        { field: 'took', label: 'Süre', name: 'took', sortable: false, align: 'left', format: (val, row) => `${val} sn` },
        { field: 'success', label: 'Durum', name: 'success', sortable: false, align: 'left', format: (val, row) => val == true ? 'Ok' : 'Hata' },

      ],
      visible: ['id', 'company', 'period', 'user', 'created', 'handler', 'method', 'related', 'took', 'success'],
      pagination: {
        sortBy: 'desc',
        descending: false,
        page: 1,
        rowsPerPage: 3,
        rowsNumber: 10
      },
      active: null,
      dialog: false,
      tab: 'bilgi',
      detail: [
        { label: 'ID', prop: 'id'},
        { label: 'Firma', prop: 'company'},
        { label: 'Dönem', prop: 'period'},
        { label: 'Yöntem', prop: 'method'},
        { label: 'Uç nokta', prop: 'endpoint'},
        { label: 'Hata kodu', prop: 'error_code'},
        { label: 'İşleyici', prop: 'handler'},
        { label: 'Obje', prop: 'related_object'},
        { label: 'Referans', prop: 'internal_ref'},
        { label: 'PID', prop: 'pid'},
        { label: 'Süre', prop: 'took'},
        { label: 'Önceki kayıt', prop: 'prev_flow'},
        { label: 'Sonraki kayıt', prop: 'next_flow'},
      ]
    }
  },
  mounted () {
    this.load({ pagination: this.pagination })
  },
  methods: {
    details(event, row, index) {
      this.$set(this, "tab", "bilgi")
      this.$set(this, "dialog", true)
      this.$set(this, "active", row)
    },
    load (sett) {
      let self = this
      this.$set(this, 'loading', true)
      this.$set(this, 'data', [])
      const params = {
        page: sett.pagination.page,
        page_size: sett.pagination.rowsPerPage,
        ordering: sett.pagination.descending ? ('-' + sett.pagination.sortBy) : sett.pagination.sortBy
      }
      Service.get('integration', { params: params })
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
