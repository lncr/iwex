import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ContactView from "../views/ContactView.vue";
import ImpressumView from "../views/ImpressumView.vue";
import DatenschutzerklaerungView from "../views/DatenschutzerklaerungView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/contact",
    name: "contact",
    component: ContactView,
  },
  {
    path: "/impressum",
    name: "impressum",
    component: ImpressumView,
  },
  {
    path: "/datenschutzerklaerung",
    name: "datenschutzerklaerung",
    component: DatenschutzerklaerungView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  window.scrollTo({
    top: 0,
    behavior: "smooth", // Плавная прокрутка
  });
  next(); // Продолжить навигацию
});

export default router;
