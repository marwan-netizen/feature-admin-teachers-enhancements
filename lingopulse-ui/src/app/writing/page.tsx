'use client'
import { useState } from 'react'

export default function WritingAssessment() {
  const [text, setText] = useState('')
  const [activeFeedback, setActiveFeedback] = useState(null)

  return (
    <div className="min-h-screen bg-indigo-950 p-8 flex flex-col md:flex-row gap-8">
      <div className="flex-1 max-w-4xl glass rounded-3xl p-10 border border-white/10 flex flex-col relative z-10">
        <header className="flex justify-between items-center mb-8">
           <div className="flex items-center gap-4">
              <button className="glass px-4 py-2 rounded-lg text-indigo-300 hover:text-cyan-400 transition-colors">
                 &larr; Exit
              </button>
              <h2 className="text-xl font-bold text-cyan-400">AI Writing Studio</h2>
           </div>
           <div className="flex items-center gap-6">
              <span className="text-sm font-medium text-indigo-400">{text.split(/\s+/).filter(x => x.length).length} / 500 words</span>
              <button className="px-6 py-2 bg-cyan-500 hover:bg-cyan-400 rounded-xl font-bold text-indigo-950 transition-all">
                 Final Grade
              </button>
           </div>
        </header>

        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Start writing your essay here..."
          className="flex-1 bg-transparent text-indigo-100 text-lg leading-relaxed outline-none resize-none placeholder:text-indigo-800"
        />

        <footer className="mt-8 pt-6 border-t border-white/5 flex justify-between items-center">
           <div className="flex gap-4">
              <div className="flex items-center gap-2">
                 <span className="w-2 h-2 rounded-full bg-red-500" />
                 <span className="text-xs font-bold text-indigo-400">Grammar</span>
              </div>
              <div className="flex items-center gap-2">
                 <span className="w-2 h-2 rounded-full bg-yellow-500" />
                 <span className="text-xs font-bold text-indigo-400">Style</span>
              </div>
              <div className="flex items-center gap-2">
                 <span className="w-2 h-2 rounded-full bg-cyan-400" />
                 <span className="text-xs font-bold text-indigo-400">Vocabulary</span>
              </div>
           </div>
           <div className="text-sm text-indigo-300">Auto-saved</div>
        </footer>
      </div>

      <div className="w-full md:w-80 flex flex-col gap-6">
         <div className="glass rounded-2xl p-6 border border-white/5 flex flex-col items-center">
            <h4 className="text-xs font-bold text-indigo-400 uppercase tracking-widest mb-4">Proficiency Meter</h4>
            <div className="w-24 h-24 rounded-full border-4 border-cyan-500/30 border-t-cyan-400 flex items-center justify-center mb-4">
               <span className="text-xl font-bold">B2.1</span>
            </div>
            <p className="text-center text-xs text-indigo-300">Keep writing for more accurate analysis.</p>
         </div>

         <div className="glass rounded-2xl p-6 border border-white/5 flex-1 flex flex-col">
            <h4 className="text-xs font-bold text-cyan-400 uppercase tracking-widest mb-6">AI Feedack</h4>
            <div className="space-y-4">
               <div className="p-4 rounded-xl bg-red-500/10 border border-red-500/20">
                  <h5 className="text-sm font-bold text-red-400 mb-1">Subject-Verb Agreement</h5>
                  <p className="text-xs text-indigo-300">Consider changing 'He have' to 'He has'.</p>
               </div>
               <div className="p-4 rounded-xl bg-cyan-500/10 border border-cyan-500/20">
                  <h5 className="text-sm font-bold text-cyan-400 mb-1">Vocabulary Upgrade</h5>
                  <p className="text-xs text-indigo-300">Try 'metropolitan' instead of 'big city'.</p>
               </div>
               <div className="p-4 rounded-xl bg-yellow-500/10 border border-yellow-500/20">
                  <h5 className="text-sm font-bold text-yellow-400 mb-1">Formal Tone</h5>
                  <p className="text-xs text-indigo-300">Avoid using contractions like 'don't' in formal essays.</p>
               </div>
            </div>
            <div className="mt-auto pt-6">
               <button className="w-full py-3 bg-indigo-800/50 hover:bg-indigo-800 border border-indigo-700 rounded-xl text-indigo-200 text-sm font-bold transition-all">
                  Ask AI Assistant
               </button>
            </div>
         </div>
      </div>
    </div>
  )
}
