<template>
  <div class="company-info">
    <div class="container">
      <div class="text-section">
        <h2 class="title">{{ $t("company.title") }}</h2>
        <p class="description">{{ $t("company.description") }}</p>
        <div class="signature">
          <img :src="signatureImage" alt="Signature" class="signature-image" />
          <p class="founder"><strong>Nurdin Sheishenov</strong><br />CEO</p>
        </div>
      </div>
      <div class="image-section">
        <div class="image-wrapper">
          <img :src="founderImage" alt="Founder" class="founder-image" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import signatureImage from "@/assets/signature.png";
import founderImage from "@/assets/container.png";
</script>

<style scoped lang="scss">
.company-info {
  padding: 0 20px;
  margin-top: 120px;

  .container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: flex-start;
    max-width: 1200px;
    margin: 0 auto;
  }

  .text-section {
    flex: 1 1 500px;
    padding-right: 30px;

    .title {
      font-size: 36px;
      font-weight: 700;
      color: rgba(45, 59, 66, 1);
      margin-bottom: 20px;
    }

    .description {
      font-size: 18px;
      color: rgba(121, 121, 121, 1);
      line-height: 1.6;
      margin-bottom: 30px;
    }

    .signature {
      display: flex;
      flex-direction: column;

      .signature-image {
        max-width: 230px; // Ограничиваем ширину до 130px
        width: 100%;
        height: auto;
        margin-right: 20px;
      }

      .founder {
        font-size: 18px;
        color: #333333;

        strong {
          font-weight: 700;
        }
      }
    }
  }

  .image-section {
    flex: 1 1 400px;
    display: flex;
    justify-content: center;
    align-items: center;

    .image-wrapper {
      //   background-color: #ffc107; // Ярко-желтый фон
      padding: 20px;
      border-radius: 10px;

      .founder-image {
        width: 100%;
        height: auto;
        border-radius: 10px;
      }
    }
  }
}

/* Адаптивность */
@media (max-width: 768px) {
  .company-info {
    padding: 40px 10px;

    .container {
      flex-direction: column;
      align-items: center;
    }

    .text-section {
      padding-right: 0;
      text-align: center;

      .signature {
        flex-direction: column;
        align-items: center;

        .signature-image {
          margin-right: 0;
          margin-bottom: 10px;
        }
      }
    }

    .image-section {
      margin-top: 30px;
    }
  }
}
</style>
