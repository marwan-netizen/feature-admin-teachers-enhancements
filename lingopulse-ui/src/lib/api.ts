import axios from 'axios';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/core/api/v1/',
  withCredentials: true,
});

export const fetchTests = async (skill?: string, level?: string) => {
  const { data } = await api.get('tests/', { params: { skill, level } });
  return data;
};

export const login = async (credentials: any) => {
  const { data } = await api.post('auth/login/', credentials);
  return data;
};

export const fetchProfile = async () => {
  const { data } = await api.get('auth/me/');
  return data;
};

export default api;
