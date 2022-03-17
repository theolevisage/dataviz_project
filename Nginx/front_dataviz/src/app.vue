<template>
  <div class="app">
      <unicorn-header></unicorn-header>
      <router-view />
      <unicorn-footer></unicorn-footer>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue';
import image from './assets/img/title.png'
import { UNICORN_STORE } from "./store/constants";

import UnicornHeader from "./components/unicornHeader.vue";
import UnicornFooter from "./components/unicornFooter.vue";

export default defineComponent({
  name: 'App',
  components: {
    UnicornHeader, UnicornFooter
  },
  data() {
    return {
      isOpen: false,
      image: image
    }
  },
  beforeCreate() {
    this.$store.dispatch(UNICORN_STORE.ACTIONS.INITIALIZE_STORE);
  }
});
</script>

<style lang="scss" scoped>
</style>