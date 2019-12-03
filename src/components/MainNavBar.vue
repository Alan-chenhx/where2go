<template>
  <div>
    <v-app-bar app 
    color = "white"
    dark>

      <v-toolbar-side-icon>
        <v-img :src="require('../assets/logob.png')" />
      </v-toolbar-side-icon>  


      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-menu bottom open-on-hover offset-y>
        <template v-slot:activator="{ on }">
          <v-btn v-on="on">
            <v-icon>person</v-icon>
            User
          </v-btn>
        </template>

        <v-list class="dropdown-menu">
          <v-list-item v-if="false" @click="() => {}">
            <v-list-item-title>Log In</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="true" @click="() => {}">
            <v-list-item-title>Log Out</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
  </div>
</template>



<script>
export default {
  data: () => ({
    
  })
};
</script>

<style>
</style>
    