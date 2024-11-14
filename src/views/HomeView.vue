<template>
  <AppTop></AppTop>
  <AppServices></AppServices>
  <AppIndustry></AppIndustry>
  <AppSteps></AppSteps>
</template>

<script>
import AppIndustry from "@/components/AppIndustry.vue";
import AppServices from "@/components/AppServices.vue";
import AppSteps from "@/components/AppSteps.vue";
import AppTop from "@/components/AppTop.vue";

export default {
  name: "HomeView",
  components: {
    AppServices,
    AppTop,
    AppIndustry,
    AppSteps,
  },
};
</script>
