<template>

  <div class="container">

    <main>
      <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
        <h1 class="h1">Dashboard</h1>
      </div>
      <div class="row">
        <div class="col-6">
          <GenresByUserScoreAVG />
        </div>
        <div class="col-6">
          <PlatformsByUserScoreAVG />
        </div>
      </div>

      <div class="row">
        <div class="col-12">
          <GameReleasePercentByPlatformInTheYears />
        </div>
      </div>
    </main>

  </div>
</template>

<script>
import GameReleasePercentByPlatformInTheYears from './components/GameReleasePercentByPlatformInTheYears.vue'
import GenresByUserScoreAVG from './components/GenresByUserScoreAVG.vue'
import PlatformsByUserScoreAVG from './components/PlatformsByUserScoreAVG.vue'

export default {
  name: 'App',
  components: {
    GameReleasePercentByPlatformInTheYears,
    GenresByUserScoreAVG,
    PlatformsByUserScoreAVG
  }
}
</script>

<style>
#app {
  font-family: Arial, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin-top: 60px;
}
</style>
