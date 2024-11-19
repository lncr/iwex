<template>
  <AppTop></AppTop>
  <AppServices></AppServices>
  <AppIndustry></AppIndustry>
  <AppSteps></AppSteps>
  <AdBanner></AdBanner>
  <CompanyInfo></CompanyInfo>
  <AppContacts></AppContacts>
  <AppFooter></AppFooter>
</template>

<script>
import AdBanner from "@/components/AdBanner.vue";
import AppContacts from "@/components/AppContacts.vue";
import AppFooter from "@/components/AppFooter.vue";
import AppIndustry from "@/components/AppIndustry.vue";
import AppServices from "@/components/AppServices.vue";
import AppSteps from "@/components/AppSteps.vue";
import AppTop from "@/components/AppTop.vue";
import CompanyInfo from "@/components/CompanyInfo.vue";

export default {
  name: "HomeView",
  components: {
    AppServices,
    AppTop,
    AppIndustry,
    AppSteps,
    AdBanner,
    CompanyInfo,
    AppContacts,
    AppFooter,
  },
};
</script>
