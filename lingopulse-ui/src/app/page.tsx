'use client'
import { useLanguage } from '@/context/LanguageContext'
import Link from 'next/link'

export default function Home() {
  const { t, setLanguage, language } = useLanguage()

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-gradient-to-br from-indigo-950 to-indigo-900 relative">
      <div className="absolute top-8 right-8 flex gap-4">
         <button
           onClick={() => setLanguage(language === 'en' ? 'ar' : 'en')}
           className="glass px-4 py-2 rounded-full border border-cyan-500/30 text-cyan-400 font-bold hover:bg-cyan-500/10 transition-all"
         >
            {language === 'en' ? 'العربية' : 'English'}
         </button>
      </div>

      <div className="text-center">
        <h1 className="text-7xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-indigo-400 mb-6 drop-shadow-[0_0_30px_rgba(34,211,238,0.3)]">
          LingoPulse AI
        </h1>
        <p className="text-2xl text-indigo-200 mb-12 max-w-2xl leading-relaxed">
          {t('welcome')} - The world's most advanced AI-powered English proficiency platform.
        </p>
        <div className="flex gap-6 justify-center">
          <Link href="/auth">
            <button className="px-10 py-4 bg-cyan-500 hover:bg-cyan-400 text-indigo-950 rounded-2xl font-extrabold text-lg transition-all shadow-[0_0_20px_rgba(34,211,238,0.5)] scale-100 hover:scale-105">
              {t('start_journey')}
            </button>
          </Link>
          <Link href="/auth">
            <button className="px-10 py-4 bg-indigo-800/50 hover:bg-indigo-800/70 border border-indigo-700 text-white rounded-2xl font-bold text-lg backdrop-blur-sm transition-all">
              {t('login')}
            </button>
          </Link>
        </div>
      </div>

      <div className="mt-24 grid grid-cols-1 md:grid-cols-4 gap-8 w-full max-w-6xl">
         {[
           { skill: 'speaking', icon: '🎙️' },
           { skill: 'writing', icon: '✍️' },
           { skill: 'vocabulary', icon: '📚' },
           { skill: 'classroom', icon: '🏫' },
         ].map((item, i) => (
           <div key={i} className="glass rounded-2xl p-8 border border-white/5 flex flex-col items-center group hover:border-cyan-500/30 transition-all cursor-pointer">
              <span className="text-4xl mb-4 group-hover:scale-125 transition-transform">{item.icon}</span>
              <h3 className="text-xl font-bold text-indigo-100 mb-2 capitalize">{t(item.skill)}</h3>
              <p className="text-sm text-indigo-400 text-center">AI-powered assessment and improvement.</p>
           </div>
         ))}
      </div>
    </main>
  )
}
