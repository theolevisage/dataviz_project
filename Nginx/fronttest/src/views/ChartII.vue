<template>
  <div>

    <v-tabs v-model="activeTab" grow dark>
      <v-tab v-for="tab of tabs" :key="tab.id" :to="tab.route" exact>
        {{ tab.name }}
      </v-tab>

      <v-tab-item v-for="tab of tabs" :key="tab.id" :value="tab.route">
        <router-view></router-view>
      </v-tab-item>
    </v-tabs>

<br><br>

<v-row justify="center">
  <div class="about">

   <ApexChart
     width="500" type="line" 
     :options="options" :series="series">
   </ApexChart>  

  </div>
</v-row>
</div>

</template>

<script>



export default {
  props: ["id"],
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
