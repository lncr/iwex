<template>
  <div class="company-info" id="about-us">
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

  .container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: flex-start;
    margin-top: 120px;
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
        max-width: 230px;
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

/* Адаптивность для планшетов и ноутбуков */
@media (max-width: 960px) {
  .company-info {
    padding: 0 15px;

    .container {
      flex-wrap: wrap;
      margin-top: 80px;
    }

    .text-section {
      flex: 1 1 100%;
      padding-right: 0;
      text-align: center;

      .title {
        font-size: 32px;
      }

      .description {
        font-size: 16px;
      }

      .signature {
        align-items: center;

        .signature-image {
          margin-right: 0;
          margin-bottom: 10px;
          max-width: 200px;
        }

        .founder {
          font-size: 16px;
        }
      }
    }

    .image-section {
      flex: 1 1 100%;
      margin-top: 30px;

      .image-wrapper {
        padding: 15px;

        .founder-image {
          max-width: 100%;
          height: auto;
        }
      }
    }
  }
}

/* Адаптивность для мобильных устройств */
@media (max-width: 600px) {
  .company-info {
    padding: 0 10px;

    .container {
      flex-direction: column;
      margin-top: 60px;
    }

    .text-section {
      padding-right: 0;
      text-align: center;

      .title {
        font-size: 28px;
      }

      .description {
        font-size: 14px;
      }

      .signature {
        flex-direction: column;
        align-items: center;

        .signature-image {
          margin-right: 0;
          margin-bottom: 10px;
          max-width: 150px;
        }

        .founder {
          font-size: 14px;
        }
      }
    }

    .image-section {
      margin-top: 20px;

      .image-wrapper {
        padding: 10px;

        .founder-image {
          max-width: 100%;
          height: auto;
        }
      }
    }
  }
}
</style>
