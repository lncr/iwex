<template>
  <div class="impressum">
    <div class="content">
      <h1>{{ $t("impressum.title") }}</h1>
      <div>
        <p>
          <strong>IWEX Germany GmbH</strong><br />70 Hahnstr.<br />60528
          Frankfurt
        </p>
        <br />
        <p>
          {{ $t("impressum.text2") }} HRB 128023<br />{{
            $t("impressum.text3")
          }}
        </p>
        <br />
        <p>
          <strong>{{ $t("impressum.text4") }}</strong
          ><br />Nurdin Sheishenov
        </p>
        <br />
        <p>
          <strong>{{ $t("impressum.text5") }}</strong>
        </p>
        <p>
          {{ $t("impressum.text6") }} 01792078900<br />{{
            $t("impressum.text7")
          }}
          info@iwex-personal.de
        </p>
        <br />
        <p>
          <strong>{{ $t("impressum.text8") }}</strong>
        </p>
        <p>
          {{ $t("impressum.text9") }}
        </p>
        <br />
        <p>
          <strong>{{ $t("impressum.text10") }}</strong>
        </p>
        <p>
          {{ $t("impressum.text11") }}
        </p>
      </div>
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
  font-size: 18px;
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
