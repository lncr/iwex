<template>
  <v-container class="container" fluid>
    <v-row class="top-row">
      <!-- Левая текстовая секция -->
      <v-col cols="12" md="5" class="text-section">
        <div class="upper-title">
          <img
            :src="require('@/assets/star.svg')"
            alt="Star Icon"
            class="star-icon"
          />
          <span class="title-text">{{ $t("appTop.text") }}</span>
        </div>
        <h1 class="title">{{ $t("appTop.title") }}</h1>
        <p class="description">
          {{ $t("appTop.description") }}
        </p>
        <v-btn class="home-btn" @click="navigateToContact">
          {{ $t("button") }}
        </v-btn>
      </v-col>

      <!-- Правая секция с изображением (скрыта на маленьких экранах) -->
      <v-col cols="12" md="7" class="image-section d-none d-md-block">
        <div class="image-wrapper">
          <img :src="SVG" alt="IWEX Mitarbeiter" class="employee-image" />
          <img :src="girl" alt="Overlay Image" class="overlay-image" />
        </div>
      </v-col>
    </v-row>

    <!-- Секция со статистикой -->
    <v-row class="stats-section top-row" justify="center" align="center">
      <v-col cols="12" md="3" class="stat">
        <div class="iwex-col">
          <span class="iwex">{{ $t("appTop.companyName") }}</span>
          <span class="iwex-yel">{{ $t("appTop.underTitle") }}</span>
          <p>
            {{ $t("appTop.companyDesc") }}
          </p>
        </div>
      </v-col>
      <v-col cols="4" md="3" class="stat">
        <h2>2500</h2>
        <p>{{ $t("appTop.students") }}</p>
      </v-col>
      <v-col cols="4" md="3" class="stat">
        <h2>35</h2>
        <p>{{ $t("appTop.partner") }}</p>
      </v-col>
      <v-col cols="4" md="3" class="stat">
        <h2>2022</h2>
        <p>{{ $t("appTop.year") }}</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { useRouter } from "vue-router";
import SVG from "../assets/SVG.svg";
import girl from "../assets/girl.png";

const router = useRouter();

function navigateToContact() {
  router.push("/contact"); // Переход на страницу контактов
}
</script>

<style scoped lang="scss">
.text-section {
  text-align: left;
  margin-top: 60px;
  box-sizing: border-box;
}

.upper-title {
  display: flex;
  align-items: center;
  gap: 12px;
}
.title-text {
  color: #767676;
  font-size: 16px;
  gap: 12px;
  font-family: "Open Sans", sans-serif;
}
.star-icon {
  width: 24px;
  height: 24px;
}
.title {
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #333333;
  font-family: "Epilogue", sans-serif;
}

.description {
  font-size: 14px;
  margin-bottom: 20px;
  color: #515151;
  font-family: "Open Sans", sans-serif;
}

.home-btn {
  background-color: #feca00;
  color: #333333;
  font-size: 14px;
  font-family: "Epilogue", sans-serif;
  text-transform: none;
  font-weight: 600;
}

.image-wrapper {
  position: relative;
  width: 100%;
  overflow: hidden; /* Чтобы изображения не выходили за пределы контейнера */
}

.employee-image {
  width: 100%;
  height: 100%;
  display: block;
  border-radius: 8px;
}

.overlay-image {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  border-radius: 8px;
}

.stats-section {
  margin-top: 20px;
  box-sizing: border-box;
  padding: 0 8px;
}

.stat {
  text-align: center;
  h2 {
    font-size: 36px;
    font-weight: bold;
    margin: 0;
    color: #ffcc01;
    font-family: "Epilogue", sans-serif;
  }
  p {
    font-size: 12px;
    color: #515151;
    font-family: "Epilogue", sans-serif;
    font-weight: 700;
  }
  .iwex-col {
    display: flex;
    flex-direction: column;
    text-align: start;
    .iwex {
      font-size: 32px;
      color: #333333;
      font-weight: 700;
    }
    .iwex-yel {
      color: #feca00;
      font-size: 14px;
      font-weight: 700;
      font-family: "Open Sans", sans-serif;
    }
    p {
      font-size: 14px;
      color: #333333;
      font-family: "Open Sans", sans-serif;
      font-weight: 400;
    }
  }
}

/* Адаптивные стили */
@media (min-width: 960px) {
  .text-section {
    margin-top: 120px;
  }
  .title {
    font-size: 60px;
  }
  .description {
    font-size: 17px;
  }
  .home-btn {
    font-size: 17px;
  }
  .stat h2 {
    font-size: 96px;
  }
  .stat p {
    font-size: 20px;
  }
  .iwex-col .iwex {
    font-size: 48px;
  }
}

@media (max-width: 600px) {
  .top-row {
    width: 95%;
  }
  .text-section {
    display: flex;
    justify-content: center;
    flex-direction: column;
  }
  .upper-title {
    justify-content: center;
  }
  .title {
    text-align: center;
  }
  .description {
    text-align: center;
  }
  .home-btn {
    display: block;
    margin: 0 auto;
  }
  .stat {
    .iwex-col {
      padding: 0 8px;
    }
  }
}
</style>
