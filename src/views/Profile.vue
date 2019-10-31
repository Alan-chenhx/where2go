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
                  <h3 class="title">{{ $store.state.userInfo.username }}</h3>
                </div>
              </div>
            </div>
          </div>
          <div>
            <md-table md-card>
              <md-table-row>
                <md-table-head>Email</md-table-head>
                <md-table-cell>{{ $store.state.userInfo.email }}</md-table-cell>
              </md-table-row>
              <md-table-row>
                <md-table-head>Phone</md-table-head>
                <md-table-cell>{{ $store.state.userInfo.phone }}</md-table-cell>
              </md-table-row>
              <md-table-row>
                <md-table-head>Tag</md-table-head>
                <md-table-cell>
                  <md-button class="md-info" v-show="$store.state.userInfo.tag[0]=='1'">Self Driving</md-button>
                  <md-button class="md-primary" v-show="$store.state.userInfo.tag[1]=='1'">Adventure Seeker</md-button>
                  <md-button class="md-success" v-show="$store.state.userInfo.tag[2]=='1'">Low Budget</md-button>
                </md-table-cell>
              </md-table-row>
            </md-table>
          </div>
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
    return {};
  },
  props: {
    header: {
      type: String,
      default: require("@/assets/img/bg.jpg")
    },
    img: {
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
