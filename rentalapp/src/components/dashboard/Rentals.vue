<template>
  <Datatable
    :headers="headers"
    :items="items"
    :crud-object="crudObject"
    :title="'Rentals'"
    :post-url="'rentals/'"
    :put-url="'rental/'"
  ></Datatable>
</template>

<script>
import rentalApi from "@/api/rentalApi";
import Datatable from "@/components/dashboard/Datatable";

export default {
  components: {
    Datatable
  },

  created() {
    rentalApi.get("rentals/").then(response => (this.items = response.data));

    rentalApi
      .get("users/")
      .then(response => (this.users = response.data))
      .then(() =>
        rentalApi.get("vehicles/").then(response => {
          this.vehicles = response.data;
          this.headers = [
            {
              id: "ID",
              align: "start",
              sortable: false,
              value: "id"
            },
            {
              text: "User",
              value: "user_id",
              list: this.users,
              label: "username"
            },
            {
              text: "Driver",
              value: "driver_id",
              list: this.users,
              label: "username"
            },
            { text: "Vehicle Rate", value: "vehicle_rate" },
            { text: "Driver Rate", value: "driver_rate" },
            { text: "Status", value: "status" },
            { text: "Dispatched", value: "dispatched" },
            { text: "Returned", value: "returned" },
            {
              text: "Vehicle",
              value: "vehicle_id",
              list: this.vehicles,
              label: "name"
            },
            { text: "Created", value: "created" },
            { text: "Updated", value: "updated" },
            { text: "Actions", value: "actions", sortable: false }
          ];
        })
      );
  },

  mounted() {},

  data: () => ({
    items: [],
    vehicles: [],
    users: [],
    headers: [],
    crudObject: {
      user_id: "",
      driver_id: "",
      vehicle_rate: "",
      driver_rate: "",
      status: "",
      dispatched: "",
      returned: "",
      vehicle_id: ""
    }
  })
};
</script>

<style></style>
