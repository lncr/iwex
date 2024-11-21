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
</style>
