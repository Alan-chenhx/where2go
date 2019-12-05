<template>
  <material-card class="elevation-12" title="Itinerary Planner">
    <v-col style="width:80%; postion:center; margin-left: auto;margin-right: auto;">
      <div v-for="(city, i) in cities" :key="i" class="pt-5">
        <v-row align="center">
          <core-search :select_data.sync="cities[i]" />
          <v-btn icon @click="remove" color="primary">
            <v-icon>clear</v-icon>
          </v-btn>
        </v-row>
      </div>
      <div>
        <v-btn text small @click="add" color="primary">+ Add destination</v-btn>
      </div>

      <p class="overline pt-3">DATES</p>
      <v-layout justify-center>
        <v-row>
          <v-col>
            <v-menu v-model="menu1" :close-on-content-click="false">
              <template v-slot:activator="{ on }">
                <v-row>
                  <v-text-field
                    outlined
                    :value="start_date"
                    label="Start Date"
                    readonly
                    v-on="on"
                    @click:clear="date = []"
                  ></v-text-field>
                </v-row>
              </template>
              <v-date-picker style="center" v-model="start_date" @input="turn"></v-date-picker>
            </v-menu>
          </v-col>
          <v-col class="ml-3">
            <v-menu v-model="menu2" :close-on-content-click="false" max-width="290">
              <template v-slot:activator="{ on }">
                <v-row>
                  <v-text-field
                    outlined
                    :value="end_date"
                    label="End Date"
                    readonly
                    v-on="on"
                    @click:clear="date = []"
                  ></v-text-field>
                </v-row>
              </template>
              <v-date-picker
                style="center"
                v-model="end_date"
                :min="start_date"
                @input="menu2 = false"
              ></v-date-picker>
            </v-menu>
          </v-col>
        </v-row>
      </v-layout>

      <p class="overline mt-n3">ACTIVITY PACE</p>
      <v-layout justify-center>
        <v-btn-toggle v-model="choice" borderless color="deep-purple accent-3">
          <v-btn value="Slow-easy">Slow-easy</v-btn>

          <v-btn value="Medium">Medium</v-btn>

          <v-btn value="Fast-paced">Fast-paced</v-btn>
        </v-btn-toggle>
      </v-layout>

      <p class="overline pt-4">Preferences</p>

      <v-layout justify-center>
        <v-chip-group v-model="chips" multiple column active-class="primary--text">
          <v-chip outlined v-for="tag in tags" :key="tag">{{ tag }}</v-chip>
        </v-chip-group>
      </v-layout>
    </v-col>
    <v-row justify="center">
      <v-btn class="ma-1" dark @click="createNew">Create New Plan</v-btn>
    </v-row>
  </material-card>
</template>

<script>
import { mapActions, mapState } from "vuex";
export default {
  data: () => ({
    cities: [
      {
        city: ""
      }
    ],
    start_date: new Date().toISOString().substr(0, 10),
    end_date: new Date().toISOString().substr(0, 10),
    menu1: false,
    menu2: false,
    choice: "Medium",
    checkbox1: true,
    checkbox2: false,
    tags: [
      "culture",
      "outdoors",
      "relaxing",
      "romantic",
      "beaches",
      "historic sites",
      "museums",
      "shopping",
      "wildlife"
    ],
    chips: []
  }),

  methods: {
    ...mapActions(['createNewPlan']),
    createNew() {
      let pref = [];
      let self = this;
      this.chips.forEach(i => {
        pref.push(self.tags[i]);
      });
      let diffTime = (new Date(this.end_date))-(new Date(this.start_date));
      let diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)) + 1; 
      const name = "My Tour " + (!!this.plans.length?this.plans.length:0 + 1);
      const payload = {
        "name": name,
        "start": this.start_date,
        "end": this.end_date,
        "dest": this.cities,
        "days": diffDays,
        "pace": this.choice,
        "tags": this.pref
      };
      createNewPlan(payload)
    },
    add() {
      this.cities.push({
        city: ""
      });
    },
    remove() {
      if (this.cities.length > 1) {
        this.cities.pop();
      }
    },
    turn() {
      this.menu1 = false;
      this.menu2 = true;
    },
    querySelections(v) {
      // Simulated ajax query
      this.items = this.cities.filter(e => {
        return (e || "").toLowerCase().indexOf((v || "").toLowerCase()) > -1;
      });
    }
  },
  watch: {
    search(val) {
      val && val !== this.cities && this.querySelections(val);
    }
  },
  computed: {
    ...mapState(["plans"]),
    dateRangeText() {
      return this.dates.join(" ~ ");
    }
  }
};
</script>
