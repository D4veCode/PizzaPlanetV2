<template>
  <v-app
    id="inspire"
  >
    <v-navigation-drawer
      v-model="drawer"
      color="Blue"
      dark
      app
    >
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>
              <router-link to="/" class="rlink">Home</router-link>
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-pizza</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>
              <router-link to="/pedido" class="rlink">Pedido</router-link>
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="red darken-2"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title> <img src="@/assets/Pizza_planet-removebg-preview.png"
      height="180" width="170"/></v-toolbar-title>
      <!---<v-toolbar-title>Pizza Planet</v-toolbar-title>-->
    </v-app-bar>

    <v-main>
      <v-container
        class="fill-height Blue darken-1"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col class="text-center">
            <v-tooltip left>
                <v-btn
                  icon
                  large
                  target="_blank"
                >
                  <v-icon large>mdi-code-tags</v-icon>
                </v-btn>
            </v-tooltip>
            <router-view></router-view>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  <Footer></Footer>
  </v-app>
</template>

<script>
import Footer from './components/Footer.vue';

export default {
  name: 'App',

  components: {
    Footer,
  },

  data: () => ({
    drawer: null,
  }),
};
</script>

<style scoped>
  .rlink {
    text-decoration: none;
    color: #ffffff;
  }
</style>
