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
          <v-col cols="12" sm="8" md="3">
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
                        label="Username"
                        name="Username"
                        prepend-icon="person"
                        type="text"
                      />

                      <v-text-field
                        label="Password"
                        name="password"
                        prepend-icon="lock"
                        type="password"
                      />
                      <v-btn color="primary" @click="login">Log In</v-btn>
                    </v-form>
                  </v-tab-item>
                  <v-tab-item value="register" align="center">
                    <v-form>
                      <v-text-field
                        label="Username"
                        name="Username"
                        prepend-icon="person"
                        type="text"
                      />

                      <v-text-field
                        label="Password"
                        name="Password"
                        prepend-icon="lock"
                        type="password"
                      />
                      <v-text-field label="Email" name="Email" prepend-icon="email" type="text" />
                      <v-btn color="primary" @click="register">Sign Up</v-btn>
                    </v-form>
                  </v-tab-item>
                </v-tabs-items>
              </v-card-text>
            </material-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "Login",

  components: {},

  data: () => ({
    tab: null,
    backgrounds: [
      {
        src: require("@/assets/yosemite.jpg")
      },
      {
        src: require("@/assets/wof.jpg")
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

  methods: {
    ...mapActions(["login", "register"])
  }
};
</script>