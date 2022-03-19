<template>
  <v-row justify="center">
    <div class="about mt-14">
      <ApexChart
          width="1000"
          type="heatmap"
          :options="options" :series="series">
      </ApexChart>
    </div>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      activeTab: `/user/${this.id}`,
      tabs: [
        { id: 1, name: "Chart I", route: `ChartI` },
        { id: 2, name: "Chart II", route: `ChartII` },
        { id: 3, name: "Chart III", route: `ChartIII` },
        { id: 4, name: "Chart IV", route: `ChartIV` },
        { id: 5, name: "Chart V", route: `ChartV` }
      ],
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
