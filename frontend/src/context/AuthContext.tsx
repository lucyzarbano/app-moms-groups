import React, { createContext, PropsWithChildren, useMemo, useState } from 'react';

type AuthContextValue = {
  accessToken: string | null;
  setAccessToken: (token: string | null) => void;
};

export const AuthContext = createContext<AuthContextValue>({
  accessToken: null,
  setAccessToken: () => undefined,
});

export function AuthProvider({ children }: PropsWithChildren) {
  const [accessToken, setAccessToken] = useState<string | null>(null);

  const value = useMemo(
    () => ({ accessToken, setAccessToken }),
    [accessToken],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}
