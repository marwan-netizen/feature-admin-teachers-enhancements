'use client'
import { useState } from 'react'

export default function LeaderboardPage() {
  const [filter, setFilter] = useState('This Week')

  const students = [
    { name: 'Ahmed Al-Farsi', level: 'B2', score: 1250, avatar: '👤' },
    { name: 'Sara Al-Mansoori', level: 'C1', score: 1120, avatar: '👤' },
    { name: 'John Doe', level: 'B2', score: 980, avatar: '👤' },
    { name: 'Emma Watson', level: 'C2', score: 950, avatar: '👤' },
    { name: 'Michael Smith', level: 'B1', score: 870, avatar: '👤' },
  ]

  return (
    <div className="min-h-screen bg-indigo-950 p-8 flex flex-col items-center justify-center relative overflow-hidden">
       <header className="mb-16 text-center relative z-10">
          <h1 className="text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-indigo-400 mb-4 drop-shadow-[0_0_20px_rgba(34,211,238,0.3)]">
             Global Hall of Fame
          </h1>
          <p className="text-indigo-400 font-medium">Top performing students across the world.</p>
       </header>

       {/* Top 3 Podium */}
       <div className="flex items-end justify-center gap-6 mb-16 relative z-10">
          <div className="flex flex-col items-center gap-4">
             <div className="w-20 h-20 rounded-full bg-indigo-900 border-2 border-slate-300 flex items-center justify-center text-3xl shadow-lg">👤</div>
             <div className="h-24 w-28 glass rounded-t-2xl border border-white/10 flex flex-col items-center justify-center relative">
                <span className="text-xl font-bold text-slate-300">2nd</span>
                <span className="text-xs font-bold text-indigo-400 uppercase">1,120 pts</span>
                <div className="absolute -bottom-6 text-sm font-bold text-indigo-200">Sara</div>
             </div>
          </div>
          <div className="flex flex-col items-center gap-4 scale-110 relative -top-6">
             <div className="w-24 h-24 rounded-full bg-indigo-900 border-4 border-cyan-400 flex items-center justify-center text-4xl shadow-[0_0_40px_rgba(34,211,238,0.5)] relative">
                👤
                <div className="absolute -top-4 -right-2 text-3xl rotate-12">👑</div>
             </div>
             <div className="h-32 w-32 glass rounded-t-2xl border border-cyan-500/30 bg-cyan-500/10 flex flex-col items-center justify-center relative">
                <span className="text-2xl font-bold text-cyan-400">1st</span>
                <span className="text-xs font-extrabold text-cyan-300 uppercase tracking-widest">1,250 pts</span>
                <div className="absolute -bottom-6 text-base font-extrabold text-indigo-100">Ahmed</div>
             </div>
          </div>
          <div className="flex flex-col items-center gap-4">
             <div className="w-20 h-20 rounded-full bg-indigo-900 border-2 border-amber-600 flex items-center justify-center text-3xl shadow-lg">👤</div>
             <div className="h-20 w-28 glass rounded-t-2xl border border-white/10 flex flex-col items-center justify-center relative">
                <span className="text-xl font-bold text-amber-600">3rd</span>
                <span className="text-xs font-bold text-indigo-400 uppercase">980 pts</span>
                <div className="absolute -bottom-6 text-sm font-bold text-indigo-200">John</div>
             </div>
          </div>
       </div>

       {/* Leaderboard Table */}
       <div className="w-full max-w-4xl glass rounded-3xl p-8 border border-white/5 relative z-10 mb-20 overflow-hidden">
          <div className="flex justify-between items-center mb-8">
             <div className="flex gap-4">
                {['This Week', 'This Month', 'All Time'].map(f => (
                   <button
                     key={f}
                     onClick={() => setFilter(f)}
                     className={`px-4 py-1.5 rounded-full text-xs font-bold uppercase transition-all ${filter === f ? 'bg-cyan-500 text-indigo-950 shadow-[0_0_15px_rgba(34,211,238,0.4)]' : 'text-indigo-400 hover:text-cyan-400'}`}
                   >
                      {f}
                   </button>
                ))}
             </div>
             <div className="flex gap-2">
                {['Vocab', 'Speaking', 'Grammar'].map(c => (
                   <span key={c} className="text-[10px] font-extrabold text-indigo-500 hover:text-indigo-300 cursor-pointer uppercase tracking-widest">{c}</span>
                ))}
             </div>
          </div>

          <div className="space-y-4">
             {students.map((s, i) => (
                <div key={i} className="flex justify-between items-center p-4 rounded-2xl bg-white/5 border border-white/5 hover:border-cyan-500/20 transition-all cursor-pointer group">
                   <div className="flex items-center gap-6">
                      <span className="text-sm font-bold text-indigo-500 w-4">#{i+1}</span>
                      <div className="w-10 h-10 rounded-full bg-indigo-900/50 flex items-center justify-center text-lg">{s.avatar}</div>
                      <div>
                         <div className="font-bold text-indigo-100">{s.name}</div>
                         <div className="text-[10px] text-indigo-400 font-bold uppercase tracking-widest">{s.level} Level</div>
                      </div>
                   </div>
                   <div className="flex items-center gap-6">
                      <div className="text-right">
                         <div className="text-lg font-extrabold text-cyan-400">{s.score}</div>
                         <div className="text-[10px] text-indigo-500 font-bold uppercase">Points</div>
                      </div>
                      <button className="w-8 h-8 rounded-full glass hover:bg-cyan-500/10 border border-white/10 flex items-center justify-center text-xs opacity-0 group-hover:opacity-100 transition-opacity">
                         &rarr;
                      </button>
                   </div>
                </div>
             ))}
          </div>
       </div>

       {/* Persistent Rank Card */}
       <div className="fixed bottom-8 left-1/2 -translate-x-1/2 w-full max-w-4xl px-4 z-50">
          <div className="glass rounded-2xl p-4 border border-cyan-500/30 flex justify-between items-center shadow-2xl backdrop-blur-xl bg-indigo-950/80">
             <div className="flex items-center gap-6">
                <div className="text-2xl font-black text-cyan-400">#1,245</div>
                <div className="flex items-center gap-4">
                   <div className="w-10 h-10 rounded-full bg-indigo-900 flex items-center justify-center text-xl">👨‍💻</div>
                   <div className="font-bold text-indigo-100">You</div>
                </div>
             </div>
             <div className="flex items-center gap-10">
                <div className="text-right">
                   <div className="text-lg font-extrabold text-indigo-100">450</div>
                   <div className="text-[10px] text-indigo-400 font-bold uppercase">Points</div>
                </div>
                <button className="px-6 py-2 bg-cyan-500 hover:bg-cyan-400 text-indigo-950 rounded-xl font-extrabold text-xs transition-all">
                   Go Pro &rarr;
                </button>
             </div>
          </div>
       </div>
    </div>
  )
}
