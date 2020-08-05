<template>
<v-container>
  <v-row>
    <v-col md6 v-for="pedido in listaPedidos" v-bind:key="pedido.id">
      <PedidoCard
        v-bind:user="pedido.user"
        v-bind:date="pedido.date"
        v-bind:pizza="pedido.pizza"
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
        pizza: 'Margarita',
        ingredientes: 'Queso, Salsa de Tomate',
      },
      {
        id: '2',
        user: 'Jaimito',
        date: '04/07/2020',
        pizza: 'Margarita',
        ingredientes: 'Queso, Salsa de Tomate, Tocineta',
      },
    ],
  }),
};
</script>
