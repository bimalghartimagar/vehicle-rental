<template>
  <v-navigation-drawer app permanent>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="title"> Vehicle Rental </v-list-item-title>
        <v-list-item-subtitle> Dashboard </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>

    <v-divider></v-divider>

    <v-list dense nav>
      <v-list-item v-for="item in items" :key="item.title" :to="item.url">
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { title: "Dashboard", icon: "mdi-view-dashboard", url: "/dashboard" },
        { title: "Home", icon: "mdi-home", url: "/" },
        { title: "Rentals", icon: "mdi-image", url: "/dashboard/rentals" },
        { title: "Vehicles", icon: "mdi-help-box", url: "/dashboard/vehicles" },
        { title: "Vendors", icon: "mdi-help-box", url: "/dashboard/vendors" },
        {
          title: "User Types",
          icon: "mdi-help-box",
          url: "/dashboard/usertypes",
        },
      ],
    };
  },
};
</script>
