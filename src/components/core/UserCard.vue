<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="4">
        <material-card class="v-card-profile">
          <v-avatar slot="offset" class="mx-auto d-block elevation-6" size="130">
            <img :src="user.avatar" />
          </v-avatar>
          <v-card-text class="text-center">
            <v-col v-if="modify" style="text-center">
              <h6 class="overline mb-3">{{user.email}}</h6>
              <h2 class="mb-3">{{user.name}}</h2>
              <p class="font-weight-light">{{user.desciption}}</p>
            </v-col>
            <v-col v-if="!modify">
              <v-text-field label="email" v-model="user.email" />
              <v-text-field label="name" v-model="user.name" />
              <v-textarea outlined label="desciption" v-model="user.desciption" />
            </v-col>
            <v-btn color="success" width="90" @click="toModify" v-if="modify">modify</v-btn>
            <v-btn color="success" width="90" @click="updateInfo(user)" v-if="!modify">save</v-btn>
            <v-btn color="red" class="ml-3" v-if="!modify" dark width="90" @click="deluser = true">Delete</v-btn>
            <core-DeleteDialogue :dialog="deluser" class="mt-4" />
          </v-card-text>
        </material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  data: () => ({
    user: {},
    deluser: false,
    modify: true
  }),

  computed: {
    ...mapState(["userProfile", "currUserId"])
  },

  methods: {
    ...mapActions(["fetchUserProfile", "updateUserProfile"]),
    enable() {
      this.modify = !this.modify;
    },
    toModify() {
      this.modify = !this.modify;
      return this.modify;
    },
    async updateInfo(userProfile) {
      console.log(userProfile);
      await this.updateUserProfile(userProfile).then(() => this.enable());
    }
  },

  watch: {
    userProfile: function() {
      this.user = this.userProfile;
    }
  },

  async created() {
    await this.fetchUserProfile(this.currUserId);
  }
};
</script>