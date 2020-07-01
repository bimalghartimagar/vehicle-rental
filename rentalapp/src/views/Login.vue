<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <h1 class="text-center">Login to Vehicle Rental</h1>
        <v-card class="elevation-12">
          <v-toolbar color="primary" dark flat>
            <v-toolbar-title>Login</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                label="Login"
                name="login"
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
            </v-form>
            <span>
              {{ errorMsg }}
            </span>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click.prevent="login">Login</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      errorMsg: ""
    };
  },

  methods: {
    login: function() {
      this.$store
        .dispatch("login", {
          username: this.username,
          password: this.password
        })
        .then(() => {
          this.$router.push("/");
        })
        .catch(error => {
          if (error.response.status === 401) {
            this.errorMsg = error.response.data.msg;
          }
        });
    }
  }
};
</script>
