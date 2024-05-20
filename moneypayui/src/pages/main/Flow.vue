<template>
  <div>
    <q-page padding>
      <q-toolbar class="bg-grey-3 text-black">
        <q-toolbar-title>
          <span class="text-red-7">Akış</span>
        </q-toolbar-title>

        <q-space />

        <q-btn
          :loading="loading"
          @click="refresh()"
          flat
          round
          dense
          icon="fas fa-sync-alt"
          class="q-mr-sm"
        >
          <q-tooltip>
            Yenile
          </q-tooltip>
        </q-btn>

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
          style="min-width: 150px"
        >
        </q-select>
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
            <q-input v-model="filter.method" filled dense label="Method" class="q-mr-sm" style="min-width:150px" />

            <q-input v-model="filter.data" filled dense label="Veri" class="q-mr-sm" style="min-width:150px" />

            <q-select v-model="filter.is_success" filled dense label="Durum" class="q-mr-sm" style="min-width:150px" :options="success" option-value="id" option-label="title" map-options emit-value clearable />

            <q-btn @click="refresh" color="orange-8" label="Filtrele" push />
            <q-btn @click="reset" color="red-5" label="Temizle" push class="q-ml-sm" />

        </template>

         <template #body-cell-related="props">
            <q-td :props="props">
              {{ props.row.related_object }} <span v-if="props.row.internal_ref">({{ props.row.internal_ref }})</span>
            </q-td>
          </template>
      </q-table>


    </q-table>

    <q-dialog v-model="dialog" transition-show="rotate" transition-hide="rotate">
      <q-card style="width: 700px; max-width: 80vw;" v-if="active">
        <q-card-section>
          <div class="text-subtitle1">{{ active.created.format(active.created, 'DD/MM/YYYY') }} tarihli <strong>{{ active.id }}</strong> nolu istek detayı</div>
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

              <template v-if="active.handler == 'XML'">
                <pre>{{ active.request | pretty_xml }}</pre>
              </template>

              <template v-else>
                <pre>{{ active.request | pretty }}</pre>
              </template>

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
  </div>
</template>

<script>
import Service from "boot/service";
import { common } from "src/mixins/common";
import { date } from "quasar";

export default {
  name: "com_flow",
  mixins: [common],
  data() {
    return {
      loading: false,
      data: [],
      cols: [
        { field: 'id', label: 'ID', name: 'id', sortable: true, align: 'left' },
        { field: 'company', label: 'Firma', name: 'company', sortable: true, align: 'left' },
        { field: 'period', label: 'Dönem', name: 'period', sortable: true, align: 'left' },
        { field: 'user', label: 'Kullanıcı', name: 'user', sortable: true, align: 'left' },
        {
            field: 'created',
            label: 'Tarih',
            name: 'created',
            sortable: true,
            align: 'left',
            format: (val, row) => date.formatDate(val, 'DD-MM-YY HH:mm:ss')
        },
        { field: 'handler', label: 'İşleyici', name: 'handler', sortable: true, align: 'left' },
        { field: 'method', label: 'Yöntem', name: 'method', sortable: true, align: 'left' },
        { field: 'related', label: 'İlgili obje', name: 'related', sortable: true, align: 'left' },
        { field: 'took', label: 'Süre', name: 'took', sortable: true, align: 'left', format: (val, row) => `${val} sn` },
        { field: 'success', label: 'Durum', name: 'success', sortable: true, align: 'left', format: (val, row) => val == true ? 'Ok' : 'Hata' },
      ],
      visible: ['id', 'company', 'period', 'user', 'created', 'handler', 'method', 'related', 'took', 'success'],
      pagination: {
        sortBy: "desc",
        descending: false,
        page: 1,
        rowsPerPage: 3,
        rowsNumber: 10
      },
      active: null,
      history: [],
      dialog: false,
      tab: 'bilgi',
      scroll: false,
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
      ],
      filter: {},
      success: [
        {
          id: 1,
          title: "Başarılı"
        },
        {
          id: 2,
          title: "Başarısız"
        }
      ]
    };
  },
  mounted() {
    this.load({ pagination: this.pagination });
  },
  methods: {
    details(event, row, index) {
      this.$set(this, "tab", "bilgi")
      this.$set(this, "dialog", true)
      this.$set(this, "active", row)
    },

    refresh() {
      this.$set(this, "pagination", {
        sortBy: "desc",
        descending: false,
        page: 1,
        rowsPerPage: 3,
        rowsNumber: 10
      });
      this.load({ pagination: this.pagination });
    },
    load(sett) {
      let self = this;
      let filter = self.filter;
      this.$set(this, "loading", true);
      this.$set(this, "data", []);
      const params = {
        page: sett.pagination.page,
        page_size: sett.pagination.rowsPerPage,
        ordering: sett.pagination.descending
          ? "-" + sett.pagination.sortBy
          : sett.pagination.sortBy,
      };

      if (filter.method) params['method__contains'] = filter.method
      if (filter.data) params['data__contains'] = filter.data
      if (filter.is_success) params['success'] = filter.is_success

      Service.get('/app/v1/flow', params)
        .then(response => {
          self.$set(self, "data", response.data.results);

          self.pagination.rowsNumber = response.data.total;
          self.pagination.page = response.data.current;
          self.pagination.rowsPerPage = response.data.page_size;
          self.pagination.descending = response.data.descending;
          self.pagination.sortBy = response.data.ordering;
        })
        .catch(error => {
          this.um("Bir hata oluştu!" + error);
        })
        .finally(() => {
          this.$set(this, "loading", false);
        });
    },
    reset() {
      this.$set(this, "filter", {});
    },
  }
};
</script>

<style scoped>
.json-pretty {
    padding-left: 30px;
    padding-right: 30px;
}
.json-selected {
    background-color: rgba(139, 191, 228, 0.19999999999999996);
}

.json-string {
    color: #6caedd;
}

.json-key {
    color: #ec5f67;
}

.json-boolean {
    color: #99c794;
}

.json-number {
    color: #99c794;
}
</style>
