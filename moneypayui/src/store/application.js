const namespaced = true

const state = {
  menu: [],
  broken: false,
  token_verified: false,
  initialized: false,
  public: true,
  ready: false,
  permission_denied: false
}

const getters = {
  menu (state) {
    return state.menu
  },
  loading (state) {
    return !(state.token_verified && state.initialized && state.ready) && state.public && !state.broken && !state.permission_denied
  },
  initialized (state) {
    return state.initialized
  },
  broken (state) {
    return state.broken
  },
  permission_denied (state) {
    return state.permission_denied
  }
}

const actions = {
}

const mutations = {
  reset (state) {
    state.menu = []
    state.broken = false
    state.token_verified = false
    state.initialized = false
    state.public = true
    state.ready = false
  },
  set_menu (state, menu) {
    state.menu = menu
  },
  set_broken (state, broken) {
    state.broken = broken
    if (broken && state.loading) {
      state.loading = false
    }
  },
  set_initialized (state, status) {
    state.initialized = status
  },
  set_verified (state, status) {
    state.token_verified = status
  },
  set_ready (state, status) {
    state.ready = status
  },
  permission_denied (state, status) {
    state.permission_denied = status
  }
}

export default {
  namespaced,
  state,
  getters,
  actions,
  mutations
}
