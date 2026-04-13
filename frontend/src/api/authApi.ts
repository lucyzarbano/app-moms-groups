import { apiClient } from './client';
import type { AuthToken, RegisterPayload } from '../types/auth';

export async function register(payload: RegisterPayload) {
  const response = await apiClient.post('/auth/register', payload);
  return response.data;
}

export async function login(payload: RegisterPayload): Promise<AuthToken> {
  const response = await apiClient.post<AuthToken>('/auth/login', payload);
  return response.data;
}
