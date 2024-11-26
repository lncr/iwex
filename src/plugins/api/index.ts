// src/services/api.ts
import axios from "axios";

const api = axios.create({
  baseURL: process.env.VUE_APP_BASE_URL || "https://iwex-germany.de/",
});

export default api;
