<template>
  <q-page padding>
    <div class="row q-mt-sm justify-center">
      <div class="col-3">
        <q-toolbar class="bg-grey-3 text-black">
          <q-toolbar-title> Senkronizasyon </q-toolbar-title>
          <q-space />
          <q-btn
            :loading="loading"
            @click="load()"
            flat
            round
            dense
            icon="fas fa-sync-alt"
          >
            <q-tooltip> Yenile </q-tooltip>
          </q-btn>
        </q-toolbar>
      </div>
    </div>

    <div class="row q-mt-sm justify-center">
      <div class="col-3">
        <q-select
          :disable="loading"
          v-model="db"
          :options="dbs"
          label="Veritabanı"
          option-value="id"
          option-label="title"
          :option-disable="(o) => !o.is_active"
          outlined
          emit-value
          map-options
          hide-dropdown-icon
          class="q-ml-sm q-mr-sm"
        >
        </q-select>

        <template v-for="model in all_models">
          <q-toggle
            :disable="loading"
            :key="model.id"
            :label="model.title"
            :color="model.color"
            keep-color
            v-model="models"
            :val="model.id"
          />
          <q-separator spaced inset vertical dark />
        </template>

        <h6 class="q-ma-none">Hareketler, Anormallikler</h6>

        <q-input
          class="q-ml-sm q-mr-sm"
          filled
          label="Başlangıç"
          v-model="start"
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
                <q-date v-model="start">
                  <div class="row items-center justify-end">
                    <q-btn v-close-popup label="Kapat" color="primary" flat />
                  </div>
                </q-date>
              </q-popup-proxy>
            </q-icon>
          </template>
        </q-input>

        <q-input
          class="q-ml-sm q-mr-sm"
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
                    <q-btn v-close-popup label="Kapat" color="primary" flat />
                  </div>
                </q-date>
              </q-popup-proxy>
            </q-icon>
          </template>
        </q-input>

        <template v-for="model in special_models">
          <q-toggle
            :key="model.id"
            :disable="loading"
            :label="model.title"
            :color="model.color"
            keep-color
            v-model="models"
            :val="model.id"
          />
          <q-separator spaced inset vertical dark />
        </template>

        <q-btn
          @click="sync()"
          unelevated
          :loading="loading"
          color="black"
          size="md"
          class="full-width"
          label="Kayıtları eşitle"
        />
      </div>
    </div>
  </q-page>
</template>

<script>
import Service from "boot/service";
import { common } from "src/mixins/common";

export default {
  name: "integration_sync",
  mixins: [common],
  components: {},
  data() {
    return {
      loading: false,
      dbs: [],
      all_models: [
        { id: "employees", title: "Personeller", color: "primary" },
        { id: "gecogroups", title: "GeCOTime Grupları", color: "primary" },
        { id: "gecodefs", title: "GeCOTime Tanımları", color: "primary" },
      ],
      special_models: [
        { id: "transactions", title: "Personel hareketleri", color: "primary" },
        { id: "anomalies", title: "Anormallikler", color: "primary" },
      ],
      models: [],
      year: null,
      month: null,
      db: null,
      start: null,
      end: null,
    };
  },
  mounted() {
    this.load();
  },
  methods: {
    load() {
      let self = this;
      this.$set(this, "loading", true);
      this.$set(this, "dbs", []);
      Service.get("integration/sync")
        .then((response) => {
          self.$set(self, "dbs", response.data.db);
        })
        .catch((error) => {
          this.um("Bir hata oluştu!" + error);
        })
        .finally(() => {
          this.$set(this, "loading", false);
        });
    },

    async sync() {
      let self = this;
      if (!self.db) {
        this.um("Lütfen veritabanı seçin!");
        return;
      }
      if (self.models.length == 0) {
        this.um("En az bir opsiyon seçin!");
        return;
      }
      let models = self.models;
      let specials = self.special_models.map((o) => o.id);

      if (models.map((val) => specials.includes(val)).some((o) => o === true)) {
        if (!self.start || !self.end) {
          this.um("Lütfen geçerli bir tarih belirtin!");
          return;
        }
      }

      for (var m of self.models){
        const day_separate = 5;
        if (m === "transactions") {
          const model = [m]
          const startDate = new Date(self.start);
          const endDate = new Date(self.end);
          for (let currentDate = startDate; currentDate <= endDate; ) {
            let start = new Date(currentDate);
            let end = new Date(currentDate.setDate(Math.min(currentDate.getDate() + day_separate)));


            let year = start.getFullYear();
            let month = String(start.getMonth() + 1).padStart(2, "0");
            let day = String(start.getDate()).padStart(2, "0");

            let newStartString = `${year}/${month}/${day}`;

            year = end.getFullYear();
            month = String(end.getMonth() + 1).padStart(2, "0");
            day = String(end.getDate()).padStart(2, "0");

            const newEndString = `${year}/${month}/${day}`;

            await Service.post("integration/sync", {
              db: self.db,
              models: model,
              start: newStartString,
              end: newEndString,
            })
            currentDate.setDate(currentDate.getDate() + 1);
          }
          self.bm(`Personel Harekteleri ${self.start} ${self.end} başarıyla güncellendi! ` );
        } else if (m === "anomalies") {
          const model = [m]
          const startDate = new Date(self.start);
          const endDate = new Date(self.end);
          for (let currentDate = startDate; currentDate <= endDate; ) {
            let start = new Date(currentDate);
            let end = new Date((currentDate.setDate(Math.min(currentDate.getDate() + day_separate))));

            let year = start.getFullYear();
            let month = String(start.getMonth() + 1).padStart(2, "0");
            let day = String(start.getDate()).padStart(2, "0");

            let newStartString = `${year}/${month}/${day}`;

            year = end.getFullYear();
            month = String(end.getMonth() + 1).padStart(2, "0");
            day = String(end.getDate()).padStart(2, "0");

            const newEndString = `${year}/${month}/${day}`;

            await Service.post("integration/sync", {
              db: self.db,
              models: model,
              start: newStartString,
              end: newEndString,
            })
            currentDate.setDate(currentDate.getDate() + 1);
          }
          self.bm(`Anormallikler ${self.start}-${self.end} tarih aralığında başarıyla güncellendi! ` );
        } else {
          const model = [m]
          let message;
          if(m ==='employees')
            message = 'Personeller'
          else if(m === 'gecodefs')
            message = 'GeCOTime Grupları'
          else
            message = 'GeCOTime Tanımları'

          await Service.post("integration/sync", {
            db: self.db,
            models: model,
          })
            self.bm(`${message} başarıyla güncellendi!` );
        }
      }
      this.$set(this, "loading", false);
    },
  },
};
</script>
