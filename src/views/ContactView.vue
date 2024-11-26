<template>
  <div class="v-application">
    <!-- Успешное или Ошибочное Сообщение -->
    <v-alert
      v-if="showAlert"
      :type="alertType"
      dismissible
      class="alert-message"
      @input="closeAlert"
      v-model="showAlert"
    >
      <div v-html="alertMessage"></div>
    </v-alert>

    <v-container class="form-container">
      <!-- Контент формы -->
      <v-row>
        <v-col cols="12">
          <h2 class="title">{{ t("form.title") }}</h2>
          <p class="description">
            {{ t("form.description") }}
          </p>
        </v-col>
      </v-row>
      <v-form v-model="valid" ref="form">
        <v-row>
          <!-- Поле "Имя" -->
          <v-col cols="12">
            <v-text-field
              v-model="formData.name"
              :label="t('form.fields.name')"
              outlined
              dense
              required
              :rules="[rules.required]"
            ></v-text-field>
          </v-col>
          <!-- Поле "Email" -->
          <v-col cols="12">
            <v-text-field
              v-model="formData.email"
              :label="t('form.fields.email')"
              outlined
              dense
              required
              :rules="[rules.required, rules.email]"
            ></v-text-field>
          </v-col>
          <!-- Поле "Телефон" -->
          <v-col cols="12">
            <v-text-field
              v-model="formData.phone"
              :label="t('form.fields.phone')"
              outlined
              dense
              required
              :rules="[rules.required, rules.phone]"
            ></v-text-field>
          </v-col>
          <!-- Поле "Тема" -->
          <v-col cols="12">
            <v-text-field
              v-model="formData.subject"
              :label="t('form.fields.subject')"
              outlined
              dense
              required
              :rules="[rules.required]"
            ></v-text-field>
          </v-col>
          <!-- Поле "Сообщение" -->
          <v-col cols="12">
            <v-textarea
              v-model="formData.message"
              :label="t('form.fields.message')"
              outlined
              dense
              rows="1"
            ></v-textarea>
          </v-col>
          <!-- Чекбокс "Согласие на обработку данных" -->
          <v-col cols="12">
            <v-checkbox
              v-model="formData.privacy"
              :label="t('form.checkbox')"
              :rules="[rules.required]"
              dense
              class="checkbox-label"
            ></v-checkbox>
          </v-col>
          <!-- Кнопка "Отправить" -->
          <v-col cols="12" class="btn">
            <v-btn
              :disabled="!valid"
              class="white--text button"
              @click="submitForm"
            >
              {{ t("form.submit") }}
            </v-btn>
          </v-col>
        </v-row>
      </v-form>
    </v-container>
  </div>
</template>

<script setup>
import { ref, reactive, computed, watch } from "vue";
import { useI18n } from "vue-i18n";
import api from "@/plugins/api";

// Получаем функцию перевода
const { t } = useI18n();

// Ссылка на форму для доступа к методам формы
const form = ref(null);

// Реактивные переменные
const valid = ref(false);

const formData = reactive({
  name: "",
  email: "",
  phone: "",
  subject: "",
  message: "",
  privacy: false,
});

// Состояния для алертов
const showAlert = ref(false);
const alertType = ref("success"); // "success" или "error"
const alertMessage = ref("");

// Переменная для хранения ID таймера
let alertTimeout = null;

// Правила валидации с использованием перевода
const rules = computed(() => ({
  required: (value) => !!value || t("form.validation.required"),
  email: (value) => /.+@.+\..+/.test(value) || t("form.validation.email"),
  phone: (value) =>
    /^\+?[1-9]\d{1,14}$/.test(value) || t("form.validation.phone"),
}));

// Функция отправки формы
const submitForm = async () => {
  console.log("submitForm called");
  if (form.value && form.value.validate()) {
    console.log("Form is valid");
    try {
      console.log("Sending data:", formData);
      const response = await api.post("/api/v1/contacts/", {
        full_name: formData.name,
        email: formData.email,
        phone_number: formData.phone,
        subject: formData.subject,
        message: formData.message,
      });
      console.log("API call successful", response);
      alertType.value = "success";
      alertMessage.value = `<p>${t("form.success")}</p>`;
      showAlert.value = true;
      resetForm();
      // Запускаем таймер для скрытия алерта через 5 секунд
      startAlertTimer();
    } catch (error) {
      console.error("Ошибка при отправке формы:", error);
      alertType.value = "error";
      // Обработка ошибок, полученных с бэкенда
      if (error.response && error.response.data) {
        const errors = error.response.data;
        const messages = [];

        for (const key in errors) {
          if (Array.isArray(errors[key])) {
            errors[key].forEach((msg) => {
              if (key === "0") {
                // Общие ошибки без привязки к полям
                messages.push(`${msg}`);
              } else {
                // Ошибки, привязанные к полям формы
                const fieldName = t(`form.fields.${key}`) || key;
                messages.push(`${fieldName}: ${msg}`);
              }
            });
          } else if (typeof errors[key] === "string") {
            messages.push(`${errors[key]}`);
          }
        }

        alertMessage.value = `<ul>${messages
          .map((msg) => `<li>${msg}</li>`)
          .join("")}</ul>`;
      } else {
        alertMessage.value = t("form.error");
      }
      showAlert.value = true;
      // Запускаем таймер для скрытия алерта через 5 секунд
      startAlertTimer();
    }
  } else {
    console.log("Form validation failed");
  }
};

// Функция сброса формы
const resetForm = () => {
  console.log("resetForm called");
  formData.name = "";
  formData.email = "";
  formData.phone = "";
  formData.subject = "";
  formData.message = "";
  formData.privacy = false;
  if (form.value) {
    form.value.resetValidation();
  }
};

// Функция закрытия алерта
const closeAlert = () => {
  showAlert.value = false;
  // Очистка таймера при ручном закрытии алерта
  if (alertTimeout) {
    clearTimeout(alertTimeout);
    alertTimeout = null;
  }
};

// Функция запуска таймера для скрытия алерта
const startAlertTimer = () => {
  // Очистка предыдущего таймера, если он существует
  if (alertTimeout) {
    clearTimeout(alertTimeout);
  }
  // Запуск нового таймера
  alertTimeout = setTimeout(() => {
    showAlert.value = false;
    alertTimeout = null;
  }, 5000); // 5000 миллисекунд = 5 секунд
};

// Очистка таймера при уничтожении компонента
watch(showAlert, (newVal) => {
  if (!newVal && alertTimeout) {
    clearTimeout(alertTimeout);
    alertTimeout = null;
  }
});
</script>

<style scoped lang="scss">
html,
body,
.v-application {
  margin: 0;
  padding: 0;
  height: 100%;
  background-color: #333; /* Цвет фона для всей страницы */
  margin-left: calc(50% - 50vw);
  margin-right: calc(50% - 50vw);
}

.alert-message {
  position: fixed;
  top: 100px; /* Положение ниже навбара, скорректируйте при необходимости */
  left: 50%; /* Центрируем по горизонтали */
  transform: translateX(-50%);
  width: 300px; /* Увеличенная ширина */
  z-index: 1000; /* Отображение поверх других элементов */
  text-align: center; /* Центрирование текста */
  font-size: 16px; /* Нормальный размер текста */
  border-radius: 8px; /* Скругление углов */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Дополнительная тень */
  opacity: 1; /* Начальная непрозрачность */
  transition: opacity 0.5s ease, transform 0.5s ease; /* Плавные переходы */
}

.alert-message .v-alert__content {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

/* Фон для контейнера формы */
.form-container {
  max-width: 600px; /* Ограничение ширины формы */
  background-color: #444; /* Цвет фона контейнера */
  color: #fff; /* Цвет текста */
  padding: 40px 50px;
  border-radius: 8px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5); /* Тень контейнера */
}

.title {
  color: rgba(255, 203, 0, 1); /* Цвет заголовка */
  text-align: start;
  font-size: 48px;
  margin-bottom: 20px;
}

.description {
  text-align: start;
  margin-bottom: 40px;
  font-size: 28px;
}

.checkbox-label .v-label {
  color: rgba(255, 203, 0, 1);
  font-size: 20px;
}

.v-text-field,
.v-textarea {
  height: auto;
}

.btn {
  display: flex;
  justify-content: center;
  margin-top: 20px;
  .button {
    background-color: rgba(222, 222, 222, 1);
    font-size: 16px;
    border-radius: 30px;
    padding: 10px 20px;
    color: rgba(51, 51, 51, 1);
    text-transform: none;
  }
}

.v-col {
  padding: 5px;
}

/* Адаптивность для планшетов и ноутбуков */
@media (max-width: 960px) {
  .form-container {
    padding: 30px 40px;
  }

  .title {
    font-size: 36px;
  }

  .description {
    font-size: 24px;
  }

  .btn .button {
    font-size: 14px;
    padding: 8px 16px;
  }
}

/* Адаптивность для мобильных устройств */
@media (max-width: 600px) {
  .form-container {
    padding: 20px 20px;
    width: 100%;
    margin-left: 0;
    margin-right: 0;
  }

  .title {
    font-size: 28px;
    text-align: center;
  }

  .description {
    font-size: 18px;
    text-align: center;
  }

  .btn .button {
    font-size: 14px;
    padding: 8px 12px;
    width: auto;
  }

  .checkbox-label .v-label {
    font-size: 16px;
  }

  .alert-message {
    width: 90%; /* Адаптивная ширина на мобильных */
    top: 120px; /* Немного ниже для мобильных устройств */
  }
}
</style>
