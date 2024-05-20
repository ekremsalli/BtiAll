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
            v-model="record.employee"
            :options="employees"
            label="Personel"
            option-value="id"
            option-label="title"
            options-dense
            emit-value
            map-options
            filled
            style="min-width:200px"
            class="q-mb-sm"
            menu-anchor="bottom middle"
            disabled
            readonly
            options-cover
          >
          </q-select>
        </div>
      </div>

      <div class="col" v-if="transactions.length > 0">
          <q-select
            :options="transactions"
            label="Bu güne ait diğer hareketler"
            :option-label="
              o =>
                `${o.start ? o.start : ''} ${o.end ? o.end : ''} ${
                  o.time_type ? o.time_type : ''
                } ${o.excuse_type ? o.excuse_type : ''}`
            "
            v-model="app.selected_transaction"
            options-dense
            filled
            style="min-width:200px"
            class="q-mb-sm"
            menu-anchor="bottom middle"
            options-cover
            @input="push_transaction()"
          >
          </q-select>
      </div>

      <div class="col" v-if="anomalies.length > 0">
        <q-select
          :options="anomalies"
          v-model="app.selected_anomaly"
          label="Bugüne ait diğer anormallikler"
          option-value="id"
          :option-label="o => `${o.geco_id} ${o.ano_text} (${o.ano_type})`"
          options-dense
          emit-value
          map-options
          filled
          style="min-width:200px"
          class="q-mb-sm"
          menu-anchor="bottom middle"
          options-cover
        >
        </q-select>
      </div>

      <div class="row">
        <div class="col">
          <q-input
            class="q-mr-sm q-mb-sm"
            filled
            label="Tarih"
            v-model="record.tr_date"
            :disable="record.is_remove_request"
          >
            <template #append>
              <q-icon name="event" class="cursor:pointer">
                <q-popup-proxy
                  ref="qTDateProxy"
                  transition-show="scale"
                  anchor="bottom middle"
                  transition-hide="scale"
                >
                  <q-date v-model="record.tr_date" mask="YYYY-MM-DD">
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
          <q-input
            type="number"
            dense
            v-model.number="record.work_time"
            label="Süre"
            :disable="record.is_remove_request"
          />
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
                  <q-time v-model="record.start">
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
                  <q-time v-model="record.end">
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
            :option-label="o => o.code + ' (' + o.name + ')'"
            options-dense
            emit-value
            map-options
            filled
            style="min-width:200px"
            class="q-mr-sm"
            menu-anchor="bottom middle"
            :disable="record.is_remove_request"
            options-cover
          >
          </q-select>
        </div>
        <div class="col">
          <q-select
            v-model="record.excuse_type"
            :options="excuse_types"
            label="Mazeret tipi"
            option-value="code"
            :option-label="o => o.code + ' (' + o.name + ')'"
            options-dense
            emit-value
            map-options
            filled
            style="min-width:200px"
            menu-anchor="bottom middle"
            :disable="record.is_remove_request"
            options-cover
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
            :option-label="o => o.code + ' (' + o.name + ')'"
            class="q-mr-sm"
            options-dense
            emit-value
            map-options
            filled
            :disable="record.is_remove_request"
            style="min-width:200px"
            menu-anchor="bottom middle"
            options-cover
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
            style="min-width:200px"
            menu-anchor="bottom right"
            :disable="record.is_remove_request"
            options-cover
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
            :option-label="o => o.code + ' (' + o.description + ')'"
            options-dense
            emit-value
            map-options
            filled
            style="min-width:200px"
            menu-anchor="bottom middle"
            class="q-mr-sm"
            :disable="record.is_remove_request"
            options-cover
          >
          </q-select>
        </div>
        <div class="col">
          <q-select
            v-model="record.pay_type"
            :options="pay_models"
            label="Puantaj tipi"
            option-value="code"
            :option-label="o => o.code + ' (' + o.name + ')'"
            options-dense
            emit-value
            map-options
            filled
            style="min-width:200px"
            menu-anchor="bottom middle"
            :disable="record.is_remove_request"
            options-cover
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
    </div>
  </q-form>
</template>

<script>
export default {
  props: {
    record: {
      type: Object,
      required: true
    },
    employees: {
      type: Array,
      default() {
        return [];
      }
    },
    time_types: {
      type: Array,
      default() {
        return [];
      }
    },
    excuse_types: {
      type: Array,
      default() {
        return [];
      }
    },
    day_models: {
      type: Array,
      default() {
        return [];
      }
    },
    excuse_days: {
      type: Array,
      default() {
        return [
          { id: 0, title: "Tam gün" },
          { id: 1, title: "Öğleden önce" },
          { id: 2, title: "Öğleden sonra" }
        ];
      }
    },
    accounts: {
      type: Array,
      default() {
        return [];
      }
    },
    pay_models: {
      type: Array,
      default() {
        return [];
      }
    },

    transactions: {
      type: Array,
      default() {
        return [];
      }
    },

    anomalies: {
      type: Array,
      default() {
        return [];
      }
    },
    app: {
      type: Object,
      required: false
    }
  },
  methods: {
    push_transaction (){
      let self = this;
      const my_params = {
        employee_id: self.app.selected_transaction.employee_id,
        tr_date: self.app.selected_transaction.tr_date
      }
      this.$router.push({name:"ops/transactions", params:{my_params}});
    }
  }
};
</script>
