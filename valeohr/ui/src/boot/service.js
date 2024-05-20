import axios from 'axios'
import { LocalStorage } from 'quasar'

const ctx = require('../../quasar.conf.js')

var host = window.location.protocol + "//" + window.location.host
var port = window.location.protocol == "https:" ? 8000 : 7979


let api_url

if (ctx().is_dev) {
    api_url = ctx().api_url
} else {
    api_url = host + ':' + port
}


class Service {
  constructor () {
    const service = axios.create({ baseURL: api_url })
    let last = null
    service.interceptors.request.use((config) => {
      config.headers.common.Authorization = 'Bearer ' + LocalStorage.getItem('atoken')
      return config
    })

    service.interceptors.response.use(response => {
      return response
    }, error => {
      let throw_list = [403]
      if (throw_list.includes(error.response.status)){
        throw error
      }
      if (error.response.status === 401) {
        const rtoken = LocalStorage.getItem('rtoken')
        axios.post(api_url + 'api/token/refresh', { refresh: rtoken })
          .then((response) => {
            LocalStorage.set('atoken', response.data.access)
            if (last) {
              const resp = service.request(last)
              last = null
              return resp
            }
          })
          .catch((error) => {
            console.log(error)
            window.location = '/p/login?reason=timeout'
          })
        return
      }
      return Promise.reject(error)
    })

    this.service = service
  }

  get (path, params) {
    this.last = {
      method: 'get',
      url: path,
      responseType: 'json',
      data: params
    }
    return this.service.get(path, {params: params })
  }

  patch (path, payload, callback) {
    this.last = {
      method: 'PATCH',
      url: path,
      responseType: 'json',
      data: payload
    }
    return this.service.request({
      method: 'PATCH',
      url: path,
      responseType: 'json',
      data: payload
    })
  }

  delete (path, payload) {
    this.last = {
      method: 'DELETE',
      url: path,
      responseType: 'json',
      data: payload
    }
    return this.service.request({
      method: 'DELETE',
      url: path,
      responseType: 'json',
      data: payload
    })
  }

  post (path, payload) {
    this.last = {
      method: 'POST',
      url: path,
      responseType: 'json',
      data: payload
    }
    return this.service.request({
      method: 'POST',
      url: path,
      responseType: 'json',
      data: payload
    })
  }
  put (path, payload) {
    this.last = {
      method: 'PUT',
      url: path,
      responseType: 'json',
      data: payload
    }
    return this.service.request({
      method: 'PUT',
      url: path,
      responseType: 'json',
      data: payload
    })
  }


}

export default new Service()
