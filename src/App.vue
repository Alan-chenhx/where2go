<template>
  <v-app>
    <core-MainNavBar />
    <router-view />
  </v-app>
</template>

<style lang="scss">
@import "@/styles/index.scss";
.container {
    -ms-overflow-style: none;  /* Internet Explorer 10+ */
    scrollbar-width: none;  /* Firefox */
}
.container::-webkit-scrollbar { 
    display: none;  /* Safari and Chrome */
}
</style>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({}),

  methods: {}
};
</script>
