<template>
    <v-app-bar       
      color="grey lighten-4"
      shrink-on-scroll
      src="https://picsum.photos/1920/1080?random"
      scroll-target="#scrolling-techniques-1"
      dense
      >

      <v-toolbar-title>Where2go</v-toolbar-title>

      <v-spacer></v-spacer>


      <v-toolbar-items>

      <div class="text-center">
      <v-menu
      v-model="menu"
      :close-on-content-click="false"
      :nudge-width="200"
      offset-x
      >
      <template v-slot:activator="{ on }">
        <v-btn
          color="indigo"
          dark
          v-on="on"
        >
          Menu as Popover
        </v-btn>
      </template>

      <v-card>
        <v-list>
          <v-list-item>
            <v-list-item-avatar>
              <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John">
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title>John Leider</v-list-item-title>
              <v-list-item-subtitle>Founder of Vuetify.js</v-list-item-subtitle>
            </v-list-item-content>

          </v-list-item>
        </v-list>

        <v-divider></v-divider>
      </v-card>
      </v-menu>
    </div>
    </v-toolbar-items>

    </v-app-bar>


</template>



<script>
export default {

}
</script>

<style>

</style>

export default{
  
  items: [
      { text: 'Real-Time', icon: 'mdi-clock' },
      { text: 'Audience', icon: 'mdi-account' },
      { text: 'Conversions', icon: 'mdi-flag' },
  ],

}
    