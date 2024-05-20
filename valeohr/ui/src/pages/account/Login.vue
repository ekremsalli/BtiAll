<template>
  <q-page
    style="background-image: url('bg.png');background-repeat: repeat, repeat;"
    class="window-height window-width row justify-center items-center">



    <div class="col-md-6">
      <q-banner v-if="timeout" inline-actions class="text-white bg-negative">
        Oturum zaman aşımına uğradı, lütfen yeniden giriş yapın!
      </q-banner>

      <q-banner v-if="fresh" inline-actions class="text-white bg-positive">
        Yeni şifreniz ile giriş yapabilirsiniz!
      </q-banner>

      <q-card square bordered class="q-pa-lg shadow-4">
        <div class="text-center">
          <q-img style="height: 37px; max-width: 97px" basic src="logo.svg" />
        </div>
        <q-card-section>
          <q-form class="q-gutter-md">
            <q-input
              ref="username"
              @keydown.enter="$refs.pwd.focus()"
              autofocus
              square
              color="black"
              v-model="login.username"
              autocomplete="off"
              :rules="[val => !!val || 'Kullanıcı adı zorunludur!']"
              type="text"
              label="kullanıcı">
              <template #before>
                <q-icon name="fas fa-user" />
              </template>
            </q-input>
            <q-input
              ref="pwd"
              @keydown.enter="giris()"
              square
              color="black"
              autocomplete="off"
              v-model="login.password"
              :rules="[val => !!val || 'Şifre zorunludur!']"
              type="password"
              label="şifre">
              <template #before>
                <q-icon name="fas fa-lock" />
              </template>
            </q-input>
            <div class="text-right">
              <q-btn :to="{name: 'remember'}" size="md" flat outline color="blue-grey-10" label="Şifremi unuttum" />
            </div>
          </q-form>
        </q-card-section>
        <q-card-actions class="q-px-md">
          <q-btn @click="giris()" unelevated color="black" size="md" class="full-width" label="Giriş" />
        </q-card-actions>
      </q-card>

      <q-chip>
        <q-avatar icon="fas fa-copyright" color="red" text-color="white" />
        <a target="_blank" href="http://www.btidanismanlik.com" style="color:black;text-decoration:none">BTI</a>
      </q-chip>

    </div>
  </q-page>
</template>
<script>
import { api } from 'boot/axios'
import { common } from 'src/mixins/common'

export default {
  mixins: [common],
  data () {
    return {
      login: {
      }
    }
  },
  mounted () {
    const uname = this.$q.localStorage.getItem('valid_username')
    if (uname) {
      this.$set(this.login, 'username', uname)
      if (this.$refs.pwd) this.$refs.pwd.focus()
    }
    this.$store.commit('application/reset')
  },
  computed: {
    timeout (){
      return (this.$router.currentRoute.query.reason && this.$router.currentRoute.query.reason == 'timeout')
    },
    fresh (){
      return (this.$router.currentRoute.query.reason && this.$router.currentRoute.query.reason == 'new_password')
    },
  },
  methods: {
    giris () {
      if (!this.login.username || !this.login.password) {
        this.um('Kullanıcı ve şifre zorunludur!', { icon: 'fa fa-exclamation-circle' })
        return
      }
      const self = this
      api.post('/token', this.login)
        .then((response) => {
          self.$q.localStorage.set('atoken', response.data.access)
          self.$q.localStorage.set('rtoken', response.data.refresh)
          self.$q.localStorage.set('valid_username', this.login.username)
          self.$nextTick(function () {
            self.$store.dispatch('account/join')
          })
        })
        .catch((err) => {
          if (err && err.response && err.response.status === 401) {
            self.um('Kullanıcı veya şifre hatalı!')
          } else {
            self.um('Sunucu bağlantı hatası!')
          }
        })
    }
  },
  meta () {
    return {
      title: this.$config.company
    }
  },
}
</script>

<style lang="css" scoped>
.text-brand {
  color: #084FA3
}

.bg-brand {
  background: #084FA3
}
</style>
