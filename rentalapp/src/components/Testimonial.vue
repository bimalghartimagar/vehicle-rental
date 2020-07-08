<template>
  <div class="testimonials-container" id="testimonials">
    <v-container class="mx-auto" style="width: 75%;">
      <div class="row justify-content-center">
        <div class="col-md-12 text-center heading-section">
          <span class="subheading">Testimonial</span>
          <h2 class="mb-3">Happy Clients</h2>
        </div>
        <v-row>
          <template v-for="testimony in testimonials">
            <v-col cols="3" :key="testimony.name + testimony.position">
              <v-card>
                <div class="d-flex flex-no-wrap justify-space-between">
                  <div>
                    <v-card-subtitle>
                      {{testimony.testimony}}
                    </v-card-subtitle>
                    <v-card-subtitle>
                      {{testimony.name}},<br/>{{testimony.position}}
                    </v-card-subtitle>
                  </div>
                  <v-avatar
                    class="ma-2 ml-1"
                    size="125"
                    tile
                  >
                  <v-img :src="'https://api.adorable.io/avatars/126/abott@adorable.png'"></v-img>
                </v-avatar>
                </div>
              </v-card>
            </v-col>
          </template>
        </v-row>
      </div>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      testimonials: [
        {
          testimony:
            "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",
          name: "Roger Scott",
          position: "UI Designer"
        },
        {
          testimony:
            "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",
          name: "Roger Scott",
          position: "Web Developer"
        },

        {
          testimony:
            "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",
          name: "Roger Scott",
          position: "System Analyst"
        },

        {
          testimony:
            "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",
          name: "Roger Scott",
          position: "Marketing Manager"
        },

        {
          testimony:
            "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",
          name: "Roger Scott",
          position: "Interface Designer"
        },

        {
          testimony:
            "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",
          name: "Roger Scott",
          position: "UI Designer"
        },

        {
          testimony:
            "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",
          name: "Roger Scott",
          position: "Web Developer"
        },
        {
          testimony:
            "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",
          name: "Roger Scott",
          position: "System Analyst"
        },
        {
          testimony:
            "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",
          name: "Roger Scott",
          position: "Marketing Manager"
        },
        {
          testimony:
            "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",
          name: "Roger Scott",
          position: "Interface Designer"
        },
        {
          testimony:
            "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",
          name: "Roger Scott",
          position: "UI Designer"
        }
      ]
    };
  }
};
</script>