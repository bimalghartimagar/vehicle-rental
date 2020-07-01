<template>
  <v-app color="red">
    <v-app-bar app color="primary" flat dark>
      <div class="d-flex align-center display-1">Vehicle Rental</div>

      <v-spacer></v-spacer>

      <v-btn to="/" text>
        <span class="mr-2">Home</span>
      </v-btn>
      <v-btn to="/about" text>
        <span class="mr-2">About</span>
      </v-btn>
      <v-btn to="/contactus" text>
        <span class="mr-2">Contact Us</span>
      </v-btn>
      <v-btn to="/vehicles" text v-if="isAuthenticated">
        <span class="mr-2">Vehicles</span>
      </v-btn>
      <v-btn to="/vendors" text v-if="isAuthenticated">
        <span class="mr-2">Vendors</span>
      </v-btn>
      <v-btn to="/usertypes" text v-if="isAuthenticated">
        <span class="mr-2">User Types</span>
      </v-btn>
      <v-btn text v-if="isAuthenticated">
        <span class="mr-2">Users</span>
      </v-btn>
      <v-btn text v-if="isAuthenticated">
        <span class="mr-2">Rentals</span>
      </v-btn>
      <v-btn to="/login" text v-if="!isAuthenticated">
        <span class="mr-2">Login</span>
      </v-btn>
      <v-btn to="/signup" text v-if="!isAuthenticated">
        <span class="mr-2">Sign Up</span>
      </v-btn>
      <v-btn @click="logout" text v-if="isAuthenticated">
        <span class="mr-2">Log Out</span>
      </v-btn>
    </v-app-bar>

    <v-content>
      <router-view></router-view>
    </v-content>
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
      this.$store.dispatch("logout");
    }
  }
};
</script>
