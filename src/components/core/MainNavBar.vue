<template>
  <div>
    <v-app-bar app color="white" dark :hide-on-scroll="['login', 'home'].indexOf($route.name) == -1">
      <v-toolbar-items>
        <v-img :src="require('@/assets/logob.png')" />
      </v-toolbar-items>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon color="black" v-if="isLoggedIn"  @click="toPlans">mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon color="black" v-if="isLoggedIn"  @click="toCreate">mdi-plus</v-icon>
      </v-btn>

      <v-menu bottom open-on-hover offset-y>
        <template v-slot:activator="{ on }">
          <v-btn v-on="on">
            <v-icon>face</v-icon>
            <span>{{ isLoggedIn?userProfile.uname:'USER' }}</span>
          </v-btn>
        </template>

        <v-list class="dropdown-menu">
          <v-list-item v-if="!isLoggedIn" @click="toLogin">
            <v-list-item-content>
              <v-icon>fingerprint</v-icon>
            </v-list-item-content>
            <v-list-item-title>Log In</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="isLoggedIn" @click="toLogout">
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
    ...mapGetters(["isLoggedIn"]),
    
  },
  data: () => ({}),
  methods: {
    ...mapActions(["logout"]),
    async toLogout() {
      await logout().then(this.$route.push('/'))
    },
    toLogin() {
      this.$router.push("/login");
    },
    toCreate() {
      this.$router.push("/home");
    },
    toPlans() {
      this.$router.push("/plans");
    }
  }
};
</script>

<style>
</style>
    