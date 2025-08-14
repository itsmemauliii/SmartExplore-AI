import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.BACKEND_URL || 'http://10.0.2.2:8000',
  timeout: 10000,
});

export default apiClient;
