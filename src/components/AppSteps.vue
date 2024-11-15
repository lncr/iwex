<template>
  <div class="container">
    <!-- Заголовок и иконка -->
    <div class="section-header">
      <span class="section-title">
        So einfach können Sie<br />
        bei IWEX Mitarbeiter anfragen
      </span>
      <v-img
        src="@/assets/stone.svg"
        alt="Semicircle Icon"
        class="semicircle-icon"
      />
    </div>

    <!-- Слайдер карточек -->
    <div class="steps-carousel">
      <div class="carousel-wrapper">
        <div
          class="carousel-item"
          v-for="(step, index) in steps"
          :key="index"
          :class="getSlideClass(index)"
          @swipeleft="nextSlide"
          @swiperight="prevSlide"
        >
          <div
            class="step-card"
            :class="{ 'active-card': index === carouselIndex }"
          >
            <img
              :src="step.icon"
              alt="Step Icon"
              class="step-icon"
              :class="{ 'active-icon': index === carouselIndex }"
            />
            <h2 class="step-title">{{ step.title }}</h2>
            <p class="step-description">{{ step.description }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Навигация слайдера -->
    <div class="carousel-navigation">
      <div class="carousel-dots">
        <span
          v-for="(dot, index) in steps.length"
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
</template>

<script setup lang="ts">
import { ref } from "vue";

// Индекс текущего слайда
const carouselIndex = ref(0);

const steps = [
  {
    icon: require("@/assets/star.svg"),
    title: "Unterstützung nach der Einstellung:",
    description:
      "Unsere Arbeit endet nicht mit der Vertragsunterzeichnung. Wir begleiten sowohl Ihr Unternehmen als auch den Mitarbeiter, um eine erfolgreiche Eingliederung und langfristige Zusammenarbeit zu gewährleisten.",
  },
  {
    icon: require("@/assets/star.svg"),
    title: "Feedback und Begleitung:",
    description:
      "Wir sammeln Feedback nach jedem Interview und unterstützen Sie bei der Entscheidungsfindung. Unser Team koordiniert die Verhandlungen mit dem Kandidaten bis zur Vertragsunterzeichnung, um einen reibungslosen Abschluss des Prozesses zu gewährleisten.",
  },
  {
    icon: require("@/assets/star.svg"),
    title: "Organisation und Koordination von Vorstellungsgesprächen:",
    description:
      "Wir übernehmen die Organisation der Interviews und passen uns Ihrem Zeitplan an, um eine effiziente Kommunikation zwischen Ihnen und den Bewerbern zu gewährleisten.",
  },
  {
    icon: require("@/assets/star.svg"),
    title: "Präsentation der besten Kandidaten:",
    description:
      "Nach der Vorauswahl stellen wir Ihnen die besten Kandidaten mit detaillierten Lebensläufen und unseren Empfehlungen vor. So erhalten Sie ein umfassendes Bild von jedem Kandidaten, bevor Sie ihn zu einem Gespräch einladen.",
  },
  {
    icon: require("@/assets/star.svg"),
    title: "Vorauswahl und Interviews:",
    description:
      "Unsere erfahrenen Recruiter führen erste Auswahlrunden durch, einschließlich Interviews und Qualifikationsprüfungen. Wir bewerten die beruflichen Fähigkeiten, Erfahrungen und persönlichen Eigenschaften der Kandidaten, um sicherzustellen, dass sie Ihren Anforderungen entsprechen.",
  },
];

// Функции навигации слайдера
function prevSlide() {
  carouselIndex.value = (carouselIndex.value - 1 + steps.length) % steps.length;
}

function nextSlide() {
  carouselIndex.value = (carouselIndex.value + 1) % steps.length;
}

// Классы для слайдов
function getSlideClass(index: number) {
  if (index === carouselIndex.value) {
    return "active-slide";
  } else if (index === (carouselIndex.value + 1) % steps.length) {
    return "next-slide";
  } else if (
    index ===
    (carouselIndex.value - 1 + steps.length) % steps.length
  ) {
    return "prev-slide";
  } else {
    return "hidden-slide";
  }
}
</script>

<style scoped lang="scss">
.container {
  text-align: center;
  margin-top: 120px;
  overflow: visible;
}

.section-header {
  position: relative;
  display: inline-block;
  margin-bottom: 40px;
  .section-title {
    font-size: 48px;
    font-weight: 700;
    font-family: "Epilogue", sans-serif;
    color: #333333;
  }
  .semicircle-icon {
    position: absolute;
    left: -140px;
    top: -10px;
    width: 220px;
  }
}

.steps-carousel {
  position: relative;
  width: 100%;
  overflow: visible;
  margin-bottom: 20px;
}

.carousel-wrapper {
  position: relative;
  width: 100%;
  height: 400px;
  perspective: 1000px;
}

.carousel-item {
  position: absolute;
  top: 0;
  left: 50%;
  width: 80%;
  transform-style: preserve-3d;
  transition: transform 0.5s ease, opacity 0.5s ease;
}

.active-slide {
  transform: translateX(-50%) translateZ(0px) scale(1);
  opacity: 1;
  z-index: 3;
}

.prev-slide {
  transform: translateX(-110%) translateZ(-150px) scale(0.9);
  opacity: 0.7;
  z-index: 2;
}

.next-slide {
  transform: translateX(10%) translateZ(-150px) scale(0.9);
  opacity: 0.7;
  z-index: 2;
}

.hidden-slide {
  opacity: 0;
  z-index: 1;
  display: none;
}

.step-card {
  background-color: #ffffff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
  padding: 30px;
  border-radius: 10px;
  max-width: 600px;
  margin: 0 auto;
  position: relative;
  overflow: visible;
}

.step-icon {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 60px;
  height: 60px;
}

.step-title {
  font-size: 24px;
  font-weight: 700;
  font-family: "Epilogue", sans-serif;
  color: #333333;
  margin-top: 100px;
  margin-bottom: 20px;
  text-align: left;
}

.step-description {
  font-size: 17px;
  font-family: "Open Sans", sans-serif;
  color: #515151;
  line-height: 1.6;
  text-align: left;
}

/* Кнопки навигации */
.carousel-navigation {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
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

.carousel-buttons .v-btn {
  margin: 0 5px;
}

/* Адаптация иконок в карточках */
.active-card .step-icon {
  width: 60px;
  height: 60px;
}

.step-card:not(.active-card) .step-icon {
  width: 50px;
  height: 50px;
}

/* Дополнительные стили для центровки боковых слайдов */
.prev-slide .step-card,
.next-slide .step-card {
  margin-top: 25px;
}
</style>
