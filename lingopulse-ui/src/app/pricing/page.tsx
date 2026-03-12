'use client'
import { useState } from 'react'

export default function PricingPage() {
  const [isYearly, setIsYearly] = useState(true)

  return (
    <div className="min-h-screen bg-indigo-950 p-8 flex flex-col items-center justify-center relative overflow-hidden">
       <header className="mb-16 text-center relative z-10">
          <h1 className="text-5xl font-extrabold text-indigo-100 mb-4">Invest in Your Future</h1>
          <p className="text-indigo-400 mb-10">Choose the plan that fits your learning journey.</p>

          <div className="flex items-center justify-center gap-6">
             <span className={`text-sm font-bold ${!isYearly ? 'text-cyan-400' : 'text-indigo-500'}`}>Monthly</span>
             <button
               onClick={() => setIsYearly(!isYearly)}
               className="w-16 h-8 bg-indigo-800 rounded-full relative p-1 cursor-pointer border border-indigo-700"
             >
                <div className={`w-6 h-6 bg-cyan-400 rounded-full absolute transition-all duration-300 ${isYearly ? 'right-1 shadow-[0_0_15px_rgba(34,211,238,0.5)]' : 'left-1'}`} />
             </button>
             <div className="flex items-center gap-2">
                <span className={`text-sm font-bold ${isYearly ? 'text-cyan-400' : 'text-indigo-500'}`}>Yearly</span>
                <span className="px-3 py-1 bg-cyan-500/10 border border-cyan-500/30 rounded-lg text-[10px] font-extrabold text-cyan-400">SAVE 20%</span>
             </div>
          </div>
       </header>

       <div className="grid grid-cols-1 md:grid-cols-3 gap-8 w-full max-w-6xl relative z-10">
          {/* Free Plan */}
          <div className="glass rounded-3xl p-10 border border-white/5 flex flex-col">
             <h3 className="text-xl font-bold text-indigo-300 mb-2">Free</h3>
             <div className="text-4xl font-extrabold text-indigo-100 mb-8">-bash<span className="text-sm font-normal text-indigo-500">/mo</span></div>
             <ul className="space-y-4 mb-12 flex-1">
                {['Basic Vocabulary', 'MCQ Tests', 'Community Support'].map(f => (
                  <li key={f} className="flex items-center gap-3 text-sm text-indigo-200">
                     <span className="text-cyan-500">✓</span> {f}
                  </li>
                ))}
             </ul>
             <button className="w-full py-3 bg-white/5 border border-white/10 hover:bg-white/10 text-white rounded-xl font-bold transition-all">
                Get Started
             </button>
          </div>

          {/* Pro Plan */}
          <div className="glass rounded-3xl p-10 border border-cyan-500/50 bg-cyan-500/5 relative flex flex-col shadow-[0_20px_50px_rgba(0,0,0,0.5)] scale-105">
             <div className="absolute -top-4 left-1/2 -translate-x-1/2 px-4 py-1 bg-cyan-500 text-indigo-950 rounded-full text-[10px] font-extrabold uppercase tracking-widest shadow-lg">Most Popular</div>
             <h3 className="text-xl font-bold text-cyan-400 mb-2">Pro</h3>
             <div className="text-4xl font-extrabold text-indigo-100 mb-8">{isYearly ? '9' : '4'}<span className="text-sm font-normal text-indigo-500">/mo</span></div>
             <ul className="space-y-4 mb-12 flex-1">
                {['AI Speaking Lab', 'AI Writing Assistant', 'Real-time Live Sessions', 'Daily Personalized Plans'].map(f => (
                  <li key={f} className="flex items-center gap-3 text-sm text-indigo-100">
                     <span className="text-cyan-400">✓</span> {f}
                  </li>
                ))}
             </ul>
             <button className="w-full py-4 bg-cyan-500 hover:bg-cyan-400 text-indigo-950 rounded-xl font-extrabold transition-all shadow-[0_0_20px_rgba(34,211,238,0.4)]">
                Upgrade to Pro
             </button>
          </div>

          {/* Enterprise Plan */}
          <div className="glass rounded-3xl p-10 border border-white/5 flex flex-col">
             <h3 className="text-xl font-bold text-indigo-300 mb-2">Enterprise</h3>
             <div className="text-4xl font-extrabold text-indigo-100 mb-8">Custom</div>
             <ul className="space-y-4 mb-12 flex-1">
                {['Unlimited Classes', 'Advanced Analytics', 'Custom AI Models', 'Priority Support'].map(f => (
                  <li key={f} className="flex items-center gap-3 text-sm text-indigo-200">
                     <span className="text-cyan-500">✓</span> {f}
                  </li>
                ))}
             </ul>
             <button className="w-full py-3 bg-white/5 border border-white/10 hover:bg-white/10 text-white rounded-xl font-bold transition-all">
                Contact Sales
             </button>
          </div>
       </div>

       <div className="mt-16 flex gap-8 relative z-10 grayscale opacity-50">
          <span className="text-2xl font-bold">VISA</span>
          <span className="text-2xl font-bold">MASTERCARD</span>
          <span className="text-2xl font-bold">APPLE PAY</span>
       </div>
    </div>
  )
}
