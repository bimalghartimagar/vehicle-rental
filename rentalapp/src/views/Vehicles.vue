<template>
  <div class="d-flex pa-2 mt-4">
    <template v-for="vehicle in vehicleList">
      <v-card class="mx-auto" max-width="400" :key="vehicle.id" :to="`vehicle/${vehicle.id}/`">
        <v-img
          class="white--text align-end"
          height="200px"
          src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
        >
          <v-card-title>{{ vehicle.name }}</v-card-title>
        </v-img>

        <v-card-subtitle class="pb-0">Rate/day: Rs{{ vehicle.rate }}</v-card-subtitle>
        <v-card-text class="text--primary">
          <div>Type: {{ vehicle.type }}</div>

          <div>Year: {{ vehicle.make_year }}</div>
        </v-card-text>
        <v-card-actions>
          <v-btn color="secondary" text>Rent</v-btn>
        </v-card-actions>
      </v-card>
    </template>
  </div>
</template>

<script>
import RentalAPI from "@/api/rentalApi";

export default {
  data: () => ({
    vehicleList: []
  }),
  created() {
    RentalAPI.get("vehicles/").then(res => (this.vehicleList = res.data));
  }
};
</script>

<style>
</style>