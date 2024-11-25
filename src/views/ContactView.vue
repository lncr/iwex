<template>
  <v-app>
    <!-- Success Message -->
    <v-alert
      v-if="showSuccessMessage"
      type="success"
      dismissible
      class="alert-message"
      @input="showSuccessMessage = false"
    >
      {{ $t("form.success") }}
    </v-alert>

    <!-- Error Message -->
    <v-alert
      v-if="showErrorMessage"
      type="error"
      dismissible
      class="alert-message"
      @input="showErrorMessage = false"
    >
      {{ $t("form.error") }}
    </v-alert>

    <v-container class="form-container">
      <!-- Ваш существующий контент формы -->
      <v-row>
        <v-col cols="12">
          <h2 class="title">{{ $t("form.title") }}</h2>
          <p class="description">
            {{ $t("form.description") }}
          </p>
        </v-col>
      </v-row>
      <v-form v-model="valid" ref="form">
        <v-row>
          <!-- Name Field -->
          <v-col cols="12">
            <v-text-field
              v-model="formData.name"
              :label="$t('form.fields.name')"
              outlined
              dense
              required
              :rules="[rules.required]"
            ></v-text-field>
          </v-col>
          <!-- Email Field -->
          <v-col cols="12">
            <v-text-field
              v-model="formData.email"
              :label="$t('form.fields.email')"
              outlined
              dense
              required
              :rules="[rules.required, rules.email]"
            ></v-text-field>
          </v-col>
          <!-- Phone Number Field -->
          <v-col cols="12">
            <v-text-field
              v-model="formData.phone"
              :label="$t('form.fields.phone')"
              outlined
              dense
              required
              :rules="[rules.required, rules.phone]"
            ></v-text-field>
          </v-col>
          <!-- Subject Field -->
          <v-col cols="12">
            <v-text-field
              v-model="formData.subject"
              :label="$t('form.fields.subject')"
              outlined
              dense
              required
              :rules="[rules.required]"
            ></v-text-field>
          </v-col>
          <!-- Message Field -->
          <v-col cols="12">
            <v-textarea
              v-model="formData.message"
              :label="$t('form.fields.message')"
              outlined
              dense
              rows="1"
            ></v-textarea>
          </v-col>
          <!-- Privacy Checkbox -->
          <v-col cols="12">
            <v-checkbox
              v-model="formData.privacy"
              :label="$t('form.checkbox')"
              :rules="[rules.required]"
              dense
              class="checkbox-label"
            ></v-checkbox>
          </v-col>
          <!-- Submit Button -->
          <v-col cols="12" class="btn">
            <v-btn
              :disabled="!valid"
              class="white--text button"
              @click="submitForm"
            >
              {{ $t("form.submit") }}
            </v-btn>
          </v-col>
        </v-row>
      </v-form>
    </v-container>
  </v-app>
</template>

<script>
import api from "@/plugins/api";

export default {
  data() {
    return {
      valid: false,
      formData: {
        name: "",
        email: "",
        phone: "",
        subject: "",
        message: "",
        privacy: false,
      },
      rules: {
        required: (value) => !!value || this.$t("form.validation.required"),
        email: (value) =>
          /.+@.+\..+/.test(value) || this.$t("form.validation.email"),
        phone: (value) =>
          /^\+?[1-9]\d{1,14}$/.test(value) || this.$t("form.validation.phone"),
      },
      showSuccessMessage: false,
      showErrorMessage: false,
    };
  },
  methods: {
    async submitForm() {
      if (this.$refs.form.validate()) {
        try {
          await api.post("/api/v1/contacts/", {
            full_name: this.formData.name,
            email: this.formData.email,
            phone_number: this.formData.phone,
            subject: this.formData.subject,
            message: this.formData.message,
          });
          this.showSuccessMessage = true;
          this.showErrorMessage = false;
          this.resetForm();
        } catch (error) {
          this.showErrorMessage = true;
          this.showSuccessMessage = false;
        }
      }
    },

    resetForm() {
      this.formData = {
        name: "",
        email: "",
        phone: "",
        subject: "",
        message: "",
        privacy: false,
      };
      this.$refs.form.resetValidation();
    },
  },
};
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

.form-container {
  max-width: 100%; /* Ширина формы */
  height: 100vh;
  background-color: #333; /* Цвет фона контейнера */
  color: #fff; /* Цвет текста */
  padding: 40px 50px;
  border-radius: 8px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5); /* Тень контейнера */
  /* Убрано margin-top */
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

.alert-message {
  position: fixed;
  top: 20px; /* Положение от верхнего края окна */
  left: 50%; /* Центрируем по горизонтали */
  transform: translateX(-50%); /* Корректировка для центрирования */
  width: 250px; /* Ширина между 200-300px */
  z-index: 1000; /* Обеспечиваем отображение поверх других элементов */
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
}
</style>
