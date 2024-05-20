<template>
  <q-page padding>
    <div class="row justify-center">
      <div class="col-6">
        <div class="row justify-end">
          <q-btn :loading="loading" @click="load()" flat round dense icon="fas fa-sync-alt">
            <q-tooltip>
              Yenile
            </q-tooltip>
          </q-btn>        
        </div>

        <template v-if="$store.getters['account/is_superuser'] || $store.getters['account/perm_check']('changes.change_changes')">
          <q-banner v-if="changes_for_approve > 0" class="bg-grey-3">
            <template v-slot:avatar>
              <q-icon name="pending_actions" color="primary" />
            </template>            
            Onaylanmayı bekleyen {{ changes_for_approve }} hareket var.
            <template v-slot:action>
              <q-btn :to="{name: 'integration/changes_for_approve'}" flat color="primary" label="Onay sayfasına git" />
            </template>
          </q-banner>    

          <br />
          <br />
          <q-banner v-if="changes_for_send > 0" class="bg-grey-3">
            <template v-slot:avatar>
              <q-icon name="published_with_changes" color="primary" />
            </template>            
            İkinci onay bekleyen {{ changes_for_send }} hareket var.
            <template v-slot:action>
              <q-btn :to="{name: 'integration/changes_for_send'}" flat color="primary" label="İkinci onay sayfasına git" />
            </template>
          </q-banner>    

          <br />
          <br />
          <q-banner v-if="changes_for_send + changes_for_approve == 0" class="bg-grey-3"> 
            <template v-slot:avatar>
              <q-icon name="task_alt" color="success" />
            </template>            
            Onay bekleyen işlem bulunmuyor!
            <template v-slot:action>
              <q-btn @click="load()" flat color="primary" label="Yenile" />
            </template>
          </q-banner>
        </template>
      </div>
    </div>

  </q-page>
</template>

<script>
import Service from 'boot/service'
import { common } from 'src/mixins/common'

export default {
  name: 'Dashboard',
  mixins: [common],
  data () {
    return {
      loading: false,
      changes_for_approve: null,
      changes_for_send: null
    }
  },
  mounted () {
    this.load()
  },
  methods: {
    load () {
      let self = this
      this.$set(this, 'loading', true)
      Service.get('user/dashboard')
      .then((response) => {
        if (self.$store.getters['account/is_superuser']) {
          self.$set(self, 'changes_for_approve', response.data.changes_for_approve)
          self.$set(self, 'changes_for_send', response.data.changes_for_send)
        }
      })
      .catch((error) => {
        this.um('Bir hata oluştu!' + error)
      })
      .finally(() => {
        this.$set(this, 'loading', false)
      })      
    }
    
  }
}
</script>
