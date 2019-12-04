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
        url: '/api/user',
        data: userId,
        method: 'GET'
      })
      .then(resp => {
        const userProfile = resp.data.userProfile
        commit('getUserProfile', userProfile)
      })
      .catch(err => {
        console.log(err)
      })
  },
  updateUserProfile({
    commit
  }, userId) {
    axios({
        url: '/api/user',
        data: userId,
        method: 'POST'
      })
      .then(resp => {
        commit('getUserProfile', userProfile)
      })
      .catch(err => {
        console.log(err)
      })
  },
  updateItinerary({
    commit
  }, planId, itId, attr) {
    axios({
        url: '/api/updateIt',
        data: [
          planId, 
          itId,
          attr
        ],
        method: 'POST'
      })
      .then(resp => {
        //FIXME 
        commit('getUserProfile', userProfile)
      })
      .catch(err => {
        console.log(err)
      })
  },
  addToItinerary({
    commit
  }, planId, itId, attr) {
    axios({
        url: '/api/addAttr',
        data: [
          planId, 
          itId,
          attr
        ],
        method: 'POST'
      })
      .then(resp => {
        //FIXME 
        commit('getUserProfile', userProfile)
      })
      .catch(err => {
        console.log(err)
      })
  },
  removeFromItinerary({
    commit
  }, planId, itId, attr) {
    axios({
        url: '/api/removeAttr',
        data: [
          planId, 
          itId
        ],
        method: 'POST'
      })
      .then(resp => {
        //FIXME 
        commit('getUserProfile', userProfile)
      })
      .catch(err => {
        console.log(err)
      })
  },
  fetchPlans({
    commit
  }, userId) {
    axios({
        url: '/api/plans',
        data: userId,
        method: 'GET'
      })
      .then(resp => {
        const plans = resp.data.plans
        commit('getPlans', userProfile)
      })
      .catch(err => {
        console.log(err)
      }),
  },
  fetchPlanDetail({
    commit
  }, planId) {
    axios({
        url: '/api/plans',
        data: planId,
        method: 'GET'
      })
      .then(resp => {
        const attrs = resp.data.attrs
        const planPref = resp.data.planPref
        commit('getAttrs', attrs)
        commit('getPlanPref', planPref)
      })
      .catch(err => {
        console.log(err)
      }),
  },
}