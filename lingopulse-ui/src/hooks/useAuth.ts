import { useState, useEffect } from 'react';
import api, { fetchProfile } from '../lib/api';

export const useAuth = () => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkAuth = async () => {
      try {
        const profile = await fetchProfile();
        setUser(profile);
      } catch (error) {
        setUser(null);
      } finally {
        setLoading(false);
      }
    };
    checkAuth();
  }, []);

  return { user, loading, authenticated: !!user };
};
