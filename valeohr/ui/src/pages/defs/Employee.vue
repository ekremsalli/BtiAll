<template>
  <q-page padding>
    <q-toolbar class="bg-grey-3 text-black">
      <q-toolbar-title>
        Personel listesi
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
      row-key="id"
      :pagination.sync="pagination"
      :loading="loading"
      binary-state-sort
      :visible-columns="visible"
      no-data-label="Personel bulunamadı!"
      :rows-per-page-options="[]"
      @request="load"
    >
      <template v-slot:top>
        <q-select
          clearable
          v-model="db"
          :options="dbs"
          label="Veritabanı"
          option-value="code"
          option-label="title"
          outlined
          options-dense
          emit-value
          map-options
          hide-dropdown-icon
          filled
          style="min-width:200px"
          class="q-mr-sm"
        >
        </q-select>

        <q-select
          :disable="db === null"
          v-model="firm"
          :options="f_firms"
          :option-label="o => o.description"
          option-value="code"
          label="Firma"
          outlined
          input-debounce="0"
          use-input
          options-dense
          emit-value
          map-options
          filled
          hide-dropdown-icon
          clearable
          multiple
          @filter="(val, update, abort) => { filter_fn(val, update, abort, 'description', 'f_firms', firms) }"
          style="min-width:200px"
          class="q-ml-sm q-mr-sm"
          options-cover
          @keyup.enter="apply_filter()"
        >
        </q-select>

        <q-input
          :disable="db === null"
          v-model="sicil_no"
          label="Personel Sicil No"
          outlined
          filled
          style="min-width:200px"
          class="q-ml-sm q-mr-sm"
          @keyup.enter="apply_filter()"
        >
        </q-input>

        <q-btn
          :disable="db === null"
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
          hide-dropdown-icon
        >
        </q-select>
      </template>

      <template #body-cell-islem="props">
        <q-td :props="props">
          <q-btn
            @click="activate(props.row)"
            round
            color="primary"
            icon="edit"
            size="xs"
          />
        </q-td>
      </template>
    </q-table>

    <q-dialog
      v-model="detail"
      persistent
      transition-show="rotate"
      transition-hide="rotate"
    >
      <q-card class="q-ma-sm" style="width: 700px; max-width: 80vw;">
        <q-card-section class="row items-center">
          <template v-if="active">
            {{ active.name.capitalize() }}
            {{ active.surname.capitalize() }} için açıklama
          </template>
        </q-card-section>

        <q-card-section>
          <q-editor v-model="description" min-height="10rem" />
        </q-card-section>

        <q-card-actions align="right">
          <q-btn

            flat
            @click="save"
            label="Kaydet"
            color="black"
            v-close-popup
          />
          <q-btn flat label="İptal" color="black" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script>
import Service from "boot/service";
import { common } from "src/mixins/common";
import { date } from "quasar";

export default {
  name: "defs_employee",
  mixins: [common],
  components: {},
  data() {
    return {
      loading: false,
      db: null,
      firm: null,
      sicil_no: null,
      data: [],
      dbs: [],
      firms: [],
      f_firms: [],
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
          field: "nr",
          label: "Sicil No.",
          name: "nr",
          sortable: true,
          align: "left"
        },
        {
          field: "name",
          label: "Adı",
          name: "name",
          sortable: true,
          align: "left",
          format: (val, row) => val.capitalize()
        },
        {
          field: "surname",
          label: "Soyadı",
          name: "surname",
          sortable: true,
          align: "left",
          format: (val, row) => val.capitalize()
        },
        {
          field: "firm",
          label: "Firma",
          name: "firm",
          sortable: true,
          align: "left"
        },
        {
          field: "department",
          label: "Departman",
          name: "department",
          sortable: true,
          align: "left"
        },
        {
          field: "title",
          label: "Ünvan",
          name: "title",
          sortable: true,
          align: "left"
        },
        {
          field: "worker_type",
          label: "Tip",
          name: "worker_type",
          sortable: true,
          align: "left"
        },
        {
          field: "account",
          label: "Hesap grubu",
          name: "account",
          sortable: true,
          align: "left"
        },
        {
          field: "cost_center",
          label: "Masraf merkezi",
          name: "cost_center",
          sortable: true,
          align: "left"
        },
        {
          field: "psoft_id",
          label: "PeopleSoft ID",
          name: "psoft_id",
          sortable: true,
          align: "left"
        },
        {
          field: "work_id",
          label: "Çalışma ID",
          name: "work_id",
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
          field: "islem",
          label: "Açıklama",
          name: "islem",
          sortable: false,
          align: "right"
        }
      ],
      visible: [
        "source_db",
        "nr",
        "name",
        "surname",
        "firm",
        "department",
        "title",
        "worker_type",
        "account",
        "islem"
      ],
      pagination: {
        sortBy: "desc",
        descending: false,
        page: 1,
        rowsPerPage: 3,
        rowsNumber: 10
      },
      detail: false,
      active: null,
      description: ""
    };
  },
  computed: {
    c_employees() {
      let self = this;
      if (this.firm) {
        return self.employees.filter(o => self.firm.includes(o.firm));
      }
      return this.employees;
    }
  },
  mounted() {
    this.load({ pagination: this.pagination });
    this.load_dbs();
  },
  methods: {
    save() {
      let self = this;
      let active = this.active;
      Service.patch(`defs/employee/${active.id}`, {
        description: self.description
      })
        .then(response => {
          self.$set(self.active, "description", self.description);
          this.bm("Başarıyla güncellendi!");
        })
        .catch(error => {
          this.um("Bir hata oluştu!" + error);
        });
    },
    activate(row) {
      this.$set(this, "active", row);
      if (row.description) this.$set(this, "description", row.description);
      this.$set(this, "detail", true);
    },
    load_dbs() {
      let self = this;
      Service.get("defs/dbs", {})
        .then(response => {
          self.$set(self, "dbs", response.data.dbs);
          self.$set(self, "db", response.data.default.code);
          self.$set(self, "firms", response.data.companies);
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
      this.$set(this, "data", [])
      const params = {
        page: sett.pagination.page,
        page_size: sett.pagination.rowsPerPage,
        ordering: sett.pagination.descending
          ? "-" + sett.pagination.sortBy
          : sett.pagination.sortBy,
      };

      if (self.db) params['source_db'] = self.db
      if (self.firm) params['firm'] = self.firm
      if (self.sicil_no) params['nr'] = self.sicil_no

      Service.get("defs/employee", params)
        .then(response => {
          self.$set(self, "data", response.data.results);
          self.pagination.rowsNumber = response.data.total;
          self.pagination.page = response.data.current;
          self.pagination.rowsPerPage = response.data.page_size;
          self.pagination.descending = response.data.descending;
          self.pagination.sortBy = response.data.ordering;
        })
        .catch(error => {
          this.um("Bir hata oluştu!" + error)
        })
        .finally(() => {
          this.$set(this, "loading", false)
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
