import Vue from "vue";
import axios from "axios";

const ctx = require("../../quasar.conf.js");

Vue.prototype.$axios = axios

var host = window.location.protocol + "//" + window.location.host
var port = window.location.protocol == "https:" ? 8000 : 7979


let api_url
if (ctx().is_dev) {
    api_url = ctx().api_url
} else {
    api_url = host + ':' + port
}

const api = axios.create({ baseURL: api_url });
Vue.prototype.$api = api;

export { axios, api };
