<template>
  <v-app-bar
    app
    hide-on-scroll
    dense
    color="unset"
    flat
    light
    class="nav-header"
  >
    <div class="d-flex align-center display-1">Vehicle Rental</div>

    <v-spacer></v-spacer>

    <v-btn small to='/' @click="$vuetify.goTo('#home', options)" text>
      <span class="mr-2">Home</span>
    </v-btn>
    <v-btn small to='/#services' @click="$vuetify.goTo('#services', options)" text>
      <span class="mr-2">Services</span>
    </v-btn>
    <v-btn small to='/#howitworks' @click="$vuetify.goTo('#howitworks', options)" text>
      <span class="mr-2">How It Works</span>
    </v-btn>
    <v-btn small to='/#testimonials' @click="$vuetify.goTo('#testimonials', options)" text>
      <span class="mr-2">Testimonials</span>
    </v-btn>
    <v-btn small to='/#about' @click="$vuetify.goTo('#about', options)" text>
      <span class="mr-2">About</span>
    </v-btn>
    <v-btn small to='/#contactus' @click="$vuetify.goTo('#contactus', options)" text>
      <span class="mr-2">Contact Us</span>
    </v-btn>
    <v-btn small to="/dashboard" text v-if="isAuthenticated">
      <span class="mr-2">Dashboard</span>
    </v-btn>
    <v-btn small to="/login" text v-if="!isAuthenticated">
      <span class="mr-2">Login</span>
    </v-btn>
    <v-btn small to="/signup" text v-if="!isAuthenticated">
      <span class="mr-2">Sign Up</span>
    </v-btn>
    <v-btn small @click="logout" text v-if="isAuthenticated">
      <span class="mr-2">Log Out</span>
    </v-btn>
  </v-app-bar>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  data() {
    return {
      options: {
        startDate: new Date().toISOString().substr(0, 10),
        endDate: new Date().toISOString().substr(0, 10),
        duration: 500,
        offset: 0,
        easing: "linear"
      }
    };
  },
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
