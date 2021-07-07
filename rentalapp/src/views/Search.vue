<template>
  <div>
    <NavBar />
    <main class="my-12">
      <v-container fluid class="my-4">
        <SearchComponent :data="searchResults" />
      </v-container>
    </main>
  </div>
</template>

<script>
import NavBar from "../components/shared/NavBar.vue";
import SearchComponent from "@/components/search/SearchComponent.vue";
import { mapGetters } from "vuex";

export default {
  components: {
    SearchComponent,
    NavBar
  },

  beforeMount() {
    this.$store.dispatch("fetchResults");
  },

  computed: {
    ...mapGetters(["searchResults"])
  }
};
</script>
