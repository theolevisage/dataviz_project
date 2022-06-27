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
import axios from 'axios'


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
      }],
       data: []
    };
  },
  created() {
    this.getdata()
  },
  methods: {
    async getdata()
    {
      let response = await axios.get('http://localhost:8080/automats')
      this.series[0].data = response.data
      window.dispatchEvent(new Event('resize'));      
      //console.log(this.data)
    }
  }

};


</script>
