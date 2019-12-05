// https://vuex.vuejs.org/en/actions.html
import axios from 'axios'
import state from './state'
//import router from '../router'

export default {
  login({
    commit, dispatch
  }, user) {
    return new Promise((resolve, reject) => {
      commit('auth_request')
      axios({
          url: '/api/login.php',
          data: user,
          method: 'POST'
        })
        .then(resp => {
          const currUserId = resp.data.currUserId
          //axios.defaults.headers.common['Authorization'] = currUserId
          commit('auth_success', currUserId)
          console.log(state.authStatus)
          dispatch('fetchUserProfile', currUserId)
          resolve(resp)
        })
        .catch(err => {
          console.log(err)
          commit('auth_error')
          reject(err)
        })
    })
  },
  register({
    commit, dispatch
  }, user) {
    return new Promise((resolve, reject) => {
      commit('auth_request')
      axios({
          url: '/api/register.php',
          data: user,
          method: 'POST'
        })
        .then(resp => {
          const currUserId = resp.data.currUserId
          //axios.defaults.headers.common['Authorization'] = currUserId
          commit('auth_success', currUserId)
          dispatch('fetchUserProfile', currUserId)
          resolve(resp)
        })
        .catch(err => {
          console.log(err)
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
  deleteUser({
    commit
  }, currUserId) {
    axios({
        url: '/api/deleteUser.php',
        data: currUserId,
        method: 'POST'
      })
      .then(resp => {
        commit('logout')
      })
      .catch(err => {
        console.log(err)
      })
  },
  fetchUserProfile({
    commit
  }, userId) {
    axios({
        url: '/api/getUser.php',
        data: userId,
        method: 'GET'
      })
      .then(resp => {
        commit('getUserProfile', resp.data)
      })
      .catch(err => {
        console.log(err)
      })
  },
  updateUserProfile({
    commit
  }, userProfile) {
    axios({
        url: '/api/updateUser.php',
        data: userProfile,
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
  }, planId, attrId, attr) {
    axios({
        url: '/api/algorithms/updateAttr.php',
        data: [
          planId,
          attrId,
          attr
        ],
        method: 'POST'
      })
      .then(resp => {
        //FIXME 
        const userProfile = resp.data.userProfile
        commit('getUserProfile', userProfile)
      })
      .catch(err => {
        console.log(err)
      })
  },
  addToItinerary({
    commit
  }, planId, attrId, attr) {
    axios({
        url: '/api/algorithms/addAttr.php',
        data: [
          planId,
          attrId,
          attr
        ],
        method: 'POST'
      })
      .then(resp => {
        //FIXME 
        const userProfile = resp.data.userProfile
        commit('getUserProfile', userProfile)
      })
      .catch(err => {
        console.log(err)
      })
  },
  removeFromItinerary({
    commit
  }, planId, attrId) {
    axios({
        url: '/api/algorithms/removeAttr.php',
        data: [
          planId,
          attrId
        ],
        method: 'POST'
      })
      .then(resp => {
        //FIXME 
        const userProfile = resp.data.userProfile
        commit('getUserProfile', userProfile)
      })
      .catch(err => {
        console.log(err)
      })
  },
  fetchPlans({
    commit
  }) {
    axios({
        url: '/api/getPlans.php',
        method: 'GET'
      })
      .then(resp => {
        const plans = resp.data
        commit('getPlans', plans)
      })
      .catch(err => {
        console.log(err)
      })
  },
  fetchPlanDetail({
    commit
  }, planId) {
    axios({
        url: '/api/algorithms/getPlanDetail.php',
        data: planId,
        method: 'POST'
      })
      .then((resp) => {
        const detail = resp.data
        console.log(detail)
        commit('getItinerary', detail)
      })
      .catch(err => {
        console.log(err)
      })
  },
}