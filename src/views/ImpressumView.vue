<template>
  <div class="impressum">
    <div class="content">
      <h1>{{ $t("impressum.title") }}</h1>
      <div v-html="$t('impressum.text')"></div>
    </div>
  </div>
</template>

<script setup>
// Пустой скрипт, если нет дополнительной логики
</script>

<style scoped>
.impressum {
  background-color: rgba(51, 51, 51, 1);
  padding: 40px 16px;
  color: #ffffff;
  min-height: 100vh; /* Чтобы контент занимал всю высоту экрана */
  margin-left: calc(50% - 50vw);
  margin-right: calc(50% - 50vw);
}

.content {
  max-width: 800px;
  margin: 0 auto;
}

h1 {
  font-size: 60px;
  font-weight: 700;
  font-family: Epilogue;
  margin-bottom: 24px;
  color: rgba(255, 203, 0, 1);
}

p {
  font-size: 48px;
  line-height: 65px;
  font-weight: 500;
  font-family: Epilogue;
  margin-bottom: 16px;
}

/* Адаптивность для планшетов и ноутбуков */
@media (max-width: 960px) {
  .impressum {
    padding: 30px 16px;
  }

  h1 {
    font-size: 48px;
    margin-bottom: 20px;
  }

  p {
    font-size: 36px;
    line-height: 50px;
    margin-bottom: 12px;
  }
}

/* Адаптивность для мобильных устройств */
@media (max-width: 600px) {
  .impressum {
    padding: 20px 10px;
    margin-left: 0;
    margin-right: 0;
  }

  .content {
    max-width: 100%;
  }

  h1 {
    font-size: 36px;
    margin-bottom: 16px;
    text-align: center;
  }

  p {
    font-size: 24px;
    line-height: 32px;
    margin-bottom: 8px;
    text-align: justify;
  }
}
</style>
