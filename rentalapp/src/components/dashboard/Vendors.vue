<template>
  <Datatable
    :headers="headers"
    :items="items"
    :crud-object="crudObject"
    :title="'Vendors'"
    :post-url="'vendors/'"
    :put-url="'vendor/'"
    @update-item="updateItem"
    @add-item="addItem"
    @remove-item="removeItem"
  ></Datatable>
</template>

<script>
import rentalApi from "@/api/rentalApi";
import Datatable from "@/components/dashboard/Datatable";

export default {
  components: {
    Datatable,
  },

  data: () => ({
    items: [],
    headers: [
      {
        id: "ID",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "Name", value: "name" },
      { text: "Created", value: "created" },
      { text: "Updated", value: "updated" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    crudObject: { name: "" },
  }),

  created() {
    rentalApi.get("vendors/").then((response) => (this.items = response.data));
  },

  methods: {
    updateItem: function (itemIndex, data) {
      this.items.splice(itemIndex, 1, data);
    },

    addItem: function (data) {
      this.items.push(data);
    },

    removeItem: function (itemIndex) {
      this.items.splice(itemIndex, 1);
    },
  },
};
</script>

<style></style>
