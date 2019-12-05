<template>
  <v-content>
    <v-container>
      <v-row>
        <v-col cols="1">
          <div>
            <div class="d-flex flex-column" style="height: 90vh;overflow-y: auto;position: fixed;">
              <div
                class="text-center"
              >{{ toDate(0).toLocaleString('default', { month: 'short' }).toUpperCase()}}</div>
              <div v-for="n in numDays" :key="n">
                <div
                  class="text-center"
                  v-if="toDate(n).getMonth() != toDate(n-1).getMonth()"
                >{{ toDate(n).toLocaleString('default', { month: 'short' }).toUpperCase() }}</div>
                <v-btn
                  class="black--text ma-0"
                  @click="scrollToDate(n)"
                  icon
                  text
                >{{ toDate(n).getDate() }}</v-btn>
              </div>
            </div>
          </div>
        </v-col>
        <v-col cols="8">
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
                    <v-card class="elevation-3">
                      <v-card-title class="headline">{{attr.name}}</v-card-title>
                      <v-card-text>Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an salutandi sententiae.</v-card-text>
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
    startDate: new Date(2019, 11, 26),
    input: null,
    nonce: 0
  }),

  computed: {
    ...mapState(["itinerary"]),
    numDays() {
      return this.itinerary.length;
    }
  },

  methods: {
    ...mapActions(["fetchPlanDetail"]),
    log: function(evt) {
      window.console.log(evt);
    },
    toDate(n) {
      return this.startDate.addDays(n);
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
    await this.fetchPlanDetail({ planId: "13458" });
  }
};
</script>