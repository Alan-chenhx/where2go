// https://vuex.vuejs.org/en/getters.html

export default {
  isLoggedIn: state => (state.authStatus=='success'),
}
