<template>
  <div class="v-application">
    <!-- Сообщение об успехе или ошибке -->
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
      <!-- Заголовок и описание формы -->
      <v-row>
        <v-col cols="12">
          <h2 class="title">{{ t("form.title") }}</h2>
          <p class="description">{{ t("form.description") }}</p>
        </v-col>
      </v-row>

      <!-- Форма -->
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

// Ссылка на форму
const form = ref(null);
const valid = ref(false);

// Данные формы
const formData = reactive({
  name: "",
  email: "",
  phone: "",
  subject: "",
  message: "",
  privacy: false,
});

// Состояния для отображения алерта
const showAlert = ref(false);
const alertType = ref("success"); // "success" или "error"
const alertMessage = ref("");
let alertTimeout = null;

// Правила валидации
const rules = computed(() => ({
  required: (value) => !!value || t("form.validation.required"),
  email: (value) => /.+@.+\..+/.test(value) || t("form.validation.email"),
  phone: (value) =>
    /^\+?[1-9]\d{1,14}$/.test(value) || t("form.validation.phone"),
}));

// Функция отправки формы
const submitForm = async () => {
  if (form.value && form.value.validate()) {
    try {
      // Отправка данных через API
      await api.post("/api/v1/contacts/", {
        full_name: formData.name,
        email: formData.email,
        phone_number: formData.phone,
        subject: formData.subject,
        message: formData.message,
      });

      // Отображение сообщения об успехе
      alertType.value = "success";
      alertMessage.value = `<p>${t("form.success")}</p>`;
      showAlert.value = true;

      // Сброс формы
      resetForm();
      startAlertTimer();

      // Вызов функции конверсии из index.html
      if (typeof window.gtag_report_conversion === "function") {
        window.gtag_report_conversion();
      } else {
        console.error("gtag_report_conversion не определена");
      }
    } catch (error) {
      console.error("Ошибка при отправке формы:", error);
      alertType.value = "error";
      // Обработка ошибок от бэкенда
      if (error.response && error.response.data) {
        const errors = error.response.data;
        const messages = [];
        for (const key in errors) {
          if (Array.isArray(errors[key])) {
            errors[key].forEach((msg) => {
              // Если ошибка не привязана к конкретному полю
              const fieldName =
                key !== "0" ? t(`form.fields.${key}`) || key : "";
              messages.push(fieldName ? `${fieldName}: ${msg}` : msg);
            });
          } else if (typeof errors[key] === "string") {
            messages.push(errors[key]);
          }
        }
        alertMessage.value = `<ul>${messages
          .map((msg) => `<li>${msg}</li>`)
          .join("")}</ul>`;
      } else {
        alertMessage.value = t("form.error");
      }
      showAlert.value = true;
      startAlertTimer();
    }
  } else {
    console.log("Валидация формы не пройдена");
  }
};

// Функция сброса формы
const resetForm = () => {
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
  if (alertTimeout) {
    clearTimeout(alertTimeout);
    alertTimeout = null;
  }
};

// Функция запуска таймера для скрытия алерта
const startAlertTimer = () => {
  if (alertTimeout) clearTimeout(alertTimeout);
  alertTimeout = setTimeout(() => {
    showAlert.value = false;
    alertTimeout = null;
  }, 5000);
};

// Очистка таймера при изменении состояния алерта
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
  background-color: #333;
  margin-left: calc(50% - 50vw);
  margin-right: calc(50% - 50vw);
}

.alert-message {
  position: fixed;
  top: 100px;
  left: 50%;
  transform: translateX(-50%);
  width: 300px;
  z-index: 1000;
  text-align: center;
  font-size: 16px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  opacity: 1;
  transition: opacity 0.5s ease, transform 0.5s ease;
}

.alert-message .v-alert__content {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.form-container {
  max-width: 600px;
  background-color: #444;
  color: #fff;
  padding: 40px 50px;
  border-radius: 8px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
}

.title {
  color: rgba(255, 203, 0, 1);
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
    width: 90%;
    top: 120px;
  }
}
</style>
