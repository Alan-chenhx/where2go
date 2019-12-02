<template>
  <v-app style="height:100vh">
    <v-content>
      <v-carousel :show-arrows="false" hide-delimiters cycle height="100%">
        <v-carousel-item v-for="(item,i) in backgrounds" :key="i" :src="item.src"></v-carousel-item>
      </v-carousel>
    </v-content>
    <v-content style="z-index:5;position:fixed;width:100%;height:100%">
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4">
            <material-card  class="elevation-12" title="Login">
              <v-card-text>
                <v-form>
                  <v-text-field label="Login" name="login" prepend-icon="person" type="text" />

                  <v-text-field
                    id="password"
                    label="Password"
                    name="password"
                    prepend-icon="lock"
                    type="password"
                  />
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn color="primary">Sign Up</v-btn>
                <v-btn color="primary">Login</v-btn>
              </v-card-actions>
            </material-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "Login",

  components: {
  },

  data: () => ({
    backgrounds: [
      {
        src: "https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg"
      },
      {
        src: "https://cdn.vuetifyjs.com/images/carousel/sky.jpg"
      },
      {
        src: "https://cdn.vuetifyjs.com/images/carousel/bird.jpg"
      },
      {
        src: "https://cdn.vuetifyjs.com/images/carousel/planet.jpg"
      }
    ]
  }),

  methods: {}
};
</script>