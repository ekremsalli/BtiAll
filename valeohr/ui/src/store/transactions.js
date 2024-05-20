const namespaced = false

const state = {
    records: {},
    refresh: false,
}

const getters = {
    records: function (state){
        if (state.records) return `${state.records}`
        return '';
    },
    refresh: function (state){
        if (state.refresh) return `${state.refresh}`
        return false;
    }
}

const mutations = {
    records (state, payload) {
        state.records = payload
    },
    refresh (state, payload) {
        state.refresh = payload
    },
}

const actions = {
    records (context, payload){
        context.commit('records', payload)
    },
    refresh (context, payload){
        context.commit('refresh', payload)
    },
}

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations
  }
  