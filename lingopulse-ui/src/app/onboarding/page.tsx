'use client'
import { useState } from 'react'

export default function OnboardingPage() {
  const [step, setStep] = useState(3) // Start at Level Test for demo

  return (
    <div className="min-h-screen bg-indigo-950 p-8 flex flex-col items-center justify-center relative overflow-hidden">
       {/* Stepper */}
       <div className="w-full max-w-2xl mb-16 flex items-center gap-4 relative z-10">
          {[1, 2, 3].map((s) => (
             <div key={s} className="flex-1 flex flex-col items-center gap-3">
                <div className={`w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm transition-all duration-500 ${s === step ? 'bg-cyan-500 text-indigo-950 shadow-[0_0_20px_rgba(34,211,238,0.5)] scale-110' : s < step ? 'bg-cyan-800 text-cyan-400' : 'bg-indigo-900 text-indigo-500'}`}>
                   {s < step ? '✓' : s}
                </div>
                <span className={`text-[10px] font-bold uppercase tracking-widest ${s === step ? 'text-cyan-400' : 'text-indigo-500'}`}>
                   {s === 1 ? 'Personal Info' : s === 2 ? 'Goals' : 'Level Test'}
                </span>
             </div>
          ))}
       </div>

       <div className="w-full max-w-4xl glass rounded-3xl p-12 border border-white/10 relative z-10 flex flex-col items-center text-center">
          <header className="mb-12">
             <h1 className="text-4xl font-extrabold text-indigo-100 mb-2">AI Proficiency Assessment</h1>
             <p className="text-indigo-400">Let's find your starting point with a quick listening and vocabulary check.</p>
          </header>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-12 w-full mb-12">
             <div className="p-8 rounded-3xl bg-white/5 border border-white/5 hover:border-cyan-500/30 transition-all text-left group cursor-pointer">
                <div className="text-4xl mb-6 group-hover:scale-125 transition-transform">🎧</div>
                <h3 className="text-xl font-bold text-indigo-100 mb-4">Listening Test</h3>
                <p className="text-sm text-indigo-400 mb-8 leading-relaxed">Listen to a short conversation and answer 3 questions to assess your auditory comprehension.</p>
                <button className="w-full py-3 bg-indigo-800/50 hover:bg-cyan-500 text-indigo-200 hover:text-indigo-950 rounded-xl font-bold transition-all border border-indigo-700 hover:border-cyan-500">
                   Start Audio Test
                </button>
             </div>

             <div className="p-8 rounded-3xl bg-white/5 border border-white/5 hover:border-cyan-500/30 transition-all text-left group cursor-pointer">
                <div className="text-4xl mb-6 group-hover:scale-125 transition-transform">📚</div>
                <h3 className="text-xl font-bold text-indigo-100 mb-4">Vocabulary Quiz</h3>
                <p className="text-sm text-indigo-400 mb-8 leading-relaxed">Match 10 words with their meanings to determine your current CEFR vocabulary range.</p>
                <button className="w-full py-3 bg-indigo-800/50 hover:bg-cyan-500 text-indigo-200 hover:text-indigo-950 rounded-xl font-bold transition-all border border-indigo-700 hover:border-cyan-500">
                   Start Word Quiz
                </button>
             </div>
          </div>

          <div className="w-full pt-12 border-t border-white/5 flex flex-col items-center">
             <h3 className="text-lg font-bold text-indigo-100 mb-8 uppercase tracking-widest">Choose Your AI Tutor</h3>
             <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full mb-12">
                {[
                  { name: 'Friendly Sophia', icon: '👩‍🏫', style: 'Conversational' },
                  { name: 'Academic Marcus', icon: '👨‍🎓', style: 'Formal' },
                  { name: 'Energetic Leo', icon: '🕺', style: 'Fast-paced' },
                ].map((t) => (
                  <div key={t.name} className="p-6 rounded-2xl bg-white/5 border border-white/5 hover:border-cyan-500/50 transition-all cursor-pointer group text-center flex flex-col items-center relative overflow-hidden">
                     <div className="text-4xl mb-4 group-hover:scale-125 transition-transform">{t.icon}</div>
                     <h4 className="font-bold text-indigo-100 mb-1">{t.name}</h4>
                     <p className="text-[10px] text-cyan-400 font-bold uppercase tracking-widest">{t.style}</p>
                     <div className="absolute top-2 right-2 w-4 h-4 rounded-full border border-white/20 group-hover:bg-cyan-500 group-hover:border-cyan-500 transition-all" />
                  </div>
                ))}
             </div>
             <button className="px-12 py-4 bg-cyan-500 hover:bg-cyan-400 text-indigo-950 rounded-2xl font-extrabold transition-all shadow-xl shadow-cyan-500/30 scale-100 hover:scale-105">
                Complete Onboarding
             </button>
          </div>
       </div>
    </div>
  )
}
