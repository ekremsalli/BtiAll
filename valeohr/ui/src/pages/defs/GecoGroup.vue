<template>
  <q-page padding>
    <q-toolbar class="bg-grey-3 text-black">
      <q-toolbar-title>
        GeCOTime Grupları
      </q-toolbar-title>
      <q-space />
      <q-btn
        :loading="loading"
        @click="load({ pagination: pagination })"
        flat
        round
        dense
        icon="fas fa-sync-alt"
      >
        <q-tooltip>
          Yenile
        </q-tooltip>
      </q-btn>
    </q-toolbar>

    <q-table
      :data="data"
      :columns="cols"
      dense
      row-key="nr"
      :pagination.sync="pagination"
      :loading="loading"
      binary-state-sort
      :visible-columns="visible"
      no-data-label="Grup bulunamadı!"
      :rows-per-page-options="[]"
      @request="load"
    >
      <template v-slot:top>
        <q-select
          v-model="db"
          :options="dbs"
          label="Veritabanı"
          option-value="code"
          option-label="title"
          outlined
          options-dense
          emit-value
          map-options
          filled
          style="min-width:200px"
          class="q-mr-sm"
          clearable
          hide-dropdown-icon
        >
        </q-select>

        <q-select
          :disable ="db == null"
          v-model="group"
          :options="f_group_types"
          :option-label="o => o.value"
          option-value="id"
          label="Grup Tipi"
          outlined
          multiple
          input-debounce="0"
          use-input
          options-dense
          emit-value
          map-options
          filled
          clearable
          @filter="(val, update, abort) => { filter_fn(val, update, abort, 'value', 'f_group_types', group_types) }"
          style="min-width:200px"
          class="q-ml-sm q-mr-sm"
          options-cover
          hide-dropdown-icon
          @keyup.enter="apply_filter()"
        >
        </q-select>

        <q-input
          :disable ="db == null"
          v-model="description"
          label="Açıklama"
          outlined
          filled
          style="min-width:200px"
          class="q-ml-sm q-mr-sm"
          @keyup.enter="apply_filter()"
        >
        </q-input>

        <q-input
          :disable ="db == null"
          v-model="code"
          label="Grup Adı"
          outlined
          filled
          style="min-width:200px"
          class="q-ml-sm q-mr-sm"
          @keyup.enter="apply_filter()"
        >
        </q-input>

        <q-btn
          :disable ="db == null"
          style="min-height: 55px"
          color="black"
          @click="apply_filter()"
          label="Filtrele"
        />

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
          style="min-width: 150px"
        >
        </q-select>
      </template>
    </q-table>
  </q-page>
</template>

<script>
import Service from "boot/service";
import { common } from "src/mixins/common";
import { date } from "quasar";

export default {
  name: "defs_geco_groups",
  mixins: [common],
  components: {},
  data() {
    return {
      loading: false,
      data: [],
      dbs: [],
      firms: [],
      descriptions: [],
      db: null,
      firm: null,
      group: null,
      group_types: [],
      description: null,
      code: null,
      f_group_types: [],
      cols: [
        { field: "id", label: "ID", name: "id", sortable: true, align: "left" },
        {
          field: "source_db",
          label: "VT",
          name: "source_db",
          sortable: true,
          align: "left"
        },
        {
          field: "gtype",
          label: "Grup tipi",
          name: "gtype",
          sortable: true,
          align: "left"
        },
        {
          field: "code",
          label: "Grup adı",
          name: "code",
          sortable: true,
          align: "left"
        },
        {
          field: "description",
          label: "Açıklama",
          name: "description",
          sortable: true,
          align: "left"
        },
        {
          field: "created_on",
          label: "Oluşturulma",
          name: "created_on",
          sortable: true,
          align: "left",
          format: (val, row) => date.formatDate(val, "DD/MM/YY HH:mm:ss")
        },
        {
          field: "created_by",
          label: "Oluşturan",
          name: "created_by",
          sortable: true,
          align: "left"
        },
        {
          field: "modified_on",
          label: "Düzenleme",
          name: "modified_on",
          sortable: true,
          align: "left",
          format: (val, row) => date.formatDate(val, "DD/MM/YY HH:mm:ss")
        },
        {
          field: "modified_by",
          label: "Düzenleyen",
          name: "modified_by",
          sortable: true,
          align: "left"
        },
        {
          field: "geco_id",
          label: "Geco ID",
          name: "geco_id",
          sortable: true,
          align: "left"
        }
      ],
      visible: ["source_db", "gtype", "code", "description"],
      pagination: {
        sortBy: "desc",
        descending: false,
        page: 1,
        rowsPerPage: 3,
        rowsNumber: 10
      }
    };
  },
  mounted() {
    this.load({ pagination: this.pagination });
    this.load_dbs()

  },
  methods: {
    load_dbs() {
      let self = this;
      Service.get("defs/dbs", {})
        .then(response => {
          self.$set(self, "dbs", response.data.dbs);
        })
        .catch(error => {
          this.um("Bir hata oluştu!" + error);
        })
        .finally(() => {
          this.$set(this, "loading", false);
        });
    },
    load(sett) {
      let self = this;
      this.$set(this, "loading", true);
      this.$set(this, "data", []);
      const params = {
        page: sett.pagination.page,
        page_size: sett.pagination.rowsPerPage,
        ordering: sett.pagination.descending
          ? "-" + sett.pagination.sortBy
          : sett.pagination.sortBy
      };

      if (self.db) params['source_db'] = self.db
      if (self.group) params['gtype'] = self.group
      if (self.description) params['description__contains'] = self.description
      if (self.code) params['code__contains'] = self.code

      Service.get("defs/geco/groups", params)
        .then(response => {
          self.$set(self, "data", response.data.results);
          self.$set(self, "group_types", response.data.group_types)
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
    apply_filter() {
      let pagination = this.pagination;
      pagination.page = 1;
      this.load({ pagination })
    }
  }
};
</script>
