<template>
  <v-content>
    <Sidebar></Sidebar>
    <router-view></router-view>
  </v-content>
</template>

<script>
import Sidebar from "../components/Sidebar";
export default {
  components: { Sidebar }
};
</script>

<style></style>
