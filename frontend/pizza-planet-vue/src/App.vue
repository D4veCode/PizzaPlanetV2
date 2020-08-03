<template>
  <v-app
    style="background: none;"
    justify="center"
  >
    <v-main>

    <v-container
      class="first-section"
    >
      <v-row justify="center">
        <v-col cols="12" md="8">
          <router-view></router-view>
          <Footer></Footer>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
  </v-app>
</template>

<style scope>
.first-section {
  background-image: url('./assets/pizza2.png');
  background-repeat: no-repeat;
  background-position: center center;
  background-attachment: fixed;
  width: 100vw;
  height: 100vh;
  display: flex;
  max-width: 100%;
  position: fixed;
  background-size: cover;
  z-index: -99;
  flex-direction: column;
  justify-content: flex-start;
}
</style>
<script>
import Footer from './components/Footer.vue';

export default {
  name: 'App',

  components: {
    Footer,
  },

  data: () => ({
    //
  }),
};
</script>
