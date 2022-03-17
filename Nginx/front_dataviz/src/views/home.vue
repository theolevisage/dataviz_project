<template>
    <div class="flex justify-center h-full">
      <div class="inline-flex justify-center flex-wrap h-screen m-4">
        <unicorn-card
                class="m-2"
                v-for="(item, index) in unicorns"
                :key="index"
                :nom="item.nom"
                :description="item.description"
                :image="item.image"
                :rank="item.rank"
                :price="item.price"
                :unicorn-type="item.type"
        />
      </div>
    </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue';
import UnicornCard from "../components/unicornCard.vue";
import { UNICORN_STORE } from "../store/constants"
import {Unicorn} from "../entities/unicorn";

export default defineComponent({
  name: 'Home',
  components: {UnicornCard},
  computed: {
    unicorns() : Array<Unicorn>{
      return this.$store.getters[UNICORN_STORE.GETTERS.GET_UNICORNS];
    }
  },
})
</script>

