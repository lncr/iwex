<template>
  <div class="container" id="services">
    <!-- Заголовок -->
    <div class="section-title">
      <span v-html="$t('services.title')"></span>
    </div>

    <!-- Описание -->
    <p class="section-description">
      {{ $t("services.description") }}
    </p>

    <!-- Карточки услуг -->
    <div class="cards-container">
      <div class="service-card" v-for="(card, index) in cards" :key="card.id">
        <div
          class="card-inner"
          @mouseenter="handleMouseEnter(index)"
          @mouseleave="handleMouseLeave(index)"
          @click="toggleFlip(index)"
          :class="{
            'is-flipped': hoverIndex === index || flipped.has(index),
          }"
        >
          <!-- Передняя сторона карточки -->
          <div class="card-front">
            <img
              :src="getIconUrl(card.icon)"
              :alt="card.title"
              class="card-icon"
            />
            <h2 class="card-title">{{ card.title }}</h2>
            <p class="card-description">
              {{ card.text }}
            </p>
          </div>
          <!-- Задняя сторона карточки -->
          <div
            class="card-back"
            :style="{ backgroundImage: `url(${getIconUrl(card.thumbnail)})` }"
          >
            <div class="card-back-content">
              <img
                :src="getIconUrl(card.icon)"
                :alt="card.title"
                class="card-icon"
              />
              <h2 class="card-back-title">{{ card.title }}</h2>
              <p class="card-description">
                {{ card.additionalText }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import api from "@/plugins/api";
import { ref, onMounted, watch } from "vue";
import { useI18n } from "vue-i18n";

// Состояние для наведения
const hoverIndex = ref<number | null>(null);

// Состояние для перевёрнутых карточек
const flipped = ref<Set<number>>(new Set());

// Состояние для карточек
const cards = ref<Array<any>>([]);

// i18n
const { locale } = useI18n();

// Функция для получения полного URL иконки
function getIconUrl(iconPath: string) {
  if (iconPath.startsWith("http")) {
    return iconPath;
  }
  const baseUrl = process.env.VUE_APP_BASE_URL || "https://iwex-germany.de/";
  return `${baseUrl}${iconPath}`;
}

// Функция для загрузки карточек
async function loadCards(language: string) {
  try {
    const response = await api.get("/api/v1/cards/", {
      params: {
        lng: language,
      },
    });
    cards.value = response.data;
  } catch (error) {
    console.error("Ошибка при загрузке данных:", error);
  }
}

// Получаем данные с API при монтировании компонента
onMounted(() => {
  loadCards(locale.value);
});

// Обновляем данные при смене языка
watch(locale, (newLocale) => {
  loadCards(newLocale);
});

// Функция для переключения переворота карточки по клику
function toggleFlip(index: number) {
  if (flipped.value.has(index)) {
    flipped.value.delete(index);
  } else {
    flipped.value.add(index);
  }
  // Обновляем реактивность
  flipped.value = new Set(flipped.value);
}

// Функции для обработки наведения
function handleMouseEnter(index: number) {
  // Только для устройств с поддержкой наведения
  if (window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
    hoverIndex.value = index;
  }
}

function handleMouseLeave(index: number) {
  // Только для устройств с поддержкой наведения
  if (window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
    hoverIndex.value = null;
  }
}
</script>

<style scoped lang="scss">
.container {
  text-align: center;
  margin-top: 120px;
  padding: 0 20px; /* Добавим отступы по бокам для мобильных устройств */
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
  max-width: 1100px;
  margin: 0 auto;
}

.service-card {
  width: calc(50% - 20px); /* Максимум две карточки в ряду */
  margin-bottom: 40px;
  perspective: 1000px;
}

/* Адаптивность для планшетов */
@media (max-width: 960px) {
  .service-card {
    width: 100%; /* Одна карточка в ряду */
  }
  .card-inner.is-flipped {
    transform: rotateY(180deg);
  }
}

/* Адаптивность для мобильных устройств */
@media (max-width: 600px) {
  .container {
    margin-top: 80px;
  }
  .section-title span {
    font-size: 26px;
  }

  .section-description {
    font-size: 16px;
  }

  .card-title {
    font-size: 20px;
  }

  .card-description {
    font-size: 16px;
  }

  .card-back-content .card-back-title {
    font-size: 24px;
  }
  .card-back {
    display: none;
  }
  .card-inner.is-flipped .card-back {
    display: flex;
  }
  .card-front {
    background-color: #ffffff;
    padding: 15px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    z-index: 2;
    .card-icon {
      width: 40px;
      height: 40px;
      margin-bottom: 20px;
      object-fit: contain;
    }
    .card-title {
      font-size: 18px;
    }
    .card-description {
      font-size: 16px;
    }
  }
}

.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  min-height: 400px;
  text-align: left;
  transition: transform 0.8s ease-in-out; /* Увеличена продолжительность и плавность */
  transform-style: preserve-3d;
  /* Сбрасываем трансформацию по умолчанию */
  transform: rotateY(0deg);
}

.card-inner.is-flipped {
  transform: rotateY(180deg);
}

.card-front,
.card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.12);
}

.card-front {
  background-color: #ffffff;
  padding: 40px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  z-index: 2;
}

.card-back {
  background-size: cover;
  background-position: center;
  transform: rotateY(180deg);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1;
}

.card-back::before {
  content: "";
  background: rgba(0, 0, 0, 0.3); /* Тёмный оверлей для контраста текста */
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.card-back-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px;
  z-index: 1;
  .card-back-title {
    font-size: 40px;
    font-weight: 700;
    font-family: "Epilogue", sans-serif;
    color: #ffffff;
    margin-bottom: 10px;
    text-align: center;
  }
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

.card-back .card-title,
.card-back .card-description {
  color: #ffffff;
  text-align: center;
}

/* Отключаем переворот на устройствах без поддержки наведения */
@media (hover: none) and (pointer: coarse) {
  .card-inner.is-flipped {
    transform: rotateY(180deg);
  }
  .card-inner {
    transform: rotateY(0deg);
  }
  .card-front,
  .card-back {
    backface-visibility: hidden;
  }
}
</style>
