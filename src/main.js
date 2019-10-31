import Vue from "vue";
import App from "./App.vue";
import Vuex from "vuex";
import router from "./router";
import axios from "axios";

import MaterialKit from "./plugins/material-kit";

Vue.config.productionTip = false;

Vue.prototype.$http = axios;

Vue.use(Vuex);
Vue.use(MaterialKit);

const NavbarStore = {
  showNavbar: false
};

Vue.mixin({
  data() {
    return {
      NavbarStore
    };
  }
});

const store = new Vuex.Store({
  state: {
    isLogged: false,
    userInfo: {
      username: "USER",
      uid: null,
      email: "",
      phone: "",
      tag: "000",
      portrait: "1"
    }
  },
  mutations: {
    updateIsLogged(state, newState) {
      state.isLogged = newState;
    },
    updateUserInfo(state, newUserInfo) {
      state.userInfo = newUserInfo;
    }
  }
});

Vue.prototype.getUserInfo = () => {
  axios
    .get("/getuser.php")
    .then(response => {
      //Success
      console.log(response.data.uname);
      console.log(response.data.usid);
      console.log(response.data.email);
      console.log(response.data.phone);
      console.log(response.data.tag);
      let userInfo = {
        username: response.data.uname,
        uid: response.data.usid,
        email: response.data.email,
        phone: response.data.phone,
        tag: response.data.tag,
        portrait: require("@/assets/img/profile/" +
          response.data.portrait +
          ".jpg")
      };
      this.$store.commit("updateUserInfo", userInfo);
    })
    .catch(error => {
      console.log(error);
    });
};

Vue.prototype.setCookie = (c_name, value, expiredays) => {
  let exdate = new Date();
  exdate.setDate(exdate.getDate() + expiredays);
  document.cookie =
    c_name +
    "=" +
    escape(value) +
    (expiredays == null ? "" : ";expires=" + exdate.toGMTString());
};

function getCookie(name) {
  let arr,
    reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
  if ((arr = document.cookie.match(reg))) return arr[2];
  else return null;
}
Vue.prototype.getCookie = getCookie;

Vue.prototype.delCookie = name => {
  let exp = new Date();
  exp.setTime(exp.getTime() - 1);
  let cval = getCookie(name);
  if (cval != null)
    document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString();
};

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
