<template>
  <div class="app">
    <nav-header></nav-header>
    <router-view />
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue';
import { UNICORN_STORE } from "./store/constants";

import NavHeader from "./components/navHeader.vue";
import { Bar } from 'vue-chartjs'

export default defineComponent({
  name: 'App',
  components: {
    NavHeader
  },
  data() {
    return {
      isOpen: false
    }
  },
  beforeCreate() {
    this.$store.dispatch(UNICORN_STORE.ACTIONS.INITIALIZE_STORE);
  },
  mounted () {
    this.renderChart(data, options)
  }
});
</script>

<style lang="scss" scoped>
</style>