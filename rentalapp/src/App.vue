<template>
  <v-app color="red">
    <v-app-bar app color="primary" flat dark>
      <div class="d-flex align-center display-1">Vehicle Rental</div>

      <v-spacer></v-spacer>

      <v-btn to="/" text>
        <span class="mr-2">Home</span>
      </v-btn>
      <v-btn to="/about" text>
        <span class="mr-2">About</span>
      </v-btn>
      <v-btn to="/contactus" text>
        <span class="mr-2">Contact Us</span>
      </v-btn>
      <v-btn to="/vehicles" text>
        <span class="mr-2">Vehicles</span>
      </v-btn>
      <v-btn to="/vendors" text>
        <span class="mr-2">Vendors</span>
      </v-btn>
      <v-btn to="/usertypes" text>
        <span class="mr-2">User Types</span>
      </v-btn>
      <v-btn text>
        <span class="mr-2">Users</span>
      </v-btn>
      <v-btn text>
        <span class="mr-2">Rentals</span>
      </v-btn>
      <v-btn to="/login" text>
        <span class="mr-2">Login</span>
      </v-btn>
    </v-app-bar>

    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data: () => ({
    //
  })
};
</script>
