<template>
  <q-page padding>
    <q-toolbar class="bg-grey-3 text-black">
      <q-toolbar-title> Anormallikler </q-toolbar-title>
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
        option-value="name"
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
      no-data-label="Anormallik bulunamadı!"
      :rows-per-page-options="[]"
      @request="load"
      @row-click="check_anomaly"
    >
      <template v-slot:top>
        <div class="row flex" :style="{ width: '100%', height: '100%' }">
          <div class="row col-3">
            <div class="col-6">
              <q-input
                @keydown.enter="load({ pagination: pagination })"
                filled
                label="Başlangıç"
                v-model="start"
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
                      <q-date v-model="start" mask="YYYY-MM-DD" today-btn>
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
                class="q-ml-sm q-mr-sm"
                @keydown.enter="load({ pagination: pagination })"
                filled
                label="Bitiş"
                v-model="end"
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
                      <q-date v-model="end" mask="YYYY-MM-DD" today-btn>
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
              v-model="firm"
              :options="f_firms"
              label="Firma"
              outlined
              options-dense
              use-input
              emit-value
              map-options
              filled
              clearable
              multiple
              hide-dropdown-icon
              @filter="
                (val, update, abort) => {
                  filter_fn(val, update, abort, '', 'f_firms', firms);
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
              v-model="collar"
              :options="collars"
              label="Yaka Tipi"
              option-label="title"
              option-value="id"
              outlined
              options-dense
              emit-value
              map-options
              filled
              clearable
              hide-dropdown-icon
              class="q-ml-sm q-mr-sm"
              @keyup.enter="apply_filter()"
            >
            </q-select>
          </div>
          <div class="col-2">
            <q-select
              v-model="employee"
              :options="f_employees"
              label="Personel"
              option-value="id"
              option-label="title"
              outlined
              options-dense
              use-input
              emit-value
              map-options
              filled
              clearable
              hide-dropdown-icon
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
              @keyup.enter="apply_filter()"
            >
            </q-select>
          </div>
          <div class="col-2">
            <q-select
              v-model="ano_type"
              :options="ano_types"
              label="Anormallik Tipi"
              outlined
              options-dense
              emit-value
              map-options
              filled
              clearable
              hide-dropdown-icon
              class="q-ml-sm q-mr-sm"
              style="height: 56px; overflow-y: auto"
              @keyup.enter="apply_filter()"
            >
            </q-select>
          </div>
          <div class="col-1">
            <q-btn
              color="black"
              @click="apply_filter"
              label="Filtrele"
              :style="{ width: '100%', height: '100%' }"
            />
          </div>
        </div>
      </template>
    </q-table>

    <q-dialog
      v-model="dialog"
      persistent
      transition-show="rotate"
      transition-hide="rotate"
    >
      <q-card
        class="q-ma-sm"
        style="width: 700px; min-height: 72vh; max-width: 80vw"
      >
        <q-card-section>
          <template v-if="active">
            <div class="text-h6 text-center bg-black text-white">
              {{ active.employee }} için&nbsp;<span class="text-italic">{{
                active.geco_id
              }}</span
              >&nbsp;nolu anormallik
            </div>
          </template>

          <q-tabs v-model="tab" align="justify" class="text-black">
            <q-tab name="insert" label="Giriş / Çıkış hareketi oluştur" />
          </q-tabs>

          <q-tab-panels v-model="tab" animated>
            <q-tab-panel name="insert">
              <template v-if="can_insert">
                <transaction-form
                  :record="record"
                  :employees="employees"
                  :time_types="time_types"
                  :ano_type="ano_type"
                  :day_models="day_models"
                  :pay_models="pay_models"
                  :accounts="accounts"
                  :transactions="transactions"
                  :anomalies="anomalies"
                  :app="app"
                  @select_transaction="select_transaction"
                />
              </template>
              <template v-else>
                <q-banner class="bg-grey-3">
                  <template v-slot:avatar>
                    <q-icon name="unpublished" color="primary" />
                  </template>
                  Bu anormallik için onay bekleyen kayıt mevcut!
                </q-banner>
              </template>
            </q-tab-panel>
          </q-tab-panels>
        </q-card-section>

        <q-card-actions class="q-mr-lg" align="right">
          <q-btn
            v-if="tab == 'insert' && can_insert"
            flat
            @click="save"
            label="Kaydet"
            color="black"
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
import TransactionForm from "components/TransactionForm";

export default {
  name: "ops_anomaly",
  mixins: [common],
  components: {
    TransactionForm,
  },
  data() {
    return {
      loading: false,
      data: [],
      cols: [
        { field: "id", label: "ID", name: "id", sortable: true, align: "left" },
        {
          field: "source_db",
          label: "VT",
          name: "source_db",
          sortable: true,
          align: "left",
        },
        {
          field: "employee",
          label: "Personel",
          name: "employee",
          sortable: true,
          align: "left",
        },
        {
          field: "tr_date",
          label: "Tarih",
          name: "tr_date",
          sortable: true,
          align: "left",
          format: (val, row) => date.formatDate(val, "DD/MM/YY"),
        },
        {
          field: "ano_type",
          label: "Anormallik tipi",
          name: "ano_type",
          sortable: true,
          align: "left",
          format: (val, row) => `(${row.ano_type}) ${row.ano_text}`,
        },
        {
          field: "description",
          label: "Açıklama",
          name: "description",
          sortable: true,
          align: "left",
        },
        {
          field: "created_on",
          label: "Oluşturulma",
          name: "created_on",
          sortable: true,
          align: "left",
          format: (val, row) => date.formatDate(val, "DD/MM/YY HH:mm:ss"),
        },
        {
          field: "created_by",
          label: "Oluşturan",
          name: "created_by",
          sortable: true,
          align: "left",
        },
        {
          field: "modified_on",
          label: "Düzenleme",
          name: "modified_on",
          sortable: true,
          align: "left",
          format: (val, row) => date.formatDate(val, "DD/MM/YY HH:mm:ss"),
        },
        {
          field: "modified_by",
          label: "Düzenleyen",
          name: "modified_by",
          sortable: true,
          align: "left",
        },
        {
          field: "geco_id",
          label: "Geco ID",
          name: "geco_id",
          sortable: true,
          align: "left",
        },
      ],
      visible: [
        "source_db",
        "employee",
        "tr_date",
        "ano_type",
        "description",
        "created_on",
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
      employees: [],
      active: null,
      history: [],
      dialog: false,
      can_insert: false,
      record: {},
      time_types: [],
      ano_types: [],
      day_models: [],
      pay_types: [],
      pay_models: [],
      shift_models: [],
      flex_shift_models: [],
      accounts: [],
      firms: [],
      tab: "insert",
      check_in: false,
      check_out: false,
      ano_type: null,
      firm: null,
      anomalies: [],
      transactions: [],
      app: {
        selected_transaction: null,
        selected_anomaly: null,
      },
      employee_id: null,
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
    this.load({ pagination: this.pagination });
    this.load_api_defs();
    this.load_api_groups();
  },
  methods: {
    load_api_defs() {
      let self = this;
      Service.get("defs/api/defs")
        .then((response) => {
          self.$set(self, "time_types", response.data.time_types);
          self.$set(self, "ano_type", response.data.ano_type);
          self.$set(self, "day_models", response.data.day_models);
          self.$set(self, "pay_types", response.data.pay_types);
          self.$set(self, "pay_models", response.data.pay_models);
          self.$set(self, "shift_models", response.data.shift_models);
          self.$set(self, "flex_shift_models", response.data.flex_shift_models);
        })
        .catch((error) => {
          this.um("Bir hata oluştu! " + error);
        });
    },
    load_api_groups() {
      let self = this;
      Service.get("defs/api/groups")
        .then((response) => {
          response;
          self.$set(self, "accounts", response.data.accounts);
        })
        .catch((error) => {
          this.um("Bir hata oluştu! " + error);
        });
    },
    select_transaction() {
      let self = this;

      this.$nextTick(function () {
        let tr = self.app.selected_transaction;
        if (tr) {
          self.$set(this, "record", {
            employee: self.employee_id,
            transaction_id: tr.id,
            tr_date: self.active.tr_date,
            is_remove_request: false,
            start: tr.start && tr.start.length > 0 ? tr.start : null,
            end: tr.end && tr.end.length > 0 ? tr.end : null,
            time_type: tr.time_type ? tr.time_type : null,
            day_model: tr.day_model ? tr.day_model : null,
            excuse_day: tr.excuse_day ? tr.excuse_day : null,
            account: tr.account ? tr.account : null,
            pay_type: tr.pay_type ? tr.pay_type : null,
            description: `${tr.id} nolu hareket için güncelleme`,
          });
        } else {
          let clone = JSON.parse(JSON.stringify(self.active));
          self.$set(this, "record", clone);
        }

        return true;
      });
    },
    check_anomaly(e, obj) {
      if (
        !this.$store.getters["account/is_superuser"] &&
        !this.$store.getters["account/is_staff"] &&
        !this.$store.getters["account/perm_check"]("changes.add_changes")
      ) {
        this.hm("Bu işlem için yetkiniz bulunmuyor!");
        return;
      }
      let self = this;
      let clone = JSON.parse(JSON.stringify(obj));
      Service.get("ops/check_anomaly", {
        geco_anomaly_id: obj.geco_id,
      })
        .then((response) => {
          self.$set(self, "can_insert", response.data.can_update);
          clone.tr_date = date.formatDate(clone.tr_date, "YYYY-MM-DD");
          clone.description = "";
          self.$set(self, "record", clone);
          self.$set(self, "active", obj);
          self.$set(self, "tab", "insert");
          self.$set(self, "dialog", true);
          self.$set(self, "transactions", response.data.transactions);
          self.$set(self, "anomalies", response.data.anomalies);
          self.$set(self, "employee_id", response.data.employee);
        })
        .catch((error) => {
          if (error.response && error.response.data) {
            if (error.response.data.custom) {
              this.um(error.response.data.message);
            } else this.um("Bir hata oluştu! " + error);
          } else this.um("Bir hata oluştu! " + error);
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
      this.load({ pagination: this.pagination });
      this.load_api_defs();
      this.load_api_groups();
    },
    save() {
      let self = this;
      Service.post(`ops/changes`, self.record)
        .then((response) => {
          if (response.data && response.data.status) {
            self.bm("Başarıyla kaydedildi!");
            self.$set(self, "dialog", false);
          }
        })
        .catch((error) => {
          if (error.response && error.response.data) {
            if (error.response.data.custom) {
              this.um(error.response.data.message);
            } else this.um("Bir hata oluştu! " + error);
          } else this.um("Bir hata oluştu! " + error);
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
          : sett.pagination.sortBy,
        tr_date__gte: sett.start
          ? sett.start
          : date.formatDate(self.start, "YYYY-MM-DD"),
        tr_date__lte: sett.end
          ? sett.end
          : date.formatDate(self.end, "YYYY-MM-DD"),
      };
      if (sett.employee || self.employee) {
        params["employee"] = sett.employee ? sett.employee : self.employee;
      }
      if (self.ano_type) params["ano_text"] = self.ano_type;
      if (self.firm) params["firm"] = self.firm;
      if (self.collar) params["worker_type"] = self.collar;
      Service.get("ops/anomalies", params)
        .then((response) => {
          self.$set(self, "data", response.data.results);
          self.$set(self, "employees", response.data.employees);
          let firms = response.data.employees.map((o) => o.firm);
          self.$set(self, "firms", [...new Set(firms)]);

          self.$set(self, "ano_types", response.data.ano_types);

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
