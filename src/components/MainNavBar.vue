<template>
  <div>
    <v-app-bar app color="accent" dark>
      <v-toolbar-title>Where2Go</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-menu bottom offset-y>
        <template v-slot:activator="{ on }">
          <v-btn v-on="on">
            <v-icon>person</v-icon>
            User
          </v-btn>
        </template>

        <v-list>
          <v-list-item v-if="false" @click="() => {}">
            <v-list-item-title>Log In</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
  </div>
</template>



<script>
export default {
  data: () => ({
    items: [
      { title: "Click Me" },
      { title: "Click Me" },
      { title: "Click Me" },
      { title: "Click Me 2" }
    ]
  })
};
</script>

<style>
</style>
    