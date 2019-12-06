<template>
  <v-app>
    <v-content>
      <core-UserCard />
      <v-row>
        <v-container>
          <v-data-iterator
            :items="plans"
            :items-per-page.sync="itemsPerPage"
            :page="page"
            hide-default-footer
          >
            <template v-slot:default="props">
              <v-row>
                <v-col v-for="(item, i) in props.items" :key="i" cols="12" sm="6" md="4" lg="3">
                  <v-hover v-slot:default="{ hover }">
                    <v-card @click="toPlan(item.planId)" :elevation="hover ? 12 : 2">
                      <v-responsive :aspect-ratio="6/5">
                        <v-img
                          :src="item.cover"
                          height="100%"
                          class="white--text text-center align-end d-flex"
                        >
                          <v-card-title
                            class="d-flex font-weight-black justify-center display-1"
                          >{{ item.name }}</v-card-title>
                          <v-card-subtitle
                            class="white--text align-center justify-center subtitle-1 font-weight-black"
                          >{{ item.start }} - {{ item.end }}</v-card-subtitle>
                          <v-spacer />
                          <v-card-text
                            style="filter: opacity(80%);"
                            class="text--primary text-center white"
                          >
                            <div v-if="hover">
                              <span style="font-weight: bold;">Preferences:</span>
                              {{ item.tag }}
                            </div>
                            <div v-if="hover">
                              <span style="font-weight: bold;">Pace:</span>
                              {{ item.pace }}
                            </div>
                            <div v-else>{{ item.pace }} pace</div>
                          </v-card-text>
                        </v-img>
                      </v-responsive>
                    </v-card>
                  </v-hover>
                </v-col>
              </v-row>
            </template>
            <template v-slot:footer>
              <v-row class="mt-2" align="center" justify="center">
                <span class="grey--text">Items per page</span>
                <v-menu offset-y>
                  <template v-slot:activator="{ on }">
                    <v-btn dark text color="primary" class="ml-2" v-on="on">
                      {{ itemsPerPage }}
                      <v-icon>mdi-chevron-down</v-icon>
                    </v-btn>
                  </template>
                  <v-list>
                    <v-list-item
                      v-for="(number, index) in itemsPerPageArray"
                      :key="index"
                      @click="updateItemsPerPage(number)"
                    >
                      <v-list-item-title>{{ number }}</v-list-item-title>
                    </v-list-item>
                  </v-list>
                </v-menu>

                <v-spacer></v-spacer>

                <span class="mr-6 grey--text">Page {{ page }} of {{ numberOfPages }}</span>
                <v-btn fab dark color="blue darken-3" class="mr-1" @click="formerPage">
                  <v-icon>mdi-chevron-left</v-icon>
                </v-btn>
                <v-btn fab dark color="blue darken-3" class="ml-1" @click="nextPage">
                  <v-icon>mdi-chevron-right</v-icon>
                </v-btn>
              </v-row>
            </template>
          </v-data-iterator>
        </v-container>
      </v-row>
    </v-content>
  </v-app>
</template>
<style>
.v-card--reveal {
  opacity: 0.5;
}
</style>
<script>
import { mapState, mapMutations, mapActions } from "vuex";
import { async } from "q";

export default {
  name: "Plans",
  data: () => ({
    itemsPerPageArray: [8, 12, 16],
    itemsPerPage: 8,
    page: 1
  }),
  computed: {
    ...mapState(["plans"]),
    numberOfPages() {
      return Math.ceil(this.plans.length / this.itemsPerPage);
    },
    filteredKeys() {
      return this.keys.filter(key => key !== `Name`);
    }
  },
  methods: {
    ...mapActions(["fetchPlans"]),
    nextPage() {
      if (this.page + 1 <= this.numberOfPages) this.page += 1;
    },
    formerPage() {
      if (this.page - 1 >= 1) this.page -= 1;
    },
    updateItemsPerPage(number) {
      this.itemsPerPage = number;
    },
    toPlan(planId, startDate) {
      this.$store.commit('getCurrPlanId', planId);
      this.$store.commit('getCurrStart', startDate);
      setTimeout(
        this.$router.push('/plan-detail')
      ,200)
    }
  },

  async created() {
    await this.fetchPlans();
  },

  async beforeRouteUpdate(to, from, next) {
    await this.fetchPlans().then(next());
  }
};
</script>