<template>
  <v-app style="height:100vh">
    <MainNavBar />
    <router-view />
  </v-app>
</template>

<style lang="scss">
@import "@/styles/index.scss";
</style>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({}),

  methods: {}
};
</script>
