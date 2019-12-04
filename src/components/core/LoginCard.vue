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
            <v-text-field label="Username" name="Username" prepend-icon="person" type="text" />

            <v-text-field label="Password" name="password" prepend-icon="lock" type="password" />
            <v-btn color="primary" @click="login">Log In</v-btn>
          </v-form>
        </v-tab-item>
        <v-tab-item value="register" align="center">
          <v-form>
            <v-text-field label="Username" name="Username" prepend-icon="person" type="text" />

            <v-text-field label="Password" name="Password" prepend-icon="lock" type="password" />
            <v-text-field label="Email" name="Email" prepend-icon="email" type="text" />
            <v-btn color="primary" @click="register">Sign Up</v-btn>
          </v-form>
        </v-tab-item>
      </v-tabs-items>
    </v-card-text>
  </material-card>
</template>

<script>
import { mapActions } from "vuex";
export default {
  methods: {
    ...mapActions(["login", "register"])
  }
};
</script>