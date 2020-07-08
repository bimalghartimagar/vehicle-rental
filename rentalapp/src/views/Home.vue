<template>
  <v-scroll>
    <v-content name="home" class="main-container">
      <div class="main-bg" id="home">
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

          <v-btn @click="$vuetify.goTo('#home', options)" text>
            <span class="mr-2">Home</span>
          </v-btn>
          <v-btn @click="$vuetify.goTo('#services', options)" text>
            <span class="mr-2">Services</span>
          </v-btn>
          <v-btn @click="$vuetify.goTo('#howitworks', options)" text>
            <span class="mr-2">How It Works</span>
          </v-btn>
          <v-btn @click="$vuetify.goTo('#testimonials', options)" text>
            <span class="mr-2">Testimonials</span>
          </v-btn>
          <v-btn @click="$vuetify.goTo('#about', options)" text>
            <span class="mr-2">About</span>
          </v-btn>
          <v-btn @click="$vuetify.goTo('#contactus', options)" text>
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
          <v-card-title>Start your trip here</v-card-title>

          <v-card-text>
            <v-text-field label="Pick-up Location" outlined></v-text-field>

            <v-text-field label="Drop-off Location" outlined></v-text-field>

            <v-text-field label="Pick-up Date" outlined></v-text-field>

            <v-text-field label="Drop-off Date" outlined></v-text-field>
          </v-card-text>

          <!-- <v-card-title>Tonight's availability</v-card-title>

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
          </v-card-text> -->

          <v-card-actions>
            <v-btn color="green" block @click="reserve">Reserve</v-btn>
          </v-card-actions>
        </v-card>
      </div>
      <Splash class="mt-n8" />
      <Services />
      <HowItWorks />
      <Testimonial />
      <About />
      <ContactUs />
      <Footer />
    </v-content>
  </v-scroll>
</template>

<script>
import { mapGetters } from "vuex";

import Splash from "@/components/Splash.vue";
import About from "@/components/About.vue";
import ContactUs from "@/components/ContactUs.vue";
import Services from "@/components/Services.vue";
import HowItWorks from "@/components/HowItWorks.vue";
import Testimonial from "@/components/Testimonial.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Home",

  components: {
    Splash,
    About,
    ContactUs,
    Services,
    HowItWorks,
    Testimonial,
    Footer
  },

  data() {
    return {
      options: {
        duration: 500,
        offset: 0,
        easing: "linear"
      }
    };
  },

  computed: {
    ...mapGetters(["isAuthenticated"])
  }
};
</script>

<style scoped>
.main-container {
  background-color: lightgray;
}
</style>
