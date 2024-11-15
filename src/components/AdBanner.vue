<template>
  <div class="ad-banner">
    <div class="overlay">
      <div class="content">
        <h1 class="headline">
          Kontaktieren Sie jetzt IWEX - Ihren <br />
          <span class="highlight">verlässlichen Personalvermittler</span>
          aus <br />Kirgisistan
        </h1>
        <p class="subheadline">
          Schreiben Sie uns eine E-Mail. Wir melden uns <br />umgehend mit einem
          Angebot bei Ihnen zurück.
        </p>
        <v-btn class="cta-button" @click="onButtonClick">
          Jetzt Personal anfragen
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

// Обработчик клика по кнопке
function onButtonClick() {
  // Здесь вы можете добавить логику, например, перенаправление на страницу контактов
  // Например:
  // this.$router.push('/contact');
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
  height: 660px; /* Вы можете настроить высоту по своему усмотрению */
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
    background-color: rgba(0, 0, 0, 0.5); /* Затемнение фона */
    display: flex;
    align-items: center;
    justify-content: center;

    .content {
      max-width: 1200px; /* Ограничиваем ширину контента для больших экранов */
      width: 100%;
      padding: 20px;
      text-align: center;
      color: #ffffff;

      .headline {
        font-size: 48px;
        font-weight: 700;
        margin-top: 100px;
        margin-bottom: 50px;
        font-family: Epilogue;

        .highlight {
          color: rgba(254, 202, 0, 1); /* Ярко-желтый цвет */
        }
      }

      .subheadline {
        font-size: 17px;
        margin-bottom: 50px;
        font-weight: 400;
        font-family: Open Sans;
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
</style>
