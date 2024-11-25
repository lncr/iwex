<template>
  <div class="container">
    <!-- Заголовок и иконка -->
    <div class="section-header">
      <span class="section-title" v-html="$t('steps.title')"> </span>
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
            <div class="icon-wrapper">
              <img :src="step.icon" alt="Step Icon" class="step-icon" />
              <img :src="step.innerIcon" alt="Inner Icon" class="inner-icon" />
            </div>
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
import { computed, ref } from "vue";
import { useI18n } from "vue-i18n";

// Импортируем иконки
import starIcon from "@/assets/star.svg";
import card1Svg from "@/assets/card1Svg.svg";
import card2Svg from "@/assets/card2Svg.svg";
import card3Svg from "@/assets/card3Svg.svg";
import card4Svg from "@/assets/card4Svg.svg";
import card5Svg from "@/assets/card5Svg.svg";

// Индекс текущего слайда
const carouselIndex = ref(0);
const { t } = useI18n();

const steps = computed(() => [
  {
    icon: starIcon,
    innerIcon: card1Svg,
    title: t("steps.card1Title"),
    description: t("steps.card1Desc"),
  },
  {
    icon: starIcon,
    innerIcon: card2Svg,
    title: t("steps.card2Title"),
    description: t("steps.card2Desc"),
  },
  {
    icon: starIcon,
    innerIcon: card3Svg,
    title: t("steps.card3Title"),
    description: t("steps.card3Desc"),
  },
  {
    icon: starIcon,
    innerIcon: card4Svg,
    title: t("steps.card4Title"),
    description: t("steps.card4Desc"),
  },
  {
    icon: starIcon,
    innerIcon: card5Svg,
    title: t("steps.card5Title"),
    description: t("steps.card5Desc"),
  },
]);

// Функции навигации слайдера
function prevSlide() {
  carouselIndex.value =
    (carouselIndex.value - 1 + steps.value.length) % steps.value.length;
}

function nextSlide() {
  carouselIndex.value = (carouselIndex.value + 1) % steps.value.length;
}

// Функция определения класса для слайда
function getSlideClass(index: number) {
  if (index === carouselIndex.value) {
    return "active-slide";
  } else if (index === (carouselIndex.value + 1) % steps.value.length) {
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
  overflow: visible;
}

.section-header {
  position: relative;
  display: inline-block;
  margin-bottom: 100px;
  width: 740px;
  .section-title {
    font-size: 48px;
    font-weight: 700;
    font-family: "Epilogue", sans-serif;
    color: #333333;
  }
  .semicircle-icon {
    position: absolute;
    left: -15%;
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

.next-slide {
  transform: translateX(20%) translateZ(-150px) scale(0.9);
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

.icon-wrapper {
  position: absolute;
  width: 60px;
  height: 60px;
  top: 20px;
  left: 20px;
}

.step-icon {
  width: 100%;
  height: 100%;
}

.inner-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 30px;
  height: 30px;
  transform: translate(-50%, -50%);
}

/* Стили для активной карточки */
.active-card .icon-wrapper {
  width: 153px;
  height: 153px;
  top: -76.5px; /* Позиционируем иконку, чтобы она перекрывала верх */
  left: -76.5px; /* Позиционируем иконку, чтобы она перекрывала левый край */
  right: auto; /* Сбрасываем значение right */
}

.active-card .inner-icon {
  width: 61px;
  height: 61px;
}

.active-card .step-title {
  margin-top: 100px;
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

/* Навигация слайдера */
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

/* Скрываем предыдущий слайд */
.prev-slide {
  display: none;
}

/* Планшеты и ноутбуки */
@media (max-width: 960px) {
  .section-header {
    width: 100%;
    margin-bottom: 50px;

    .section-title {
      font-size: 36px;
    }

    .semicircle-icon {
      width: 150px;
      left: 0;
    }
  }

  .carousel-wrapper {
    height: 350px;
  }

  .step-card {
    padding: 20px;
    max-width: 500px;
  }

  .active-card .icon-wrapper {
    width: 120px;
    height: 120px;
    top: -60px;
    left: -60px;
  }

  .active-card .inner-icon {
    width: 50px;
    height: 50px;
  }

  .active-card .step-title {
    margin-top: 80px;
  }

  .step-title {
    font-size: 20px;
    margin-top: 80px;
    margin-bottom: 15px;
  }

  .step-description {
    font-size: 16px;
  }

  .carousel-item {
    width: 80%;
  }

  .active-slide {
    transform: translateX(-50%) translateZ(0px) scale(0.9);
  }

  .next-slide {
    transform: translateX(20%) translateZ(-150px) scale(0.8);
  }
}

/* Мобильные устройства */
@media (max-width: 600px) {
  .section-header {
    width: 100%;
    margin-bottom: 30px;

    .section-title {
      font-size: 24px;
    }

    .semicircle-icon {
      width: 100px;
      left: -5%;
    }
  }

  .carousel-wrapper {
    height: 300px;
  }

  .step-card {
    padding: 15px;
    max-width: 100%;
  }

  .active-card .icon-wrapper {
    width: 80px;
    height: 80px;
    top: -40px;
    left: -40px;
  }

  .active-card .inner-icon {
    width: 30px;
    height: 30px;
  }

  .active-card .step-title {
    margin-top: 60px;
  }

  .step-title {
    font-size: 18px;
    margin-top: 60px;
    margin-bottom: 10px;
  }

  .step-description {
    font-size: 14px;
  }

  .carousel-item {
    width: 90%;
  }

  .active-slide {
    transform: translateX(-50%) translateZ(0px) scale(0.8);
  }

  .next-slide {
    transform: translateX(20%) translateZ(-100px) scale(0.7);
  }

  /* Скрываем иконку на очень маленьких экранах */
  @media (max-width: 400px) {
    .semicircle-icon {
      display: none;
    }
  }
}
</style>
