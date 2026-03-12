'use client'
import React, { createContext, useContext, useState, useEffect } from 'react';

type Language = 'en' | 'ar';

interface LanguageContextType {
  language: Language;
  setLanguage: (lang: Language) => void;
  t: (key: string) => string;
  isRTL: boolean;
}

const translations: Record<Language, Record<string, string>> = {
  en: {
    welcome: 'Welcome to LingoPulse AI',
    start_journey: 'Start Your Journey',
    login: 'Login',
    register: 'Register',
    dashboard: 'Dashboard',
    speaking: 'Speaking',
    writing: 'Writing',
    vocabulary: 'Vocabulary',
    classroom: 'Classroom',
  },
  ar: {
    welcome: 'مرحباً بك في لينجو بلس AI',
    start_journey: 'ابدأ رحلتك',
    login: 'تسجيل الدخول',
    register: 'إنشاء حساب',
    dashboard: 'لوحة التحكم',
    speaking: 'المحادثة',
    writing: 'الكتابة',
    vocabulary: 'المفردات',
    classroom: 'الفصل الدراسي',
  }
};

const LanguageContext = createContext<LanguageContextType | undefined>(undefined);

export const LanguageProvider = ({ children }: { children: React.ReactNode }) => {
  const [language, setLanguage] = useState<Language>('en');

  useEffect(() => {
    document.dir = language === 'ar' ? 'rtl' : 'ltr';
    document.documentElement.lang = language;
  }, [language]);

  const t = (key: string) => translations[language][key] || key;
  const isRTL = language === 'ar';

  return (
    <LanguageContext.Provider value={{ language, setLanguage, t, isRTL }}>
      {children}
    </LanguageContext.Provider>
  );
};

export const useLanguage = () => {
  const context = useContext(LanguageContext);
  if (!context) throw new Error('useLanguage must be used within a LanguageProvider');
  return context;
};
