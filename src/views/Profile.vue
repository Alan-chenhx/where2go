<template>
  <div class="wrapper">
    <parallax class="section page-header header-filter" :style="headerStyle"></parallax>
    <div class="main main-raised">
      <div class="section profile-content">
        <div class="container">
          <div class="md-layout">
            <div class="md-layout-item md-size-50 mx-auto">
              <div class="profile">
                <div class="avatar">
                  <img
                    :src="this.$store.state.userInfo.portrait"
                    alt="Circle Image"
                    class="img-raised rounded-circle img-fluid"
                  />
                </div>
                <div class="name">
                  <h3 class="title">{{ this.$store.state.userInfo.username }}</h3>
                </div>
              </div>
            </div>
          </div>
          <div>
            <md-table md-card>
              <md-table-row>
                <md-table-head>Email</md-table-head>
                <md-table-cell v-if="!isEditting">{{ this.$store.state.userInfo.email }}</md-table-cell>
                <md-table-cell v-else>
                  <md-field>
                    <md-input v-model="email"></md-input>
                  </md-field>
                </md-table-cell>
              </md-table-row>
              <md-table-row>
                <md-table-head>Phone</md-table-head>
                <md-table-cell v-if="!isEditting">{{ this.$store.state.userInfo.phone }}</md-table-cell>
                <md-table-cell v-else>
                  <md-field>
                    <md-input v-model="phone"></md-input>
                  </md-field>
                </md-table-cell>
              </md-table-row>
              <md-table-row>
                <md-table-head>Tag</md-table-head>
                <md-table-cell v-if="!isEditting">
                  <md-button
                    class="md-info"
                    v-show="this.$store.state.userInfo.tag[0]=='1'"
                  >Self Driving</md-button>
                  <md-button
                    class="md-primary"
                    v-show="this.$store.state.userInfo.tag[1]=='1'"
                  >Adventure Seeker</md-button>
                  <md-button
                    class="md-success"
                    v-show="this.$store.state.userInfo.tag[2]=='1'"
                  >Low Budget</md-button>
                </md-table-cell>
                <md-table-cell v-else>
                  <md-checkbox v-model="tag0" value="true">Self Driving</md-checkbox>
                  <md-checkbox v-model="tag1" value="true">Adventure Seeker</md-checkbox>
                  <md-checkbox v-model="tag2" value="true">Low Budget</md-checkbox>
                </md-table-cell>
              </md-table-row>
            </md-table>
          </div>
          <div>
            <md-button class="md-block" @click="edit" v-if="!isEditting">Edit</md-button>
            <md-button class="md-info md-block" @click="updateInfo" v-else>Update</md-button>
            <md-button class="md-rose md-block" @click="deleteMyself">Delete</md-button>
          </div>
          <p></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Tabs } from "@/components";

export default {
  components: {
    Tabs
  },
  bodyClass: "profile-page",
  data() {
    return {
      username: "",
      email: "",
      phone: "",
      tag0: false,
      tag1: false,
      tag2: false,
      isEditting: false
    };
  },
  props: {
    header: {
      type: String,
      default: require("@/assets/img/bg.jpg")
    }
  },
  computed: {
    headerStyle() {
      return {
        backgroundImage: `url(${this.header})`
      };
    }
  },
  methods: {
    edit() {
      this.isEditting = true;
    },
    updateInfo() {
      let tag = "";
      if (this.tag0) tag += "1";
      else tag += "0";
      if (this.tag1) tag += "1";
      else tag += "0";
      if (this.tag2) tag += "1";
      else tag += "0";
      let portrait = parseInt(Math.random() * (4 - 1 + 1), 10) + 1;
      this.$http
        .post("/updateinfo.php", {
          email: this.email,
          phone: this.phone,
          tag: tag,
          portrait: portrait.toString()
        })
        .catch(error => {
          console.log(error);
        });
      let userInfo = {
        username: this.$store.state.userInfo.username,
        uid: this.$store.state.userInfo.uid,
        email: this.email,
        phone: this.phone,
        tag: tag,
        portrait: require("@/assets/img/profile/" +
          portrait.toString() +
          ".jpg")
      };
      this.$store.commit("updateUserInfo", userInfo);
      this.isEditting = false;
    },
    deleteMyself() {
      this.$http.post("/delete.php", {});
      this.delCookie("session");
      let userInfo = {
        username: "USER",
        uid: null,
        email: "",
        phone: "",
        tag: "000",
        portrait: require("@/assets/img/profile/1.jpg")
      };
      this.$store.commit("updateUserInfo", userInfo);
      this.$router.push("/");
    }
  },
  created() {
    if (!this.getCookie("session")) {
      this.$router.push("/login");
    }
  }
};
</script>

<style lang="scss" scoped>
.section {
  padding: 0;
}

.profile-tabs /deep/ {
  .md-card-tabs .md-list {
    justify-content: center;
  }

  [class*="tab-pane-"] {
    margin-top: 3.213rem;
    padding-bottom: 50px;

    img {
      margin-bottom: 2.142rem;
    }
  }
}
</style>
