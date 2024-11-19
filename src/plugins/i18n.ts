import { createI18n } from "vue-i18n";
import localeDe from "./locales/de.json";
import localeEn from "./locales/en.json";

export type Locales = "eng" | "deu";

// Получаем сохраненную локаль из localStorage или используем 'en' по умолчанию
const savedLocale = localStorage.getItem("locale") || "eng";

const i18n = createI18n({
  legacy: false, // Используем Composition API
  locale: savedLocale,
  fallbackLocale: "eng",
  messages: {
    deu: localeDe,
    eng: localeEn,
  },
});

export default i18n;
