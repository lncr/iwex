<template>
  <v-app-bar app fixed color="#333333" dark>
    <!-- Обёртка контента Navbar -->
    <v-container fluid class="navbar-container">
      <v-row align="center" justify="space-between" no-gutters>
        <!-- Логотип -->
        <v-col cols="auto">
          <div class="logo" @click="navigateToHome">
            <img :src="logoImage" alt="Logo" class="logo-img" />
          </div>
        </v-col>

        <!-- Навигационные ссылки для планшетов и десктопов -->
        <v-col class="d-none d-sm-flex" cols="auto">
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
        </v-col>

        <!-- Правые элементы: Переключатель языка и бургер-меню -->
        <v-col cols="auto">
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
              class="d-sm-none"
            ></v-app-bar-nav-icon>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-app-bar>

  <!-- Навигационный ящик для мобильных устройств -->
  <v-navigation-drawer v-model="drawer" app temporary class="d-sm-none">
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

// Для мобильных устройств, включаем "Contact Us"
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
  router.push("/contact"); // Переход на страницу контактов
}
</script>

<style scoped lang="scss">
.navbar-container {
  max-width: 1440px;
  margin: 0 auto;
}

.logo {
  cursor: pointer;

  img {
    max-height: 40px;
    max-width: 150px;
  }
}

.nav-links {
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

.right-items {
  display: flex;
  align-items: center;
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

/* Адаптивные стили */
@media (max-width: 600px) {
  .language-btn,
  .nav-button {
    margin-left: 8px;
  }

  .logo img {
    max-height: 30px;
    max-width: 120px;
  }
}
</style>
