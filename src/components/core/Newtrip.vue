<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600">
      <template v-slot:activator="{ on }">
        <v-btn color="primary" dark v-on="on">Create new plan</v-btn>
      </template>

      <v-card>
        <v-col style="width:70%;postion:center;margin-left: auto;margin-right: auto;">
          <v-card-title class="justify-center pt-12">Itinerary Planner</v-card-title>
          <div v-for="i in counter" :key="i" class="pt-5">
            <core-search />
          </div>
          <div>
            <v-btn text small @click="add" color="primary">+ Add destination</v-btn>
          </div>

          <v-row style="padding-left:6%;padding-top:5px">
            <v-menu v-model="menu1" :close-on-content-click="false" max-width="290">
              <template v-slot:activator="{ on }">
                <v-row>
                  <v-text-field
                    outlined
                    :value="date1"
                    label="Start Date"
                    readonly
                    v-on="on"
                    style="max-width:80%"
                    @click:clear="date = []"
                  ></v-text-field>
                </v-row>
              </template>
              <v-date-picker style="center" v-model="date1" @input="turn"></v-date-picker>
            </v-menu>

            <v-menu
              style="padding-left:10%;"
              v-model="menu2"
              :close-on-content-click="false"
              max-width="290"
            >
              <template v-slot:activator="{ on }">
                <v-row>
                  <v-text-field
                    outlined
                    :value="date2"
                    label="End Date"
                    readonly
                    v-on="on"
                    style="max-width:80%"
                    @click:clear="date = []"
                  ></v-text-field>
                </v-row>
              </template>
              <v-date-picker style="center" v-model="date2" :min="date1" @input="menu2 = false"></v-date-picker>
            </v-menu>
          </v-row>
          <p class="overline">ACTIVITY PREFERENCES (OPTIONAL)</p>
          <v-btn-toggle
            v-model="choise"
            borderless
            style="margin-left: 10%;margin-right: auto;"
            color="deep-purple accent-3"
          >
            <v-btn value="Slow-easy">Slow-easy</v-btn>

            <v-btn value="Medium">Medium</v-btn>

            <v-btn value="Fast-paced">Fast-paced</v-btn>
          </v-btn-toggle>
          <v-checkbox v-model="checkbox1" :label="`Checkbox 1: ${checkbox1.toString()}`"></v-checkbox>
          <v-checkbox v-model="checkbox2" :label="`Checkbox 2: ${checkbox2.toString()}`"></v-checkbox>
        </v-col>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="dialog = false">OK</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  data: vm => ({
    dialog: false,
    counter: 1,
    date1: new Date().toISOString().substr(0, 10),
    date2: new Date().toISOString().substr(0, 10),
    menu1: false,
    menu2: false,
    choise: "Medium",
    checkbox1: true,
    checkbox2: false
  }),

  methods: {
    add() {
      this.counter += 1;
    },
    turn() {
      this.menu1 = false;
      this.menu2 = true;
    }
  },
  computed: {
    dateRangeText() {
      return this.dates.join(" ~ ");
    }
  }
};
</script>
