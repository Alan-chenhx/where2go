// https://vuex.vuejs.org/en/actions.html
import axios from 'axios'

export default {
  login({
    commit
  }, user) {
    return new Promise((resolve, reject) => {
      commit('auth_request')
      axios({
          url: '/api/login',
          data: user,
          method: 'POST'
        })
        .then(resp => {
          const currUserId = resp.data.currUserId
          //axios.defaults.headers.common['Authorization'] = currUserId
          commit('auth_success', currUserId)
          resolve(resp)
        })
        .catch(err => {
          commit('auth_error')
          reject(err)
        })
    })
  },
  register({
    commit
  }, user) {
    return new Promise((resolve, reject) => {
      commit('auth_request')
      axios({
          url: '/api/register',
          data: user,
          method: 'POST'
        })
        .then(resp => {
          const currUserId = resp.data.currUserId
          //axios.defaults.headers.common['Authorization'] = currUserId
          commit('auth_success', currUserId)
          resolve(resp)
        })
        .catch(err => {
          commit('auth_error', err)
          reject(err)
        })
    })
  },
  logout({
    commit
  }) {
    return new Promise((resolve) => {
      commit('logout')
      //delete axios.defaults.headers.common['Authorization']
      resolve()
    })
  },
  fetchUserProfile({
    commit
  }, userId) {
    axios({
      url: '/api/register',
      data: userId,
      method: 'POST'
    })
    .then(resp => {
      const userProfile = resp.data.userProfile
      commit('fetchUserProfile', userProfile)
    })
    .catch(err => {
      console.log(err)
    })
  },
  fetchPlans({
    commit
  }, userId) {
    axios({
      url: '/api/register',
      data: userId,
      method: 'POST'
    })
    .then(resp => {
      const userProfile = resp.data.userProfile
      commit('fetchPlans', userProfile)
    })
    .catch(err => {
      console.log(err)
    })
  },
}