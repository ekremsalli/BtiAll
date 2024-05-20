<template>
  <q-page padding>
    <q-toolbar class="bg-grey-3 text-black">
      <q-toolbar-title>
        Bordro
      </q-toolbar-title>
      <q-space />
      <q-btn
        :loading="loading"
        @click="load_dbs()"
        flat
        round
        dense
        icon="fas fa-sync-alt"
      >
        <q-tooltip>
          Yenile
        </q-tooltip>
      </q-btn>
      <q-btn
          :disable="filter.db === null || payrolls_data === false"
          style="max-height: 55px; min-height: 55px"
          color="primary"
          @click="save_csv()"
          class="on-right"
          label="CSV Kaydet"
        />

        <q-btn
          :disable="filter.db === null || payrolls_data === false"
          style="max-height: 55px; min-height: 55px"
          color="red"
          @click="save_excel()"
          class="on-right"
          label="XLS Kaydet"
        />
        <q-btn
          :disable="filter.db === null || payrolls_data === false"
          style="max-height: 55px; min-height: 55px"
          color="secondary"
          @click="save_ftp()"
          class="on-right"
          label="FTP Aktar"
          :loading="sending"
          unelevated
        >
        </q-btn>
    </q-toolbar>
    <q-table hide-no-data dense>
      <template v-slot:top >
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
                clearable
                hide-dropdown-icon
                filled
                class="q-mr-sm"
                @keyup.enter="load()"
                >
              </q-select>
            </div>
            <div class="row col-3">
              <div class="col-6">
                <q-input
                  :disable="filter.db === null"
                  filled
                  label="Başlangıç"
                  v-model="filter.start"
                  mask="date"
                  readonly

                  @keyup.enter="load()"
                >
                  <template #append>
                    <q-icon name="event" class="cursor:pointer">
                      <q-popup-proxy
                        ref="qSDateProxy"
                        transition-show="scale"
                        anchor="bottom middle"
                        transition-hide="scale"
                      >
                        <q-date v-model="filter.start">
                          <div class="row items-center justify-end">
                            <q-btn v-close-popup label="Kapat" color="primary" flat />
                          </div>
                        </q-date>
                      </q-popup-proxy>
                    </q-icon>
                  </template>
                </q-input>
              </div>
              <div class="col-6">
                <q-input
                  :disable="filter.db === null"
                  class="q-ml-sm q-mr-sm"
                  filled
                  label="Bitiş"
                  v-model="filter.end"
                  mask="date"
                  readonly
                  @keyup.enter="load()"
                >
                <template #append>
                  <q-icon name="event" class="cursor:pointer">
                    <q-popup-proxy
                      ref="qEDateProxy"
                      transition-show="scale"
                      anchor="bottom middle"
                      transition-hide="scale"
                    >
                      <q-date v-model="filter.end">
                        <div class="row items-center justify-end">
                          <q-btn v-close-popup label="Kapat" color="primary" flat />
                        </div>
                      </q-date>
                    </q-popup-proxy>
                  </q-icon>
                </template>
              </q-input>
              </div>
            </div>
            <div class="row col-5">
              <div class="col-6">
                <q-select
                  :disable="filter.db === null"
                  v-model="filter.firm"
                  :options="f_firms"
                  :option-label="o => o.description"
                  option-value="code"
                  label="Firma"
                  filled
                  multiple
                  input-debounce="1"
                  options-dense
                  emit-value
                  map-options
                  clearable
                  hide-dropdown-icon
                  use-input
                  @filter="(val, update, abort) => { filter_fn(val, update, abort, 'description', 'f_firms', firms) }"
                  class="q-mr-sm"
                  style="height: 56px; overflow-y: auto"
                  @keyup.enter="load()"
                >
                </q-select>
              </div>
              <div class="col-6">
                <q-select
                  filled
                  v-model="filter.employees"
                  input-debounce="0"
                  multiple
                  :options="f_employees"
                  :option-label="o => `${o.name} ${o.surname} - (${o.firm})`"
                  option-value="nr"
                  label="Personel"
                  emit-value
                  map-options
                  clearable
                  hide-dropdown-icon
                  use-input
                  @filter="(val, update, abort) => { filter_fn(val, update, abort, 'title', 'f_employees', c_employees) }"
                  class="q-mr-sm"
                  style="height: 56px; overflow-y: auto"
                  @keyup.enter="load()"
                />
              </div>
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
                  hide-dropdown-icon
                  filled
                  clearable
                  class="q-ml-sm q-mr-sm"
                  @keyup.enter="load()"
                >
                </q-select>
              </div>
            <div class="col-1">
              <q-btn
                :disable="filter.db === null"
                style="max-height: 55px; min-height: 55px"
                :style="{ width: '100%', height: '100%' }"
                color="black"
                @click="load()"
                label="Getir"
              />
            </div>
          </div>
        </div>
      </template>
    </q-table>

      <div class="row items-start q-gutter-md p-cards">
        <template class="col-md-4"
            v-for="item in data">
          <q-card
            class="my-card"
            style="max-width: 400px; min-width: 400px"
          >
            <q-card-section class="bg-primary text-white">
              <div class="text-h6">{{ `${item.name} ${item.surname}` }}</div>
              <div class="text-subtitle2">{{ item.people_soft_id }}</div>
              <div class="card-list">
                <div>
                  Grup 1: <span>{{ item.group1 }}</span>
                </div>
                <div>
                  Grup 2: <span>{{ item.group2 }}</span>
                </div>
                <div>
                  Grup 3: <span>{{ item.group3 }}</span>
                </div>
                <div>
                  Grup 4: <span>{{ item.group4 }}</span>
                </div>
              </div>
            </q-card-section>

            <q-separator />

            <q-card-actions align="right">
              <q-btn flat @click="detail(item)">DETAY</q-btn>
            </q-card-actions>
          </q-card>
        </template>
      </div>
    </div>

    <q-dialog
      v-model="dialog"
      persistent
      :maximized="toggle"
      transition-show="slide-up"
      transition-hide="slide-down"
    >
      <template v-if="active">
        <q-card class="bg-primary text-white">
          <q-bar>
            <q-space />

            <q-btn
              dense
              flat
              icon="minimize"
              @click="toggle = false"
              :disable="!toggle"
            >
              <q-tooltip v-if="toggle" class="bg-white text-primary"
                >Küçült</q-tooltip
              >
            </q-btn>
            <q-btn
              dense
              flat
              icon="crop_square"
              @click="toggle = true"
              :disable="toggle"
            >
              <q-tooltip v-if="!toggle" class="bg-white text-primary"
                >Büyült</q-tooltip
              >
            </q-btn>
            <q-btn dense flat icon="close" v-close-popup>
              <q-tooltip class="bg-white text-primary">Kapat</q-tooltip>
            </q-btn>
          </q-bar>

          <q-card-section>
            <div class="text-h6 q-pa-none q-ma-none">{{ active.name + " " + active.surname }}</div>
          </q-card-section>

          <q-card-section class="q-pt-none text-black">
            <div class="q-pa-none">
              <div class="q-gutter-y-md">
                <q-card>
                  <q-tabs
                    v-model="tab"
                    dense
                    class="text-grey"
                    active-color="primary"
                    indicator-color="primary"
                    align="justify"
                    narrow-indicator
                    default
                  >
                    <q-tab name="geco" label="GECO" />
                    <q-tab name="daily" label="DAILY" />
                    <q-tab name="monthly" label="MONTHLY" />
                  </q-tabs>

                  <q-separator />

                  <q-tab-panels v-model="tab" animated>
                    <q-tab-panel name="geco" >
                      <q-table
                        class="tab-q-table"
                        :data="active.geco"
                        :columns="geco_columns"
                        dense
                        row-key="id"
                        binary-state-sort
                        no-data-label="Hareket bulunamadı!"
                        :rows-per-page-options="[0]"
                      >
                      </q-table>
                    </q-tab-panel>

                    <q-tab-panel name="daily">
                      <q-table
                        class="tab-q-table"
                        :data="active.daily"
                        :columns="daily_columns"
                        dense
                        row-key="id"
                        binary-state-sort
                        no-data-label="Hareket bulunamadı!"
                        :rows-per-page-options="[0]"
                        hide-bottom
                      >
                      </q-table>
                    </q-tab-panel>

                    <q-tab-panel name="monthly">
                      <q-markup-table>
                        <template>
                                <thead>
                                  <tr>
                                    <th class="text-left"  v-for="key in Object.keys(active.monthly.totals)">
                                      <td>{{ key }}</td>
                                    </th>
                                  </tr>
                                </thead>
                                <tbody>
                                  <tr>
                                    <th class="text-left"  v-for="value in Object.values(active.monthly.totals)">
                                      <td>{{  value }}</td>
                                    </th>
                                  </tr>
                                </tbody>
                        </template>
                      </q-markup-table>

                    </q-tab-panel>
                  </q-tab-panels>
                </q-card>
              </div>
            </div>
          </q-card-section>
        </q-card>
      </template>
    </q-dialog>
    <a ref="download" />
  </q-page>
</template>

<script>
import Service from "boot/service";
import { common } from "src/mixins/common";
import TransactionForm from "components/TransactionForm";
import ChangeHistory from "components/ChangeHistory";
import Dashboard from "../Dashboard.vue";
import XLSX from "xlsx";
import { date } from "quasar";

export default {
  name: "ops_transaction",
  mixins: [common],
  components: {
    TransactionForm,
    ChangeHistory,
    Dashboard,
  },
  data() {
    return {
      loading: true,
      data: [],
      dbs: [],
      f_firms: [],
      f_employees: [],
      firms: [],
      filter: {
        start: date.formatDate(
          date.adjustDate(Date.now(), { date: 1 }),
          "YYYY/MM/DD"
        ),
        end: date.formatDate(Date.now(), "YYYY/MM/DD"),
      },
      employees: [],
      employees_list: [],
      dialog: false,
      firm: null,
      active: null,
      toggle: true,
      tab: "geco",
      geco_columns: [],
      daily_columns: [],
      payrolls_data: false,
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
      sending: false,
    };
  },

  mounted() {
    this.load_dbs();
  },
  computed: {
    c_employees() {
      let self = this;
      if (this.filter.firm) {
        return this.employees.filter((o) => this.filter.firm.includes(o.firm));
      }
      return this.employees;
    },
  },
  methods: {
    load_dbs() {
      let self = this;
      Service.get("defs/dbs", {})
        .then((response) => {
          self.$set(self, "dbs", response.data.dbs);
          self.$set(self.filter, "db", response.data.default.code);
          self.$set(self, "firms", response.data.companies);
          self.$set(self, "employees_list", response.data.employees);
          self.$set(self, "employees", response.data.employees);
        })
        .catch((error) => {
          this.um("Bir hata oluştu!" + error);
        })
        .finally(() => {
          this.$set(this, "loading", false);
        });
    },
    load() {
      let self = this;
      let filter = self.filter;
      if (!filter.db || !filter.start || !filter.end) {
        self.um("Lütfen tüm bilgileri doldurun!");
        return;
      }
      if (self.firm) filter["firm[]"] = self.firm;
      if (!filter.employees) delete filter.employees;
      if (self.collar) filter["worker_type"] = self.collar;

      this.$set(this, "loading", true);
      this.$set(this, "data", []);

      Service.post("ops/payroll", filter)
        .then((response) => {
          if (response.data.employees && response.data.employees.length > 0) {
            if (response.data.employees[0].geco) {
              if (response.data.employees[0].geco[0]) {
                let geco_cols = Object.keys(response.data.employees[0].geco[0]);
                let blacklist = ["CalismaId"];
                let localization = {
                  BaslaTarihi: "Başlangıç tarihi",
                  BitisTarihi: "Bitiş tarihi",
                };
                let mapped_geco_cols = geco_cols
                  .filter((o) => !blacklist.includes(o))
                  .map((o) => {
                    return {
                      field: o,
                      label: o in localization ? localization[o] : o,
                      name: o,
                      sortable: true,
                      align: "left",
                    };
                  });
                self.$set(self, "geco_columns", mapped_geco_cols);
              }
            }

            if (response.data.employees[0].daily) {
              if (response.data.employees[0].daily[0]) {
                let daily_cols = Object.keys(
                  response.data.employees[0].daily[0]
                );
                let localization = {
                  BaslaTarihi: "Başlangıç tarihi",
                  BitisTarihi: "Bitiş tarihi",
                };
                let mapped_daily_cols = daily_cols.map((o) => {
                  return {
                    field: o,
                    label: o in localization ? localization[o] : o,
                    name: o,
                    sortable: true,
                    align: "left",
                  };
                });
                self.$set(self, "daily_columns", mapped_daily_cols);
              }
            }
          }
          self.$set(self, "data", response.data.employees);
          self.payrolls_data = true;
        })
        .catch((error) => {
          this.um("Bir hata oluştu!" + error);
        })
        .finally(() => {
          this.$set(this, "loading", false);
        });
    },

    save_csv() {
      let self = this;
      let payrolls = [];
      self.data.forEach((emp) => {
        Object.keys(emp.monthly.totals).forEach((item) => {
          let temp = [];
          temp.push(emp.people_soft_id);
          temp.push(emp.monthly.month);
          temp.push(emp.monthly.year);
          temp.push("tl");
          temp.push(item);
          temp.push(emp.monthly.totals[item]);
          payrolls.push(temp);
        });
      });

      var wb = XLSX.utils.book_new();
      var ws = XLSX.utils.json_to_sheet(payrolls, { skipHeader: 1 });
      XLSX.utils.book_append_sheet(wb, ws, "Bordro");

      var wbout = XLSX.write(wb, { bookType: "csv", type: "array" });
      let blob = new Blob([wbout], { type: "application/octet-stream" });

      try {
        self.$refs["download"].href = URL.createObjectURL(blob);
        self.$refs["download"].download = "bordro.csv";
        self.$refs["download"].click();
        self.bm("CSV dosya indirme işlemi başarılı");
      } catch (err) {
        this.um("İndirme işleminde bir hata oluştu" + err);
      }
    },

    save_excel() {
      let self = this;
      let payrolls = [];
      self.data.forEach((emp) => {
        let temp = emp.monthly.totals;
        temp.title = `${emp.name} ${emp.surname}`;
        payrolls.push(temp);
      });
      var wb = XLSX.utils.book_new();
      var ws = XLSX.utils.json_to_sheet(payrolls, { skipHeader: 0 });
      XLSX.utils.book_append_sheet(wb, ws, "Bordro");
      var wbout = XLSX.write(wb, { bookType: "xlsx", type: "array" });
      let blob = new Blob([wbout], { type: "application/octet-stream" });
      try {
        self.$refs["download"].href = URL.createObjectURL(blob);
        self.$refs["download"].download = "bordro.xlsx";
        self.$refs["download"].click();
        self.bm("XLSX dosya indirme işlemi başarılı");
      } catch (err) {
        this.um("İndirme işleminde bir hata oluştu" + err);
      }
    },

    save_ftp() {
      this.sending = true;
      const intervals = null;

      let self = this;
      let payrolls = [];
      self.data.forEach((emp) => {
        Object.keys(emp.monthly.totals).forEach((item) => {
          let temp = [];
          temp.push(emp.people_soft_id);
          temp.push(emp.monthly.month);
          temp.push(emp.monthly.year);
          temp.push("tl");
          temp.push(item);
          temp.push(emp.monthly.totals[item]);
          payrolls.push(temp);
        });
      });

      Service.put("ops/payroll", payrolls)
        .then((response) => {
          if (response.data.success === true) {
            self.sending = false;

            self.bm("FTP aktarması başarılı!");
          }
        })
        .catch((e) => {
          this.um("FTP aktarımında bir sorun oluştu. " + err);
        });
    },

    detail(item) {
      this.$set(this, "active", item);
      this.$set(this, "dialog", true);
    },
  },
};
</script>

<style scoped>
#annualTable {
  margin-top: 10px;
}

.p-cards {
  margin-top: 10px;
}

.card-list {
  margin-top: 10px;
}

.card-list > div {
  padding-top: 5px;
}

.card-list > div > span {
  font-weight: bold;
}

.q-tab-table {
  height: 100% !important;
}
</style>
