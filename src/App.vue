<template>
  <v-app class="container">
    <v-main>
      <AppNavbar></AppNavbar>
      <router-view />
    </v-main>
  </v-app>
</template>

<script lang="ts" setup>
import AppNavbar from "./components/AppNavbar.vue";
</script>
