'use client'

export default function VocabularyPage() {
  const games = [
    { name: 'Word Race', icon: '🏎️', description: 'Fast-paced word matching.' },
    { name: 'Sentence Architect', icon: '🏗️', description: 'Build correct structures.' },
    { name: 'Phonetic Duel', icon: '⚔️', description: 'Master pronunciation.' },
  ]

  return (
    <div className="min-h-screen bg-indigo-950 p-8">
      <header className="mb-12 flex justify-between items-center">
        <div>
          <h1 className="text-4xl font-bold text-cyan-400 mb-2">AI Vocabulary Lab</h1>
          <p className="text-indigo-300">Master new words with AI-powered personalized exercises.</p>
        </div>
        <div className="glass px-6 py-4 rounded-3xl border border-cyan-500/30 flex items-center gap-4">
           <div className="text-4xl">🔥</div>
           <div>
              <div className="text-xl font-bold text-cyan-400">7 Day Streak</div>
              <div className="text-[10px] text-indigo-400 uppercase tracking-widest font-bold">Keep it up!</div>
           </div>
        </div>
      </header>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-12">
        {/* Word of the Day */}
        <div className="lg:col-span-2 glass rounded-3xl p-10 border border-white/5 relative overflow-hidden group">
           <div className="absolute top-0 right-0 p-10 opacity-10 text-9xl transform rotate-12">📖</div>
           <div className="relative z-10">
              <span className="px-4 py-1.5 bg-cyan-500 text-indigo-950 rounded-full text-xs font-bold mb-6 inline-block">WORD OF THE DAY</span>
              <h2 className="text-5xl font-extrabold text-indigo-100 mb-2">Epiphany</h2>
              <div className="flex items-center gap-4 mb-6">
                 <span className="text-indigo-400 italic">/ɪˈpɪf.ə.ni/</span>
                 <button className="w-10 h-10 rounded-full bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400 hover:bg-cyan-500/20 transition-all">
                    🔊
                 </button>
                 <span className="px-3 py-1 bg-indigo-900 border border-indigo-800 rounded-lg text-xs font-bold text-cyan-400">CEFR C1</span>
              </div>
              <p className="text-xl text-indigo-200 mb-8 max-w-2xl leading-relaxed">
                 "A moment of sudden and great revelation or realization."
              </p>
              <div className="p-6 bg-white/5 rounded-2xl border border-white/5 border-l-cyan-400 border-l-4">
                 <p className="text-indigo-300 italic text-lg">"She had an epiphany while walking in the park; she realized she wanted to change her career."</p>
              </div>
           </div>
        </div>

        {/* Global Leaderboard Snapshot */}
        <div className="glass rounded-3xl p-8 border border-white/5">
           <h3 className="text-lg font-bold text-cyan-400 mb-6">Top Performers</h3>
           <div className="space-y-4">
              {[
                { name: 'Ahmed', level: 'C1', score: 1250 },
                { name: 'Sara', level: 'B2', score: 1120 },
                { name: 'John', level: 'B2', score: 980 },
              ].map((u, i) => (
                <div key={i} className="flex justify-between items-center p-3 rounded-xl bg-white/5 border border-white/5 hover:border-cyan-500/30 transition-all cursor-pointer">
                   <div className="flex items-center gap-4">
                      <div className="w-10 h-10 rounded-full bg-indigo-800/50 flex items-center justify-center font-bold text-indigo-200">#{i+1}</div>
                      <div>
                         <div className="font-bold text-indigo-100">{u.name}</div>
                         <div className="text-[10px] text-indigo-400 font-bold">{u.level}</div>
                      </div>
                   </div>
                   <div className="text-cyan-400 font-extrabold">{u.score} pts</div>
                </div>
              ))}
           </div>
           <button className="w-full mt-6 py-2 text-sm font-bold text-indigo-400 hover:text-cyan-400 transition-colors">View All Rankings &rarr;</button>
        </div>
      </div>

      <section>
         <h3 className="text-2xl font-bold text-indigo-100 mb-8">Vocabulary Arena</h3>
         <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {games.map((g) => (
              <div key={g.name} className="glass rounded-3xl p-8 border border-white/5 group hover:border-cyan-500/30 transition-all cursor-pointer flex flex-col items-center text-center">
                 <div className="w-20 h-20 bg-gradient-to-br from-indigo-800 to-cyan-800 rounded-3xl flex items-center justify-center text-4xl mb-6 shadow-xl group-hover:scale-110 transition-transform">
                    {g.icon}
                 </div>
                 <h4 className="text-xl font-bold text-indigo-100 mb-2">{g.name}</h4>
                 <p className="text-sm text-indigo-400 mb-6">{g.description}</p>
                 <button className="w-full py-3 bg-cyan-500/10 hover:bg-cyan-500 text-cyan-400 hover:text-indigo-950 border border-cyan-500/30 rounded-xl font-bold transition-all">
                    Play Now
                 </button>
              </div>
            ))}
         </div>
      </section>
    </div>
  )
}
