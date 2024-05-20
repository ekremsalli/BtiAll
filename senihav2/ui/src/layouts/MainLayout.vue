<template>
  <q-layout view="hHh lpR fFf">
    <template v-if="$store.getters['application/broken']">
      <q-page-container>
        <q-page
          style="background-image: linear-gradient(rgba(255,255,255,0.5), rgba(255,255,255,0.5)), url('bg.png');"
          class="window-height window-width row justify-center items-center">
          <div class="column items-center" style="height: 150px">
            <div class="col">
              <q-banner class="bg-grey-3">
                <q-icon size="64px" color="negative" name="fas fa-exclamation-circle" />
                <span class="text-h6 q-pl-lg">Sunucu bağlantısı sağlanamıyor...</span>
                <template v-slot:action>
                  <q-btn flat color="primary" @click="reload()" label="Yeniden dene" />
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
          style="background-image: linear-gradient(rgba(255,255,255,0.5), rgba(255,255,255,0.5)), url('bg.png');"
          class="window-height window-width row justify-center items-center">
          <div class="column items-center" style="height: 150px">
            <div class="col">
              <q-banner class="bg-grey-3">
                <q-icon size="64px" color="negative" name="fas fa-exclamation-circle" />
                <span class="text-h6 q-pl-lg">Yetki hatası...</span>
                <template v-slot:action>
                  <q-btn flat color="primary" @click="cikis()" label="Çıkış" />
                  <q-btn flat color="primary" @click="reload()" label="Yeniden dene" />
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
          <span class="q-mx-xl">{{ $config.company }}</span>
          <q-separator dark vertical inset />
          <q-btn :to="{name: 'dashboard'}" stretch flat label="Entegrasyon" />
          <q-separator dark vertical inset />
          <q-btn-dropdown stretch flat label="Trendyol">
            <q-list class="bg-black">
              <q-item :to="{name: 'trendyol/siparis_gecmisi'}">
                <q-item-section class='text-white'>
                  <q-item-label>Sipariş geçmişi</q-item-label>
                </q-item-section>
              </q-item>
              <q-item :to="{name: 'trendyol/urun_aktarimi'}">
                <q-item-section class='text-white'>
                  <q-item-label>Ürün aktarımı</q-item-label>
                </q-item-section>
              </q-item>
              <q-item :to="{name: 'trendyol/urun_esleme'}">
                <q-item-section class='text-white'>
                  <q-item-label>Ürün eşleme</q-item-label>
                </q-item-section>
              </q-item>
              <q-item :to="{name: 'trendyol/eksik_eslesme'}">
                <q-item-section class='text-white'>
                  <q-item-label>Eşleşmeyen ürünler</q-item-label>
                </q-item-section>
              </q-item>


            </q-list>
          </q-btn-dropdown>
          <q-space />
          <q-btn-dropdown stretch flat>
            <template #label>
              <span class="text-capitalize">{{ $store.getters['account/username'] }}</span>
            </template>
            <q-list>
              <q-item clickable v-close-popup @click="cikis">
                <q-item-section>
                  <q-item-label>Çıkış</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>

          </q-btn-dropdown>
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
  name: 'MainLayout',
  data () {
    return {
      left: true
    }
  },
  computed: {
    loading () {
      return this.$store.getters['application/loading']
    }
  },
  mounted () {
    if (this.loading) {
      this.$q.loading.show({
        delay: 100
      })
    }
  },
  watch: {
    loading (nval, oval) {
      if (nval) {
        this.$q.loading.show({
          delay: 100
        })
      } else {
        this.$q.loading.hide()
      }
    }
  },
  methods: {
    cikis () {
      this.$store.commit('account/logout')
    },
    reload () {
      window.location.reload()
    }
  }
}
</script>
