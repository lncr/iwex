<template>
  <div class="container">
    <!-- Заголовок и круг с текстом -->
    <div class="section-header">
      <span class="section-title">
        In diesen Bereichen<br />
        sind wir tätig!
      </span>
      <div class="circle-text">
        <span class="two"
          ><p>200</p>
          Studenten<br />direkt vermittelbar</span
        >
      </div>
    </div>

    <!-- Иконки с описаниями -->
    <div class="industries">
      <div
        class="industry-item"
        v-for="(industry, index) in industries"
        :key="index"
      >
        <img :src="industry.icon" :alt="industry.name" class="industry-icon" />
        <p class="industry-name">{{ industry.name }}</p>
      </div>
    </div>

    <!-- Галерея изображений слайдер -->
    <div class="gallery-section">
      <!-- Слайдер изображений -->
      <v-carousel
        :show-arrows="false"
        v-model="carouselIndex"
        hide-delimiters
        :cycle="false"
      >
        <v-carousel-item v-for="(imageSet, i) in galleryImages" :key="i">
          <div class="gallery-images">
            <img :src="imageSet.main" alt="Main Image" class="main-image" />
            <div class="side-images">
              <img
                v-for="(img, idx) in imageSet.side"
                :key="idx"
                :src="img"
                alt="Side Image"
                class="side-image"
              />
            </div>
          </div>
        </v-carousel-item>
      </v-carousel>

      <!-- Навигация слайдера -->
      <div class="carousel-navigation">
        <div class="carousel-dots">
          <span
            v-for="(dot, index) in galleryImages.length"
            :key="index"
            :class="{ active: index === carouselIndex }"
          ></span>
        </div>
        <div class="carousel-buttons">
          <v-btn icon @click="prevSlide">
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
          <v-btn icon @click="nextSlide">
            <v-icon>mdi-chevron-right</v-icon>
          </v-btn>
        </div>
      </div>
    </div>

    <!-- Кнопка под слайдером -->
    <div class="slider-button">
      <v-btn color="#FECA00" class="btn-center">
        Jetzt Personal anfragen
      </v-btn>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

// Данные индустрий
const industries = [
  { name: "Tourismus", icon: require("@/assets/tourism.svg") },
  { name: "Logistik", icon: require("@/assets/logistic.svg") },
  {
    name: "System Gastronomie",
    icon: require("@/assets/gastronomy.svg"),
    class: "line-break",
  },
  { name: "Flughafen", icon: require("@/assets/air.svg") },
  { name: "Hotel", icon: require("@/assets/hotel.svg") },
];

// Данные галереи изображений
const galleryImages = [
  {
    main: require("@/assets/photo1.png"),
    side: [require("@/assets/photo2.png"), require("@/assets/photo3.png")],
  },
  {
    main: require("@/assets/photo1.png"),
    side: [require("@/assets/photo2.png"), require("@/assets/photo3.png")],
  },
];

// Индекс текущего слайда
const carouselIndex = ref(0);

// Функции навигации слайдера
function prevSlide() {
  if (carouselIndex.value > 0) {
    carouselIndex.value--;
  }
}

function nextSlide() {
  if (carouselIndex.value < galleryImages.length - 1) {
    carouselIndex.value++;
  }
}
</script>

<style scoped lang="scss">
.section-header {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 120px;
  .section-title {
    font-size: 48px;
    font-weight: 700;
    font-family: "Epilogue", sans-serif;
    color: #ffcb00;
    text-align: center;
  }
}

.circle-text {
  position: absolute;
  right: -50px;
  top: -70px;
  width: 221px;
  height: 221px;
  background-color: #feca00;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  .two {
    transform: rotate(20deg);
    color: #333333;
    font-family: Epilogue;
    font-weight: 700;
    font-size: 15px;
    text-align: center;
    P {
      font-size: 72px;
    }
  }
}

.industries {
  display: flex;
  justify-content: center;
  margin-top: 40px;
  margin-bottom: 60px;
  gap: 40px;
  .industry-item {
    text-align: center;
  }

  .industry-icon {
    max-width: 80px;
    margin-bottom: 10px;
  }

  .industry-name {
    font-size: 20px;
    font-family: "Open Sans", sans-serif;
    color: #333333;
  }
}

.gallery-section {
  position: relative;
}

.gallery-images {
  display: flex;
  gap: 24px;
}

.main-image {
  max-width: 600px;
  width: 100%;
  max-height: 475px;
  border-radius: 30px;
}

.side-images {
  max-width: 315px;
  display: flex;
  gap: 24px;
}

.side-image {
  max-width: 100%;
  height: auto;
  margin-bottom: 10px;
  border-radius: 10px;
}

.carousel-navigation {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
  flex-direction: column;
}

.carousel-dots {
  display: flex;
  margin-bottom: 10px;
}

.carousel-dots span {
  display: block;
  width: 10px;
  height: 10px;
  background-color: #ccc;
  margin: 0 5px;
  border-radius: 50%;
}

.carousel-dots .active {
  background-color: #000000;
}

.carousel-buttons {
  display: flex;
}

.carousel-buttons .v-btn {
  margin: 0 10px;
}

.slider-button {
  text-align: center;
  margin-top: 40px;
}

.btn-center {
  background-color: #feca00;
  color: #333333;
  text-transform: none;
}
</style>
