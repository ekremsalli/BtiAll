<template>
  <div>
    <q-page padding>
      <q-toolbar class="bg-grey-3 text-black">
        <q-toolbar-title>
          <span class="text-red-7">Aktiviteler</span>
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
      >
        <template v-slot:top>
          <q-input filled v-model="filter.activity" label="Aktivite" dense />

          <q-select
            filled
            v-model="filter.is_success"
            :options="success"
            option-value="id"
            option-label="title"
            map-options
            emit-value
            class="q-ml-sm"
            label="Durum"
            dense
            style="min-width: 150px"
            clearable
          />

          <q-btn
            push
            color="orange-8"
            @click="refresh"
            label="Filtrele"
            class="q-ml-sm"
          />
          <q-btn @click="reset" color="red-5" label="Temizle" push class="q-ml-sm" />
          
        </template>

        <template #body-cell-is_success="props">
            <q-td :props="props" v-if="props.row.is_success">
              👍
            </q-td>
            <q-td :props="props" v-else>
              👎
            </q-td>
          </template>
      </q-table>
    </q-page>
  </div>
</template>

<script>
import Service from "boot/service";
import { common } from "src/mixins/common";
import { date } from "quasar";

export default {
  name: "com_activity",
  mixins: [common],
  data() {
    return {
      loading: false,
      data: [],
      cols: [
        {
          field: "id",
          label: "ID",
          name: "id",
          sortable: true,
          align: "left"
        },
        {
          field: "name",
          label: "Aktivite",
          name: "name",
          sortable: true,
          align: "left"
        },

        {
          field: "is_success",
          label: "Durum",
          name: "is_success",
          sortable: true,
          align: "left"
        },
        {
          field: "took",
          label: "took",
          name: "took",
          sortable: true,
          align: "left"
        },
        {
          field: "created",
          label: "created",
          name: "created",
          sortable: true,
          align: "left",
          format: (val, row) => date.formatDate(val, "DD/MM/YY HH:mm:ss")
        },
        {
          field: "params",
          label: "params",
          name: "params",
          sortable: true,
          align: "left"
        },
        {
          field: "exception",
          label: "exception",
          name: "exception",
          sortable: true,
          align: "left"
        }
      ],
      visible: ["id", "name", "is_success", "took", "created"],
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
      can_update: false,
      is_removed: false,
      scroll: false,
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
          : sett.pagination.sortBy
      };
      
      if (filter.activity) params['name__contains'] = filter.activity
      if (filter.is_success) params['is_success'] = filter.is_success

      Service.get('/app/v1/activity', params)
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

<style scoped></style>
