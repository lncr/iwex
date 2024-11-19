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
        <!-- Все три изображения -->
        <img :src="mainImage" alt="Main Image" class="gallery-image" />
        <img :src="sideImage1" alt="Side Image 1" class="gallery-image" />
        <img :src="sideImage2" alt="Side Image 2" class="gallery-image" />
      </div>
    </div>

    <!-- Кнопка под галереей -->
    <div class="slider-button">
      <v-btn class="btn-center">{{ $t("button") }}</v-btn>
    </div>
  </div>
</template>

<script setup lang="ts">
import api from "@/plugins/api";
import { onMounted, ref, watch } from "vue";
import { useI18n } from "vue-i18n";

// Импортируем изображения
import mainImage from "@/assets/photo1.png";
import sideImage1 from "@/assets/photo2.png";
import sideImage2 from "@/assets/photo3.png";

const { locale } = useI18n();
const industries = ref<Array<any>>([]);

function getIconUrl(iconPath: string) {
  if (iconPath.startsWith("http")) {
    return iconPath;
  }
  const baseUrl = process.env.VUE_APP_BASE_URL || "http://159.223.21.167";
  return `${baseUrl}${iconPath}`;
}

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

watch(locale, (newLocale) => {
  loadIndustries(newLocale);
});

onMounted(() => {
  loadIndustries(locale.value);
});
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
    p {
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
  margin-bottom: 40px; /* Добавляем отступ снизу */
}

.gallery-images {
  display: flex;
  gap: 24px;
  justify-content: center; /* Центруем галерею */
}

.main-image {
  max-width: 600px;
  width: 100%;
  max-height: 475px;
  border-radius: 30px;
}

.side-images {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.side-image {
  max-width: 315px;
  width: 100%;
  height: auto;
  border-radius: 10px;
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
