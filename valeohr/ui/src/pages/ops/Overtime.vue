<template>
  <q-page padding>
    <q-toolbar class="bg-grey-3 text-black">
      <q-toolbar-title> Fazla Mesailer </q-toolbar-title>
      <q-space />
      <q-btn
        class="q-mr-xs q-px-sm"
        :loading="loading"
        @click="refresh()"
        flat
        round
        dense
        icon="fas fa-sync-alt"
      >
        <q-tooltip> Yenile </q-tooltip>
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
        hide-dropdown-icon
        option-value="name"
        style="min-width: 150px"
      >
      </q-select>
    </q-toolbar>

    <q-table
      :data="data"
      :columns="cols"
      dense
      row-key="idnr"
      :pagination.sync="pagination"
      :loading="loading"
      binary-state-sort
      :visible-columns="visible"
      no-data-label="Fazla mesai bulunamadı!"
      :rows-per-page-options="[]"
      @request="load"
    >
      <template v-slot:top>
        <div class="row flex" :style="{ width: '100%', height: '100%' }">
          <div class="col-1">
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
              hide-dropdown-icon
              filled
              class="q-ml-sm q-mr-sm"
            >
            </q-select>
          </div>
          <div class="row flex col-3">
            <div class="col-6">
              <q-input
                :disabled="db === null"
                @keydown.enter="load({ pagination: pagination })"
                filled
                label="Başlangıç"
                v-model="start"
                mask="date"
                readonly
              >
                <template #append>
                  <q-icon name="event" class="cursor:pointer">
                    <q-popup-proxy
                      ref="qSDateProxy"
                      transition-show="scale"
                      anchor="bottom middle"
                      transition-hide="scale"
                    >
                      <q-date v-model="start">
                        <div class="row items-center justify-end">
                          <q-btn
                            v-close-popup
                            label="Kapat"
                            color="primary"
                            flat
                          />
                        </div>
                      </q-date>
                    </q-popup-proxy>
                  </q-icon>
                </template>
              </q-input>
            </div>
            <div class="col-6">
              <q-input
                :disabled="db === null"
                class="q-ml-sm q-mr-sm"
                @keydown.enter="load({ pagination: pagination })"
                filled
                label="Bitiş"
                v-model="end"
                mask="date"
                readonly
              >
                <template #append>
                  <q-icon name="event" class="cursor:pointer">
                    <q-popup-proxy
                      ref="qEDateProxy"
                      transition-show="scale"
                      anchor="bottom middle"
                      transition-hide="scale"
                    >
                      <q-date v-model="end">
                        <div class="row items-center justify-end">
                          <q-btn
                            v-close-popup
                            label="Kapat"
                            color="primary"
                            flat
                          />
                        </div>
                      </q-date>
                    </q-popup-proxy>
                  </q-icon>
                </template>
              </q-input>
            </div>
          </div>
          <div class="col-2">
            <q-select
              :disabled="db === null"
              v-model="firm"
              :options="f_firms"
              label="Firma"
              :option-label="(o) => o.code"
              option-value="code"
              outlined
              input-debounce="0"
              options-dense
              emit-value
              use-input
              hide-dropdown-icon
              map-options
              filled
              clearable
              multiple
              @filter="
                (val, update, abort) => {
                  filter_fn(
                    val,
                    update,
                    abort,
                    'description',
                    'f_firms',
                    firms
                  );
                }
              "
              class="q-ml-sm q-mr-sm"
              style="height: 56px; overflow-y: auto"
              @keyup.enter="apply_filter()"
            >
            </q-select>
          </div>
          <div class="col-2">
            <q-select
              @keyup.enter="apply_filter()"
              :disabled="db === null"
              v-model="employee"
              :options="f_employees"
              label="Personel"
              option-value="nr"
              :option-label="(o) => `[${o.firm}] - ${o.title}`"
              outlined
              options-dense
              map-options
              use-input
              emit-value
              hide-dropdown-icon
              filled
              clearable
              @filter="
                (val, update, abort) => {
                  filter_fn(
                    val,
                    update,
                    abort,
                    'title',
                    'f_employees',
                    c_employees
                  );
                }
              "
              class="q-ml-sm q-mr-sm"
              style="height: 56px; overflow-y: auto"
            >
            </q-select>
          </div>
          <div class="col-2">
            <q-select
              v-model="collar"
              :options="collars"
              label="Yaka Tipi"
              option-label="title"
              option-value="id"
              outlined
              options-dense
              emit-value
              hide-dropdown-icon
              map-options
              filled
              clearable
              class="q-ml-sm q-mr-sm"
              @keyup.enter="apply_filter()"
            >
            </q-select>
          </div>
          <div class="col-1">
            <q-select
              v-model="fm_filter"
              :options="fm_filters"
              label="Fazla Mesai Tipi"
              option-label="title"
              option-value="id"
              outlined
              options-dense
              emit-value
              map-options
              filled
              hide-dropdown-icon
              clearable
              multiple
              class="q-ml-sm q-mr-sm"
              style="height: 56px; overflow-y: auto"
              @keyup.enter="apply_filter()"
            >
            </q-select>
          </div>
          <div class="col-1">
            <q-btn
              :style="{ width: '100%', height: '100%' }"
              color="black"
              @click="apply_filter"
              label="Filtrele"
            />
          </div>
        </div>
      </template>
    </q-table>
  </q-page>
</template>

<script>
import Service from "boot/service";
import { common } from "src/mixins/common";
import { date } from "quasar";
import TransactionForm from "components/TransactionForm";
import ChangeHistory from "components/ChangeHistory";

export default {
  name: "ops_transaction",
  mixins: [common],
  components: {
    TransactionForm,
    ChangeHistory,
  },
  data() {
    return {
      loading: false,
      data: [],
      cols: [
        {
          field: "idnr",
          label: "ID",
          name: "idnr",
          sortable: true,
          align: "left",
        },
        {
          field: "employee",
          label: "Personel",
          name: "employee",
          sortable: false,
          align: "left",
        },
        {
          field: "tr_date",
          label: "Tarih",
          name: "tze_datum",
          sortable: true,
          align: "left",
          format: (val, row) => date.formatDate(val, "DD/MM/YY"),
        },
        {
          field: "tze_vonzeit",
          label: "Giriş Zamanı",
          name: "tze_vonzeit",
          sortable: true,
          align: "left",
        },
        {
          field: "tze_biszeit",
          label: "Çıkış Zamanı",
          name: "tze_biszeit",
          sortable: true,
          align: "left",
        },
        {
          field: "interval",
          label: "Fazla Mesai Süresi",
          name: "tze_istzeit",
          sortable: true,
          align: "left",
        },
        {
          field: "firm",
          label: "Firma",
          name: "firm",
          sortable: false,
          align: "left",
        },
      ],
      visible: [
        "idnr",
        "employee",
        "tze_datum",
        "tze_istzeit",
        "tze_vonzeit",
        "tze_biszeit",
        "firm",
      ],
      pagination: {
        sortBy: "desc",
        descending: false,
        page: 1,
        rowsPerPage: 3,
        rowsNumber: 10,
      },
      start: date.formatDate(
        date.subtractFromDate(new Date(), { days: 2 }),
        "YYYY-MM-DD"
      ),
      end: date.formatDate(
        date.subtractFromDate(new Date(), { days: 1 }),
        "YYYY-MM-DD"
      ),
      employee: null,
      db: null,
      firm: null,
      dbs: [],
      employees: [],
      firms: [],
      f_firms: [],
      f_employees: [],
      collars: [
        {
          id: 1,
          title: "Beyaz Yaka",
        },
        {
          id: 2,
          title: "Mavi Yaka",
        },
      ],
      collar: null,
      fm_filters: [
        {
          id: "FM1",
          title: "FM1",
        },
        {
          id: "FM2",
          title: "FM2",
        },
        {
          id: "FM3",
          title: "FM3",
        },
        {
          id: "FM4",
          title: "FM4",
        },
      ],
      fm_filter: null,
    };
  },
  computed: {
    c_employees() {
      let self = this;
      if (this.firm) {
        return self.employees.filter((o) => self.firm.includes(o.firm));
      }
      return this.employees;
    },
  },
  mounted() {
    this.load_dbs();
    this.load({ pagination: this.pagination });
  },
  methods: {
    load_dbs() {
      let self = this;
      Service.get("defs/dbs", {})
        .then((response) => {
          self.$set(self, "dbs", response.data.dbs);
          self.$set(self, "db", response.data.default.code);
          self.$set(self, "employees", response.data.employees);
          self.$set(self, "firms", response.data.companies);
        })
        .catch((error) => {
          this.um("Bir hata oluştu!" + error);
        })
        .finally(() => {
          this.$set(this, "loading", false);
        });
    },
    refresh() {
      this.$set(
        this,
        "start",
        date.formatDate(
          date.subtractFromDate(new Date(), { days: 2 }),
          "YYYY-MM-DD"
        )
      );
      this.$set(
        this,
        "end",
        date.formatDate(
          date.subtractFromDate(new Date(), { days: 1 }),
          "YYYY-MM-DD"
        )
      );
      this.$set(this, "pagination", {
        sortBy: "desc",
        descending: false,
        page: 1,
        rowsPerPage: 3,
        rowsNumber: 10,
      });
      this.$set(this, "employee", null);
      this.$set(this, "firm", null);
      this.load({ pagination: this.pagination });
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
          : sett.pagination.sortBy,
        tze_datum__gte: sett.start
          ? sett.start
          : date.formatDate(self.start, "YYYY-MM-DD"),
        tze_datum__lte: sett.end
          ? sett.end
          : date.formatDate(self.end, "YYYY-MM-DD"),
      };
      if (sett.employee || self.employee)
        params["employee"] = sett.employee ? sett.employee : self.employee;
      if (sett.db || self.db) params["db"] = sett.db ? sett.db : self.db;
      if (self.firm) params["firm"] = self.firm;
      if (self.collar) params["worker_type"] = self.collar;
      if (self.fm_filter) params["fm_filter"] = self.fm_filter;

      Service.get("ops/overtime", params)
        .then((response) => {
          self.$set(self, "data", response.data.results);
          self.pagination.rowsNumber = response.data.total;
          self.pagination.page = response.data.current;
          self.pagination.rowsPerPage = response.data.page_size;
          self.pagination.descending = response.data.descending;
          self.pagination.sortBy = response.data.ordering;
        })
        .catch((error) => {
          this.um("Bir hata oluştu!" + error);
        })
        .finally(() => {
          this.$set(this, "loading", false);
        });
    },
    apply_filter() {
      let pagination = this.pagination;
      pagination.page = 1;
      this.load({ pagination });
    },
  },
};
</script>
