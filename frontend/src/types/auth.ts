export type RegisterPayload = {
  email: string;
  password: string;
  full_name?: string;
};

export type AuthToken = {
  access_token: string;
  token_type: 'bearer';
};
