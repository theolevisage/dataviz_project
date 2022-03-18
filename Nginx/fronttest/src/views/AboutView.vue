<template>
<div>
  <v-tabs fixed-tabs  dark>
    <v-tab>Chart I</v-tab>
    <v-tab>Chart II</v-tab>
    <v-tab>Chart III</v-tab>
    <v-tab>Chart IV</v-tab>
    <v-tab>Chart V</v-tab>
  </v-tabs>
<br><br>

<v-row justify="center">
  <div class="about">

   <ApexChart
     width="500" type="bar" 
     :options="options" :series="series">
   </ApexChart>  

  </div>
</v-row>
</div>
</template>

<script>

export default {
  name: 'HelloWorld',
  data: () => ({
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
  })
}
</script>