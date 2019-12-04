<template>
  <material-card class="elevation-12">
    <template v-slot:header>
      <v-tabs v-model="tab" centered>
        <v-tabs-slider></v-tabs-slider>

        <v-tab href="#login">Log in</v-tab>

        <v-tab href="#register">Sign Up</v-tab>
      </v-tabs>
    </template>
    <v-card-text>
      <v-tabs-items v-model="tab">
        <v-tab-item value="login" align="center">
          <v-form>
            <v-text-field
              :error="authStatus=='error' || !eclear"
              label="Username"
              name="Username"
              :rules="nameRules"
              v-model="username"
              prepend-icon="person"
              type="text"
            />

            <v-text-field
              :error="authStatus=='error' || !eclear"
              label="Password"
              name="password"
              :rules="passwordRules"
              v-model="password"
              prepend-icon="lock"
              type="password"
            />
            <v-btn color="primary" @click="login({'username':username, 'password':password})">Log In</v-btn>
          </v-form>
        </v-tab-item>
        <v-tab-item value="register" align="center">
          <v-form>
            <v-text-field
              label="Username"
              name="Username"
              :rules="nameRules"
              v-model="username"
              prepend-icon="person"
              type="text"
            />
            <v-text-field
              label="Password"
              name="Password"
              :rules="passwordRules"
              v-model="password"
              prepend-icon="lock"
              type="password"
            />
            <v-text-field
              label="Email"
              name="Email"
              :rules="emailRules"
              v-model="email"
              prepend-icon="email"
              type="text"
            />
            <v-btn
              color="primary"
              @click="register({'username':username, 'password':password, 'email':email})"
            >Sign Up</v-btn>
          </v-form>
        </v-tab-item>
      </v-tabs-items>
    </v-card-text>
  </material-card>
</template>

<script>
import { mapActions, mapState } from "vuex";
export default {
  computed: {
    ...mapState(["authStatus"])
  },
  data: () => ({
    eclear: true,
    tab: null,
    username: "",
    password: "",
    email: "",
    nameRules: [
      v => !!v || "Name is required",
      v => (v && v.length <= 10) || "Name must be less than 10 characters"
    ],
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+\..+/.test(v) || "E-mail must be valid"
    ],
    passwordRules: [
      v => !!v || "Password is required",
      v => (v && v.length >= 6) || "Password must be greater than 6 characters"
    ]
  }),
  methods: {
    ...mapActions(["login", "register"])
  },
  watch: {
    authStatus: function() {
      if (this.authStatus == "success") {
        this.$router.push("/home");
      }
    },
    username: function() {
      this.eclear = true;
    }
  }
};
</script>