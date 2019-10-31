<template>
  <div class="wrapper">
    <div class="section page-header header-filter" :style="headerStyle">
      <div class="container">
        <div class="md-layout">
          <div
            class="md-layout-item md-size-33 md-small-size-66 md-xsmall-size-100 md-medium-size-40 mx-auto"
          >
            <login-card header-color="green">
              <h4 slot="title" class="card-title">Login</h4>
              <p slot="description" class="description">Hi There</p>
              <md-field class="md-form-group" slot="inputs">
                <md-icon>face</md-icon>
                <label>User Name...</label>
                <md-input v-model="username"></md-input>
              </md-field>
              <md-field class="md-form-group" slot="inputs">
                <md-icon>email</md-icon>
                <label>Email...</label>
                <md-input v-model="email" type="email"></md-input>
              </md-field>
              <md-field class="md-form-group" slot="inputs">
                <md-icon>lock_outline</md-icon>
                <label>Password...</label>
                <md-input type="password" v-model="password"></md-input>
              </md-field>
              <md-button slot="footer" class="md-simple md-success md-lg" @click="login">Log in</md-button>
              <md-button slot="footer" class="md-simple md-success md-lg" @click="register">Register</md-button>
            </login-card>
            <modal v-if="popupModal">
              <template slot="header">
                <md-button
                  class="md-simple md-just-icon md-round modal-default-button"
                  @click="popupModalHide"
                >
                  <md-icon>clear</md-icon>
                </md-button>
              </template>

              <template slot="body">
                <p class="text-primary">{{ popupInfo }}</p>
              </template>
            </modal>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { LoginCard, Modal } from "@/components";

export default {
  components: {
    LoginCard,
    Modal
  },
  bodyClass: "login-page",
  data() {
    return {
      popupModal: false,
      popupInfo: "",
      username: null,
      password: null,
      email: null
    };
  },
  props: {
    header: {
      type: String,
      default: require("@/assets/img/bg.jpg")
    }
  },
  computed: {
    headerStyle() {
      return {
        backgroundImage: `url(${this.header})`
      };
    }
  },
  methods: {
    login() {
      if (this.username && this.email && this.password) {
        this.toLogin();
      }
    },

    toLogin() {
      //let password_sha = hex_sha1(hex_sha1( this.password ));
      let password_sha = this.password;

      this.$http
        .post("/login.php", { username: this.username, password: password_sha })
        .then(response => {
          if (response.data.success == 1) {
            let expireDays = 1000 * 60 * 60 * 24 * 15;
            console.log("success");
            this.setCookie("session", response.data.session, expireDays);
            this.getUserInfo();
            this.$router.push("/profile");
          } else {
            this.popupInfo = "Incorrent User Name or Password!";
            this.popupModal = true;
          }
        })
        .catch(error => {
          console.log(error);
        });
    },

    register() {
      if (this.username && this.email && this.password) {
        this.toRegister();
      }
    },

    toRegister() {
      let password_sha = this.password;
      let registerParam = {
        username: this.username,
        email: this.email,
        password: password_sha
      };

      console.log(registerParam);
      this.$http
        .post("/register.php", {
          username: this.username,
          email: this.email,
          password: password_sha
        })
        .then(response => {
          if (response.data.code == 1) {
            this.popupInfo = "You have successfully registered!";
            this.popupModal = true;
          }
        })
        .catch(error => {
          console.log(error);
        });

      this.popupModal = true;
    },

    popupModalHide() {
      this.popupModal = false;
      this.$router.go();
    },

    getUserInfo() {
      this.$http
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
            portrait: require("@/assets/img/profile/1.jpg")
          };
          this.$store.commit("updateUserInfo", userInfo);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style lang="css"></style>
