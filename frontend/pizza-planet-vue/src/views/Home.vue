<template>
<v-container>
  <v-row>
      <v-col>
        <v-btn small m8 color="grey" @click="sortBy('user')">
          <span class="caption text-lowercase">By User name</span>
        </v-btn>
      </v-col>
      <v-col>
        <v-btn small m8 color="grey" @click="sortBy('price')">
          <span class="caption text-lowercase">By price</span>
        </v-btn>
      </v-col>
      <v-col>
        <v-btn small m8 color="grey" @click="sortBy('size')">
          <span class="caption text-lowercase">By Pizza size</span>
        </v-btn>
      </v-col>
      <v-col>
        <v-btn small m8 color="grey" @click="sortBy('date')">
          <span class="caption text-lowercase">By Date</span>
        </v-btn>
      </v-col>
      <v-col>
        <v-btn small m8 color="grey" @click="sortBy('ingredientes')">
          <span class="caption text-lowercase">By ingredientes</span>
        </v-btn>
      </v-col>
  </v-row>
  <v-row v-for="pedido in listaPedidos" v-bind:key="pedido.id" wrap>
    <v-col md6>
      <PedidoCard
        v-bind:user="pedido.user"
        v-bind:date="pedido.date"
        v-bind:pizza="pedido.pizza"
        v-bind:price="pedido.price"
        v-bind:size="pedido.size"
        v-bind:ingredientes="pedido.ingredientes"
      >
      </PedidoCard>
    </v-col>
  </v-row>
</v-container>
</template>

<script>
import axios from 'axios';
import PedidoCard from '../components/PedidoCard.vue';

export default {
  name: 'Home',
  components: {
    PedidoCard,
  },
  data: () => ({
    listaPedidos: [],
  }),
  methods: {
    sortBy(prop) {
      this.listaPedidos.sort((prev, current) => (prev[prop] < current[prop] ? 1 : -1));
    },
  },
  mounted() {
    const vue = this;
    axios.get('http://127.0.0.1:8000/pedidos/').then((response) => {
      vue.listaPedidos = response.data;
      console.log(response.data);
    }).catch((error) => console.log(error));
  },
};
</script>
