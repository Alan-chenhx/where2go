<template>
  <v-content>
    <v-container>
      <v-row justify="center">
        <v-col cols="1" :v-if="!loading">
          <div>
            <div class="d-flex flex-column" style="height: 90vh;overflow-y: auto;position: fixed;">
              <div
                class="text-center"
              >{{ toDate(0).toLocaleString('default', { month: 'short' }).toUpperCase()}}</div>
              <div v-for="n in numDays" :key="n">
                <div
                  class="text-center"
                  v-if="toDate(n-1).getMonth() != toDate(n-2).getMonth()"
                >{{ toDate(n-1).toLocaleString('default', { month: 'short' }).toUpperCase() }}</div>
                <v-btn
                  class="black--text ma-0"
                  @click="scrollToDate(n-1)"
                  icon
                  text
                >{{ toDate(n-1).getDate() }}</v-btn>
              </div>
            </div>
          </div>
        </v-col>
        <v-col cols="9" :v-if="!loading">
          <v-timeline dense>
            <div v-for="(day, i) in itinerary" :key="i">
              <v-timeline-item fill-dot small :id="'date-'+i">
                <template v-slot:icon>
                  <v-sheet
                    class="title text-no-wrap pa-2 white--text"
                    color="black"
                  >{{toDate(i).toLocaleString('default', { weekday: 'short', day: 'numeric', month: 'short'})}}</v-sheet>
                </template>
              </v-timeline-item>
              <v-timeline-item
                large
                class="align-center"
                v-if="!!day[0].city?(i>0&&!!itinerary[i-1][0].city)?day[0].city!=itinerary[i-1][0].city:true:false"
              >
                <span class="headline text-center text-no-wrap">{{day[0].city}}</span>
              </v-timeline-item>
              <draggable :v-model="day" :group="'city'+day[0].city">
                <div v-for="(attr, j) in day" :key="j">
                  <v-timeline-item>
                    <template v-slot:icon>
                      <v-sheet
                        class="text-no-wrap pa-2 white--text text-center"
                        color="purple"
                        min-width="90"
                      >{{attr.duration}} mins</v-sheet>
                    </template>
                    <v-card class="elevation-3">
                      <v-img
                        gradient="to top right, rgba(100,115,201,.33), rgba(25,32,72,.7)"
                        :src="attr.photo"
                        max-height="150"
                        class="white--text v-card--reveal;"
                      >
                        <v-card-title
                          class="headline"
                          :class="attr.photo?'white--text':'black--text'"
                        >
                          {{ attr.name }}
                          <v-btn
                            rounded
                            class="ml-5"
                            @click="deleteAttr(currPlanId, attr.city, attr.name, i, j)"
                          >
                            <v-icon>clear</v-icon>
                          </v-btn>
                        </v-card-title>
                        <v-card-subtitle
                          :class="attr.photo?'white--text':'black--text'"
                        >{{ attr.address }}</v-card-subtitle>
                        <v-row align="center" class="mx-0">
                          <v-rating
                            class="ml-4"
                            :value="attr.rating"
                            color="amber"
                            dense
                            half-increments
                            readonly
                            size="14"
                            v-if="!!attr.rating"
                          ></v-rating>
                          <div
                            :class="attr.photo?'white--text ml-4':'black--text ml-4'"
                            v-if="!!attr.rating"
                          >{{attr.rating}}</div>
                          <div
                            :class="attr.photo?'white--text ml-4':'black--text ml-4'"
                          >{{ attr.tag }}</div>
                        </v-row>
                      </v-img>
                      <v-card-text>
                        <div
                          style="display: -webkit-box;-webkit-line-clamp: 5; -webkit-box-orient: vertical;overflow: hidden;"
                        >{{ attr.description }}</div>
                      </v-card-text>
                    </v-card>
                  </v-timeline-item>
                  <v-timeline-item
                    class="align-center"
                    color="white"
                    fill-dot
                    v-if="attr.timetonext!=0"
                  >
                    <template v-slot:icon>
                      <v-icon color="black">mdi-car</v-icon>
                    </template>
                    <span>{{ attr.timetonext }} mins</span>
                  </v-timeline-item>
                </div>
              </draggable>
            </div>
          </v-timeline>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
import draggable from "vuedraggable";
import { mapState, mapActions } from "vuex";

Date.prototype.addDays = function(day) {
  var date = new Date(this.valueOf());
  date.setDate(date.getDate() + day);
  return date;
};

export default {
  name: "PlanDetail",
  components: {
    draggable
  },
  data: () => ({
    loading: true,
    input: null,
    nonce: 0
  }),

  computed: {
    ...mapState(["itinerary", "currPlanId", "currStart"]),
    numDays() {
      return this.itinerary.length;
    },
    startDate() {
      return new Date(this.currStart);
    }
  },

  methods: {
    ...mapActions(["fetchPlanDetail", "removeFromItinerary"]),
    log: function(evt) {
      window.console.log(evt);
    },
    async deleteAttr(currPlanId, city, name, i, j) {
      const payload = { planId: currPlanId, city: city, name: name };
      //console.log(payload);
      await this.removeFromItinerary(payload);
      if (this.itinerary[i].length > 1) {
        this.itinerary[i].splice(j, 1);
      } else this.itinerary.splice(i, 1);
    },
    toDate(n) {
      return this.startDate.addDays(n + 1);
    },
    scrollToDate(n) {
      this.$vuetify.goTo("#date-" + n);
    },
    comment() {
      const time = new Date().toTimeString();
      this.events.push({
        id: this.nonce++,
        text: this.input,
        time: time.replace(/:\d{2}\sGMT-\d{4}\s\((.*)\)/, (match, contents) => {
          return ` ${contents
            .split(" ")
            .map(v => v.charAt(0))
            .join("")}`;
        })
      });

      this.input = null;
    }
  },

  async created() {
    this.loading = true;
    await this.fetchPlanDetail({ planId: this.currPlanId }).then(
      (this.loading = false)
    );
  }
};
</script>