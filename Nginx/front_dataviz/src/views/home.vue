<template>
    <div class="flex justify-center h-full">
      <div class="inline-flex justify-center flex-wrap h-screen m-4">
        <random-chart></random-chart>
      </div>
    </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue';
import RandomChart from "../components/RandomChart.vue";

export default defineComponent({
  name: 'Home',
  components: {RandomChart}
})
</script>

