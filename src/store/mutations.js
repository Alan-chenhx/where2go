// https://vuex.vuejs.org/en/mutations.html

export default {
  auth_request(state) {
    state.authStatus = 'loading'
  },
  auth_success(state, currUserId) {
    state.authStatus = 'success'
    state.currUserId = currUserId
  },
  auth_error(state) {
    state.authStatus = 'error'
  },
  logout(state) {
    state.authStatus = ''
    state.currUserId = ''
  },
  fetchUserProfile(state, userProfile){
    state.userProfile = userProfile
  },
  fetchPlans(state, plans){
    state.plans = plans
  }
}
