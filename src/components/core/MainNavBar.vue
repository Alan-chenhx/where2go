<template>
  <div>
    <v-app-bar app color="white" dark :hide-on-scroll="['login'].indexOf($route.name) == -1">
      <v-toolbar-items>
        <v-img :src="require('@/assets/logob.png')" />
      </v-toolbar-items>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-menu bottom open-on-hover offset-y>
        <template v-slot:activator="{ on }">
          <v-btn v-on="on">
            <v-icon>face</v-icon>
            {{ userProfile.name }}
          </v-btn>
        </template>

        <v-list class="dropdown-menu">
          <v-list-item v-if="!isLoggedIn" @click="toLogin">
            <v-list-item-content>
              <v-icon>fingerprint</v-icon>
            </v-list-item-content>
            <v-list-item-title>Log In</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="isLoggedIn" @click="logout">
            <v-list-item-content>
              <v-icon>clear</v-icon>
            </v-list-item-content>
            <v-list-item-title>Log Out</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
  </div>
</template>


<script>
import { mapGetters, mapActions, mapState } from "vuex";
export default {
  computed: {
    ...mapState(["userProfile"]),
    ...mapGetters(["isLoggedIn"])
  },
  data: () => ({}),
  methods: {
    ...mapActions(["logout"]),
    toLogin() {
      this.$router.push("/login");
    }
  }
};
</script>

<style>
</style>
    