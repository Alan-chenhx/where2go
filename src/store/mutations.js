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
  getUserProfile(state, userProfile) {
    state.userProfile = userProfile
  },
  getItinerary(state, itinerary) {
    state.itinerary = itinerary
  }
}