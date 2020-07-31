<template>
  <div>
      <Header>
      </Header>
      <md-app-content>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae non explicabo, neque.</p>
      </md-app-content>
  </div>
</template>

<script>
import Header from '@/components/Header.vue';

export default {
  name: 'Home',
  components: {
    Header,
  },
};
</script>
