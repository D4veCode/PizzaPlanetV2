<template>
    <v-card>
        <v-card-title>
          <h2>Pedido</h2>
        </v-card-title>
        <v-card-text>
          <h3>User: {{user}}</h3>
          <h3>Fecha: {{date}}</h3>
          <p> Pizza: {{pizza}}</p>
          <p> Size: {{size}}</p>
          <p> Ingredientes: {{ingredientes}}</p>
        </v-card-text>
      </v-card>
</template>

<script>
export default {
  name: 'PedidoCard',
  props: {
    user: String,
    date: String,
    pizza: String,
    size: String,
    ingredientes: String,
  },
};
</script>
