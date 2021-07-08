<template>
  <v-form ref="form" v-model="valid">
    <v-card class="my-8 mx-auto ml-12" max-width="374">
      <v-card-title>Start your trip here</v-card-title>
      <v-card-text>
        <v-text-field
          v-model="pickup"
          :rules="pickupRules"
          prepend-icon="mdi-map-marker"
          label="Pick-up Location"
          outlined
          required
        ></v-text-field>

        <v-text-field
          v-model="dropoff"
          prepend-icon="mdi-map-marker"
          label="Drop-off Location"
          outlined
        ></v-text-field>

        <v-menu
          v-model="pickupMenu"
          :close-on-content-click="false"
          :nudge-right="40"
          transition="scale-transition"
          offset-y
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="pickupDate"
              :rules="pickupDateRules"
              prepend-icon="mdi-calendar"
              label="Pick-up Date"
              outlined
              v-bind="attrs"
              v-on="on"
              required
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="pickupDate"
            @input="pickupMenu = false"
          ></v-date-picker>
        </v-menu>

        <v-menu
          v-model="dropoffMenu"
          :close-on-content-click="false"
          :nudge-right="40"
          transition="scale-transition"
          offset-y
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="dropoffDate"
              :rules="dropoffDateRules"
              prepend-icon="mdi-calendar"
              label="Drop-off Date"
              outlined
              v-bind="attrs"
              v-on="on"
              required
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="dropoffDate"
            @input="dropoffMenu = false"
          ></v-date-picker>
        </v-menu>
      </v-card-text>
      <v-card-actions>
        <v-btn color="green" block @click="validate">Search</v-btn>
      </v-card-actions>
    </v-card>
  </v-form>
</template>

<script>
export default {
  data() {
    return {
      valid: true,
      pickupMenu: false,
      dropoffMenu: false,
      pickup: "",
      pickupRules: [(v) => !!v || "Pick-up Location is required"],
      dropoff: "",
      dropoffDate: null,
      dropoffDateRules: [(v) => !!v || "Drop-off Date is required"],
      pickupDate: null,
      pickupDateRules: [(v) => !!v || "Pick-up Date is required"],
    };
  },

  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.valid) {
        this.$router.push({
          path: "search",
          query: {
            pickup: this.pickup,
            dropoff: this.dropoff,
            pickupDate: this.pickupDate,
            dropoffDate: this.dropoffDate,
          },
        });
      }
    },
  },
};
</script>
