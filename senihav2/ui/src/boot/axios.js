import Vue from 'vue'
import axios from 'axios'

const ctx = require('../../quasar.conf.js')

Vue.prototype.$axios = axios

const api = axios.create({ baseURL: ctx().api_url })
Vue.prototype.$api = api

export { axios, api }
