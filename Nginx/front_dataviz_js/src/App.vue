<template>
  <v-app>
    <v-app-bar
        color="teal lighten-2"
        dark
        max-height="65px"
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Dataviz'</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-tabs
          v-model="activeTab"
          background-color="teal lighten-2"
          color="white"
          fixed-tabs
      >
        <v-tabs-slider color="indigo darken-4"></v-tabs-slider>

        <v-tab
            v-for="(tabContent, index) in tabs"
            :key="index + 'y'"
            :to="tabContent.route"
        >
          {{ tabContent.name }}
        </v-tab>
      </v-tabs>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data () {
    return {
      activeTab: null,
      tabs: [
        { id: 1, name: "Chart I", route: `ChartI` },
        { id: 2, name: "Chart II", route: `ChartII` },
        { id: 3, name: "Chart III", route: `ChartIII` },
        { id: 4, name: "Chart IV", route: `ChartIV` },
        { id: 5, name: "Chart V", route: `ChartV` }
      ]
    }
  }
};
</script>
