<template>
  <div class="card mb-4">
    <div class="card-header">
      Game Releases Percent By Platform in The Years
    </div>
    <div class="card-body">
      <div class="row g-3">
        <div class="col-auto">
          <div class="form-floating">
            <select id="start-year" class="form-select" v-model="start_year" aria-label="Start">
              <option v-for="(option, index) in years" :key="index" v-bind:value="option.value">
                {{ option.text }}
              </option>
            </select>
            <label for="start-year">Start</label>
          </div>
        </div>
        <div class="col-auto">
          <div class="form-floating">
            <select id="end-year" class="form-select" v-model="end_year" aria-label="End">
              <option v-for="(option, index) in years" :key="index" v-bind:value="option.value">
                {{ option.text }}
              </option>
            </select>
            <label for="end-year">End</label>
          </div>
        </div>
        <div class="col-auto">
          <div class="dropdown">
            <button class="btn btn-lg btn-light dropdown-toggle" style="padding-bottom: .8rem; padding-top: .8rem;" type="button" id="genres" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="true">
              Genres
            </button>
            <ul class="dropdown-menu p-0" aria-labelledby="genres">
              <li v-for="(option, index) in genres" :key="index" class="pt-1 ps-3 pe-3 pb-1 border-bottom">
                <div class="form-check">
                  <input class="form-check-input" :id="'genres-' + index" type="checkbox" v-model="selectedGenres" :value="option.value">
                  <label class="form-check-label" :for="'genres-' + index">
                    {{ option.text }}
                  </label>
                </div>
              </li>
            </ul>
          </div>
        </div>
        <div class="col-auto">
          <input type="button" class="btn btn-lg btn-primary"  style="padding-bottom: .8rem; padding-top: .8rem;" v-on:click="filter()" value="Filter">
        </div>
      </div>
    </div>
    <div class="card-body">
      <div id="game-release-percent-by-platform-in-the-years"></div>
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
      start_year: null,
      end_year: null,
      years: null,
      genres: null,
      selectedGenres: []
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
        'start_year': this.start_year,
        'end_year': this.end_year
      };

      if (this.selectedGenres) {
        params['genres'] = this.selectedGenres.join(',');
      }

      const url = `${process.env.VUE_APP_CHART_API_URL}/game-release-percent-by-platform-in-the-years`;

      axios
          .get(url, { params: params })
          .then(response => {
            Plotly.purge('game-release-percent-by-platform-in-the-years');

            this.chart = response.data.chart;
            this.start_year = response.data.properties.start_year;
            this.end_year = response.data.properties.end_year;

            this.years = response.data.properties.years.map(x => ({text: x, value: x}))
            this.genres = response.data.properties.genres.map(x => ({text: x, value: x}))
            this.selectedGenres = response.data.properties.selected_genres;

            Plotly.newPlot('game-release-percent-by-platform-in-the-years', this.chart.data, this.chart.layout);
          });

    }
  }
}
</script>
