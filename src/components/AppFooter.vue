<template>
  <v-footer padless class="footer-block">
    <!-- Фон на всю ширину экрана -->
    <div class="footer-container">
      <div class="left">
        <!-- Левая колонка: Логотип -->
        <div class="logo">
          <img :src="logo" alt="Firmenlogo" />
          <span>IWEX</span>
        </div>

        <!-- Центральная колонка: Контактная информация -->
        <div class="numbers">
          <span class="title"
            ><v-icon>mdi-phone-outline</v-icon>{{ $t("footer.contact") }}</span
          >
          <p>{{ $t("footer.tel") }}: 069-870033755</p>
          <p>{{ $t("footer.mob") }}: 0179-2078900</p>
          <p class="email">
            <a href="mailto:info@iwex-personal.de">info@iwex-personal.de</a>
          </p>
          <p class="firma">IWEX Germany GmbH</p>
        </div>

        <!-- Правая колонка: Социальные сети -->
        <div class="links">
          <span class="title"
            ><v-icon>mdi-web</v-icon> {{ $t("footer.link") }}:</span
          >
          <a
            icon
            href="https://www.linkedin.com/company/iwex-germany-gmbh/"
            target="_blank"
          >
            <v-icon class="icon">mdi-linkedin</v-icon>
            Linkedin
          </a>
          <a
            icon
            href="https://www.instagram.com/iwex.germany.gmbh/profilecard/?igsh=MXFnMnZkc29lYmFxOQ=="
            target="_blank"
          >
            <v-icon class="icon">mdi-instagram</v-icon>
            Instagram
          </a>
          <a
            icon
            href="https://www.xing.com/pages/iwex-germany-gmbh"
            target="_blank"
          >
            <img width="24" class="icon" :src="xing" />
            Xing
          </a>
        </div>

        <div class="address">
          <span class="title"
            ><v-icon>mdi-map-marker-outline</v-icon>
            {{ $t("footer.adresse") }}:</span
          >
          <p>IWEX Germany GmbH</p>
          <p class="street">Hahnstraße 70</p>
          <p>60528 Frankfurt am Main</p>
          <iframe
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2625.337218675491!2d8.645756815674943!3d50.08273577942562!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47bce7eb80000001%3A0x6e3b4c5d8d8b8d8!2sHahnstra%C3%9Fe%2070%2C%2060528%20Frankfurt%20am%20Main%2C%20Germany!5e0!3m2!1sen!2sde!4v1600000000000!5m2!1sen!2sde"
            width="100%"
            height="100%"
            frameborder="0"
            allowfullscreen=""
            aria-hidden="false"
            tabindex="0"
            class="frame"
          ></iframe>
        </div>
      </div>

      <!-- Нижняя строка футера -->
      <div class="footer-bottom">
        <p>
          © IWEX 2024. Registry court: AG Frankfurt am Main, HRB 128023
          <span class="footer-links">
            <router-link to="/impressum">Impressum</router-link>
            <router-link to="/datenschutzerklaerung"
              >Datenschutzerklärung</router-link
            >
          </span>
        </p>
      </div>
    </div>
  </v-footer>
</template>

<script setup>
import logo from "../assets/contact-logo.svg";
import xing from "../assets/xing.svg";
// Импорт компонентов и иконок
</script>

<style scoped lang="scss">
.footer-block {
  width: 100vw;
  margin-left: calc(50% - 50vw);
  background-color: rgba(51, 51, 51, 1);
  padding-top: 60px;
  padding-bottom: 40px;
}

.footer-container {
  width: 100%;
  padding: 0 16px;

  .left {
    display: flex;
    justify-content: space-between;
    align-items: center;
    .logo {
      display: flex;
      align-items: center;
      gap: 24px;
      img {
        width: 180px;
      }
      span {
        font-size: 72px;
        color: #ffffff;
        font-weight: 700;
      }
    }
    .numbers {
      display: flex;
      flex-direction: column;
      align-self: flex-start;
      p {
        color: rgba(214, 221, 235, 1);
        font-size: 16px;
      }
      .email {
        margin-top: 30px;
        a {
          color: rgba(214, 221, 235, 1);
          text-decoration: none;
        }
      }
      .firma {
        margin-top: 40px;
      }
    }
    .links {
      display: flex;
      flex-direction: column;
      align-self: flex-start;
      a {
        display: flex;
        align-items: center;
        gap: 8px;
        text-decoration: none;
        color: rgba(214, 221, 235, 1);
        margin-top: 8px;
        .icon {
          width: 24px !important;
          color: rgba(255, 204, 1, 1);
        }
      }
    }
    .address {
      display: flex;
      flex-direction: column;
      align-self: flex-start;
      p {
        color: rgba(214, 221, 235, 1);
      }
      .street {
        margin-top: 20px;
      }
      .frame {
        margin-top: 20px;
      }
    }
  }
}

.address-map-block {
  flex-direction: column;
  align-items: center;
}

.footer-bottom {
  display: flex;
  padding: 16px 0;
  text-align: center;
  p {
    font-size: 16px;
    font-family: Epilogue;
    color: #afafaf;
    font-weight: 500;
  }
  .footer-links {
    margin-left: 16px;
  }

  .footer-links a {
    color: rgba(214, 221, 235, 1);
    text-decoration: none;
    margin-left: 40px;
  }
}

.title {
  font-size: 18px;
  color: rgba(255, 203, 0, 1);
  align-items: center;
  display: flex;
  gap: 8px;
  margin-bottom: 10px;

  i {
    font-size: 23px;
  }
}
</style>
