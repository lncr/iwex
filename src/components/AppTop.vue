<template>
  <v-container class="container" fluid>
    <v-row>
      <!-- Left Side Text Section -->
      <v-col cols="4" md="4" class="text-section">
        <div class="upper-title">
          <img
            :src="require('@/assets/star.svg')"
            alt="Star Icon"
            class="star-icon"
          />

          <span class="title-text">Personalvermittlung</span>
        </div>
        <h1 class="title">Sie suchen Mitarbeiter?</h1>
        <p class="description">
          Als Spezialist für Personalvermittlung findet IWEX das passende
          Personal für Ihre spezifischen Anforderungen – bundesweit und für Ihre
          Branche.
        </p>
        <v-btn class="home-btn" @click="onRequestPersonnel"
          >Jetzt Personal anfragen</v-btn
        >
      </v-col>

      <!-- Right Side Image Section -->
      <v-col cols="8" md="8" class="image-section">
        <v-img
          src="@/assets/SVG.svg"
          alt="IWEX Mitarbeiter"
          class="employee-image"
        />
      </v-col>
    </v-row>

    <!-- Bottom Statistics Section -->
    <v-row class="stats-section" justify="center" align="center">
      <v-col cols="5" md="5" class="stat">
        <div class="iwex-col">
          <span class="iwex">IWEX</span>
          <span class="iwex-yel">Zufriedene Partner in ganz Deutschland</span>
          <p>
            IWEX hat es sich zum Ziel gesetzt, eine wertvolle Verbindung
            zwischen Studenten, insbesondere aus Kirgistan und Zentralasien, und
            dem deutschen Arbeitsmarkt herzustellen.
          </p>
        </div>
      </v-col>
      <v-col cols="3" md="3" class="stat">
        <h2>2500</h2>
        <p>vermittelte Studenten</p>
      </v-col>
      <v-col cols="1" md="1" class="stat">
        <h2>35</h2>
        <p>Partner</p>
      </v-col>
      <v-col cols="3" md="3" class="stat">
        <h2>2022</h2>
        <p>Firmengründung</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "AppTop",
  methods: {
    onRequestPersonnel() {
      // Function to handle the personnel request button click
      console.log("Personnel request initiated");
    },
  },
};
</script>

<style scoped lang="scss">
.text-section {
  text-align: left;
  margin-top: 120px;
}

.upper-title {
  display: flex;
  align-items: center;
  gap: 12px;
}
.title-text {
  color: #767676;
  font-size: 20px;
  gap: 12px;
  font-family: Open Sans;
}
.star {
  width: 48px;
  height: 48px;
}
.title {
  font-size: 60px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #333333;
  font-family: Epilogue;
}

.description {
  font-size: 17px;
  margin-bottom: 20px;
  color: #515151;
  font-family: Open Sans;
}

.home-btn {
  background-color: #feca00;
  color: #333333;
  font-size: 17px;
  font-family: Epilogue;
  text-transform: none;
  font-weight: 600;
}

.employee-image {
  max-width: 1000px;
  width: 100%;
  border-radius: 8px;
}

.stats-section {
  margin-top: 40px;
}

.stat {
  text-align: center;
  h2 {
    font-size: 96px;
    font-weight: bold;
    margin: 0;
    color: #ffcc01;
  }
  p {
    font-size: 20px;
    color: #666;
    color: #515151;
    font-family: Epilogue;
  }
  .iwex-col {
    display: flex;
    flex-direction: column;
    text-align: start;
    .iwex {
      font-size: 48px;
      color: #333333;
      font-weight: 700;
    }
    .iwex-yel {
      color: #feca00;
      font-size: 15px;
      font-weight: 700;
      font-family: Open Sans;
    }
    p {
      font-size: 17px;
      color: #333333;
      font-family: Open Sans;
    }
  }
}
</style>
