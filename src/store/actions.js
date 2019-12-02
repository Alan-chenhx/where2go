// https://vuex.vuejs.org/en/actions.html

export default {
  login({
    commit
  }, user) {
    return new Promise((resolve, reject) => {
      commit('auth_request')
      this.$http({
          url: '/api/login',
          data: user,
          method: 'POST'
        })
        .then(resp => {
          const currUserId = resp.data.currUserId
          //this.$http.defaults.headers.common['Authorization'] = currUserId
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
      this.$http({
          url: '/api/register',
          data: user,
          method: 'POST'
        })
        .then(resp => {
          const currUserId = resp.data.currUserId
          //this.$http.defaults.headers.common['Authorization'] = currUserId
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
      //delete this.$http.defaults.headers.common['Authorization']
      resolve()
    })
  },
  fetchUserProfile({
    commit
  }, userId) {
    this.$http({
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
    this.$http({
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