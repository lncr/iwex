<template>
  <div class="container">
    <!-- Заголовок и круг с текстом -->
    <div class="section-header">
      <span class="section-title" v-html="$t('industry.title')"></span>
      <div class="circle-text">
        <span class="two">
          <p>200</p>
          <span v-html="$t('industry.circle')"></span>
        </span>
      </div>
    </div>

    <!-- Иконки с описаниями -->
    <div class="industries">
      <div
        class="industry-item"
        v-for="industry in industries"
        :key="industry.id"
      >
        <img
          :src="getIconUrl(industry.icon)"
          :alt="industry.name"
          class="industry-icon"
        />
        <p class="industry-name">{{ industry.name }}</p>
      </div>
    </div>

    <!-- Галерея изображений -->
    <div class="gallery-section">
      <div class="gallery-images">
        <!-- Главная картинка -->
        <img
          :src="mainImage"
          alt="Main Image"
          class="gallery-image main-image"
        />
        <!-- Боковые картинки -->
        <img
          :src="sideImage1"
          alt="Side Image 1"
          class="gallery-image side-image"
        />
        <img
          :src="sideImage2"
          alt="Side Image 2"
          class="gallery-image side-image"
        />
      </div>
    </div>

    <!-- Кнопка под галереей -->
    <div class="slider-button">
      <v-btn
        color="rgba(254, 202, 0, 1)"
        @click="navigateToContact"
        class="btn-center"
      >
        {{ $t("button") }}
      </v-btn>
    </div>
  </div>
</template>

<script setup lang="ts">
import api from "@/plugins/api";
import { onMounted, ref, watch } from "vue";
import { useI18n } from "vue-i18n";
import mainImage from "@/assets/photo1.png";
import sideImage1 from "@/assets/photo2.png";
import sideImage2 from "@/assets/photo3.png";
import { useRouter } from "vue-router";

const { locale } = useI18n();
const industries = ref<Array<any>>([]);
const router = useRouter();

// Функция для получения полного URL иконки
function getIconUrl(iconPath: string) {
  if (iconPath.startsWith("http")) {
    return iconPath;
  }
  const baseUrl = process.env.VUE_APP_BASE_URL || "http://159.223.21.167";
  return `${baseUrl}${iconPath}`;
}

// Функция для загрузки индустрий
async function loadIndustries(language: string) {
  try {
    const response = await api.get("/api/v1/workareas/", {
      params: {
        lng: language,
      },
    });
    industries.value = response.data;
  } catch (error) {
    console.error("Ошибка при загрузке данных индустрий:", error);
  }
}

// Обработчик клика по кнопке
function navigateToContact() {
  router.push("/contact"); // Переход на страницу контактов
}

// Загрузка данных при монтировании компонента
onMounted(() => {
  loadIndustries(locale.value);
});

// Обновление данных при смене языка
watch(locale, (newLocale) => {
  loadIndustries(newLocale);
});
</script>

<style scoped lang="scss">
.container {
  text-align: center;
  margin-top: 120px;
  padding: 0 20px; /* Отступы по бокам для мобильных устройств */
}

/* Заголовок и круг с текстом */
.section-header {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 40px; /* Увеличенный отступ между заголовком и кругом */
  flex-wrap: wrap; /* Позволяет элементам переноситься на новую строку при необходимости */

  .section-title {
    font-size: 48px;
    font-weight: 700;
    font-family: "Epilogue", sans-serif;
    color: #ffcb00;
    text-align: center;
  }

  .circle-text {
    position: absolute;
    top: -70px;
    right: -20px;
    width: 221px;
    height: 221px;
    background-color: #feca00;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    box-sizing: border-box;

    .two {
      transform: rotate(20deg);
      color: #333333;
      font-family: "Epilogue", sans-serif;
      font-weight: 700;
      font-size: 15px;
      text-align: center;

      p {
        font-size: 72px;
        margin: 0;
      }
    }
  }
}

/* Иконки с описаниями */
.industries {
  display: flex;
  justify-content: center; /* Центрируем блок */
  margin-top: 40px;
  margin-bottom: 60px;
  gap: 10px; /* Уменьшили gap для ближе расположения элементов */

  .industry-item {
    text-align: center;
    flex: 0 0 15%; /* 5 элементов в ряду: примерно 18% каждый с учетом gap */
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

/* Галерея изображений */
.gallery-section {
  position: relative;
  margin-bottom: 40px;
}

.gallery-images {
  display: flex;
  gap: 24px;
  justify-content: center;
  align-items: stretch; /* Выровнять по высоте */
  flex-wrap: nowrap; /* Предотвращаем перенос элементов */
}

.gallery-image {
  border-radius: 30px;
  height: 100%; /* Равная высота */
  object-fit: cover; /* Заполнение без искажения */
}

.main-image {
  flex: 0 1 50%; /* Главная картинка занимает 50% ширины */
  max-width: 600px;
  height: auto; /* Автоматическая высота */
}

.side-image {
  flex: 0 1 25%; /* Каждая боковая картинка занимает 25% ширины */
  max-width: 315px;
  height: auto; /* Автоматическая высота */
}

/* Адаптивные стили */

/* Планшеты и меньшие экраны (до 960px) */
@media (max-width: 960px) {
  /* Галерея изображений */
  .gallery-images {
    flex-direction: column;
    align-items: center;
    flex-wrap: wrap;
  }

  .main-image,
  .side-image {
    width: 80%;
    max-width: none;
    height: auto;
  }

  /* Заголовок и круг с текстом */
  .section-header {
    flex-direction: column;
    gap: 20px; /* Уменьшенный отступ */
    .circle-text {
      display: none;
    }
  }

  /* Иконки с описаниями */
  .industries {
    justify-content: center;

    .industry-item {
      flex: 0 0 18%; /* Сохраняем 5 элементов в ряду */
      margin: 1%;
    }
  }
}

/* Мобильные устройства (до 600px) */
@media (max-width: 600px) {
  /* Галерея изображений */
  .gallery-images {
    flex-direction: column;
    align-items: center;
  }

  .main-image,
  .side-image {
    width: 100%;
    max-width: none;
  }

  /* Скрываем круг с текстом */
  .circle-text {
    display: none;
  }

  /* Иконки с описаниями */
  .industries {
    flex-wrap: nowrap;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    justify-content: center; /* Центрируем элементы */

    .industry-item {
      flex: 0 0 18%;
      margin: 1%;
    }

    .industry-icon {
      max-width: 60px;
    }

    .industry-name {
      font-size: 14px;
    }
  }

  /* Заголовок */
  .section-title {
    font-size: 32px;
  }

  /* Описание */
  .section-description {
    font-size: 15px;
  }

  /* Кнопка */
  .btn-center {
    width: 100%;
    max-width: 300px;
    border-radius: 8px;
  }
}
</style>
