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
      <!-- Your existing form content -->
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
          <v-col cols="5"></v-col>
          <v-col cols="3" class="btn">
            <v-btn
              :disabled="!valid"
              block
              class="white--text button"
              @click="submitForm"
            >
              {{ $t("form.submit") }}
            </v-btn>
          </v-col>
          <v-col cols="5"></v-col>
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
  background-color: #333; /* Background color for the whole page */
  margin-left: calc(50% - 50vw);
  margin-right: calc(50% - 50vw);
}

.form-container {
  max-width: 100%; /* Form width */
  height: 100%;
  background-color: #333; /* Container background color */
  color: #fff; /* Text color */
  padding: 40px;
  border-radius: 8px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5); /* Container shadow */
}

.title {
  color: rgba(255, 203, 0, 1); /* Title color */
  text-align: start;
  font-size: 48px;
  margin-left: 50px;
}

.description {
  text-align: start;
  margin-bottom: 20px;
  font-size: 28px;
  margin-left: 50px;
}

.checkbox-label ::v-deep .v-label {
  color: rgba(255, 203, 0, 1);
  font-size: 20px;
}

.v-text-field {
  height: 100px;
}

.btn {
  .button {
    background-color: rgba(222, 222, 222, 1);
    font-size: 24px;
    border-radius: 30px;
    padding: 25px;
    color: rgba(51, 51, 51, 1);
  }
}

/* New CSS for the alert messages */
.alert-message {
  position: fixed;
  top: 20px; /* Position from the top of the viewport */
  left: 50%; /* Center horizontally */
  transform: translateX(-50%); /* Adjust for centering */
  width: 250px; /* Set width between 200-300px */
  z-index: 1000; /* Ensure it appears above other elements */
}

.v-col {
  padding: 5px;
}
</style>
