<template>
  <div class="card mb-4">
    <div class="card-header">
      Platforms By User AVG
    </div>
    <div class="card-body">
      <div class="row g-3">
        <div class="col-auto">
          <div class="form-floating">
            <select id="start-year" class="form-select" v-model="top" aria-label="Top">
              <option v-for="(option, index) in options" :key="index" v-bind:value="option.value">
                {{ option.text }}
              </option>
            </select>
            <label for="start-year">Top</label>
          </div>
        </div>
        <div class="col-auto">
          <input type="button" class="btn btn-lg btn-primary"  style="padding-bottom: .8rem; padding-top: .8rem;" v-on:click="filter()" value="Filter">
        </div>
      </div>
    </div>
    <div class="card-body">
      <div id="platforms-by-user-score-avg"></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Plotly from "plotly.js-dist";

export default {
  name: 'Chart',
  data () {
    return {
      chart: null,
      options: null,
      top: null,
    }
  },
  mounted () {
    // - pre-load charts
    this.loadChart();
  },
  methods: {
    filter: function (value) {
      // - filter charts
      this.loadChart([value]);
    },
    loadChart: function () {
      let params = {
        'top': this.top
      };

      const url = `${process.env.VUE_APP_CHART_API_URL}/platforms-by-user-score-avg`;

      axios
          .get(url, { params: params })
          .then(response => {
            Plotly.purge('platforms-by-user-score-avg');

            this.chart = response.data.chart;
            this.top = response.data.properties.top;
            this.options = Array.from({length: 20}, (x, i) => i + 1).map(x => ({text: x, value: x}));

            Plotly.newPlot('platforms-by-user-score-avg', this.chart.data, this.chart.layout);
          });

    }
  }
}
</script>
