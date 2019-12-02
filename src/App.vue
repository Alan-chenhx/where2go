<template>
  <v-app style="height:100vh">
    <!-- <v-app-bar app color="primary" dark></v-app-bar> -->
    <div>
      <router-view />
    </div>
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
