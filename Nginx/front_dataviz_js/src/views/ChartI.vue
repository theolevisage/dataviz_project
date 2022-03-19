<template>
  <v-row justify="center">
    <div class="about mt-14">
      <ApexChart
          width="1000"
          type="bar"
          :options="options" :series="series">
      </ApexChart>

    </div>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      options: {
        chart: {
          id: 'vuechart-example'
        },
        xaxis: {
          categories: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec"
          ]
        }
      },
      series: [{
        name: 'series-1',
        data: [55, 62, 89, 66, 98, 72, 101, 75, 94, 120, 117, 139]
      }]
    };
  }
};
</script>
