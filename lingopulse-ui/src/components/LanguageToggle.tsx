'use client'
import { useLanguage } from '@/context/LanguageContext'

export const LanguageToggle = () => {
  const { language, setLanguage } = useLanguage()
  return (
    <button
      onClick={() => setLanguage(language === 'en' ? 'ar' : 'en')}
      className="glass px-4 py-2 rounded-full border border-cyan-500/30 text-cyan-400 font-bold hover:bg-cyan-500/10 transition-all text-xs"
    >
      {language === 'en' ? 'العربية' : 'English'}
    </button>
  )
}
