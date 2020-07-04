<template>
  <v-container>
    <v-row class="text-center mt-n12" no-gutters>
      <v-col cols="3" class="px-8">
        <v-img
          :src="require('../assets/car1.jpg')"
          class="my-3 rounded"
          contain
        />
      </v-col>
      <v-col cols="3" class="px-8">
        <v-img
          :src="require('../assets/car2.jpg')"
          class="my-3 rounded"
          contain
        />
      </v-col>
      <v-col cols="3" class="px-8">
        <v-img
          :src="require('../assets/car3.jpg')"
          class="my-3 rounded"
          contain
        />
      </v-col>
      <v-col cols="3" class="px-8">
        <v-img
          :src="require('../assets/car4.jpg')"
          class="my-3 rounded"
          contain
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Splash",

  data: () => ({})
};
</script>

<style scoped>
.rounded {
  border-radius: 15px;
}
</style>
