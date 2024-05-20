<template>
  <q-page
    style="background-image: url('bg.png');background-repeat: repeat, repeat;"
    class="window-height window-width row justify-center items-center">

    <div class="col-md-6">
      <q-banner inline-actions class="text-white bg-black">
          Şifremi unuttum
      </q-banner>

      <q-card square bordered class="q-pa-lg shadow-4">
        <div class="text-center">
          <q-img style="height: 37px; max-width: 97px" basic src="logo.svg" />
        </div>
        <q-card-section>
          <q-form @submit.prevent class="q-gutter-md">
            <q-input
              :disable="step != 1"
              @keydown.enter="reset()"
              ref="email"
              autofocus
              square
              color="black"
              v-model="email"
              autocomplete="off"
              :rules="[val => !!val || 'E-posta zorunludur!']"
              type="text"
              label="E-posta">
              <template #before>
                <q-icon name="email" />
              </template>
            </q-input>

            <q-input
              v-if="step > 1"
              :disable="step != 2"
              @keydown.enter="reset()"
              ref="token"
              square
              color="black"
              v-model="token"
              autocomplete="off"
              :rules="[val => !!val || 'Anahtar zorunludur!']"
              type="text"
              label="E-posta adresine gönderilen anahtar">
              <template #before>
                <q-icon name="vpn_key" />
              </template>
            </q-input>

            <q-input
              v-if="step > 2"
              ref="pwd"
              @keydown.enter="$refs.repwd.focus()"
              square
              color="black"
              autocomplete="off"
              v-model="new_password"
              :rules="[val => !!val || 'Şifre zorunludur!']"
              type="password"
              label="Yeni şifre">
              <template #before>
                <q-icon name="fas fa-lock" />
              </template>
              <template #hint>
                <span :key="error" class="text-negative" v-for="error in pwd_errors">
                  {{ error }}
                </span>
              </template>
            </q-input>

            <q-input
              v-if="step > 2"
              ref="repwd"
              @keydown.enter="reset()"
              square
              color="black"
              autocomplete="off"
              v-model="repeat_password"
              type="password"
              label="Yeni şifre (tekrar)">
              <template #before>
                <q-icon name="fas fa-lock" />
              </template>
            </q-input>

            <div class="text-right">
              <q-btn :to="{name: 'login'}" size="md" flat outline color="blue-grey-10" icon="chevron_left" label="Geri dön" />
            </div>

          </q-form>
        </q-card-section>
        <q-card-actions class="q-px-md">
          <q-btn @click="reset()" unelevated color="black" size="md" class="full-width" label="İleri" />
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
      email: null,
      token: null,
      new_password: null,
      repeat_password: null,
      pwd_errors: [],
      step: 1
    }
  },
  methods: {
    transfer_email(){
      const self = this
      if (!this.email) {
        this.um('Geçerli bir e-posta adresi belirtin!', { icon: 'fa fa-exclamation-circle' })
        return
      }
      api.post(`/reset/${this.step}/`, {email: this.email})
        .then((response) => {
          self.$set(self, 'step', 2)
        })
        .catch((err) => {
          self.um('Sunucu bağlantı hatası!')
        })
    },
    validate_token() {
      const self = this
      if (!this.token) {
        this.um('Geçerli bir güvenlik anahtarı belirtin!', { icon: 'fa fa-exclamation-circle' })
        return
      }
      api.post(`/reset/${this.step}/`, {
        email: this.email,
        token: this.token})
        .then((response) => {
          if (response && response.data && response.data.continue) {
            self.$set(self, 'step', 3)
          } else self.um('Geçersiz güvenlik anahtarı!')
        })
        .catch((err) => {
          self.um('Sunucu bağlantı hatası!')
        })
    },
    change_password() {
      const self = this
      if (!this.new_password || !this.repeat_password) {
        this.um('Lütfen bir şifre belirtin!', { icon: 'fa fa-exclamation-circle' })
        return
      }
      if (this.new_password != this.repeat_password) {
        this.um('Şifreler aynı olmalıdır!', { icon: 'fa fa-exclamation-circle' })
        return
      }
      self.$set(self, 'pwd_errors', [])
      api.post(`/reset/${this.step}/`, {
        email: this.email,
        token: this.token,
        new_password: this.new_password
        })
        .then((response) => {
          if (response.data && response.data) {
            if (response.data.continue) {
              self.bm('Şifreniz başarıyla değiştirildi!')
              self.$router.push({ name: 'login', query: { reason: 'new_password' } })
            } else {
              self.$set(self, 'pwd_errors', response.data.errors)
              if (self.pwd_errors.length > 0) {
                self.$set(self, 'repeat_password', '')
                self.$refs.pwd.focus()
              }
            }
          }
        })
        .catch((err) => {
          self.um('Sunucu bağlantı hatası!')
        })
    },

    reset () {
      switch(this.step) {
        case 1:
          this.transfer_email()
          break;
        case 2:
          this.validate_token()
          break;
        case 3:
          this.change_password()
          break;
      }
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
