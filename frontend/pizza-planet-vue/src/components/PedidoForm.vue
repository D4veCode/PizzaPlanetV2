<template>
  <v-row justify='center'>
    <v-col cols='12' sm='10' md='8' lg='6'>
      <v-card ref='form'>
        <v-card-title>¡Bienvenido! Por favor elija su(s) pizza(s)</v-card-title>
        <v-card-text>
          <v-text-field label='Name' placeholder='Nombre' v-model='nombre' solo></v-text-field>
          <v-select :items='pizzas' v-model='pizza' solo label='Tamaño de Pizza'></v-select>
          <v-select
            v-model='ingredientsTotal'
            :items='ingredients'
            item-text='ing'
            chips
            label='Ingredientes'
            multiple
            solo
            hint='Elije cualquier ingrediente'
            persistent-hint
          ></v-select>
          <v-slider v-model='cantPizzas' thumb-label label='Cantidad de Pizzas'
          min='1' max='20'>
          </v-slider>
        </v-card-text>
        <v-divider class='mt-12'></v-divider>
        <v-card-text v-show='pizza'>
          <v-row justify='center'>
            <h1>Su orden</h1>
          </v-row>
          <v-row>
            <v-col md6>
              <b>Tamaño Pizza(s)</b>
            </v-col>
            <v-col md6>
              <b>Precio Base de Pizza</b>
            </v-col>
          </v-row>
          <v-row>
            <v-col md6>{{ pizza }}</v-col>
            <v-col md6>$ {{ precioPizzaSola() }}</v-col>
          </v-row>
          <v-row v-show='ingredientsTotal.length != 0'>
            <v-col md6>
              <b>Ingrediente(s)</b>
            </v-col>
            <v-col md6>
              <b>Precio</b>
            </v-col>
          </v-row>
          <v-row v-for='ing in ingredientsTotal' :key='ing'>
            <v-col md6>{{ ing }}</v-col>
            <v-col md6>{{ingredientPrice(ing)}}</v-col>
          </v-row>
          <v-row v-show='nombre && pizza'>
            <v-col md4>
              <h2>Cliente</h2>
            </v-col>
            <v-col md4>
              <h2>Cantidad de Pizzas</h2>
            </v-col>
            <v-col md4>
              <h2>Total</h2>
            </v-col>
          </v-row>
          <v-row v-show='nombre && pizza'>
            <v-col md4>
              <h3>{{nombre}}</h3>
            </v-col>
            <v-col md4>
              <h3>{{cantPizzas}}</h3>
            </v-col>
            <v-col md4>
              <h3>$ {{sumTotal()}}</h3>
            </v-col>
          </v-row>
        </v-card-text>
        <v-divider class='mt-12'></v-divider>
        <v-card-actions>
          <v-row justify='end'>
            <v-btn color='primary' text @click='submit'>Submit</v-btn>
          </v-row>
        </v-card-actions>
        <v-card-text v-if='message'>
          <v-alert v-if='success' dense text type='success'>{{message}}</v-alert>
          <v-alert v-else dense text type='error'>{{message}}</v-alert>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PedidoForm',
  data: () => ({
    pizzas: ['Personal', 'Mediana', 'Grande'],
    pizza: '',
    ingredients: [
      {
        price: 4,
        ing: 'Jamon',
      },

      {
        price: 3.5,
        ing: 'Champiñones',
      },

      {
        price: 3,
        ing: 'Pimenton',
      },

      {
        price: 4,
        ing: 'Doble Queso',
      },

      {
        price: 5.75,
        ing: 'Aceitunas',
      },

      {
        price: 3.85,
        ing: 'Pepperoni',
      },

      {
        price: 6.25,
        ing: 'Salchichon',
      },
    ],
    ingredientsTotal: [],
    cantPizzas: 1,
    nombre: '',
    success: false,
    message: '',
  }),
  methods: {
    submit() {
      axios
        .post('http://localhost:8000/pedidos/', {
          user: this.nombre,
          price: this.sumTotal(),
          pizza: 'Margarita',
          size: this.pizza,
          ingredientes: this.ingredientsTotal.toString(),
        })
        .then((data) => {
          console.log(data);
          this.message = 'Pedido registrado con exito';
          this.success = true;
        })
        .catch((error) => {
          this.message = (error.response && error.response.data.message)
            || error.message || error.toString();
          this.success = false;
        });
    },
    precioPizzaSola() {
      let precioSola;
      if (this.pizza.toLowerCase() === 'personal') {
        precioSola = 10;
      } else if (this.pizza.toLowerCase() === 'mediana') {
        precioSola = 16;
      } else if (this.pizza.toLowerCase() === 'grande') {
        precioSola = 20;
      } else {
        precioSola = 0;
      }
      return precioSola;
    },
    ingredientPrice(ing) {
      const ingredientsPrices = {
        jamon: 4,
        champiñones: 3.5,
        pimenton: 3,
        'doble queso': 4,
        aceitunas: 5.75,
        pepperoni: 3.85,
        salchichon: 6.25,
      };
      let finalPrice = 0;
      let val;
      const arr = Object.entries(ingredientsPrices);
      // eslint-disable-next-line
      arr.forEach((ele) => {
        if (ing.toLowerCase() === ele[0]) {
          [val, finalPrice] = ele;
          console.log(val);
        }
      });
      return finalPrice;
    },
    sumTotal() {
      let total = 0;
      total += this.precioPizzaSola();
      this.ingredientsTotal.forEach((ele) => {
        total += this.ingredientPrice(ele);
      });
      console.log('total: ', total);
      return total * this.cantPizzas;
    },
  },
};
</script>
