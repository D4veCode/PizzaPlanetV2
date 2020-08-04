<template>
  <v-app
    style="background: none;"
    justify="center"
  >
    <Navigation></Navigation>
    <Navbar></Navbar>
    <v-main>

      <v-row justify="center">
        <v-col cols="12" md="8">
          <router-view></router-view>
          
        </v-col>
      </v-row>
  </v-main>
  <Footer></Footer>
  </v-app>
</template>

<script>
import Footer from './components/Footer.vue';
import Navbar from './components/Navbar.vue';
import Navigation from './components/Navigation.vue';

export default {
  name: 'App',

  components: {
    Footer,
    Navbar,
    Navigation,
  },

  data: () => ({
    //
  }),
};
</script>
