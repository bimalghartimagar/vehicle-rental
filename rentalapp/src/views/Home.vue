<template>
  <v-content name="home">
    <div class="main-bg rounded-b-xl">
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

        <v-btn to="/" text>
          <span class="mr-2">Home</span>
        </v-btn>
        <v-btn to="/about" text>
          <span class="mr-2">About</span>
        </v-btn>
        <v-btn to="/contactus" text>
          <span class="mr-2">Contact Us</span>
        </v-btn>
        <v-btn to="/dashboard" text v-if="isAuthenticated">
          <span class="mr-2">Dashboard</span>
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

      <v-card class="my-8 mx-auto ml-12" max-width="374">
        <v-img
          height="250"
          src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
        ></v-img>

        <v-card-title>Cafe Badilico</v-card-title>

        <v-card-text>
          <v-row align="center" class="mx-0">
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

          <div class="my-4 subtitle-1">$ • Italian, Cafe</div>

          <div>
            Small plates, salads & sandwiches - an intimate setting with 12
            indoor seats plus patio seating.
          </div>
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
          <v-btn color="deep-purple lighten-2" text @click="reserve"
            >Reserve</v-btn
          >
        </v-card-actions>
      </v-card>
      <Splash />
      <About />
      <ContactUs />
    </div>
  </v-content>
</template>

<script>
import { mapGetters } from "vuex";

import Splash from "@/components/Splash.vue";
import About from "@/components/About.vue";
import ContactUs from "@/components/ContactUs.vue";

export default {
  name: "Home",
  components: {
    Splash,
    About,
    ContactUs
  },

  computed: {
    ...mapGetters(["isAuthenticated"])
  },
};
</script>
