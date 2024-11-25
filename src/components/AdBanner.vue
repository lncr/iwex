<template>
  <div class="ad-banner">
    <div class="overlay">
      <div class="content">
        <h1 class="headline">
          {{ $t("banner.title.part1") }} <br />
          <span
            ><span class="highlight">{{ $t("banner.title.highlight") }}</span>
            {{ $t("banner.title.part2") }}
          </span>
          <br />
          {{ $t("banner.title.part3") }}
        </h1>
        <p class="subheadline" v-html="$t('banner.description')"></p>
        <v-btn class="cta-button" @click="navigateToContact">
          {{ $t("button") }}
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();

function navigateToContact() {
  router.push("/contact"); // Переход на страницу контактов
}
</script>

<style scoped lang="scss">
.ad-banner {
  position: relative;
  background-image: url("@/assets/background.jpg"); /* Замените на ваш путь к изображению */
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  width: 100vw; /* Устанавливаем ширину в 100% от ширины окна */
  margin-left: calc(
    50% - 50vw
  ); /* Сдвигаем контейнер влево на половину лишней ширины */
  height: 660px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 120px;

  .overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;

    .content {
      max-width: 1200px;
      width: 100%;
      padding: 20px;
      text-align: center;
      color: #ffffff;

      .headline {
        font-size: 48px;
        font-weight: 700;
        margin-top: 100px;
        margin-bottom: 50px;
        font-family: "Epilogue", sans-serif;

        .highlight {
          color: rgba(254, 202, 0, 1);
        }
      }

      .subheadline {
        font-size: 17px;
        margin-bottom: 50px;
        font-weight: 400;
        font-family: "Open Sans", sans-serif;
      }

      .cta-button {
        background-color: rgba(254, 202, 0, 1);
        color: #000000;
        font-weight: 700;
        border-radius: 8px;
        height: 62px;
        width: 270px;
        text-transform: none;
        margin-bottom: 100px;
      }
    }
  }
}

/* Планшеты и ноутбуки */
@media (max-width: 960px) {
  .ad-banner {
    height: 500px; /* Уменьшаем высоту баннера */
    margin-top: 80px; /* Уменьшаем верхний отступ */

    .overlay {
      .content {
        .headline {
          font-size: 36px; /* Уменьшаем размер шрифта заголовка */
          margin-top: 60px; /* Уменьшаем верхний отступ заголовка */
          margin-bottom: 30px; /* Уменьшаем нижний отступ заголовка */
        }
        .subheadline {
          font-size: 15px; /* Уменьшаем размер шрифта подзаголовка */
          margin-bottom: 30px; /* Уменьшаем нижний отступ подзаголовка */
        }
        .cta-button {
          height: 50px;
          width: 220px;
          margin-bottom: 80px;
        }
      }
    }
  }
}

/* Мобильные устройства */
@media (max-width: 600px) {
  .ad-banner {
    height: 400px; /* Еще больше уменьшаем высоту баннера */
    margin-top: 60px; /* Уменьшаем верхний отступ */
    width: 100%; /* Устанавливаем ширину в 100% */
    margin-left: 0; /* Убираем смещение */

    .overlay {
      .content {
        padding: 15px;
        .headline {
          font-size: 28px; /* Уменьшаем размер шрифта заголовка */
          margin-top: 40px; /* Уменьшаем верхний отступ заголовка */
          margin-bottom: 20px; /* Уменьшаем нижний отступ заголовка */
        }
        .subheadline {
          font-size: 13px; /* Уменьшаем размер шрифта подзаголовка */
          margin-bottom: 20px; /* Уменьшаем нижний отступ подзаголовка */
        }
        .cta-button {
          height: 45px;
          width: 200px;
          margin-bottom: 60px;
        }
      }
    }
  }
}
</style>
