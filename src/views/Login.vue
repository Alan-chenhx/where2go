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
          <v-col cols="12" sm="8" md="4">
            <material-card  class="elevation-12" title="Login">
              <v-card-text>
                <v-form>
                  <v-text-field label="Username" name="Username" prepend-icon="person" type="text" />

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
        src: require("@/assets/gate.jpg")
      },
      {
        src: require("@/assets/sunset1.jpg")
      },
      {
        src: require("@/assets/sunset2.jpg")
      },
      {
        src: require("@/assets/uni.jpg")
      }
    ]
  }),

  methods: {}
};
</script>