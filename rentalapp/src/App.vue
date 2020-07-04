<template>
  <v-app class="app">
    <v-main name="app">
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "App",
  data: () => ({}),

  computed: {
    ...mapGetters(["isAuthenticated"])
  },

  methods: {
    logout: function() {
      this.$store.dispatch("logout").then(() => {
        this.$router.push("/login");
      });
    }
  }
};
</script>

<style>
.app {
  background-color: #faf4f2 !important;
}
.main-bg {
  background-image: url("assets/car3.jpg");
  background-repeat: no-repeat;
  background-size: auto;
  background-position: center;
  margin-top: -64px;
  padding-top: 90px;
  padding-bottom: 80px;
  border-bottom-left-radius: 50px;
  border-bottom-right-radius: 50px;
}
.nav-header {
  background: unset !important;
}
</style>
