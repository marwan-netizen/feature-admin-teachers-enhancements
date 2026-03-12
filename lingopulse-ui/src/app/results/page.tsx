'use client'

export default function ResultsPage() {
  return (
    <div className="min-h-screen bg-indigo-950 p-8">
      <header className="mb-12 text-center">
        <div className="w-32 h-32 rounded-full border-4 border-cyan-400 mx-auto mb-6 flex items-center justify-center shadow-[0_0_30px_rgba(34,211,238,0.4)]">
           <span className="text-4xl font-bold text-cyan-400">B2.4</span>
        </div>
        <h1 className="text-4xl font-bold text-indigo-100 mb-2">Your Performance Report</h1>
        <p className="text-indigo-400">Upper Intermediate - You can interact with a degree of fluency.</p>
      </header>

      <div className="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
         <div className="glass rounded-3xl p-8 border border-white/5">
            <h3 className="text-lg font-bold text-cyan-400 mb-6">Skill Breakdown</h3>
            <div className="space-y-6">
               {[
                 { skill: 'Reading', score: 85 },
                 { skill: 'Listening', score: 72 },
                 { skill: 'Writing', score: 90 },
                 { skill: 'Speaking', score: 88 },
               ].map((s) => (
                 <div key={s.skill} className="space-y-2">
                    <div className="flex justify-between text-sm">
                       <span className="text-indigo-200">{s.skill}</span>
                       <span className="text-cyan-400 font-bold">{s.score}%</span>
                    </div>
                    <div className="h-2 bg-indigo-900 rounded-full overflow-hidden">
                       <div className="h-full bg-cyan-500 rounded-full" style={{ width: `${s.score}%` }} />
                    </div>
                 </div>
               ))}
            </div>
         </div>

         <div className="space-y-8">
            <div className="glass rounded-3xl p-8 border border-cyan-500/20 bg-cyan-500/5">
               <h3 className="text-lg font-bold text-cyan-400 mb-4">AI Insights</h3>
               <p className="text-indigo-200 leading-relaxed italic">
                 "Your speaking fluency has improved by 15% this month! You are using more complex transition words. Focus on refining your pronunciation of 'th' sounds."
               </p>
            </div>

            <div className="glass rounded-3xl p-8 border border-white/5">
               <h3 className="text-lg font-bold text-indigo-100 mb-4">Recommended Next Steps</h3>
               <ul className="space-y-4">
                  <li className="flex gap-4 items-center p-3 bg-white/5 rounded-xl border border-white/5 hover:border-cyan-500/30 transition-all cursor-pointer">
                     <span className="text-2xl">🎧</span>
                     <span className="text-sm text-indigo-200">Practice Advanced Listening: BBC News 102</span>
                  </li>
                  <li className="flex gap-4 items-center p-3 bg-white/5 rounded-xl border border-white/5 hover:border-cyan-500/30 transition-all cursor-pointer">
                     <span className="text-2xl">📚</span>
                     <span className="text-sm text-indigo-200">Vocab Mastery: Academic Idioms</span>
                  </li>
               </ul>
            </div>
         </div>

         <div className="md:col-span-2 flex gap-4 justify-center mt-8">
            <button className="px-10 py-4 bg-cyan-500 hover:bg-cyan-400 text-indigo-950 rounded-2xl font-extrabold transition-all shadow-[0_0_20px_rgba(34,211,238,0.3)]">
               Download PDF Certificate
            </button>
            <button className="px-10 py-4 glass hover:bg-white/5 border border-white/10 text-white rounded-2xl font-bold transition-all">
               Share on LinkedIn
            </button>
         </div>
      </div>
    </div>
  )
}
