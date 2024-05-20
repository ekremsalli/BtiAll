<template>
  <q-layout view="hHh lpR fFf">
    <template v-if="$store.getters['application/broken']">
      <q-page-container>
        <q-page
          style="
            background-image: linear-gradient(
                rgba(255, 255, 255, 0.5),
                rgba(255, 255, 255, 0.5)
              ),
              url('bg.png');
          "
          class="window-height window-width row justify-center items-center"
        >
          <div class="column items-center" style="height: 150px">
            <div class="col">
              <q-banner class="bg-grey-3">
                <q-icon
                  size="64px"
                  color="negative"
                  name="fas fa-exclamation-circle"
                />
                <span class="text-h6 q-pl-lg"
                  >Sunucu bağlantısı sağlanamıyor...</span
                >
                <template v-slot:action>
                  <q-btn
                    flat
                    color="primary"
                    @click="reload()"
                    label="Yeniden dene"
                  />
                </template>
              </q-banner>
            </div>
          </div>
        </q-page>
      </q-page-container>
    </template>
    <template v-else-if="$store.getters['application/permission_denied']">
      <q-page-container>
        <q-page
          style="
            background-image: linear-gradient(
                rgba(255, 255, 255, 0.5),
                rgba(255, 255, 255, 0.5)
              ),
              url('bg.png');
          "
          class="window-height window-width row justify-center items-center"
        >
          <div class="column items-center" style="height: 150px">
            <div class="col">
              <q-banner class="bg-grey-3">
                <q-icon
                  size="64px"
                  color="negative"
                  name="fas fa-exclamation-circle"
                />
                <span class="text-h6 q-pl-lg">Yetki hatası...</span>
                <template v-slot:action>
                  <q-btn flat color="primary" @click="cikis()" label="Çıkış" />
                  <q-btn
                    flat
                    color="primary"
                    @click="reload()"
                    label="Yeniden dene"
                  />
                </template>
              </q-banner>
            </div>
          </div>
        </q-page>
      </q-page-container>
    </template>
    <template v-else>
      <q-header elevated class="bg-dark text-white" v-if="!loading">
        <q-toolbar>
          <router-link
            style="text-decoration: none"
            class="text-white text-weight-bolder"
            :to="{ name: 'dashboard' }"
          >
            <span class="q-mx-xl">
              {{ $config.company }}
            </span>
          </router-link>
          <q-separator dark vertical inset />

          <q-btn stretch flat label="Tanımlar" style="width: 200px">
            <q-menu fit>
              <q-list class="bg-black">
                <q-item
                  v-perm-checker="{
                    dx: 'flex',
                    px: 'employees.view_employees',
                  }"
                  :to="{ name: 'defs/employee' }"
                >
                  <q-item-section class="text-white">
                    <q-item-label>Personel Listesi</q-item-label>
                  </q-item-section>
                </q-item>
                <q-item
                  v-perm-checker="{
                    dx: 'flex',
                    px: 'gecogroups.view_gecogroups',
                  }"
                  :to="{ name: 'defs/geco/groups' }"
                >
                  <q-item-section class="text-white">
                    <q-item-label>GeCOTime Grupları</q-item-label>
                  </q-item-section>
                </q-item>
                <q-item
                  v-perm-checker="{ dx: 'flex', px: 'gecodefs.view_gecodefs' }"
                  :to="{ name: 'defs/geco/defs' }"
                >
                  <q-item-section class="text-white">
                    <q-item-label>GeCOTime Tanımları</q-item-label>
                  </q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>

          <q-separator dark vertical inset />

          <q-btn stretch flat label="İşlemler" style="width: 200px">
            <q-menu fit>
              <q-list class="bg-black">
                <q-item
                  v-perm-checker="{
                    dx: 'flex',
                    px: 'transactions.view_transactions',
                  }"
                  :to="{ name: 'ops/transactions' }"
                >
                  <q-item-section class="text-white">
                    <q-item-label>Giriş/Çıkış Zamanları</q-item-label>
                  </q-item-section>
                </q-item>
                <q-item
                  v-perm-checker="{
                    dx: 'flex',
                    px: 'anomalies.view_anomalies',
                  }"
                  :to="{ name: 'ops/anomalies' }"
                >
                  <q-item-section class="text-white">
                    <q-item-label>Anormallikler</q-item-label>
                  </q-item-section>
                </q-item>
                <q-item :to="{ name: 'ops/overtime' }">
                  <q-item-section class="text-white">
                    <q-item-label>Fazla Mesailer</q-item-label>
                  </q-item-section>
                </q-item>
                <q-item
                  v-perm-checker="{
                    dx: 'flex',
                    px: 'annualoffs.view_annualoffs',
                  }"
                  :to="{ name: 'ops/annualoffs' }"
                >
                  <q-item-section class="text-white">
                    <q-item-label>Yıllık İzinler</q-item-label>
                  </q-item-section>
                </q-item>
                <q-item
                  v-perm-checker="{ dx: 'flex', px: 'payroll.view_payroll' }"
                  :to="{ name: 'ops/payroll' }"
                >
                  <q-item-section class="text-white">
                    <q-item-label>Bordro</q-item-label>
                  </q-item-section>
                </q-item>

                <!--
              <q-item :to="{name: 'islemler/'}">
                <q-item-section class='text-white'>
                  <q-item-label>Hesaplanan Zamanlar</q-item-label>
                </q-item-section>
              </q-item>
              <q-item :to="{name: 'islemler/'}">
                <q-item-section class='text-white'>
                  <q-item-label>Fazla Mesai</q-item-label>
                </q-item-section>
              </q-item>
              <q-item :to="{name: 'islemler/'}">
                <q-item-section class='text-white'>
                  <q-item-label>Yıllık İzinler</q-item-label>
                </q-item-section>
              </q-item>
              <q-item :to="{name: 'islemler/'}">
                <q-item-section class='text-white'>
                  <q-item-label>Beyaz Yaka</q-item-label>
                </q-item-section>
              </q-item>
              <q-item :to="{name: 'islemler/'}">
                <q-item-section class='text-white'>
                  <q-item-label>SGK Raporları</q-item-label>
                </q-item-section>
              </q-item>
              <q-item :to="{name: 'islemler/'}">
                <q-item-section class='text-white'>
                  <q-item-label>Yol Parası</q-item-label>
                </q-item-section>
              </q-item>
              <q-item :to="{name: 'islemler/'}">
                <q-item-section class='text-white'>
                  <q-item-label>İşten Ayrılma</q-item-label>
                </q-item-section>
              </q-item>
              -->
              </q-list>
            </q-menu>
          </q-btn>

          <!--
          <q-separator dark vertical inset />

          <q-btn :to="{name: 'dashboard'}" stretch flat label="Raporlar" />
          -->
          <q-separator dark vertical inset />

          <q-btn stretch flat label="Entegrasyon" style="width: 220px">
            <q-menu fit>
              <q-list class="bg-black">
                <q-item
                  v-perm-checker="{
                    dx: 'flex',
                    px: 'changes.change_changes',
                    only_super: true,
                  }"
                  :to="{ name: 'integration/changes_for_approve' }"
                >
                  <q-item-section class="text-white">
                    <q-item-label>Onay bekleyen hareketler</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item
                  v-perm-checker="{
                    dx: 'flex',
                    px: 'changes.change_changes',
                    only_super: true,
                  }"
                  :to="{ name: 'integration/changes_for_send' }"
                >
                  <q-item-section class="text-white">
                    <q-item-label>İkinci onay bekleyen hareketler</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item
                  v-if="$store.getters['account/is_staff_or_super']"
                  :to="{ name: 'integration/sync' }"
                >
                  <q-item-section class="text-white">
                    <q-item-label>Senkronizasyon</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item
                  v-if="$store.getters['account/is_superuser']"
                  :to="{ name: 'integration/db' }"
                >
                  <q-item-section class="text-white">
                    <q-item-label>Veritabanları</q-item-label>
                  </q-item-section>
                </q-item>

                <!--
              <q-item :to="{name: 'entegrasyon/'}">
                <q-item-section class='text-white'>
                  <q-item-label>Grupları Güncelle</q-item-label>
                </q-item-section>
              </q-item>
              <q-item :to="{name: 'entegrasyon/'}">
                <q-item-section class='text-white'>
                  <q-item-label>Tanımları Güncelle</q-item-label>
                </q-item-section>
              </q-item>
              <q-item :to="{name: 'entegrasyon/'}">
                <q-item-section class='text-white'>
                  <q-item-label>Personel Listesi Güncelle</q-item-label>
                </q-item-section>
              </q-item>
              <q-item :to="{name: 'entegrasyon/'}">
                <q-item-section class='text-white'>
                  <q-item-label>Günlük Hareketleri Güncelle</q-item-label>
                </q-item-section>
              </q-item>
              <q-item :to="{name: 'entegrasyon/'}">
                <q-item-section class='text-white'>
                  <q-item-label>Anormallikleri Güncelle</q-item-label>
                </q-item-section>
              </q-item>
              <q-item :to="{name: 'entegrasyon/'}">
                <q-item-section class='text-white'>
                  <q-item-label>Hesaplanmış Hareketleri Güncelle</q-item-label>
                </q-item-section>
              </q-item>
              -->
              </q-list>
            </q-menu>
          </q-btn>

          <q-space />
          <q-btn flat :label="$store.getters['account/username']">
            <q-menu fit>
              <q-list>
                <q-item clickable @click="cikis">
                  <q-item-section>
                    <q-item-label>Çıkış</q-item-label>
                  </q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
        </q-toolbar>
      </q-header>

      <q-page-container v-if="!loading">
        <router-view />
      </q-page-container>
    </template>
  </q-layout>
</template>
<script>
export default {
  name: "MainLayout",
  data() {
    return {
      left: true,
      interval: null,
    };
  },
  computed: {
    loading() {
      return this.$store.getters["application/loading"];
    },
  },
  mounted() {
    if (this.loading) {
      this.$q.loading.show({
        delay: 100,
      });
    }

    // verify token
    this.interval = setInterval(this.check_token, 1000 * 60 * 3);
  },
  destroyed() {
    clearInterval(this.interval);
  },
  watch: {
    loading(nval, oval) {
      if (nval) {
        this.$q.loading.show({
          delay: 100,
        });
      } else {
        this.$q.loading.hide();
      }
    },
  },
  methods: {
    check_token() {
      this.$store.dispatch("account/check");
    },
    cikis() {
      this.$store.commit("account/logout");
    },
    reload() {
      window.location.reload();
    },
  },
};
</script>
