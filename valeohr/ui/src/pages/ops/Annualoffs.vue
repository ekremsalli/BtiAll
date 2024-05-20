<template>
  <q-page padding>
    <q-toolbar class="bg-grey-3 text-black">
      <q-toolbar-title> Yıllık İzinler </q-toolbar-title>
      <q-btn
        class="q-mr-xs q-px-sm"
        :loading="loading"
        @click="load_dbs()"
        flat
        round
        dense
        icon="fas fa-sync-alt"
      >
        <q-tooltip> Yenile </q-tooltip>
      </q-btn>
      <q-btn
        label="Yeni Kayıt Ekle"
        class="q-ml-sm q-mr-xs q-px-sm"
        type="submit"
        color="primary"
      />
      <q-btn
        label="Temizle"
        type="reset"
        color="primary"
        flat
        class="q-ml-sm q-mr-xs q-px-sm"
      />
    </q-toolbar>
    <q-table dense>
      <template v-slot:top>
        <div id="annualTable" :style="{ width: '100%', height: '100%' }">
          <div class="row flex" :style="{ width: '100%', height: '100%' }">
            <div class="col-1">
              <q-select
                v-model="filter.db"
                :options="dbs"
                label="Veritabanı"
                option-value="code"
                option-label="title"
                outlined
                options-dense
                emit-value
                map-options
                filled
                hide-dropdown-icon
                style="max-height: 56px"
              >
              </q-select>
            </div>
            <div class="col-3">
              <q-select
                v-model="filter.firm"
                :disable="filter.db === null"
                :options="f_firms"
                label="Firma"
                :option-label="(o) => o.code"
                option-value="code"
                outlined
                input-debounce="0"
                options-dense
                emit-value
                hide-dropdown-icon
                map-options
                filled
                clearable
                multiple
                use-input
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
                @keyup.enter="load()"
              >
              </q-select>
            </div>
            <div class="col-3">
              <q-select
                v-if="filter.db"
                :disable="filter.db === null"
                v-model="filter.employee"
                :options="f_employees"
                label="Personel"
                use-input
                option-value="id"
                :option-label="(o) => `${o.name} ${o.surname}`"
                outlined
                options-dense
                emit-value
                map-options
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
                @keyup.enter="load()"
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
            <div class="col-1">
              <q-select
                v-if="filter.db"
                :disable="filter.db === null"
                v-model="filter.year"
                :options="years"
                label="Yıl"
                option-value="id"
                option-label="title"
                outlined
                options-dense
                emit-value
                map-options
                hide-dropdown-icon
                filled
                clearable
                class="q-ml-sm q-mr-sm"
                @keyup.enter="load()"
              >
              </q-select>
            </div>
            <div class="col-1">
              <q-select
                v-if="filter.db"
                :disable="filter.db === null"
                v-model="filter.month"
                :options="months"
                label="Ay"
                option-value="id"
                option-label="title"
                outlined
                options-dense
                emit-value
                map-options
                filled
                clearable
                hide-dropdown-icon
                class="q-ml-sm q-mr-sm"
                @keyup.enter="load()"
              >
              </q-select>
            </div>
            <div class="col-1">
              <q-btn
                color="black"
                @click="load()"
                label="Getir"
                :style="{ width: '100%', height: '100%' }"
              />
            </div>
          </div>

          <template v-if="type_controller == 'year'">
            <FullCalendar :data="data" :year="filter.year" />
          </template>

          <template v-else-if="ready">
            <annual-monthly-table
              :days="days"
              :data="pre_data"
              :name="pre_name"
              @show_panel="show_panel"
            ></annual-monthly-table>
            <annual-monthly-total
              :days="days"
              :data="pre_report"
            ></annual-monthly-total>

            <annual-monthly-table
              :days="days"
              :data="cur_data"
              :name="cur_name"
              @show_panel="show_panel"
            ></annual-monthly-table>
            <annual-monthly-total
              :days="days"
              :data="cur_report"
            ></annual-monthly-total>

            <annual-monthly-table
              :days="days"
              :data="nxt_data"
              :name="nxt_name"
              @show_panel="show_panel"
            ></annual-monthly-table
            >""
            <annual-monthly-total
              :days="days"
              :data="nxt_report"
            ></annual-monthly-total>
          </template>
        </div>
      </template>
    </q-table>
    <q-dialog
      transition-show="rotate"
      v-model="panel_show"
      transition-hide="rotate"
      style="min-width: 700px"
    >
      <q-card style="min-width: 700px; max-width: 400px">
        <q-card-section>
          <div class="text-h6">Yeni Yıllık İzin Kaydı</div>
          <hr />
        </q-card-section>

        <q-card-section class="q-pt-none">
          <div class="q-pa-sm">
            <q-form
              dense
              ref="add_excuse_form"
              class="q-gutter-md"
              @submit="add_new_annual()"
              @reset="reset()"
            >
              <div class="row">
                <div class="col-6">
                  <q-input
                    filled
                    label="Başlangıç"
                    v-model="record.start"
                    readonly
                    :rules="[
                      (val) =>
                        (val && val.length > 0) ||
                        'Lütfen giriş tarihi giriniz',
                    ]"
                  >
                    <template #append>
                      <q-icon name="event" class="cursor:pointer">
                        <q-popup-proxy
                          ref="qSDateProxy"
                          transition-show="scale"
                          anchor="bottom middle"
                          transition-hide="scale"
                        >
                          <q-date v-model="record.start" mask="YYYY-MM-DD">
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
                <div class="col-6 q-pl-sm">
                  <q-select
                    clearable
                    filled
                    color="primary"
                    v-model="record.start_annual_type"
                    :options="annual_off_type"
                    options-dense
                    emit-value
                    map-options
                    option-value="id"
                    :option-label="(o) => `${o.title}`"
                    label="Başlangıç Tipi"
                    :rules="[(val) => val > 0 || 'Lütfen tip seçiniz']"
                  />
                </div>
              </div>

              <div class="row">
                <div class="col-6">
                  <q-input
                    filled
                    label="Bitiş"
                    v-model="record.end"
                    readonly
                    :rules="[
                      (val) =>
                        (val && val.length > 0) ||
                        'Lütfen bitiş tarihi giriniz',
                    ]"
                  >
                    <template #append>
                      <q-icon name="event" class="cursor:pointer">
                        <q-popup-proxy
                          ref="qEDateProxy"
                          transition-show="scale"
                          anchor="bottom middle"
                          transition-hide="scale"
                        >
                          <q-date v-model="record.end" mask="YYYY-MM-DD">
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

                <div class="col-6 q-pl-sm">
                  <q-select
                    clearable
                    filled
                    color="primary"
                    v-model="record.end_annual_type"
                    :options="annual_off_type"
                    options-dense
                    emit-value
                    map-options
                    option-value="id"
                    :option-label="(o) => `${o.title}`"
                    label="Bitiş Tipi"
                    :rules="[(val) => val > 0 || 'Lütfen tip seçiniz']"
                  />
                </div>
              </div>

              <q-select
                clearable
                filled
                color="primary"
                v-model="record.excuse_type"
                :options="f_excuse_types"
                options-dense
                emit-value
                map-options
                option-value="code"
                :option-label="(o) => `${o.name} (${o.code})`"
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
                label="İzin Türü"
                :rules="[
                  (val) =>
                    (val && val.length > 0) || 'Lütfen izin türü seçiniz',
                ]"
              />

              <q-input
                v-model="record.description"
                label="Açıklama"
                hint="Zorunlu değil"
                filled
                type="textarea"
              />

              <div>
                <q-btn label="Yeni Kayıt Ekle" type="submit" color="primary" />
                <q-btn
                  label="Temizle"
                  type="reset"
                  color="primary"
                  flat
                  class="q-ml-sm"
                />
              </div>
            </q-form>
          </div>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Kapat" color="primary" v-close-popup />
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
import ChangeHistory from "components/ChangeHistory";
import Dashboard from "../Dashboard.vue";
import AnnualMonthlyTable from "components/AnnualMonthlyTable";
import AnnualMonthlyTotal from "components/AnnualMonthlyTotal";
import FullCalendar from "src/components/FullCalendar.vue";

export default {
  name: "ops_transaction",
  mixins: [common],
  components: {
    TransactionForm,
    ChangeHistory,
    Dashboard,
    AnnualMonthlyTable,
    AnnualMonthlyTotal,
    FullCalendar,
  },
  data() {
    return {
      loading: true,
      data: [],
      days: [
        "Pazartesi",
        "Salı",
        "Çarşamba",
        "Perşembe",
        "Cuma",
        "Cumartesi",
        "Pazar",
      ],
      months: [
        { id: 1, title: "Ocak" },
        { id: 2, title: "Şubat" },
        { id: 3, title: "Mart" },
        { id: 4, title: "Nisan" },
        { id: 5, title: "Mayıs" },
        { id: 6, title: "Haziran" },
        { id: 7, title: "Temmuz" },
        { id: 8, title: "Ağustos" },
        { id: 9, title: "Eylül" },
        { id: 10, title: "Ekim" },
        { id: 11, title: "Kasım" },
        { id: 12, title: "Aralık" },
      ],
      options: ["Google", "Facebook", "Twitter", "Apple", "Oracle"],
      years: [],
      employees: [],
      dbs: [],
      firms: [],
      filter: {},
      is_data_pulled: true,
      cur_data: [],
      cur_name: {},
      nxt_data: [],
      nxt_name: {},
      pre_data: [],
      pre_name: {},
      cur_report: [],
      nxt_report: [],
      pre_report: [],
      excuse_types: [],
      annual_off_type: [
        { title: "Tam Gün", id: 1 },
        { title: "Öğleden Önce", id: 2 },
        { title: "Öğleden Sonra", id: 3 },
      ],
      get_month: null,
      panel_show: false,
      excuse_type: null,
      start: null,
      end: null,
      personal_name: null,
      record: {
        db: null,
        start: null,
        end: null,
        employee: null,
        excuse_type: null,
        description: null,
        annual_off: true,
        start_annual_type: null,
        end_annual_type: null,
      },
      ready: false,
      f_firms: [],
      f_employees: [],
      f_excuse_types: [],
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
      type_controller: null,
    };
  },
  computed: {
    c_employees() {
      if (this.filter.firm) {
        return this.employees.filter((o) => this.filter.firm.includes(o.firm));
      }
      return this.employees;
    },
  },
  mounted() {
    let today = new Date();
    let years = [];
    for (let i = 0; i <= 10; i++) {
      years.push(today.getFullYear() - i);
    }
    this.$set(this, "years", years);
    this.load_dbs();
    this.load_api_defs();
  },
  methods: {
    load_dbs() {
      let self = this;
      Service.get("defs/dbs", {})
        .then((response) => {
          self.$set(self, "dbs", response.data.dbs);
          self.$set(self.filter, "db", response.data.default.code);
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
    load_api_defs() {
      let self = this;
      Service.get("defs/api/defs", {})
        .then((response) => {
          self.$set(self, "excuse_types", response.data.excuse_types);
        })
        .catch((error) => {
          this.um("Bir hata oluştu! " + error);
        });
    },
    load() {
      let self = this;
      self.$set(self, "ready", false);
      let filter = self.filter;
      filter.white_collar = self.collar;
      if (!filter.db || !filter.employee || !filter.year) {
        self.um("Lütfen tüm bilgileri doldurun!");
        return;
      }

      this.$set(this, "loading", true);
      this.$set(this, "data", null);

      Service.get("ops/annualoffs", filter)
        .then((response) => {
          self.$set(self, "type_controller", "month");
          if (response.data.data_type === "year") {
            self.$set(self, "data", response.data);
            self.$set(self, "type_controller", "year");
          } else {
            self.$set(self, "cur_data", response.data.cur_data);
            self.$set(self, "cur_name", response.data.cur_name);
            self.$set(self, "nxt_data", response.data.nxt_data);
            self.$set(self, "nxt_name", response.data.nxt_name);
            self.$set(self, "pre_data", response.data.pre_data);
            self.$set(self, "pre_name", response.data.pre_name);
            self.$set(self, "cur_report", response.data.cur_report);
            self.$set(self, "nxt_report", response.data.nxt_report);
            self.$set(self, "pre_report", response.data.pre_report);
          }
          self.$set(self, "ready", true);
          self.record.employee = self.filter.employee;
        })
        .catch((error) => {
          this.um("Bir hata oluştu!" + error);
        })
        .finally(() => {
          this.$set(this, "loading", false);
        });
    },
    show_panel() {
      this.panel_show = true;
    },
    add_new_annual() {
      let self = this;
      let record = self.record;
      record.db = this.filter.db;
      record.annual_off = true;
      record.employee = self.filter.employee;

      this.$set(this, "loading", true);
      Service.post("ops/changes", record)
        .then((response) => {
          self.$set(self, "record", {});
          if (self.$refs["add_excuse_form"])
            self.$refs["add_excuse_form"].reset();
          self.bm("Başarıyla eklendi!");
          self.$set(self, "panel_show", false);
          self.load();
        })
        .catch((error) => {
          this.um("Bir hata oluştu!" + error);
        })
        .finally(() => {
          this.$set(this, "loading", false);
        });
    },
    reset() {
      this.$set(this, "record", {});
    },
  },
};
</script>

<style scoped>
#annualTable {
  margin-top: 10px;
}
</style>
