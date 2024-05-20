<template>
  <q-page padding>
    <q-toolbar class="bg-grey-3 text-black">
      <q-toolbar-title>
        Veritabanları
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
      no-data-label="Veritabanı bulunamadı!"
      :rows-per-page-options="[]"
      @request="load"
      >
      <template #body-cell-is_active="props">
          <q-toggle @input="save(props.row)" v-model="props.row.is_active" />
      </template>

      <template #body-cell-title="props">
          <q-td style="cursor:pointer" :props="props">
            {{ props.row.title }}
            <q-popup-edit @save="save(props.row)" v-model="props.row.title" title="Tanım" buttons>
              <q-input v-model="props.row.title" dense autofocus />
            </q-popup-edit>
          </q-td>
      </template>      

    </q-table>
  </q-page>
</template>

<script>
import Service from 'boot/service'
import { common } from 'src/mixins/common'

export default {
  name: 'integration_db',
  mixins: [common],
  components: {
  },
  data () {
    return {
      loading: false,
      data: [],
      cols: [
        { field: 'is_active', label: 'Aktif', name: 'is_active', sortable: true, align: 'left' },
        { field: 'code', label: 'VT', name: 'code', sortable: true, align: 'left' },
        { field: 'title', label: 'Tanım', name: 'title', sortable: true, align: 'left' },
      ],
      pagination: {
        sortBy: 'desc',
        descending: false,
        page: 1,
        rowsPerPage: 3,
        rowsNumber: 10
      }
    }
  },
  mounted () {
    this.load({ pagination: this.pagination })
  },
  methods: {
    save (row) {
        Service.patch(`integration/db/edit/${row.id}`, {
            'is_active': row.is_active,
            'title': row.title
        })
        .then((response) => {
            this.bm('Başarıyla güncellendi!')            
        })
        .catch((error) => {
            this.um('Bir hata oluştu! ' + error)
        })
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
      Service.get('integration/db', params)
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
