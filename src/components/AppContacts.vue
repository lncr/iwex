<template>
  <div class="contact-us-block">
    <div class="contacts">
      <!-- Текстовый блок -->
      <div class="contact-left">
        <span class="title" v-html="$t('contacts.title')"></span>
        <span class="subtitle">
          {{ $t("contacts.subtitle") }}
        </span>
        <v-btn @click="navigateToContact" class="btn">{{ $t("button") }}</v-btn>
      </div>

      <!-- Блок с изображением -->
      <div class="contact-right">
        <v-img
          src="../assets/contact-logo.svg"
          alt="Firmenlogo"
          width="350"
        ></v-img>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();
// Обработчик клика по кнопке
function navigateToContact() {
  router.push("/contact"); // Переход на страницу контактов
}
</script>

<style scoped lang="scss">
.contact-us-block {
  position: relative;
  color: white;
  background-image: url("../assets/contacts.jpg");
  background-size: cover;
  background-position: center;
  width: 100vw;
  height: 670px;
  margin-left: calc(50% - 50vw);
  margin-top: 120px;
}

.contact-us-block::before {
  content: "";
  background: rgba(0, 0, 0, 0.3); /* Тёмный оверлей для контраста текста */
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.contacts {
  display: flex;
  justify-content: space-between;
  padding: 150px 100px;
  align-items: center;

  .contact-left {
    z-index: 1;
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 30%;

    .title {
      color: #ffffff;
      font-size: 60px;
      font-family: Epilogue;
      font-weight: 700;
    }
    .subtitle {
      color: rgba(222, 222, 222, 1);
      font-size: 17px;
    }

    .btn {
      background-color: rgba(254, 202, 0, 1);
      color: rgba(51, 51, 51, 1);
      text-transform: none;
      margin-top: 80px;
      width: 270px;
      height: 50px;
      font-size: 17px;
      border-radius: 8px;
    }
  }

  .contact-right {
    z-index: 1;
  }
}

h1 {
  font-size: 48px;
  font-weight: bold;
}

h4 {
  font-size: 24px;
  margin-top: 16px;
}

/* Адаптивность для планшетов и ноутбуков */
@media (max-width: 960px) {
  .contact-us-block {
    height: 600px;
    margin-top: 100px;
  }

  .contacts {
    padding: 100px 50px;

    .contact-left {
      max-width: 100%;
      .title {
        font-size: 48px;
      }
      .subtitle {
        font-size: 16px;
      }
      .btn {
        margin-top: 60px;
        width: 220px;
        height: 45px;
        font-size: 16px;
      }
    }

    .contact-right {
      display: none; /* Скрываем правый блок на планшетах */
    }
  }
}

/* Адаптивность для мобильных устройств */
@media (max-width: 600px) {
  .contact-us-block {
    height: auto;
    margin-top: 80px;
    width: 100%;
    margin-left: 0;
  }

  .contacts {
    flex-direction: column;
    padding: 50px 20px;
    text-align: center;

    .contact-left {
      max-width: 100%;
      align-items: center;

      .title {
        font-size: 36px;
      }
      .subtitle {
        font-size: 14px;
      }
      .btn {
        margin-top: 40px;
        width: 200px;
        height: 40px;
        font-size: 14px;
      }
    }

    .contact-right {
      display: none; /* Скрываем правый блок на мобильных устройствах */
    }
  }
}
</style>
