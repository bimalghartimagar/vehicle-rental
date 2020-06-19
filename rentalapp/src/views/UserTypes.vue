<template>
  <Datatable
    :headers="headers"
    :items="items"
    :crud-object="crudObject"
    :title="'User Types'"
    :post-url="'usertypes/'"
    :put-url="'usertype/'"
  ></Datatable>
</template>

<script>
import rentalApi from "../api/rentalApi";
import Datatable from "../components/Datatable";

export default {
  components: {
    Datatable
  },

  data: () => ({
    items: [],
    headers: [
      {
        id: "ID",
        align: "start",
        sortable: false,
        value: "id"
      },
      { text: "Name", value: "name" },
      { text: "Created", value: "created" },
      { text: "Updated", value: "updated" },
      { text: "Actions", value: "actions", sortable: false }
    ],
    crudObject: { name: "" }
  }),

  created() {
    rentalApi.get("usertypes/").then(response => (this.items = response.data));
  }
};
</script>

<style></style>
