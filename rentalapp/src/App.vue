<template>
  <v-app class="app">
    <v-content>
          <div class="main-bg rounded-b-xl">
            
          <v-app-bar app hide-on-scroll dense color="unset" flat light class="nav-header">
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

    <v-card
    class="my-8 mx-auto  ml-12"
    max-width="374"
  >
    <v-img
      height="250"
      src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
    ></v-img>

    <v-card-title>Cafe Badilico</v-card-title>

    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
      >
        <v-rating
          :value="4.5"
          color="amber"
          dense
          half-increments
          readonly
          size="14"
        ></v-rating>

        <div class="grey--text ml-4">4.5 (413)</div>
      </v-row>

      <div class="my-4 subtitle-1">
        $ • Italian, Cafe
      </div>

      <div>Small plates, salads & sandwiches - an intimate setting with 12 indoor seats plus patio seating.</div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-title>Tonight's availability</v-card-title>

    <v-card-text>
      <v-chip-group
        v-model="selection"
        active-class="deep-purple accent-4 white--text"
        column
      >
        <v-chip>5:30PM</v-chip>

        <v-chip>7:30PM</v-chip>

        <v-chip>8:00PM</v-chip>

        <v-chip>9:00PM</v-chip>
      </v-chip-group>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="deep-purple lighten-2"
        text
        @click="reserve"
      >
        Reserve
      </v-btn>
    </v-card-actions>
  </v-card>

    </div>
    <v-container>
      <router-view></router-view>
      </v-container>
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
      this.$store.dispatch("logout").then(() => {
        this.$router.push("/login");
      });
    }
  }
};
</script>

<style>
.app{
  background-color: #FAF4F2!important;
}
.main-bg{
  background-image: url("assets/car3.jpg");
   background-repeat:no-repeat;
   background-size:auto;
   background-position:center;
   margin-top: -64px;
   padding-top: 90px;
   padding-bottom: 80px;
   border-bottom-left-radius: 50px;
   border-bottom-right-radius: 50px;
}
.nav-header{
  background: unset!important;
}
</style>
