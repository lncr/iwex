<template>
  <div class="container">
    <!-- Заголовок -->
    <div class="section-title">
      <span>
        Willkommen bei IWEX<br />
        Das sind unsere Top-4 Personaldienstleistungen
      </span>
    </div>

    <!-- Описание -->
    <p class="section-description">
      Seit 2014 verbinden wir motivierte Studenten und Arbeitskräfte aus
      Kirgisistan mit deutschen Unternehmen, um gemeinsam die Herausforderungen
      des Fachkräftemangels zu bewältigen. Mit unserer Expertise und unserem
      Engagement für exzellenten Service setzen wir neue Maßstäbe in der
      Vermittlung von temporären und langfristigen Arbeitsplätzen sowie
      Ausbildungsplätzen.
    </p>

    <!-- Карточки услуг -->
    <div class="cards-container">
      <div
        class="service-card"
        v-for="(card, index) in cards"
        :key="index"
        @mouseover="hover = index"
        @mouseleave="hover = null"
        :class="{ 'card-hover': hover === index }"
      >
        <img :src="card.icon" :alt="card.title" class="card-icon" />
        <h2 class="card-title">{{ card.title }}</h2>
        <p class="card-description">
          {{ card.description }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

// Состояние для анимации при наведении
const hover = ref<number | null>(null);

// Данные карточек
const cards = [
  {
    icon: require("@/assets/icon1.svg"),
    title: "Studenten für Saisonarbeit",
    description:
      "Wir vermitteln Studenten für temporäre Stellen in Bereichen wie Produktion, Gastronomie, Hotellerie und Reinigung – ideal für Unternehmen mit saisonalem Personalbedarf.",
  },
  {
    icon: require("@/assets/icon2.svg"),
    title: "Zertifizierte Fachkräfte:",
    description:
      "Stellen Sie bei uns Fachkräfte mit höherer Ausbildung ein, um ein hohes Maß an Fachkompetenz und Professionalität in Ihrem Unternehmen sicherzustellen.",
  },
  {
    icon: require("@/assets/icon3.svg"),
    title: "Ausbildung:",
    description:
      "Die Ausbildung ist ein deutsches Berufsausbildungsprogramm, das den Studierenden praktische Fähigkeiten und Kenntnisse in einem bestimmten Beruf vermittelt.",
  },
  {
    icon: require("@/assets/icon4.svg"),
    title: "Kurzzeitige Beschäftigung:",
    description:
      "Wir stellen Arbeitskräfte für kurzfristige Verträge (bis zu 8 Monate) in den genannten Bereichen – ideal für Projekte oder saisonale Spitzen.",
  },
];
</script>

<style scoped lang="scss">
.container {
  text-align: center;
  margin-top: 120px;
}

.section-title {
  width: 100%;
  display: flex;
  justify-content: center;
  margin-bottom: 30px;
  span {
    color: #333333;
    font-size: 48px;
    font-weight: 700;
    font-family: "Epilogue", sans-serif;
  }
}

.section-description {
  color: #515151;
  font-size: 17px;
  font-weight: 400;
  font-family: "Open Sans", sans-serif;
  max-width: 800px;
  margin: 0 auto 50px;
  line-height: 1.6;
}

/* Стили для карточек */
.cards-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  max-width: 1000px;
  margin: 0 auto;
}

.service-card {
  background-color: #ffffff;
  width: calc(50% - 100px); /* Две карточки в ряду с отступами */
  margin-bottom: 40px;
  padding: 20px;
  box-sizing: border-box;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.12);
  cursor: pointer;
}

.service-card:hover {
  transform: translateY(-10px);
}

.card-icon {
  width: 60px;
  height: 71px;
  margin-bottom: 20px;
  object-fit: contain;
}

.card-title {
  font-size: 22px;
  font-weight: 700;
  font-family: "Epilogue", sans-serif;
  color: #333333;
  margin-bottom: 10px;
}

.card-description {
  font-size: 20px;
  font-weight: 400;
  font-family: "Open Sans", sans-serif;
  color: #515151;
  flex-grow: 1;
  text-align: start;
}

/* Обеспечиваем одинаковую высоту карточек */
.service-card {
  min-height: 400px; /* Установите нужную минимальную высоту */
}

/* Адаптивность для мобильных устройств */
@media (max-width: 767px) {
  .service-card {
    width: 100%;
  }
}
</style>
