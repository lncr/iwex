<template>
  <v-app-bar app fixed color="#333333" dark>
    <!-- Navbar content wrapper -->
    <div class="navbar-content">
      <!-- Logo -->
      <div class="logo">
        <img
          :src="logoImage"
          alt="Logo"
          style="max-height: 40px; max-width: 150px"
        />
      </div>

      <!-- Spacer -->
      <v-spacer></v-spacer>

      <!-- Burger menu for mobile devices -->
      <v-app-bar-nav-icon
        @click="drawer = !drawer"
        class="d-md-none"
      ></v-app-bar-nav-icon>

      <!-- Navigation links for desktop -->
      <div class="nav-links d-none d-md-flex">
        <v-btn variant="text" :to="'/unsere-dienstleistungen'" class="nav-link">
          Unsere Dienstleistungen
        </v-btn>
        <v-btn variant="text" :to="'/ueber-uns'" class="nav-link">
          Über uns
        </v-btn>
        <!-- Kontaktieren Sie uns button -->
        <v-btn :to="'/kontaktieren-sie-uns'" class="nav-button">
          Kontaktieren Sie uns
        </v-btn>
      </div>

      <!-- Language switcher -->
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
    </div>
  </v-app-bar>

  <!-- Navigation drawer for mobile -->
  <v-navigation-drawer v-model="drawer" app temporary class="d-md-none">
    <v-list dense>
      <!-- Navigation links -->
      <v-list-item
        v-for="(item, index) in mobileNavItems"
        :key="index"
        @click="navigateTo(item.path)"
      >
        <v-list-item-title>{{ item.label }}</v-list-item-title>
      </v-list-item>
    </v-list>

    <!-- Divider -->
    <v-divider></v-divider>

    <!-- Language switcher -->
    <v-list dense>
      <v-subheader>Sprache</v-subheader>
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
  </v-navigation-drawer>
</template>

<script setup lang="ts">
import { ref, watch } from "vue";
import { useRouter } from "vue-router";
import { useI18n } from "vue-i18n";
import germanyFlag from "@/assets/germany-flag.png";
import usaFlag from "@/assets/usa-flag.png";
import logoImage from "@/assets/logo.png";

// Router
const router = useRouter();

// i18n
const { locale } = useI18n();

// Drawer state
const drawer = ref(false);

// Navigation links
const navLinks = [
  { label: "Unsere Dienstleistungen", path: "/unsere-dienstleistungen" },
  { label: "Über uns", path: "/ueber-uns" },
];

// For mobile, include the "Kontaktieren Sie uns" as well
const mobileNavItems = [
  { label: "Unsere Dienstleistungen", path: "/unsere-dienstleistungen" },
  { label: "Über uns", path: "/ueber-uns" },
  { label: "Kontaktieren Sie uns", path: "/kontaktieren-sie-uns" },
];

// Language settings
const languages = [
  {
    code: "de",
    name: "Deutsch",
    flag: germanyFlag,
  },
  {
    code: "en",
    name: "English",
    flag: usaFlag,
  },
];

// Current language
const currentLanguage = ref(
  languages.find((lang) => lang.code === locale.value)
);

// Watch locale change
watch(locale, (newLocale) => {
  currentLanguage.value = languages.find((lang) => lang.code === newLocale);
});

// Change language function
function changeLanguage(lang: any) {
  locale.value = lang.code;
  localStorage.setItem("locale", lang.code);
}

// Navigation function
function navigateTo(path: string) {
  router.push(path);
  drawer.value = false; // Close drawer after navigation
}
</script>

<style scoped>
.navbar-content {
  display: flex;
  align-items: center;
  width: 100%;
  max-width: 1440px;
  margin: 0 auto;
}

.logo {
  padding: 0 16px;
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

.language-btn {
  margin-left: 16px;
}

.v-list-item__prepend {
  width: 14px !important;
}
</style>
