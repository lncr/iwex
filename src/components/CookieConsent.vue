<template>
  <v-snackbar
    v-model="showBanner"
    color="rgba(255, 203, 0, 1)"
    elevation="0"
    bottom
    :timeout="-1"
    persistent
    max-width="100%"
  >
    <div class="cookie-content">
      <h2 class="cookie-title">{{ t("cookieConsent.title") }}</h2>
      <p class="cookie-message">{{ t("cookieConsent.message") }}</p>
      <br />
      <p class="cookie-message">{{ t("cookieConsent.message2") }}</p>
      <div class="button-group">
        <v-btn class="cookie-button" @click="rejectAll">
          {{ t("cookieConsent.reject") }}
        </v-btn>
        <v-btn class="cookie-button" @click="acceptAll">
          {{ t("cookieConsent.accept") }}
        </v-btn>
      </div>
    </div>
  </v-snackbar>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useI18n } from "vue-i18n";

const { t } = useI18n();

const showBanner = ref(false);

onMounted(() => {
  const consent = localStorage.getItem("cookieConsent");
  if (!consent) {
    showBanner.value = true;
  }
});

function acceptAll() {
  localStorage.setItem("cookieConsent", "accepted");
  showBanner.value = false;
}

function rejectAll() {
  localStorage.setItem("cookieConsent", "rejected");
  showBanner.value = false;
}
</script>

<style scoped>
.cookie-content {
  color: #000000;
  max-width: 100%;
}

.cookie-title {
  font-weight: bold;
  margin-bottom: 10px;
  font-size: 32px;
  font-family: Epilogue;
  color: #ffffff;
}

.cookie-message {
  margin-bottom: 20px;
  font-size: 18px;
  font-family: Epilogue;
  color: rgba(51, 51, 51, 1);
}

.button-group {
  display: flex;
  justify-content: flex-end;
}

.cookie-button {
  color: #ffffff;
  margin: 0 10px;
  text-transform: none;
}

.cookie-button.v-btn {
  background-color: rgba(51, 51, 51, 1);
  border-radius: 8px;
}
</style>
