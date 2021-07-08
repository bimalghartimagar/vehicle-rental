<template>
  <v-container class="fill-height" fluid>
    <nav-bar />
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <h1 class="text-center">Sign up for Vehicle Rental</h1>
        <v-card class="elevation-12">
          <v-toolbar color="primary" dark flat>
            <v-toolbar-title>Signup</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                label="Email"
                name="email"
                prepend-icon="email"
                type="text"
                v-model="email"
              ></v-text-field>

              <v-text-field
                label="Username"
                name="username"
                prepend-icon="person"
                type="text"
                v-model="username"
              ></v-text-field>

              <v-text-field
                id="password"
                label="Password"
                name="password"
                prepend-icon="lock"
                type="password"
                v-model="password"
              ></v-text-field>

              <v-text-field
                id="password2"
                label="Re-type Password"
                name="password"
                prepend-icon="lock"
                type="password"
                v-model="password2"
              ></v-text-field>
            </v-form>
            <span>
              {{ errorMsg }}
            </span>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click.prevent="signup()">Signup</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import rentalApi from "@/api/rentalApi";
import NavBar from "../components/shared/NavBar.vue";

export default {
  components: { NavBar },
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      errorMsg: "",
      email: "",
    };
  },

  methods: {
    signup: function () {
      if (this.email.trim().length === 0) {
        this.errorMsg = "Email cannot be empty.";
        return;
      } else if (!this.validEmail(this.email)) {
        this.errorMsg = "Invalid Email address.";
        return;
      } else if (this.username.trim().length === 0) {
        this.errorMsg = "Username cannot be empty.";
        return;
      } else if (this.password.length === 0 || this.password2.length === 0) {
        this.errorMsg = "Password cannot be empty.";
        return;
      } else if (this.password !== this.password2) {
        this.errorMsg = "Passwords should be same.";
        return;
      }

      rentalApi
        .post("auth/signup/", {
          email: this.email,
          username: this.username,
          password: this.password,
          type_id: 1,
        })
        .then((response) => {
          this.username = "";
          this.email = "";
          this.password = "";
          this.password2 = "";
          this.errorMsg = response.data.msg;
        })
        .catch((error) => {
          if (error.response.status === 401) {
            this.errorMsg = error.response.data.msg;
          }
        });
    },
    validEmail: function (email) {
      var re =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
  },
};
</script>
