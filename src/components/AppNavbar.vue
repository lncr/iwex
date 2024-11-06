<template>
  <v-app-bar app fixed color="#333333" dark>
    <!-- Логотип -->
    <div class="logo">
      <img
        :src="logoImage"
        alt="Logo"
        style="max-height: 40px; max-width: 150px"
      />
    </div>

    <!-- Spacer для выравнивания -->
    <v-spacer></v-spacer>

    <!-- Бургер-меню для мобильных устройств -->
    <v-app-bar-nav-icon
      @click="drawer = !drawer"
      class="d-md-none"
    ></v-app-bar-nav-icon>

    <!-- Навигационные вкладки для больших экранов -->
    <div class="d-none d-md-flex nav-tabs">
      <v-tabs
        v-model="activeTab"
        background-color="#333333"
        dark
        slider-color="#FFFFFF"
      >
        <v-tab
          v-for="(item, index) in navItems"
          :key="index"
          :to="item.path"
          :style="{ color: activeTab === index ? '#FFFFFF' : '#AFAFAF' }"
        >
          {{ $t(item.label) }}
        </v-tab>
      </v-tabs>
    </div>

    <!-- Переключатель языков для больших экранов -->
    <v-menu offset-y>
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props">
          <v-avatar size="24" class="mr-2">
            <v-img :src="currentLanguage.flag"></v-img>
          </v-avatar>
          <span style="color: #afafaf">{{ currentLanguage.name }}</span>
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(lang, index) in languages"
          :key="index"
          @click="changeLanguage(lang)"
          :prepend-avatar="lang.flag"
        >
          <v-list-item-title>{{ lang.name }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-app-bar>

  <!-- Боковое меню для мобильных устройств -->
  <v-navigation-drawer v-model="drawer" app temporary class="d-md-none">
    <!-- Список навигации -->
    <v-list dense>
      <v-list-item
        v-for="(item, index) in navItems"
        :key="index"
        @click="navigateTo(item.path)"
      >
        <v-list-item-title>{{ $t(item.label) }}</v-list-item-title>
      </v-list-item>
    </v-list>

    <!-- Разделитель -->
    <v-divider></v-divider>

    <!-- Переключатель языков -->
    <v-list dense>
      <v-subheader>{{ $t("languages.language") }}</v-subheader>
      <v-list-item
        v-for="(lang, index) in languages"
        :key="index"
        @click="changeLanguage(lang)"
        :prepend-avatar="lang.flag"
      >
        <v-list-item-title>{{ lang.name }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script setup lang="ts">
import { ref, watch } from "vue";
import { useRouter } from "vue-router";
import { useI18n } from "vue-i18n";
import germanyFlag from "@/assets/germany-flag.png";
import usaFlag from "@/assets/usa-flag.png";
import logoImage from "@/assets/logo.png";

// Маршрутизатор
const router = useRouter();

// i18n
const { locale, t } = useI18n();

// Состояние бокового меню
const drawer = ref(false);

// Список навигационных вкладок с путями и ключами локализации
const navItems = [
  { label: "navigation.home", path: "/" },
  { label: "navigation.aboutUs", path: "/unser-unternehmen" },
  { label: "navigation.temporaryWorkers", path: "/zeitarbeiter" },
  {
    label: "navigation.certifiedSpecialists",
    path: "/zertifizierte-spezialisten",
  },
  { label: "navigation.training", path: "/ausbildung" },
  { label: "navigation.contactUs", path: "/kontaktieren-sie-uns" },
];

// Текущая активная вкладка
const activeTab = ref(0);

// Языковые настройки
const languages = [
  {
    code: "en",
    name: t("languages.en"),
    flag: usaFlag,
  },
  {
    code: "de",
    name: t("languages.de"),
    flag: germanyFlag,
  },
];

// Текущий язык
const currentLanguage: any = ref(
  languages.find((lang) => lang.code === locale.value)
);

// Следим за изменением локали, чтобы обновлять текущий язык и имена языков
watch(locale, (newLocale) => {
  currentLanguage.value = languages.find((lang) => lang.code === newLocale);
  // Обновляем имена языков при смене локали
  languages.forEach((language) => {
    language.name = t(`languages.${language.code}`);
  });
});

// Функция смены языка
function changeLanguage(lang: any) {
  locale.value = lang.code;
  localStorage.setItem("locale", lang.code);
}

// Функция навигации
function navigateTo(path: string) {
  router.push(path);
  drawer.value = false; // Закрываем меню после перехода
}
</script>

<style scoped>
.logo {
  padding: 0 16px;
}

.nav-tabs {
  flex: 1 1 auto;
  display: flex;
  align-items: center;
}

.v-tabs {
  color: #afafaf;
}

.v-tab {
  min-width: 100px;
}

.v-tab:hover {
  color: #ffffff !important;
}

.v-tab--active {
  color: #ffffff !important;
}
.v-list-item__prepend {
  width: 14px !important;
}
</style>
