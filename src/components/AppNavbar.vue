<template>
  <v-app-bar app fixed color="#333333" dark>
    <!-- Обёртка контента Navbar -->
    <div class="navbar-content">
      <!-- Логотип -->
      <div class="logo" @click="navigateToHome">
        <img
          :src="logoImage"
          alt="Logo"
          style="max-height: 40px; max-width: 150px"
        />
      </div>

      <!-- Навигационные ссылки для десктопа -->
      <div class="nav-links-container d-none d-md-flex">
        <div class="nav-links">
          <v-btn
            variant="text"
            @click="scrollToSection('services')"
            class="nav-link"
          >
            {{ t("navigation.services") }}
          </v-btn>
          <v-btn
            variant="text"
            @click="scrollToSection('about-us')"
            class="nav-link"
          >
            {{ t("navigation.aboutUs") }}
          </v-btn>
          <!-- Кнопка "Kontaktieren Sie uns" -->
          <v-btn @click="navigateToContact" class="nav-button">
            {{ t("navigation.contactUs") }}
          </v-btn>
        </div>
      </div>

      <!-- Правые элементы: Переключатель языка и бургер-меню -->
      <div class="right-items">
        <!-- Переключатель языка -->
        <v-menu offset-y>
          <template v-slot:activator="{ props }">
            <v-btn v-bind="props" class="language-btn">
              <v-avatar size="24">
                <v-img :src="currentLanguage?.flag"></v-img>
              </v-avatar>
            </v-btn>
          </template>
          <v-list>
            <v-list-item
              v-for="(lang, index) in languages"
              :key="index"
              @click="changeLanguage(lang)"
            >
              <v-list-item-avatar>
                <v-img :src="lang.flag"></v-img>
              </v-list-item-avatar>
              <v-list-item-title>{{ lang.name }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>

        <!-- Бургер-меню для мобильных устройств -->
        <v-app-bar-nav-icon
          @click="drawer = !drawer"
          class="d-md-none"
        ></v-app-bar-nav-icon>
      </div>
    </div>
  </v-app-bar>

  <!-- Навигационный ящик для мобильных устройств -->
  <v-navigation-drawer v-model="drawer" app temporary class="d-md-none">
    <v-list dense>
      <!-- Навигационные ссылки -->
      <v-list-item
        v-for="(item, index) in mobileNavItems"
        :key="index"
        @click="handleMobileNavigation(item.path, item.sectionId)"
      >
        <v-list-item-title>{{ t(item.labelKey) }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script setup lang="ts">
import { ref, watch, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useI18n } from "vue-i18n";
import germanyFlag from "@/assets/germany-flag.png";
import usaFlag from "@/assets/usa-flag.png";
import logoImage from "@/assets/logo.png";

// Маршрутизатор
const router = useRouter();

// i18n
const { locale, t } = useI18n();

// Состояние навигационного ящика
const drawer = ref(false);

// Для мобильных устройств, включаем "Kontaktieren Sie uns"
const mobileNavItems = [
  { labelKey: "navigation.services", path: "/unsere-dienstleistungen" },
  { labelKey: "navigation.aboutUs", path: "#about-us", sectionId: "about-us" },
  { labelKey: "navigation.contactUs", path: "/kontaktieren-sie-uns" },
];

// Настройки языка
const languages = [
  {
    code: "deu",
    name: "Deutsch",
    flag: germanyFlag,
  },
  {
    code: "eng",
    name: "English",
    flag: usaFlag,
  },
];

// Текущий язык
const currentLanguage = ref(
  languages.find((lang) => lang.code === locale.value) || languages[0]
);

// Установка локали из localStorage при загрузке компонента
onMounted(() => {
  const savedLocale = localStorage.getItem("locale");
  if (savedLocale) {
    locale.value = savedLocale;
    currentLanguage.value =
      languages.find((lang) => lang.code === savedLocale) || languages[0];
  }
});

// Отслеживание изменения локали
watch(locale, (newLocale) => {
  currentLanguage.value =
    languages.find((lang) => lang.code === newLocale) || languages[0];
});

// Функция смены языка
function changeLanguage(lang: any) {
  locale.value = lang.code;
  localStorage.setItem("locale", lang.code);
}

function scrollToSection(sectionId: string) {
  const section = document.getElementById(sectionId);
  if (section) {
    section.scrollIntoView({
      behavior: "smooth", // Плавная прокрутка
      block: "start", // Прокрутка к началу блока
    });
  }
}
function handleMobileNavigation(path: any, sectionId?: string) {
  drawer.value = false; // Закрываем бургер-меню
  if (sectionId) {
    scrollToSection(sectionId); // Прокручиваем к секции
  } else {
    router.push(path).then(() => {
      window.scrollTo({
        top: 0,
        behavior: "smooth", // Плавная прокрутка
      });
    });
  }
}

function navigateToHome() {
  router.push("/").then(() => {
    window.scrollTo({
      top: 0,
      behavior: "smooth", // Плавная прокрутка
    });
  });
}
function navigateToContact() {
  router.push("/contact"); // Переход на главную страницу
}
</script>

<style scoped lang="scss">
.navbar-content {
  display: flex;
  align-items: center;
  width: 100%;
  max-width: 1440px;
  margin: 0 auto;
}
.logo {
  cursor: pointer;
}
.nav-links-container {
  flex: 1;
  display: flex;
  justify-content: center;
}

.nav-links {
  display: flex;
  align-items: center;
}

.right-items {
  display: flex;
  align-items: center;
}

.nav-link {
  color: #afafaf;
  margin: 0 8px;
  text-transform: none;
}

.nav-link:hover {
  color: #ffffff !important;
}

.nav-button {
  margin-left: 16px;
  background-color: #feca00;
  color: #383838;
  text-transform: none;
}

.language-btn {
  margin-left: 16px;
}

.v-list-item {
  display: flex;
  .v-list-item__content {
    display: flex;
    .v-img {
      width: 20px;
    }
    .v-list-item-title {
      color: #383838;
    }
  }
}

/* Обеспечить корректное отображение переключателя языка на мобильных устройствах */
@media (max-width: 960px) {
  .language-btn {
    margin-left: 8px;
  }
}
</style>
