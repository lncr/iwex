<template>
  <v-container class="hero-section">
    <!-- Ваш контент остается без изменений -->

    <!-- Заголовок -->
    <v-row class="text-center mt-4">
      <v-col cols="12">
        <h1 class="hero-title">
          PERSONAL LEASING PLACEMENT AND SERVICE FOR CRAFTS, RESTAURANTS AND
          SERVICE
        </h1>
      </v-col>
    </v-row>

    <!-- Галерея изображений под заголовком -->
    <v-row class="justify-center mt-4">
      <v-col cols="auto" v-for="(image, index) in galleryImages" :key="index">
        <v-img
          :src="image"
          height="220px"
          width="190px"
          class="gallery-image"
        ></v-img>
      </v-col>
    </v-row>

    <!-- Кнопка для связи -->
    <div class="contact-container">
      <span class="contact-title">Need personnel?</span>

      <!-- Основной блок с текстом и кнопкой -->
      <v-row no-gutters class="contact-content">
        <v-col cols="7" class="description-container">
          <span class="description">
            Contact us! We will quickly and efficiently find personnel for you.
            Our team will strive to assist you promptly in the nearest future.
          </span>
        </v-col>
        <v-col cols="5" class="contact-button-container">
          <v-btn class="contact-button" large>CONTACT NOW</v-btn>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from "vue";

// Импорт изображений из папки assets
import image1 from "@/assets/image1.png";
import image2 from "@/assets/image2.png";
import image3 from "@/assets/image3.png";
import image4 from "@/assets/image4.png";
import image5 from "@/assets/image5.png";

// Создание массива изображений с использованием ref
const galleryImages = ref([image1, image2, image3, image4, image5]);
</script>

<style scoped>
.hero-section {
  position: relative;
  color: white; /* Белый текст для контраста */
  padding: 50px 20px;
  text-align: center;
  margin: 0;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow: hidden; /* Prevents scrollbars */
}

/* Переносим фоновое изображение в псевдоэлемент ::before */
.hero-section::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-image: url("@/assets/home-image.png");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  z-index: 1;
  /* Применяем маску градиента для исчезновения изображения снизу вверх */
  mask-image: linear-gradient(to top, transparent 0%, black 100%);
  mask-mode: alpha;
  -webkit-mask-image: linear-gradient(to top, transparent 0%, black 100%);
  -webkit-mask-mode: alpha;
}

/* Обеспечиваем, чтобы контент был поверх псевдоэлемента ::before */
.hero-title {
  margin-top: 220px;
  color: #333333;
  font-size: 56px;
}
.hero-title,
.gallery-image,
.contact-button {
  position: relative;
  z-index: 2; /* Устанавливаем z-index выше, чтобы элементы были поверх фонового изображения */
}

.gallery-image {
  border-radius: 8px;
  margin: 8px;
}

.contact-container {
  width: 100%;
  max-width: 900px;
  margin: auto;
  text-align: left;
}

.contact-title {
  font-size: 18px;
  font-weight: bold;
  display: block;
  margin-bottom: 8px;
  color: #333333;
}

.contact-content {
  border-radius: 50px;
  background-color: #d1d1d1; /* Основной серый фон */
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Тень для эффекта */
}

.description-container {
  background-color: white;
  padding: 12px 16px !important;
  border-top-left-radius: 50px;
  border-bottom-left-radius: 50px;
  display: flex;
  align-items: center;
  border-radius: 24px;
}

.description {
  font-size: 14px;
  color: #333333;
  line-height: 1.5;
}

.contact-button-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.contact-button {
  background-color: transparent;
  color: black;
  font-weight: bold;
  text-transform: uppercase;
  font-size: 16px;
  padding: 0;
}

.contact-button .v-btn__content::after {
  content: ">";
  font-weight: bold;
  margin-left: 8px;
}
</style>
