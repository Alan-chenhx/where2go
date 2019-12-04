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
                class="mt-n12 text--center "
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
            <v-btn color="success" @click="enable">{{ bottum }}</v-btn>
            <core-DeleteDialogue :hidden="modify" class="mt-4"/>
          </v-card-text>
        </material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    user: {
      name: "Abdu Alawini",
      avatar:
        "https://wiki.illinois.edu/wiki/download/attachments/700856761/BV32p154.jpg?version=1&modificationDate=1565897325000",
      email: "alawini@illinois.edu ",
      discription: "laobi"
    },
    modify: true,
    rows: 1,
    singleLine: true,
    rounded: true,
    autoGrow: true
  }),

  computed: {
    bottum() {
      if (this.modify) {
        return "Modify";
      } else {
        return "Save";
      }
    }
  },

  methods: {
    enable() {
      this.modify = !this.modify;
    }
  }
};
</script>