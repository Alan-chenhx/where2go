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
            <div v-for="(days, i) in attrs" :key="i">
              <v-timeline-item fill-dot small :id="'date-'+i">
                <template v-slot:icon>
                  <v-sheet
                    class="title text-no-wrap pa-2 white--text"
                    color="black"
                  >{{toDate(i).toLocaleString('default', { weekday: 'short', day: 'numeric', month: 'short'})}}</v-sheet>
                </template>
              </v-timeline-item>
              <div v-for="(attr, j) in days" :key="j">
                <v-timeline-item
                  large
                  class="align-center"
                  v-if="!!attr.city?(j>0&&!!days[j-1].city)?attr.city!=days[j-1].city:true:false"
                >
                  <span class="headline text-center text-no-wrap">{{attr.city}}</span>
                </v-timeline-item>
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
            </div>
          </v-timeline>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
Date.prototype.addDays = function(days) {
  var date = new Date(this.valueOf());
  date.setDate(date.getDate() + days);
  return date;
};

export default {
  data: () => ({
    startDate: new Date(2019, 11, 26),
    attrs: [
      [
        {
          city: "Los Angeles",
          duration: "120",
          name: "Santa Monica Museum of Art",
          rating: 2.8,
          timetonext: 3.0
        },
        {
          city: "Los Angeles",
          duration: "120",
          name: "Fantastic Race",
          rating: 4.8,
          timetonext: 5.0
        },
        {
          city: "Los Angel",
          duration: "120",
          name: "Chinatown",
          rating: 1.4,
          timetonext: 0
        }
      ],
      [
        {
          duration: "60",
          name: "Griffith Observatory",
          rating: 4.6,
          timetonext: 0.0
        },
        {
          duration: "30",
          name: "Rebel Without a Cause Monument",
          rating: 1.0,
          timetonext: 6.0
        },
        {
          duration: "150",
          name: "Los Angeles Zoo & Botanical Gardens",
          rating: 2.7,
          timetonext: 11.0
        },
        {
          duration: "90",
          name: "Guinness World Records Museum",
          rating: 1.9,
          timetonext: 0
        }
      ],
      [
        {
          duration: "240",
          name: "Museum of Tolerance",
          rating: 4.2,
          timetonext: 6.0
        },
        {
          duration: "30",
          name: "Diorama-museum of Bhagavad-gita",
          rating: 4.9,
          timetonext: 3.0
        },
        {
          duration: "90",
          name: "The Wende Museum of the Cold War",
          rating: 4.8,
          timetonext: 0
        }
      ],
      [
        {
          duration: "60",
          name: "Santa Monica Pier",
          rating: 4.1,
          timetonext: 61.0
        },
        {
          duration: "120",
          name: "The Huntington Desert Garden",
          rating: 5.0,
          timetonext: 63.0
        },
        {
          duration: "300",
          name: "Universal Studios Hollywood",
          rating: 4.4,
          timetonext: 0
        }
      ],
      [
        {
          duration: "240",
          name: "Studio Tour",
          rating: 4.7,
          timetonext: 100.0
        },
        {
          duration: "330",
          name: "Disneyland Park",
          rating: 4.2,
          timetonext: 0
        }
      ],
      [
        {
          duration: "300",
          name: "Luigi's Rollickin' Roadsters",
          rating: 4.2,
          timetonext: 0
        }
      ],
      [
        {
          city: "San Diego",
          duration: "360",
          name: "LEGOLAND California",
          rating: 2.7,
          timetonext: 0
        }
      ],
      [
        {
          duration: "300",
          name: "SeaWorld San Diego",
          rating: 4.1,
          timetonext: 0
        }
      ],
      [
        {
          duration: "180",
          name: "USS Midway Museum",
          rating: 4.8,
          timetonext: 6.0
        },
        {
          duration: "90",
          name: "AxeVentures",
          rating: 4.9,
          timetonext: 77.0
        },
        {
          duration: "300",
          name: "San Diego Zoo",
          rating: 4.5,
          timetonext: 0
        }
      ]
    ],
    input: null,
    nonce: 0
  }),

  computed: {
    numDays() {
      return this.attrs.length
    }
  },

  methods: {
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
  }
};
</script>