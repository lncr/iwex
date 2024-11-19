// src/services/api.ts
import axios from "axios";

const api = axios.create({
  baseURL: process.env.VUE_APP_BASE_URL || "http://159.223.21.167",
});

export default api;
