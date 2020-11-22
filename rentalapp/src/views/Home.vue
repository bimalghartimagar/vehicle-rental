<template>
  <v-scroll>
    <v-content name="home" class="main-container">
      <div class="main-bg" id="home">
        <NavBar />
        <v-card class="my-8 mx-auto ml-12" max-width="374">
          <v-card-title>Start your trip here</v-card-title>

          <v-card-text>
            <v-text-field
              prepend-icon="mdi-map-marker"
              label="Pick-up Location"
              outlined
            ></v-text-field>

            <v-text-field
              prepend-icon="mdi-map-marker"
              label="Drop-off Location"
              outlined
            ></v-text-field>

            <v-menu
              v-model="menu1"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="startDate"
                  prepend-icon="mdi-calendar"
                  label="Pick-up Date"
                  outlined
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="startDate"
                @input="menu1 = false"
              ></v-date-picker>
            </v-menu>

            <v-menu
              v-model="menu2"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="endDate"
                  prepend-icon="mdi-calendar"
                  label="Drop-off Date"
                  outlined
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="endDate"
                @input="menu2 = false"
              ></v-date-picker>
            </v-menu>
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
import Splash from "@/components/home/Splash.vue";
import About from "@/components/home/About.vue";
import ContactUs from "@/components/home/ContactUs.vue";
import Services from "@/components/home/Services.vue";
import HowItWorks from "@/components/home/HowItWorks.vue";
import Testimonial from "@/components/home/Testimonial.vue";
import Footer from "@/components/home/Footer.vue";
import NavBar from "@/components/shared/NavBar.vue";

export default {
  name: "Home",

  components: {
    Splash,
    About,
    ContactUs,
    Services,
    HowItWorks,
    Testimonial,
    Footer,
    NavBar
  }
};
</script>

<style scoped>
.main-container {
  background-color: lightgray;
}
</style>
