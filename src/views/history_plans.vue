<template>
  <v-app>
    <v-content>
      <v-container >
        <v-data-iterator
          :items="items"
          :items-per-page.sync="itemsPerPage"
          :page="page"
          hide-default-footer
        >
          <template v-slot:default="props">
            <v-row>
              <v-col v-for="item in props.items" :key="item.name" cols="12" sm="6" md="4" lg="3">
                <v-hover
                    v-slot:default="{ hover }"
                    >
                  <v-card
                    :elevation="hover ? 12 : 2"
                    >
                    <v-img
                      :src = "item.background" 
                      height="200px"
                      class="white--text levation-0 text-center align-center"
                    >
                      <v-card-title class="font-weight-black justify-center display-1">
                        {{ item.trip_name }}
                      </v-card-title>
                      <v-card-subtitle class="white--text align-center justify-center subtitle-1">
                        {{ item.begin_time }} -{{ item.end_time }}
                      </v-card-subtitle>
                    </v-img>
                    <v-card-text class="text--primary" >
                      <div>{{ item.preference }}, {{ item.pace }}</div>
                    </v-card-text>
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
                  <v-btn
                    dark
                    text
                    color="primary"
                    class="ml-2"
                    v-on="on"
                  >
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

              <span
                class="mr-4
                grey--text"
              >
                Page {{ page }} of {{ numberOfPages }}
              </span>
              <v-btn
                fab
                dark
                color="blue darken-3"
                class="mr-1"
                @click="formerPage"
              >
                <v-icon>mdi-chevron-left</v-icon>
              </v-btn>
              <v-btn
                fab
                dark
                color="blue darken-3"
                class="ml-1"
                @click="nextPage"
              >
                <v-icon>mdi-chevron-right</v-icon>
              </v-btn>
            </v-row>
          </template>
        </v-data-iterator>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  export default {
    data: () => ({
      itemsPerPageArray: [4, 8, 12],
      itemsPerPage: 4,
      page: 1,
      items: [
        {
          trip_id:12,
          background:'https://s.inspirockcdn.com/ds10/photos/United States/1/bradbury-building--1985987038.jpg',
          trip_name: 'fuck front-end',
          destination: 'los angeles',
          begin_time: 'Dec. 5th',
          end_time:'Dec. 9th',
          time: '5 days',
          preference:'Popular sights',
          pace:"Medium"

        },
        {
          trip_id:12,
          background:'https://s.inspirockcdn.com/ds10/photos/United States/1/bradbury-building--1985987038.jpg',
          trip_name: 'fuck front-end',
          destination: 'los angeles',
          begin_time: 'Dec. 5th',
          end_time:'Dec. 9th',
          time: '5 days',
          preference:'Popular sights',
          pace:"Medium"

        },
        {
          trip_id:12,
          background:'https://s.inspirockcdn.com/ds10/photos/United States/1/bradbury-building--1985987038.jpg',
          trip_name: 'fuck front-end',
          destination: 'los angeles',
          begin_time: 'Dec. 5th',
          end_time:'Dec. 9th',
          time: '5 days',
          preference:'Popular sights',
          pace:"Medium"

        },
        {
          trip_id:12,
          background:'https://s.inspirockcdn.com/ds10/photos/United States/1/bradbury-building--1985987038.jpg',
          trip_name: 'fuck front-end',
          destination: 'los angeles',
          begin_time: 'Dec. 5th',
          end_time:'Dec. 9th',
          time: '5 days',
          preference:'Popular sights',
          pace:"Medium"

        },
        {
          trip_id:12,
          background:'https://s.inspirockcdn.com/ds10/photos/United States/1/bradbury-building--1985987038.jpg',
          trip_name: 'fuck front-end',
          destination: 'los angeles',
          begin_time: 'Dec. 5th',
          end_time:'Dec. 9th',
          time: '5 days',
          preference:'Popular sights',
          pace:"Medium"

        },
        {
          trip_id:12,
          background:'https://s.inspirockcdn.com/ds10/photos/United States/1/bradbury-building--1985987038.jpg',
          trip_name: 'fuck front-end',
          destination: 'los angeles',
          begin_time: 'Dec. 5th',
          end_time:'Dec. 9th',
          time: '5 days',
          preference:'Popular sights',
          pace:"Medium"

        },
        {
          trip_id:12,
          background:'https://s.inspirockcdn.com/ds10/photos/United States/1/bradbury-building--1985987038.jpg',
          trip_name: 'fuck front-end',
          destination: 'los angeles',
          begin_time: 'Dec. 5th',
          end_time:'Dec. 9th',
          time: '5 days',
          preference:'Popular sights',
          pace:"Medium"

        },
      ],
    }),
    computed: {
      numberOfPages () {
        return Math.ceil(this.items.length / this.itemsPerPage)
      },
      filteredKeys () {
        return this.keys.filter(key => key !== `Name`)
      },
    },
    methods: {
      nextPage () {
        if (this.page + 1 <= this.numberOfPages) this.page += 1
      },
      formerPage () {
        if (this.page - 1 >= 1) this.page -= 1
      },
      updateItemsPerPage (number) {
        this.itemsPerPage = number
      },
    },
  }
</script>