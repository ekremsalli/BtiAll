<template>
  <q-form
    ref="form"
    autocorrect="off"
    autocapitalize="off"
    autocomplete="off"
    spellcheck="false"
  >
    <div class="q-pa-md">
      <div class="row">
        <div class="col">
          <q-select
            v-model="record.employee_id"
            :options="f_employees"
            input-debounce="0"
            label="Personel"
            option-value="employee_id"
            option-label="title"
            options-dense
            emit-value
            map-options
            filled
            style="min-width: 200px"
            class="q-mb-sm"

            options-cover
            :rules="[(val) => val || 'Lütfen bir personel seçiniz.']"
            clearable
            @filter="
              (val, update, abort) => {
                filter_fn(
                  val,
                  update,
                  abort,
                  'title',
                  'f_employees',
                  employees
                );
              }
            "
            use-input
          >
          </q-select>
        </div>
      </div>

      <div class="row">
        <div class="col">
          <q-input
            class="q-mr-sm q-mb-sm"
            filled
            label="Tarih"
            v-model="record.tr_date"
            :disable="record.is_remove_request"
            :rules="[(val) => (val && !val.length < 1) || 'Lütfen bir tarih giriniz.']"
           
          >
            <template #append>
              <q-icon name="event" class="cursor:pointer">
                <q-popup-proxy
                  ref="qTDateProxy"
                  transition-show="scale"
                  anchor="bottom middle"
                  transition-hide="scale"
                >
                  <q-date v-model="record.tr_date" mask="YYYY-MM-DD" today-btn>
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Kapat" color="primary" flat />
                    </div>
                  </q-date>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </div>
        <div class="col">
          <q-select
            v-model="record.day_types"
            :options="day_types"
            label="Gün Tipi"
            option-value="id"
            option-label="title"
            options-dense
            emit-value
            map-options
            filled
            style="min-width: 200px"
            menu-anchor="bottom right"
            options-cover
            clearable
          >
          </q-select>
        </div>
      </div>

      <div class="row">
        <div class="col">
          <q-input
            :disable="record.is_remove_request"
            class="q-mr-sm"
            label="Giriş"
            filled
            v-model="record.start"
            mask="time"
            :rules="['time']"
          >
            <template v-slot:append>
              <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy transition-show="scale" transition-hide="scale">
                  <q-time v-model="record.start" now-btn>
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Kapat" color="primary" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </div>
        <div class="col">
          <q-input
            label="Çıkış"
            filled
            v-model="record.end"
            mask="time"
            :disable="record.is_remove_request"
            :rules="['time']"
          >
            <template v-slot:append>
              <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy transition-show="scale" transition-hide="scale">
                  <q-time v-model="record.end" now-btn>
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Kapat" color="primary" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </div>
      </div>

      <div class="row">
        <div class="col">
          <q-select
            v-model="record.time_type"
            :options="time_types"
            label="Zaman tipi"
            option-value="code"
            :option-label="(o) => o.code + ' (' + o.name + ')'"
            options-dense
            emit-value
            map-options
            filled
            style="min-width: 200px"
            class="q-mr-sm"
            menu-anchor="bottom middle"
            :disable="record.is_remove_request"
            options-cover
            clearable
          >
          </q-select>
        </div>
        <div class="col">
          <q-select
            v-model="record.excuse_type"
            :options="excuse_types"
            label="Mazeret tipi"
            option-value="code"
            :option-label="(o) => o.code + ' (' + o.name + ')'"
            options-dense
            emit-value
            map-options
            filled
            style="min-width: 200px"
            menu-anchor="bottom middle"
            :disable="record.is_remove_request"
            options-cover
            clearable
          >
          </q-select>
        </div>
      </div>

      <div class="row q-mt-sm">
        <div class="col">
          <q-select
            v-model="record.day_model"
            :options="day_models"
            label="Gün modeli"
            option-value="code"
            :option-label="(o) => o.code + ' (' + o.name + ')'"
            class="q-mr-sm"
            options-dense
            emit-value
            map-options
            filled
            style="min-width: 200px"
            menu-anchor="bottom middle"
            options-cover
            clearable
            :rules="[
              (val) => (val && val.length) || 'Lütfen bir gün modeli seçiniz.',
            ]"
          >
          </q-select>
        </div>
        <div class="col">
          <q-select
            v-model="record.excuse_day"
            :options="excuse_days"
            label="Gün"
            option-value="id"
            option-label="title"
            options-dense
            emit-value
            map-options
            filled
            style="min-width: 200px"
            menu-anchor="bottom right"
            options-cover
            clearable
          >
          </q-select>
        </div>
      </div>

      <div class="row q-mt-sm">
        <div class="col">
          <q-select
            v-model="record.account"
            :options="accounts"
            label="Hesap grubu"
            option-value="code"
            :option-label="(o) => o.code + ' (' + o.description + ')'"
            options-dense
            emit-value
            map-options
            filled
            style="min-width: 200px"
            menu-anchor="bottom middle"
            class="q-mr-sm"
            options-cover
            clearable
          >
          </q-select>
        </div>
        <div class="col">
          <q-select
            v-model="record.pay_type"
            :options="pay_models"
            label="Puantaj tipi"
            option-value="code"
            :option-label="(o) => o.code + ' (' + o.name + ')'"
            options-dense
            emit-value
            map-options
            filled
            style="min-width: 200px"
            menu-anchor="bottom middle"
            options-cover
            clearable
          >
          </q-select>
        </div>
      </div>

      <div class="row">
        <div class="col">
          <q-editor
            class="q-mt-sm"
            placeholder="Açıklama"
            v-model="record.description"
            min-height="5rem"
          />
        </div>
      </div>

      <q-card-actions class="action_buttons">
        <q-btn flat label="İptal" color="black" v-close-popup />
        <q-space />
        <q-btn
          :disabled="
            !record.employee_id ||
            !record.tr_date ||
            !record.start ||
            !record.end ||
            !record.day_model
          "
          color="primary"
          label="Yeni Kayıt Ekle"
          @click="add_new_record"
        />
      </q-card-actions>
    </div>
  </q-form>
</template>

<script>
import Service from "boot/service";
import { common } from "src/mixins/common";
import { ref } from "vue";
export default {
  name: "NewAddTransactionForm",
  mixins: [common],
  data() {
    return {
      record: {
        description: "",
        employee_id: null,
      },
      f_employees: [],
      options: null,
    };
  },
  props: {
    // record: {
    //   type: Object,
    //   required: true
    // },
    defs: {
      type: Object,
      default() {
        return {};
      },
    },
    employees: {
      type: Array,
      default() {
        return [];
      },
    },
    time_types: {
      type: Array,
      default() {
        return [];
      },
    },
    excuse_types: {
      type: Array,
      default() {
        return [];
      },
    },
    day_models: {
      type: Array,
      default() {
        return [];
      },
    },
    day_types:{
      type: Array,
      default() {
        return [
          { id: -1, title: "Dün" },
          { id: 0, title: "Bugün" },
          { id: 1, title: "Sonraki Gün" },
        ];
      },
    },
    excuse_days: {
      type: Array,
      default() {
        return [
          { id: 0, title: "Tam gün" },
          { id: 1, title: "Öğleden önce" },
          { id: 2, title: "Öğleden sonra" },
        ];
      },
    },
    accounts: {
      type: Array,
      default() {
        return [];
      },
    },
    pay_models: {
      type: Array,
      default() {
        return [];
      },
    },

    transactions: {
      type: Array,
      default() {
        return [];
      },
    },

    anomalies: {
      type: Array,
      default() {
        return [];
      },
    },
    app: {
      type: Object,
      required: false,
    },
  },

  methods: {
    push_transaction() {
      let self = this;
      const my_params = {
        employee_id: self.app.selected_transaction.employee_id,
        tr_date: self.app.selected_transaction.tr_date,
      };
      this.$router.push({ name: "ops/transactions", params: { my_params } });
    },
    add_new_record() {
      const params = this.record;

      params.start = params.tr_date + " " + params.start;
      params.end = params.tr_date + " " + params.end;
      Service.post(`excuse`, params)
        .then((response) => {
          this.$store.dispatch("refresh", true);
          this.bm("Yeni kayıt eklendi!");
        })
        .catch((err) => {
          this.um("Yeni kayıt eklenirken bir hata oluştu! -> " + err);
        });
    },

    filterFn(val) {

    },
  },
};
</script>

<style>
.action_buttons {
  width: 100%;
  padding-right: 0;
  margin-top: 6px;
}
</style>
