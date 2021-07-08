<template>
  <v-scroll>
    <v-content name="home" class="main-container">
      <div class="main-bg" id="home">
        <NavBar />
        <SearchForm />
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
import SearchForm from "@/components/home/SearchForm.vue";
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
    SearchForm,
    Splash,
    About,
    ContactUs,
    Services,
    HowItWorks,
    Testimonial,
    Footer,
    NavBar,
  },
};
</script>

<style scoped>
.main-container {
  background-color: lightgray;
}
</style>
