<template>
  <v-footer
    color="red darken-2"
    app
  >
    <span class="white--text">&copy; {{ new Date().getFullYear() }}</span>
  </v-footer>
</template>

<script>
export default {
  name: 'Footer',
};
</script>
