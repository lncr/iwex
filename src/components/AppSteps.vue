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
      <v-carousel
        v-model="carouselIndex"
        hide-delimiters
        height="auto"
        :cycle="false"
        :show-arrows="false"
        class="custom-carousel"
      >
        <v-carousel-item
          v-for="(step, index) in steps"
          :key="index"
          :class="getSlideClass(index)"
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
        </v-carousel-item>
      </v-carousel>
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

// Данные шагов (10 карточек)
const steps = [
  {
    icon: require("@/assets/star.svg"),
    title: "Bedarfsanalyse des Unternehmens:",
    description:
      "Unsere Zusammenarbeit beginnt mit einer gründlichen Analyse Ihrer Unternehmensanforderungen. Wir prüfen die Spezifikationen Ihres Unternehmens, die Anforderungen der offenen Stellen und die notwendigen Kernkompetenzen der Kandidaten. Dieser Ansatz ermöglicht es uns, das ideale Kandidatenprofil klar zu definieren.",
  },
  {
    icon: require("@/assets/star.svg"),
    title: "Bedarfsanalyse des Unternehmens:",
    description:
      "Unsere Zusammenarbeit beginnt mit einer gründlichen Analyse Ihrer Unternehmensanforderungen. Wir prüfen die Spezifikationen Ihres Unternehmens, die Anforderungen der offenen Stellen und die notwendigen Kernkompetenzen der Kandidaten. Dieser Ansatz ermöglicht es uns, das ideale Kandidatenprofil klar zu definieren.",
  },
  {
    icon: require("@/assets/star.svg"),
    title: "Bedarfsanalyse des Unternehmens:",
    description:
      "Unsere Zusammenarbeit beginnt mit einer gründlichen Analyse Ihrer Unternehmensanforderungen. Wir prüfen die Spezifikationen Ihres Unternehmens, die Anforderungen der offenen Stellen und die notwendigen Kernkompetenzen der Kandidaten. Dieser Ansatz ermöglicht es uns, das ideale Kandidatenprofil klar zu definieren.",
  },
  {
    icon: require("@/assets/star.svg"),
    title: "Bedarfsanalyse des Unternehmens:",
    description:
      "Unsere Zusammenarbeit beginnt mit einer gründlichen Analyse Ihrer Unternehmensanforderungen. Wir prüfen die Spezifikationen Ihres Unternehmens, die Anforderungen der offenen Stellen und die notwendigen Kernkompetenzen der Kandidaten. Dieser Ansatz ermöglicht es uns, das ideale Kandidatenprofil klar zu definieren.",
  },
  {
    icon: require("@/assets/star.svg"),
    title: "Bedarfsanalyse des Unternehmens:",
    description:
      "Unsere Zusammenarbeit beginnt mit einer gründlichen Analyse Ihrer Unternehmensanforderungen. Wir prüfen die Spezifikationen Ihres Unternehmens, die Anforderungen der offenen Stellen und die notwendigen Kernkompetenzen der Kandidaten. Dieser Ansatz ermöglicht es uns, das ideale Kandidatenprofil klar zu definieren.",
  },
  {
    icon: require("@/assets/star.svg"),
    title: "Bedarfsanalyse des Unternehmens:",
    description:
      "Unsere Zusammenarbeit beginnt mit einer gründlichen Analyse Ihrer Unternehmensanforderungen. Wir prüfen die Spezifikationen Ihres Unternehmens, die Anforderungen der offenen Stellen und die notwendigen Kernkompetenzen der Kandidaten. Dieser Ansatz ermöglicht es uns, das ideale Kandidatenprofil klar zu definieren.",
  },
  {
    icon: require("@/assets/star.svg"),
    title: "Bedarfsanalyse des Unternehmens:",
    description:
      "Unsere Zusammenarbeit beginnt mit einer gründlichen Analyse Ihrer Unternehmensanforderungen. Wir prüfen die Spezifikationen Ihres Unternehmens, die Anforderungen der offenen Stellen und die notwendigen Kernkompetenzen der Kandidaten. Dieser Ansatz ermöglicht es uns, das ideale Kandidatenprofil klar zu definieren.",
  },
  {
    icon: require("@/assets/star.svg"),
    title: "Bedarfsanalyse des Unternehmens:",
    description:
      "Unsere Zusammenarbeit beginnt mit einer gründlichen Analyse Ihrer Unternehmensanforderungen. Wir prüfen die Spezifikationen Ihres Unternehmens, die Anforderungen der offenen Stellen und die notwendigen Kernkompetenzen der Kandidaten. Dieser Ansatz ermöglicht es uns, das ideale Kandidatenprofil klar zu definieren.",
  },
  {
    icon: require("@/assets/star.svg"),
    title: "Bedarfsanalyse des Unternehmens:",
    description:
      "Unsere Zusammenarbeit beginnt mit einer gründlichen Analyse Ihrer Unternehmensanforderungen. Wir prüfen die Spezifikationen Ihres Unternehmens, die Anforderungen der offenen Stellen und die notwendigen Kernkompetenzen der Kandidaten. Dieser Ansatz ermöglicht es uns, das ideale Kandidatenprofil klar zu definieren.",
  },
  {
    icon: require("@/assets/star.svg"),
    title: "Bedarfsanalyse des Unternehmens:",
    description:
      "Unsere Zusammenarbeit beginnt mit einer gründlichen Analyse Ihrer Unternehmensanforderungen. Wir prüfen die Spezifikationen Ihres Unternehmens, die Anforderungen der offenen Stellen und die notwendigen Kernkompetenzen der Kandidaten. Dieser Ansatz ermöglicht es uns, das ideale Kandidatenprofil klar zu definieren.",
  },
  // Добавьте остальные 9 карточек с соответствующими данными и иконками
];

// Функции навигации слайдера
function prevSlide() {
  if (carouselIndex.value > 0) {
    carouselIndex.value--;
  }
}

function nextSlide() {
  if (carouselIndex.value < steps.length - 1) {
    carouselIndex.value++;
  }
}

// Классы для слайдов
function getSlideClass(index: number) {
  if (index === carouselIndex.value) {
    return "active-slide";
  } else if (
    index === carouselIndex.value - 1 ||
    (carouselIndex.value === 0 && index === steps.length - 1)
  ) {
    return "prev-slide";
  } else if (
    index === carouselIndex.value + 1 ||
    (carouselIndex.value === steps.length - 1 && index === 0)
  ) {
    return "next-slide";
  } else {
    return "hidden-slide";
  }
}
</script>

<style scoped lang="scss">
.container {
  text-align: center;
  margin-top: 120px;
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
}

.custom-carousel {
  overflow: visible;
}

.v-carousel-item {
  transition: transform 0.5s ease, opacity 0.5s ease;
}

.step-card {
  background-color: #ffffff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 30px;
  border-radius: 10px;
  max-width: 600px;
  margin: 0 auto;
  position: relative;
}

.step-icon {
  position: absolute;
  top: -30px;
  left: -30px;
  width: 60px;
  height: 60px;
}

.step-title {
  font-size: 24px;
  font-weight: 700;
  font-family: "Epilogue", sans-serif;
  color: #333333;
  margin-top: 40px;
  margin-bottom: 20px;
}

.step-description {
  font-size: 17px;
  font-family: "Open Sans", sans-serif;
  color: #515151;
  line-height: 1.6;
}

/* Стили для активного слайда */
.active-slide {
  transform: scale(1);
  opacity: 1;
}

.prev-slide,
.next-slide {
  transform: scale(0.8);
  opacity: 0.5;
  background-color: #dedede;
}

.hidden-slide {
  display: none;
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
  top: -30px;
  left: -30px;
  width: 60px;
  height: 60px;
}

.step-card:not(.active-card) .step-icon {
  top: -20px;
  left: -20px;
  width: 40px;
  height: 40px;
}
</style>
