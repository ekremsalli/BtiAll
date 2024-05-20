import Vue from 'vue'
import Vue2Filters from 'vue2-filters'

const ctx = require('../../quasar.conf.js')
Vue.prototype.$config = ctx()

Vue.use(Vue2Filters)
