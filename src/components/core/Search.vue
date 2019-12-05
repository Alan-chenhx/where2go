<template>
  <v-autocomplete
    v-model="select"
    :loading="loading"
    :items="items"
    :search-input.sync="search"
    cache-items
    flat
    hide-no-data
    hide-details
    label="Enter destination city"
    solo-inverted
  ></v-autocomplete>
</template>

<script>
export default {
  props: ["select_data"],
  data() {
    return {
      select: null,
      loading: false,
      items: [],
      search: null,
      data: [
        "Los Angeles",
        "San Francisco",
        "San Diego",
        "Sacramento",
        "San Jose",
        "Irvine",
        "Oakland",
        "Long Beach",
        "Anaheim",
        "Berkeley",
        "Santa Monica",
        "Palo Alto",
        "Pasadena",
        "Fresno",
        "Santa Ana",
        "Oceanside",
        "Bakersfield",
        "Fremont",
        "Carlsbad",
        "Santa Barbara",
        "Stockton",
        "Newport Beach",
        "Riverside",
        "Oxnard",
        "San Bernardino",
        "Santa Rosa",
        "Chula Vista",
        "Sunnyvale",
        "Torrance",
        "Mountain View",
        "Huntington Beach",
        "Santa Cruz",
        "Thousand Oaks",
        "Burbank",
        "Beverly Hills",
        "Modesto",
        "Santa Clarita",
        "Garden Grove",
        "Fontana",
        "Encinitas",
        "Manhattan Beach",
        "Temecula",
        "Moreno Valley",
        "San Mateo",
        "Costa Mesa",
        "Rancho Cucamonga"
      ]
    };
  },
  watch: {
    select: function(val) {
      this.$emit("update:select_data", val);
    },
    search(val) {
      val && val !== this.select && this.querySelections(val);
    }
  },
  methods: {
    querySelections(v) {
      this.loading = true;
      // Simulated ajax query
      setTimeout(() => {
        this.items = this.data.filter(e => {
          return (e || "").toLowerCase().indexOf((v || "").toLowerCase()) > -1;
        });
        this.loading = false;
      }, 500);
    }
  }
};
</script>