import axios from 'axios'
import { LocalStorage } from 'quasar'

const ctx = require('../../quasar.conf.js')



class Service {
  constructor () {
    const api = ctx().api_url
    const service = axios.create({ baseURL: api })
    let last = null
    service.interceptors.request.use((config) => {
      config.headers.common.Authorization = 'Bearer ' + LocalStorage.getItem('atoken')
      return config
    })

    service.interceptors.response.use(response => {
      return response
    }, error => {
      if (error.response.status == 403){
        throw error
      }
      if (error.response.status === 401) {
        const rtoken = LocalStorage.getItem('rtoken')
        axios.post(api + 'api/token/refresh', { refresh: rtoken })
          .then((response) => {
            LocalStorage.set('atoken', response.data.access)
            console.log('last soyle', last)
            if (last) {
              const resp = service.request(last)
              last = null
              return resp
            }
          })
          .catch((error) => {
            console.log(error)
            window.location = '/p/login'
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
    return this.service.get(path, params)
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
}

export default new Service()
