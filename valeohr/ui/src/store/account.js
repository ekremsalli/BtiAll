import Service from 'boot/service'
import { LocalStorage, Notify, LoadingBar, Loading } from 'quasar'

const namespaced = true

const state = {
  user: null,
  logged: false
}

const getters = {
  logged: function (state) {
    return state.logged
  },
  has_logged: function (state) {
    return LocalStorage.getItem('atoken')
  },
  fullname: function (state) {
    if (state.user) return `${state.user.detail.name} ${state.user.detail.surname}`
    return ''
  },
  username: function (state) {
    if (state.user) return `${state.user.username}`
    return ''
  },
  first_name: function (state) {
    if (state.user) return `${state.user.detail.name}`
    return ''
  },
  is_staff: function (state) {
    if (state.user) return state.user.is_staff
  },
  is_superuser: function (state) {
    if (state.user) return state.user.is_superuser
  },
  is_staff_or_super: function (state) {
    if (state.user) return state.user.is_staff || state.user.is_superuser
  },
  perms: function (state) {
    if (state.user) return state.user.user_permissions
  },
  perm_check: (state) => px => {
    if (state.user) {
      return state.user.user_permissions.includes(px)
    }
    return false
  }
}

const actions = {
  join (context) {
    context.dispatch('check')
  },
  verify_again (context) {
    const token = LocalStorage.getItem('atoken')
    Service.post('/token/verify', { token: token })
      .then((response) => {
        context.dispatch('enter')
      })
      .catch(() => {
        context.commit('timeout')
      })
  },
  check (context) {
    if (LocalStorage.getItem('atoken')) {
      let size = LoadingBar.size
      LoadingBar.setDefaults({'size': '0px'})

      Service.post('/token/verify', { token: LocalStorage.getItem('atoken') })
        .then((response) => {
          context.dispatch('enter')
        })
        .catch((error) => {
          if (error.response) {
            if (error.response.status === 401) {
              const rtoken = LocalStorage.getItem('rtoken')
              Service.post('/token/refresh', { refresh: rtoken })
                .then((response) => {
                  LocalStorage.set('atoken', response.data.access)
                  context.dispatch('verify_again')
                })
                .catch((error) => {
                  if (error.response.status === 401) context.commit('timeout')
                  else context.commit('application/set_broken', true, { root: true })
                })
            } else context.commit('application/set_broken', true, { root: true })
          } else context.commit('application/set_broken', true, { root: true })
        })
        .finally(() => {
          LoadingBar.setDefaults({'size': size})

        }) 
    } else {
      // no token no cry!
      context.commit('_clear')
      this.$router.push({ name: 'login', query: { reason: 'timeout' } })
    }
  },
  enter (context) {
    this.commit('application/set_verified', true)
    Service.get('user/profile')
      .then((response) => {
        if (response.data.user) {
          context.commit('set_user', response.data.user)
          context.commit('application/set_menu', response.data.menu, { root: true })
          context.commit('application/set_initialized', true, { root: true })
          context.commit('application/set_ready', true, { root: true })
        }
      })
      .catch((err) => {
        if (err.response) {
          if (err.response.status === 401) {
            context.commit('timeout')
          } else {
            if (err.response.status == 403) {
              Notify.create({
                color: 'negative',
                position: 'top',
                icon: 'fa fa-exclamation-triangle',
                message: 'Yetki hatası!'
              })
              context.commit('application/permission_denied', true, { root: true })
            } else {
              context.commit('application/set_broken', true, { root: true })
            }
          }
        }
      })
  }
}

const mutations = {
  _clear () {
    state.user = null
    state.logged = false
    LocalStorage.remove('atoken')
    LocalStorage.remove('rtoken')
    this.commit('application/reset')
  },
  logout (state) {
    this.commit('account/_clear')
    Notify.create({
      color: 'dark',
      position: 'top',
      icon: 'fa fa-check',
      message: 'Oturum başarıyla kapatıldı!'
    })
    this.$router.push({ name: 'login' })
  },
  timeout (state) {
    this.commit('account/_clear')
    this.$router.push({ name: 'login', query: { reason: 'timeout' } })
  },
  set_user (state, user) {
    state.user = user
    state.logged = true
    if (this.$router.history.current.name === 'login') this.$router.push({ name: 'dashboard' })
  }
}

export default {
  namespaced,
  state,
  getters,
  actions,
  mutations
}
