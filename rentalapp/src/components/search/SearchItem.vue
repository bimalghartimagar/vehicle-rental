<template>
  <v-card class="mx-auto" max-width="600" outlined>
    <v-list-item three-line>
      <v-list-item-content>
        <div class="text-h5 mb-4 font-weight-bold">{{ item.name }}</div>
        <v-list-item-title class="text-h6 mb-1">
          {{ item.vendor }}
        </v-list-item-title>
        <v-list-item-subtitle
          ><v-icon color="blue darken-2"> mdi-seat </v-icon
          >{{ item.seats }} Seats</v-list-item-subtitle
        >
        <v-list-item-subtitle
          ><v-icon color="blue darken-2"> mdi-bag-checked </v-icon
          >{{ item.seats }} Luggages</v-list-item-subtitle
        >
        <v-list-item-subtitle
          ><v-icon color="blue darken-2"> mdi-car-shift-pattern </v-icon>Rs.{{
            item.rate
          }}/day</v-list-item-subtitle
        >
        <v-list-item-subtitle
          ><v-icon color="blue darken-2"> mdi-gas-station </v-icon
          >{{ item.seats }} km/l</v-list-item-subtitle
        >
        <v-list-item-subtitle
          ><v-icon color="blue darken-2"> mdi-cash-100 </v-icon>Rs.{{
            item.rate
          }}/day</v-list-item-subtitle
        >
      </v-list-item-content>

      <v-list-item-avatar tile size="200" color="grey"></v-list-item-avatar>
    </v-list-item>

    <v-card-actions>
      <v-btn :to="`vehicle/${item.id}`" color="secondary" light>Details</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      required: true,
    },
  },
};
</script>
