<template>
  <v-data-table
    :headers="headers"
    :items="items"
    sort-by="id"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-toolbar-title>{{ title }}</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on"
              >New Item</v-btn
            >
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <template v-for="(value, name) in editedItem">
                    <v-col cols="12" sm="6" md="4" :key="name">
                      <v-text-field
                        v-model="editedItem[name]"
                        :label="getLabelName(name)"
                        v-if="!hasList(name)"
                      ></v-text-field>
                      <v-select
                        v-if="hasList(name)"
                        :items="hasList(name)"
                        :label="getLabelName(name)"
                        :item-text="getLabelForDropdown(name)"
                        :item-value="'id'"
                        v-model="editedItem[name]"
                      ></v-select>
                    </v-col>
                  </template>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="save">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>

    <template
      v-for="value in headersWithList"
      v-slot:[getAttrName(value.value)]="{ item }"
      >{{ getNameFromList(item, value.list, value.value, value.label) }}
    </template>

    <template v-slot:[`item.actions`]="{ item }">
      <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
      <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
    </template>
    <template v-slot:no-data>
      <v-btn text color="primary">No data.</v-btn>
    </template>
  </v-data-table>
</template>

<script>
import rentalApi from "@/api/rentalApi";

export default {
  props: ["headers", "items", "crudObject", "title", "postUrl", "putUrl"],
  data: () => ({
    dialog: false,
    editedIndex: -1,
    editedItem: {},
    defaultItem: {},
  }),

  created() {
    this.editedItem = { ...this.crudObject };
    this.defaultItem = { ...this.crudObject };
  },

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },
    headersWithList: function () {
      return this.headers.filter((x) => Object.hasOwnProperty.call(x, "list"));
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
  },

  methods: {
    editItem(item) {
      this.editedIndex = item.id;
      let itemToEdit = {};
      for (let key in this.editedItem) {
        if (Object.keys(item).includes(key)) {
          itemToEdit[key] = item[key];
        }
      }
      this.editedItem = Object.assign({}, itemToEdit);
      this.dialog = true;
    },

    deleteItem(item) {
      let flag = confirm("Are you sure you want to delete this item?");
      if (flag) {
        rentalApi
          .delete(this.putUrl + item.id + "/")
          .then((response) => {
            console.log(response);
            let itemIndex = this.items.findIndex(
              (x) => x.id == response.data.id
            );
            this.$emit("remove-item", itemIndex);
          })
          .catch(function (error) {
            console.log(error);
          });
      }
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        rentalApi
          .put(this.putUrl + this.editedIndex + "/", this.editedItem)
          .then((response) => {
            console.log(response);
            let itemIndex = this.items.findIndex(
              (x) => x.id == response.data.id
            );
            this.$emit("udpate-item", itemIndex, response.data);
          })
          .catch(function (error) {
            console.log(error);
          });
      } else {
        rentalApi
          .post(this.postUrl, this.editedItem)
          .then((response) => {
            console.log(response);
            this.$emit("add-item", response.data);
          })
          .catch(function (error) {
            console.log(error);
          });
      }
      this.close();
    },
    getLabelName(name) {
      let items = this.headers.filter((x) => x.value === name);
      if (items.length === 0) return;
      return items[0].text;
    },
    hasList(name) {
      let items = this.headers.filter((x) => x.value === name);
      if (items.length === 0) return false;
      let item = items[0];
      if (Object.prototype.hasOwnProperty.call(item, "list")) return item.list;
      return false;
    },
    getNameFromList(item, list, attr, label) {
      let items = list.filter((x) => x.id === item[attr]);
      if (items.length == 0) return;
      return items[0][label];
    },
    getAttrName(value) {
      return "item." + value;
    },
    getLabelForDropdown(name) {
      let items = this.headers.filter((x) => x.value === name);
      if (items.length == 0) return "NO-VALUE";
      return items[0]["label"];
    },
  },
};
</script>

<style></style>
