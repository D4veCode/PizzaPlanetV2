<template>
    <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Pizza Planet</v-toolbar-title>
    </v-app-bar>
</template>

<script>
export default {
  name: 'Footer',
};
</script>
