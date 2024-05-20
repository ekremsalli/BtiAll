<template>
  <q-layout view="hHh lpR fFf">
    <template v-if="$store.getters['application/broken']">
      <q-page-container>
        <q-page
          style="background-image: linear-gradient(rgba(255,255,255,0.5), rgba(255,255,255,0.5)), url('bg.png');"
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
          style="background-image: linear-gradient(rgba(255,255,255,0.5), rgba(255,255,255,0.5)), url('bg.png');"
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
            style="text-decoration:none"
            class="text-white text-weight-bolder"
            :to="{ name: 'dashboard' }"
          >
            <span class="q-mx-xl">
              {{ $config.company }}
            </span>
          </router-link>
          <q-separator dark vertical inset />

          <q-separator dark vertical inset />

          <template v-for="item, index in menu">
            <template v-if="item.type == 'node'">
              <q-btn
                no-caps
                v-perm-checker="{
                  dx: item.perm_class,
                  px: item.permission
                }"
                stretch
                align="around"
                flat
                :label="item.title"
                :to="item.target"
              >
              </q-btn>              
              <q-separator dark vertical inset />
              
            </template>
            <template v-if="item.type == 'seperator'">
              <q-separator dark vertical inset />
            </template>
            <template v-if="item.type == 'group'">
              <q-btn-dropdown stretch flat v-if="multi_perm_check(dig_perms(item))">
                <template #label>
                  <span class="text-capitalize">{{ item.title }}</span>
                </template>
                <q-list dense class="bg-black">
                  <template v-for="submenu, subindex in item.childs">
                    <template v-if="submenu.type == 'subgroup'">
                      <q-item clickable v-if="multi_perm_check(submenu.childs.map(o => o.permission))">
                        <q-item-section class="text-white">{{ submenu.title }}</q-item-section>
                        <q-item-section side>
                          <q-icon name="keyboard_arrow_right" />
                        </q-item-section>                 
                        <q-menu anchor="top end" self="top start">
                          <q-list class="bg-black" style="margin-left:.6px">
                            <template v-for="node, nindex in submenu.childs">
                              <q-item
                                v-perm-checker="{
                                  dx: node.perm_class,
                                  px: node.permission,
                                }"
                                :to="node.target">
                                <q-item-section class="text-white">
                                  <q-item-label>{{ node.title }}</q-item-label>
                                </q-item-section>
                              </q-item>                              
                          </template>
                          </q-list>
                        </q-menu>

                      </q-item>
                    </template>
                  </template>
                </q-list>
              </q-btn-dropdown>
            </template>
          </template>

          <q-space />
          <q-btn-dropdown stretch flat>
            <template #label>
              <span class="text-capitalize">{{
                $store.getters["account/username"]
              }}</span>
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
import { common } from "src/mixins/common";

export default {
  name: "MainLayout",
  mixins: [common],
  data() {
    return {
      left: true,
      interval: null,
      menu: [
        {
          type: 'node', 
          title: 'Aktivite', 
          target: {'name': 'activity'}, 
          permission: 'activity.view_activity',
          perm_class: 'flex'
        },  
        {
          type: 'node', 
          title: 'Akış', 
          target: {'name': 'flow'}, 
          permission: 'flow.view_flow',
          perm_class: 'flex'
        },  
        {
          type: 'node', 
          title: 'Operasyon', 
          target: {'name': 'operation'}, 
          permission: 'taskactivity.view_taskactivity',
          perm_class: 'flex'
        },   
      ]
    };
  },
  computed: {
    loading() {
      return this.$store.getters["application/loading"];
    }
  },
  mounted() {
    if (this.loading) {
      this.$q.loading.show({
        delay: 100
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
          delay: 100
        });
      } else {
        this.$q.loading.hide();
      }
    }
  },
  methods: {
    dig_perms (item) {
      let px = []
      if (item.childs) {        
        item.childs.forEach(element => {
          if (element.childs) {
            element.childs.forEach(subelem => {
              px.push(subelem.permission)
            })
          } else {
            if (subelem.permission) px.push(subelem.permission)
          }
        })
      } else {
        if (item.permission) px.push(itme.permission)
      }
      return px

    },
    check_token() {
      this.$store.dispatch("account/check");
    },
    cikis() {
      this.$store.commit("account/logout");
    },
    reload() {
      window.location.reload();
    }
  }
};
</script>
