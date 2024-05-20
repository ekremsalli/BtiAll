<template>
  <q-page padding>
    <q-toolbar class="bg-grey-3 text-black">
      <q-toolbar-title>
        Onay bekleyen hareketler / anormallikler
      </q-toolbar-title>
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

    <div
      class="row q-mt-sm all-container"
      v-if="(data && data.length > 0) || (excuseData && excuseData.length > 0)"
    >
      <div class="all-button-groups">
        <div class="q-pa-md">
          <q-btn-dropdown
            v-if="(data && data.length > 0)"
            color="orange"
            label="Toplu Güncellenen İşlemler"
            dropdown-icon="change_history"
            class="q-mr-md"
          >
            <q-list>
              <q-item clickable v-close-popup @click="update_all(1)">
                <q-item-section>
                  <q-item-label>Tümünü Onayla</q-item-label>
                </q-item-section>
              </q-item>

              <q-item clickable v-close-popup @click="update_all(3)">
                <q-item-section>
                  <q-item-label>Tümünü Reddet</q-item-label>
                </q-item-section>
              </q-item>

              <q-item clickable v-close-popup @click="delete_all()">
                <q-item-section>
                  <q-item-label class="text-red-6">Tümünü Sil</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-btn-dropdown>

          <q-btn-dropdown
            v-if="(excuseData && excuseData.length > 0)"
            color="primary"
            label="Toplu Yeni Eklenen İşlemler"
            dropdown-icon="change_history"
          >
            <q-list>
              <q-item clickable v-close-popup @click="approve_all(1)">
                <q-item-section>
                  <q-item-label>Tümünü Onayla</q-item-label>
                </q-item-section>
              </q-item>

              <q-item clickable v-close-popup @click="approve_all(3)">
                <q-item-section>
                  <q-item-label>Tümünü Reddet</q-item-label>
                </q-item-section>
              </q-item>

              <q-item clickable v-close-popup @click="_delete_all()">
                <q-item-section>
                  <q-item-label class="text-red-6">Tümünü Sil</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-btn-dropdown>
        </div>
      </div>
    </div>

    <div class="row q-mt-sm">
      <template v-for="item in data">
        <div :key="'div-' + item.id" class="col-3 flex">
          <q-card :key="'card-' + item.id" class="q-ma-xs">
            <q-card-section class="bg-black text-white">
              <div class="text-subtitle2">
                {{ item.employee }}
              </div>
              <div class="q-mt-xs">
                <q-icon name="today" style="font-size: 1.6em" />
                <template v-if="item.is_annual_off">
                  Yıllık izin <b>( {{ item.annual_excuse_type }} )</b>
                </template>
                <template v-else>
                  <template v-if="item.is_remove_request">
                    {{ item.tr_date }}
                  </template>
                  <template v-else>
                    {{ item.tr_date }}
                  </template>
                  tarihli
                  <template v-if="item.transaction">hareket</template>
                  <template v-else>anormallik</template>
                </template>
              </div>
            </q-card-section>

            <q-card-section class="q-pt-none" v-if="!item.is_annual_off">
              <div class="q-pt-md">
                <span class="text-subtitle2">Güncelleme</span>
                <ul style="list-style-type: none" class="q-mt-none">
                  <li
                    :key="item.id + '_' + index"
                    v-for="(report, index) in diff(item.snapshot, item.updates)"
                  >
                    <span class="text-success">{{
                      report.key | translate
                    }}</span>
                    >
                    <span class="text-orange"> {{ report.old }}</span>
                    >
                    <span class="text-primary">{{ report.new }}</span>
                  </li>
                </ul>
              </div>
            </q-card-section>

            <q-card-section class="q-pt-none">
              <div class="text-caption q-pt-md">
                <template v-if="item.is_annual_off">
                  {{ item.start_annual }} - {{ item.end_annual }}
                  Yıllık izin
                </template>

                <b>{{ item.created_by }}</b> tarafından
                <span v-if="item.description && item.description.length > 0"
                  >'{{ item.description }}' açıklaması ile</span
                >
                {{ fdate(item.created_on, "DD.MMM.YYYY HH:mm") }} tarihinde
                <template v-if="item.is_remove_request">
                  <span class="text-negative"
                    >oluşturulan kayıt silme isteği!</span
                  >
                </template>
                <template v-else> oluşturuldu. </template>
              </div>
            </q-card-section>

            <q-separator />

            <q-card-actions align="right">
              <q-btn
                @click="update(item, 1)"
                :loading="all_progressing || in_progress.includes(item.id)"
                :disabled="updates.includes(item.id)"
                flat
                >Onayla</q-btn
              >
              <q-btn
                @click="update(item, 3)"
                :loading="all_progressing || in_progress.includes(item.id)"
                :disabled="updates.includes(item.id)"
                flat
                >Reddet</q-btn
              >
              <q-btn
                @click="delete_item(item)"
                :loading="all_progressing || in_progress.includes(item.id)"
                :disabled="updates.includes(item.id)"
                color="negative"
                flat
                >Sil</q-btn
              >
            </q-card-actions>
          </q-card>
        </div>
      </template>

      <div v-for="(item, i) in excuseData" :key="i">
        <div class="col-3 flex">
          <q-card :key="'card-' + item.i" class="q-ma-xs">
            <q-card-section class="bg-secondary text-white">
              <div class="text-bold">{{ item.employee }}</div>
              için bir kayıt
              <div class="text-subtitle2 text-white">
                {{ item.created_by ? item.created_by : "--" }} tarafından
                oluşturuldu.
              </div>
            </q-card-section>

            <q-card-section class="q-pt-none">
              <ul style="list-style-type: none">
                <li>
                  <span class="text-bold text-orange"
                    >Oluşturulma Tarihi :
                  </span>
                  <span>{{ fdate(item.created_on, "DD/MM/YYYY HH:mm") }}</span>
                </li>

                <li>
                  <span class="text-bold text-orange">Giriş : </span>
                  <span>{{ fdate(item.start, "DD/MM/YYYY HH:mm") }}</span>
                </li>

                <li>
                  <span class="text-bold text-orange">Çıkış : </span>
                  <span>{{ fdate(item.end, "DD/MM/YYYY HH:mm") }}</span>
                </li>

                <li>
                  <span class="text-bold text-orange">Açıklama : </span>
                  <span>{{ item.description }}</span>
                </li>

                <li>
                  <span class="text-bold text-orange">Tarih : </span>
                  <span>{{ item.tr_date }}</span>
                </li>
                <!-- <li>
                  <span class="text-bold text-orange">Hesap Grubu : </span>
                  <span>{{ item.account }}</span>
                </li> -->
                <!-- <li>
                  <span class="text-bold text-orange">Gün Modeli : </span>
                  <span>{{ item.day_model }}</span>
                </li> -->
                <!-- 
                <li>
                  <span class="text-bold text-orange">Personel ID : </span>
                  <span>{{ item.employee_id }}</span>
                </li>

                <li>
                  <span class="text-bold text-orange">Gün : </span>
                  <span>{{ item.excuse_day }}</span>
                </li>

                <li>
                  <span class="text-bold text-orange">Mazaret Tipi : </span>
                  <span>{{ item.excuse_type }}</span>
                </li>
 
                <li>
                  <span class="text-bold text-orange">geco_user : </span>
                  <span>{{ item.geco_user }}</span>
                </li>

                <li>
                  <span class="text-bold text-orange">Puantaj Tipi : </span>
                  <span>{{ item.pay_type }}</span>
                </li>
                -->
                <!-- 
                <li>
                  <span class="text-bold text-orange">source_db : </span>
                  <span>{{ item.source_db }}</span>
                </li> -->

                <!-- <li>
                  <span class="text-bold text-orange">Zaman Tipi : </span>
                  <span>{{ item.time_type }}</span>
                </li> -->

                <!-- <li>
                  <span class="text-bold text-orange">Süre : </span>
                  <span>{{ item.work_time }}</span>
                </li> -->
              </ul>
            </q-card-section>

            <q-space />
            <q-separator />

            <q-card-actions align="right">
              <q-btn
                @click="patch_excuse(item, 1)"
                :loading="all_progressing || in_progress.includes(item.id)"
                :disabled="updates.includes(item.id)"
                flat
                >Onayla</q-btn
              >
              <q-btn
                @click="reject_excuse(item, 3)"
                :loading="all_progressing || in_progress.includes(item.id)"
                :disabled="updates.includes(item.id)"
                flat
                >Reddet</q-btn
              >
              <q-btn
                @click="delete_excuse(item)"
                :loading="all_progressing || in_progress.includes(item.id)"
                :disabled="updates.includes(item.id)"
                color="negative"
                flat
                >Sil</q-btn
              >
            </q-card-actions>
          </q-card>
        </div>
      </div>
    </div>
    
    <div
      class="row q-mt-sm all-container"
      v-if="(data && data.length > 0) || (excuseData && excuseData.length > 0)"
    >
      <div class="all-button-groups">
        <div class="q-pa-md">
          <q-btn-dropdown
            v-if="(data && data.length > 0)"
            color="orange"
            label="Toplu Güncellenen İşlemler"
            dropdown-icon="change_history"
            class="q-mr-md"
          >
            <q-list>
              <q-item clickable v-close-popup @click="update_all(1)">
                <q-item-section>
                  <q-item-label>Tümünü Onayla</q-item-label>
                </q-item-section>
              </q-item>

              <q-item clickable v-close-popup @click="update_all(3)">
                <q-item-section>
                  <q-item-label>Tümünü Reddet</q-item-label>
                </q-item-section>
              </q-item>

              <q-item clickable v-close-popup @click="delete_all()">
                <q-item-section>
                  <q-item-label class="text-red-6">Tümünü Sil</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-btn-dropdown>

          <q-btn-dropdown
            v-if="(excuseData && excuseData.length > 0)"
            color="primary"
            label="Toplu Yeni Eklenen İşlemler"
            dropdown-icon="change_history"
          >
            <q-list>
              <q-item clickable v-close-popup @click="approve_all(1)">
                <q-item-section>
                  <q-item-label>Tümünü Onayla</q-item-label>
                </q-item-section>
              </q-item>

              <q-item clickable v-close-popup @click="approve_all(3)">
                <q-item-section>
                  <q-item-label>Tümünü Reddet</q-item-label>
                </q-item-section>
              </q-item>

              <q-item clickable v-close-popup @click="_delete_all()">
                <q-item-section>
                  <q-item-label class="text-red-6">Tümünü Sil</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-btn-dropdown>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import Service from "boot/service";
import { common } from "src/mixins/common";
import { date } from "quasar";

export default {
  name: "integration_changes_for_approve",
  mixins: [common],
  components: {},
  data() {
    return {
      loading: false,
      data: [],
      excuseData: [],
      updates: [],
      in_progress: [],
      all_progressing: false,
    };
  },
  watch: {
    updates: {
      handler: function () {},
      deep: true,
    },
  },
  mounted() {
    this.load();
    this.loadExcuse();
  },
  methods: {
    fdate(dx, fmt) {
      return date.formatDate(dx, fmt);
    },
    delete_all() {
      let self = this;
      self.$set(self, "all_progressing", true);
      Service.delete("integration/changes/edit/bulk", {
        items: self.data.map((o) => o.id),
      })
        .then((response) => {
          self.bm("Tümü başarıyla silindi!");
          self.load();
        })
        .catch((error) => {
          if (error.response && error.response.data) {
            if (error.response.data.custom) {
              this.um(error.response.data.message);
            } else this.um("Bir hata oluştu! " + error);
          } else this.um("Bir hata oluştu! " + error);
        })
        .finally(() => {
          self.$set(self, "all_progressing", false);
        });
    },
    delete_item(item) {
      let self = this;
      this.in_progress.push(item.id);

      Service.delete(`integration/changes/edit/${item.id}`, {})
        .then((response) => {
          self.updates.push(item.id);
          self.load();
          this.bm("Başarıyla silindi!");
        })
        .catch((error) => {
          this.um("Bir hata oluştu! " + error);
        })
        .finally(() => {
          let dx = self.in_progress.indexOf(item.id);
          if (dx > -1) self.in_progress.splice(dx, 1);
        });
    },
    update_all(op) {
      let self = this;
      self.$set(self, "all_progressing", true);
      Service.patch("integration/changes/edit/bulk", {
        items: self.data.map((o) => o.id),
        op: op,
      })
        .then((response) => {
          self.bm("Tümü başarıyla işlendi!");
          self.load();
        })
        .catch((error) => {
          if (error.response && error.response.data) {
            if (error.response.data.custom) {
              this.um(error.response.data.message);
            } else this.um("Bir hata oluştu! " + error);
          } else this.um("Bir hata oluştu! " + error);
        })
        .finally(() => {
          self.$set(self, "all_progressing", false);
        });
    },
    update(item, op) {
      let self = this;
      this.in_progress.push(item.id);

      Service.patch(`integration/changes/edit/${item.id}`, {
        verify_status: op,
      })
        .then((response) => {
          self.updates.push(item.id);
          self.load();
          self.bm("Başarıyla işlendi!");
        })
        .catch((error) => {
          self.um("Bir hata oluştu! " + error);
        })
        .finally(() => {
          let dx = self.in_progress.indexOf(item.id);
          if (dx > -1) self.in_progress.splice(dx, 1);
        });
    },
    load(sett) {
      let self = this;
      this.$set(this, "loading", true);
      this.$set(this, "data", []);
      this.$set(this, "updates", []);
      Service.get("integration/changes/waiting_for_approve")
        .then((response) => {
          self.$set(self, "data", response.data);
        })
        .catch((error) => {
          self.um("Bir hata oluştu!" + error);
        })
        .finally(() => {
          self.$set(self, "loading", false);
        });
    },
    loadExcuse(sett) {
      let self = this;
      this.$set(this, "loading", true);
      this.$set(this, "excuseData", []);
      this.$set(this, "updates", []);
      Service.get("excuse")
        .then((response) => {
          self.$set(self, "excuseData", response.data);
        })
        .catch((error) => {
          self.um("Bir hata oluştu!" + error);
        })
        .finally(() => {
          self.$set(self, "loading", false);
        });
    },
    patch_excuse(items, status) {
      const params = {
        verify_status: status,
      };

      Service.patch(`excuse/${items.id}`, params)
        .then((response) => {
          this.bm("Kayıt başarıyla ikinci onaya aktarıldı.");
          this.loadExcuse();
        })
        .catch((err) => {
          this.um("Kayıt onaylanırken bir hata oluştu! " + err);
        });
    },

    delete_excuse(items) {
      const params = {
        id: items.id,
      };

      Service.delete(`excuse/${items.id}`, params)
        .then((response) => {
          this.loadExcuse();
          this.bm("Kayıt başarıyla silindi.");
        })
        .catch((err) => {
          this.um("Kayıt silinirken bir hata oluştu! " + err);
        });
    },

    reject_excuse(items, status) {
      const params = {
        verify_status: status,
      };

      Service.patch(`excuse/${items.id}`, params)
        .then((response) => {
          this.loadExcuse();
          this.bm("Kayıt başarıyla reddedildi.");
        })
        .catch((err) => {
          this.um("Kayıt reddedilirken bir hata oluştu! " + err);
        });
    },

    approve_all(status) {
      let excuses = [];
      this.excuseData.map((excuse) => {
        excuses.push(excuse.id);
      });

      const params = {
        excuse_ids: excuses,
        verify_status: status,
      };

      Service.post(`excuse_all/approve`, params)
        .then((response) => {
          this.loadExcuse();
          this.bm(
            status === 1
              ? "Yeni eklenen kayıtlar tümüyle onaylandı."
              : "Yeni eklenen kayıtlar tümüyle reddedildi!"
          );
        })
        .catch((err) => {
          this.um("Bir hata oluştu! " + err);
        });
    },

    _delete_all() {
      let excuses = [];
      this.excuseData.map((excuse) => {
        excuses.push(excuse.id);
      });

      const params = {
        excuse_ids: excuses,
      };

      Service.post(`excuses_delete/all`, params)
        .then((response) => {
          this.loadExcuse();
          this.bm("Yeni eklenen kayıtların tümü silindi!");
        })
        .catch((err) => {
          this.um("Bir hata oluştu! " + err);
        });
    },
  },
};
</script>

<style>
.all-container {
  width: 100%;
  display: inline-flex;
  justify-content: flex-end;
}
</style>
