<template>
<v-container>
  <v-row>
      <v-col>
        <v-btn small m8 flat color="grey" @click="sortBy('user')">
          <span class="caption text-lowercase">By User name</span>
        </v-btn>
      </v-col>
      <v-col>
        <v-btn small m8 flat color="grey" @click="sortBy('size')">
          <span class="caption text-lowercase">By Pizza size</span>
        </v-btn>
      </v-col>
      <v-col>
        <v-btn small m8 flat color="grey" @click="sortBy('date')">
          <span class="caption text-lowercase">By Date</span>
        </v-btn>
      </v-col>
      <v-col>
        <v-btn small m8 flat color="grey" @click="sortBy('ingredientes')">
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
import PedidoCard from '../components/PedidoCard.vue';

export default {
  name: 'Home',
  components: {
    PedidoCard,
  },
  data: () => ({
    listaPedidos: [
      {
        id: '1',
        user: 'Pepito',
        date: '04/08/2020',
        price: 20,
        pizza: 'Margarita',
        size: 'mediana',
        ingredientes: 'Queso, Salsa de Tomate',
      },
      {
        id: '2',
        user: 'Jaimito',
        date: '04/07/2020',
        price: 25,
        pizza: 'Margarita',
        size: 'pequena',
        ingredientes: 'Queso, Salsa de Tomate, Tocineta',
      },
      {
        id: '3',
        user: 'Pedro',
        date: '04/08/2020',
        price: 30,
        pizza: 'Margarita',
        size: 'mediana',
        ingredientes: 'Queso, Salsa de Tomate, Tocineta, Maiz, Aceituna',
      },
      {
        id: '4',
        user: 'Thomas',
        date: '04/07/2020',
        price: 28,
        pizza: 'Margarita',
        size: 'grande',
        ingredientes: 'Queso, Salsa de Tomate, Maiz, Aceituna',
      },
    ],
  }),
  methods: {
    sortBy(prop) {
      this.listaPedidos.sort((prev, current) => (prev[prop] < current[prop] ? 1 : -1));
    },
  },
};
</script>
