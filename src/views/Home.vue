<template>
  <v-content>
    <v-container>
      <v-row>
        <v-col cols="1">
          <div>
            <div class="d-flex flex-column" style="height: 90vh;overflow-y: auto;position: fixed;">
              <v-btn v-for="n in 100" class="black--text ma-0" :key="n" @click="$vuetify.goTo('#date' + n)" icon text>{{ n }}</v-btn>
            </div>
          </div>
        </v-col>
        <v-col cols="20">
          <v-timeline dense clipped>
            <div v-for="(city, index) in attrs" :key="index">
              <div v-for="(days, index) in city" :key="index">
                <v-timeline-item fill-dot small :id="'date'+index">
                  <template v-slot:icon>
                    <v-btn class="headline white--text" color="black">{{index}}</v-btn>
                  </template>
                </v-timeline-item>
                <div v-for="(attr, index) in days" :key="index">
                  <v-timeline-item>
                    <v-card class="elevation-3">
                      <v-card-title class="headline">{{attr.name}}</v-card-title>
                      <v-card-text>Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an salutandi sententiae.</v-card-text>
                    </v-card>
                  </v-timeline-item>
                  <v-timeline-item color="white" fill-dot v-if="attr.timetonext!=0">
                    <template v-slot:icon>
                      <v-icon color="black">mdi-car</v-icon>
                    </template>
                    <span>{{ attr.timetonext }} mins</span>
                  </v-timeline-item>
                </div>
              </div>
            </div>
          </v-timeline>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
export default {
  data: () => ({
    attrs: {
      "Los Angeles": [
        [
          {
            duration: "120",
            name: "Santa Monica Museum of Art",
            rating: 2.8,
            timetonext: 3.0
          },
          {
            duration: "120",
            name: "Fantastic Race",
            rating: 4.8,
            timetonext: 5.0
          },
          { duration: "120", name: "Chinatown", rating: 1.4, timetonext: 0 }
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
        ]
      ],
      "San Diego": [
        [
          {
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
      ]
    },
    events: [],
    input: null,
    nonce: 0
  }),

  computed: {
    timeline() {
      return this.events.slice().reverse();
    }
  },

  methods: {
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