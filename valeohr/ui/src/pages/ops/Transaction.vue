<template>
  <q-page padding>
    <q-toolbar class="bg-grey-3 text-black">
      <q-toolbar-title> Giriş / Çıkış Zamanları </q-toolbar-title>
      <q-btn
        class="q-mr-xs q-px-sm"
        color="primary"
        dense
        label="Yeni Kayıt Ekle"
        @click="add_new_dialog"
      />
      <q-btn
        :loading="loading"
        @click="refresh()"
        class="q-mr-xs q-px-sm"
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
        style="min-width: 150px"
      />
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
      no-data-label="Hareket bulunamadı!"
      :rows-per-page-options="[]"
      @request="load"
      @row-click="check_transaction"
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
              v-model="firm"
              :options="f_firms"
              label="Firma"
              outlined
              input-debounce="0"
              use-input
              options-dense
              emit-value
              map-options
              filled
              clearable
              multiple
              hide-dropdown-icon
              @filter="
                (val, update, abort) => {
                  filter_fn(val, update, abort, null, 'f_firms', firms);
                }
              "
              style="height: 56px; overflow-y: auto"
              class="q-ml-sm q-mr-sm"
              options-cover
              @keyup.enter="apply_filter()"
            >
            </q-select>
          </div>
          <div class="col-2">
            <q-select
              v-model="employee"
              :options="f_employees"
              label="Personel"
              use-input
              option-value="id"
              option-label="title"
              outlined
              options-dense
              emit-value
              map-options
              filled
              hide-dropdown-icon
              :options-cover="true"
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
              @keyup.enter="apply_filter()"
            >
            </q-select>
          </div>
          <div class="col-2">
            <q-select
              v-model="excuse_type"
              :options="f_excuse_types"
              label="Mazaret"
              option-value="code"
              :option-label="(o) => `${o.name} (${o.code})`"
              outlined
              options-dense
              emit-value
              map-options
              hide-dropdown-icon
              use-input
              filled
              clearable
              @filter="
                (val, update, abort) => {
                  filter_fn(
                    val,
                    update,
                    abort,
                    'name',
                    'f_excuse_types',
                    excuse_types
                  );
                }
              "
              class="q-ml-sm q-mr-sm"
              style="height: 56px; overflow-y: auto"
              options-cover
              @keyup.enter="apply_filter()"
            >
            </q-select>
          </div>
          <div class="col-2">
            <q-select
              clearable
              class="q-ml-sm q-mr-sm"
              filled
              hide-dropdown-icon
              v-model="check"
              :options="check_options"
            />
          </div>
          <div class="col-1">
            <q-btn
              color="black"
              @click="apply_filter"
              :style="{ width: '100%', height: '100%' }"
              label="Filtrele"
            />
          </div>
        </div>

        <q-space />
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
              >&nbsp;nolu hareket
            </div>
          </template>
          <q-tabs v-model="tab" align="justify" class="text-black">
            <q-tab name="update" label="Kayıt güncelle" />
            <q-tab name="history" label="Güncelleme geçmişi" />
          </q-tabs>

          <q-tab-panels v-model="tab" animated>
            <q-tab-panel name="update">
              <template v-if="can_update">
                <q-toggle
                  class="q-ml-sm"
                  v-model="record.is_remove_request"
                  label="Bu hareketi silmek istiyorum"
                />

                <transaction-form
                  :record="record"
                  :employees="employees"
                  :time_types="time_types"
                  :excuse_types="excuse_types"
                  :day_models="day_models"
                  :pay_models="pay_models"
                  :accounts="accounts"
                />
              </template>
              <template v-else>
                <q-banner class="bg-grey-3">
                  <template v-slot:avatar>
                    <q-icon name="unpublished" color="primary" />
                  </template>
                  <template v-if="is_removed"> Bu hareket silinmiş! </template>
                  <template v-else>
                    Bu hareket için onay bekleyen kayıt mevcut!
                  </template>
                </q-banner>
              </template>
            </q-tab-panel>

            <q-tab-panel name="history">
              <change-history :history="history" />
            </q-tab-panel>
          </q-tab-panels>
        </q-card-section>

        <q-card-actions class="q-mr-lg" align="right">
          <q-btn
            v-if="tab == 'update' && can_update"
            flat
            @click="save"
            label="Kaydet"
            color="black"
          />
          <q-btn flat label="İptal" color="black" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>

    <q-dialog
      v-model="new_dialog"
      persistent
      transition-show="rotate"
      transition-hide="rotate"
    >
      <q-card
        class="q-ma-sm"
        style="width: 700px; min-height: 72vh; max-width: 80vw"
      >
        <q-card-section>
          <!-- <template v-if="!active">
            <div class="text-h6 text-center bg-black text-white">
              {{ active.employee }} için&nbsp;<span class="text-italic">{{
                active.geco_id
              }}</span
              >&nbsp;nolu hareket
            </div>
          </template> -->
          <q-tabs v-model="tab" align="justify" class="text-black">
            <q-tab name="update" label="Yeni Kayıt Ekle" />
          </q-tabs>

          <q-tab-panels v-model="tab" animated>
            <q-tab-panel name="update">
              <template>
                <NewAddTransactionForm
                  :defs="defs"
                  :employees="employees"
                  :time_types="time_types"
                  :excuse_types="excuse_types"
                  :day_models="day_models"
                  :pay_models="pay_models"
                  :accounts="accounts"
                />
              </template>
            </q-tab-panel>
          </q-tab-panels>
        </q-card-section>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script>
import Service from "boot/service";
import { common } from "src/mixins/common";
import { date } from "quasar";
import TransactionForm from "components/TransactionForm";
import ChangeHistory from "components/ChangeHistory";
import NewAddTransactionForm from "components/NewAddTransactionForm";

export default {
  name: "ops_transaction",
  mixins: [common],
  components: {
    TransactionForm,
    ChangeHistory,
    NewAddTransactionForm,
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
          field: "start",
          label: "Giriş",
          name: "start",
          sortable: true,
          align: "left",
        },
        {
          field: "end",
          label: "Çıkış",
          name: "end",
          sortable: true,
          align: "left",
        },
        {
          field: "work_time",
          label: "Süre",
          name: "work_time",
          sortable: true,
          align: "left",
        },
        {
          field: "time_type",
          label: "Zaman tipi",
          name: "time_type",
          sortable: true,
          align: "left",
        },
        {
          field: "excuse_type",
          label: "Mazeret tipi",
          name: "excuse_type",
          sortable: true,
          align: "left",
        },
        {
          field: "excuse_day",
          label: "Gün",
          name: "excuse_day",
          sortable: true,
          align: "left",
        },
        {
          field: "day_model",
          label: "Gün modeli",
          name: "day_model",
          sortable: true,
          align: "left",
        },
        {
          field: "account",
          label: "Hesap grubu",
          name: "account",
          sortable: true,
          align: "left",
        },
        {
          field: "pay_type",
          label: "Puantaj tipi",
          name: "pay_type",
          sortable: true,
          align: "left",
        },
        {
          field: "cost_center",
          label: "Masraf merkezi",
          name: "cost_center",
          sortable: true,
          align: "left",
        },
        {
          field: "psoft_id",
          label: "PeopleSoft ID",
          name: "psoft_id",
          sortable: true,
          align: "left",
        },
        {
          field: "work_id",
          label: "Çalışma ID",
          name: "work_id",
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
        "start",
        "end",
        "work_time",
        "time_type",
        "worker_type",
        "excuse_type",
        "excuse_day",
        "day_model",
        "account",
        "pay_type",
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
      new_dialog: false,
      can_update: false,
      is_removed: false,
      record: {},
      time_types: [],
      excuse_types: [],
      day_models: [],
      pay_types: [],
      pay_models: [],
      shift_models: [],
      flex_shift_models: [],
      firms: [],
      accounts: [],
      tab: "update",
      check_in: false,
      check_out: false,
      excuse_type: null,
      firm: null,
      check_options: [
        "Yalnızca Giriş Zamanı Olanlar",
        "Yalnızca Çıkış Zamanı Olanlar",
      ],
      check: "Giriş - Çıkış",
      f_firms: [],
      f_employees: [],
      f_excuse_types: [],
      defs: {},
    };
  },
  mounted() {
    //this.load({ pagination: this.pagination })
    this.load_api_defs();
    this.load_api_groups();
    let params = this.$route.params.my_params;

    if (params && Object.keys(params).length > 0) {
      let self = this;
      this.$set(this, "start", this.$route.params.my_params.tr_date);
      this.$set(this, "end", this.$route.params.my_params.tr_date);
      this.$set(this, "employee", this.$route.params.my_params.employee_id);
      self.apply_filter();
    } else {
      this.load({ pagination: this.pagination });
    }
    this.$store.dispatch("refresh", false);
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
  methods: {
    load_api_defs() {
      let self = this;
      Service.get("defs/api/defs", {})
        .then((response) => {
          self.$set(self, "time_types", response.data.time_types);
          self.$set(self, "excuse_types", response.data.excuse_types);
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
      Service.get("defs/api/groups", {})
        .then((response) => {
          response;
          self.$set(self, "accounts", response.data.accounts);
        })
        .catch((error) => {
          this.um("Bir hata oluştu! " + error);
        });
    },
    check_transaction(e, obj) {
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
      Service.get("ops/check_transaction", {
        geco_id: obj.geco_id,
      })
        .then((response) => {
          self.$set(self, "can_update", response.data.can_update);
          self.$set(self, "is_removed", response.data.is_removed);
          clone.tr_date = date.formatDate(clone.tr_date, "YYYY-MM-DD");
          clone.description = "";
          clone.is_remove_request = false;
          self.$set(self, "record", clone);
          self.$set(self, "active", obj);
          self.$set(self, "history", response.data.history);
          self.$set(self, "tab", "update");
          self.$set(self, "dialog", true);
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
      this.$store.dispatch("refresh", false);
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
      let filter = self.filter;
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
      if (sett.employee || self.employee)
        params["employee"] = sett.employee ? sett.employee : self.employee;
      if (self.check_in) params["end__isnull"] = true;
      if (self.check_out) params["start__isnull"] = true;
      if (self.excuse_type) params["excuse_type"] = self.excuse_type;
      if (self.firm) params["firm"] = self.firm;

      Service.get("ops/transactions", params)
        .then((response) => {
          self.$set(self, "data", response.data.results);
          self.$set(self, "employees", response.data.employees);
          let firms = response.data.employees.map((o) => o.firm);
          self.$set(self, "firms", [...new Set(firms)]);
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

    add_new_dialog(e, obj) {
      // if (
      //   !this.$store.getters["account/is_superuser"] &&
      //   !this.$store.getters["account/is_staff"] &&
      //   !this.$store.getters["account/perm_check"]("changes.add_changes")
      // ) {
      //   this.hm("Bu işlem için yetkiniz bulunmuyor!");
      //   return;
      // }
      let self = this;

      Service.get("defs/api/defs")
        .then((response) => {
          self.$set(self, "defs", response.data);
          self.$set(self, "new_dialog", true);
        })
        .catch((error) => {
          if (error.response && error.response.data) {
            if (error.response.data.custom) {
              this.um(error.response.data.message);
            } else this.um("Bir hata oluştu! " + error);
          } else this.um("Bir hata oluştu! " + error);
        });
    },

    apply_filter() {
      let pagination = this.pagination;
      pagination.page = 1;
      this.load({ pagination });
    },
  },
  watch: {
    check: function (value) {
      if (value === this.check_options[0]) {
        this.check_in = true;
        this.check_out = false;
      } else if (value === this.check_options[1]) {
        this.check_out = true;
        this.check_in = false;
      } else {
        this.check = "Giriş - Çıkış";
        this.check_in = false;
        this.check_out = false;
      }
    },

    "$store.state.transactions.refresh": function (value) {
      if (value === true) {
        this.refresh();
        this.new_dialog = false;
      }
    },
  },
};
</script>
