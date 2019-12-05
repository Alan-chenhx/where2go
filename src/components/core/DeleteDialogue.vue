<template>
  <v-dialog v-model="dialog" max-width="350">
    <v-card>
      <v-card-title class="headline">Do you want to delete your account ?</v-card-title>

      <v-card-text>Are you sure you want to delete your account?</v-card-text>
      <v-card-text>If you want to change your email address/ name/ discription, simply do so in the previous page.</v-card-text>
      <v-card-text>
        <span class="font-weight-black">Please note:</span>If you delete your account, you won't be able to reactivate it later.
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn color="green darken-1" text @click="toDeleteUser(false)">Disagree</v-btn>

        <v-btn color="green darken-1" text @click="toDeleteUser(true)">Agree</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapActions, mapState } from "vuex";

//FIXME 

export default {
  computed: {
    ...mapState(['currUserId']),
  },
  props: {
    dialog: Boolean,
  },
  methods: {
    ...mapActions(['deleteUser']),
    toDeleteUser(agree) {
      let myDialog = this.dialog;
      this.$emit("close-dialog", myDialog);
      if (agree) {
        this.deleteUser(this.currUserId)
      }
    }
  }
};
</script>