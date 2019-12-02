import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import axios from "axios"

// Components
import './components'
// Plugins
import './plugins'
import { sync } from 'vuex-router-sync'

// Sync store with router
sync(store, router)

Vue.config.productionTip = false

Vue.prototype.$http = axios;

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
