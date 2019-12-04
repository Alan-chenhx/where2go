<template>
  <v-container fill-height fluid>
    <v-row justify="center">
      <v-col cols="12" md="4">
        <material-card class="v-card-profile">
          <v-avatar slot="offset" class="mx-auto d-block elevation-6" size="130">
            <img :src="user.avatar" />
          </v-avatar>
          <v-card-text class="text-center pt-n12">
            <v-col style="text-align: center">
              <v-textarea
                class="mt-n12 text--center"
                color="success"
                style=" text-align-last: center; "
                :readonly="modify"
                v-model="user.name"
                :single-line="singleLine"
                :rows="rows"
                :auto-grow="autoGrow"
                :rounded="rounded"
              ></v-textarea>

              <v-textarea
                class="mt-n12"
                color="success"
                style=" text-align-last: center; "
                :readonly="modify"
                v-model="user.email"
                :single-line="singleLine"
                :rows="rows"
                :auto-grow="autoGrow"
                :rounded="rounded"
              ></v-textarea>

              <v-textarea
                class="mt-n10"
                color="success"
                style=" text-align-last: center; "
                :readonly="modify"
                v-model="user.discription"
                :single-line="singleLine"
                :rows="rows"
                :auto-grow="autoGrow"
                :rounded="rounded"
              ></v-textarea>
            </v-col>
            <v-btn color="success" @click="updateUserProfile(currUserId, userProfile)">{{ button }}</v-btn>
            <core-DeleteDialogue :hidden="modify" class="mt-4" />
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
    modify: true,
    rows: 1,
    singleLine: true,
    rounded: true,
    autoGrow: true
  }),

  computed: {
    ...mapState(["userProfile", "currUserId"]),
    button() {
      if (this.modify) {
        return "Modify";
      } else {
        return "Save";
      }
    }
  },

  methods: {
    ...mapActions(['fetchUserProfile', 'updateUserProfile']),
    enable() {
      this.modify = !this.modify;
    }
  },

  watch: {
    userProfile: function() {
      this.user = this.userProfile
    }
  },

  async created () {
    await this.fetchUserProfile(this.currUserId)
  }
};
</script>