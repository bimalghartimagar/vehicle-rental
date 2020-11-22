<template>
  <Datatable
    :headers="headers"
    :items="items"
    :crud-object="crudObject"
    :title="'Vehicles'"
    :post-url="'vehicles/'"
    :put-url="'vehicle/'"
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
    rentalApi.get("vehicles/").then(response => (this.items = response.data));
    rentalApi.get("vendors/").then(response => {
      this.vendors = response.data;
      this.headers = [
        {
          id: "ID",
          align: "start",
          sortable: false,
          value: "id"
        },
        { text: "Name", value: "name" },
        { text: "Seats", value: "seats" },
        { text: "Color", value: "color" },
        { text: "Make Year", value: "make_year" },
        { text: "Rate", value: "rate" },
        { text: "Type", value: "type" },
        {
          text: "Vendor",
          value: "vendor_id",
          list: this.vendors,
          label: "name"
        },
        { text: "Created", value: "created" },
        { text: "Updated", value: "updated" },
        { text: "Actions", value: "actions", sortable: false }
      ];
    });
  },

  mounted() {},

  data: () => ({
    items: [],
    vendors: [],
    headers: [],
    crudObject: {
      name: "",
      seats: "",
      color: "",
      make_year: "",
      rate: "",
      type: "",
      vendor_id: ""
    }
  })
};
</script>

<style></style>
