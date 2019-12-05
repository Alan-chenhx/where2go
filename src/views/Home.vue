<template>
  <v-app>
    <v-content>
      <v-carousel :show-arrows="false" hide-delimiters cycle height="100vh">
        <v-carousel-item v-for="(item,i) in backgrounds" :key="i" :src="item.src"></v-carousel-item>
      </v-carousel>
    </v-content>
    <v-content style="z-index:1;position:fixed;width:100%;height:100%">
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="5">
            <core-NewTripCard />
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "Home",

  components: {},

  data: () => ({
    backgrounds: [
      {
        src: require("@/assets/yosemite.jpg")
      },
      {
        src: require("@/assets/lake.jpeg")
      },
      {
        src: require("@/assets/sunset1.jpg")
      },
      {
        src: require("@/assets/sunset2.jpg")
      },
      {
        src: require("@/assets/uni.jpg")
      },
      {
        src: require("@/assets/cali1.jpg")
      },
      {
        src: require("@/assets/gate.jpg")
      }
    ]
  }),
};
</script>