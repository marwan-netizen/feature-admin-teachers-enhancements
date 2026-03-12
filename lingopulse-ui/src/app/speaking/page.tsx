'use client'
import { useState, useEffect } from 'react'

export default function SpeakingAssessment() {
  const [isRecording, setIsRecording] = useState(false)
  const [progress, setProgress] = useState(0)

  useEffect(() => {
    let interval: any
    if (isRecording) {
      interval = setInterval(() => {
        setProgress(prev => (prev < 100 ? prev + 0.5 : 100))
      }, 50)
    }
    return () => clearInterval(interval)
  }, [isRecording])

  return (
    <div className="min-h-screen bg-indigo-950 p-8 flex flex-col items-center justify-center relative overflow-hidden">
      <div className="absolute top-8 left-8 flex items-center gap-4">
        <button className="glass px-4 py-2 rounded-lg text-indigo-300 hover:text-cyan-400 transition-colors">
          &larr; Exit
        </button>
        <span className="text-sm font-medium text-indigo-400">Task 3 of 5</span>
      </div>

      <div className="absolute top-8 right-8 glass px-4 py-2 rounded-lg flex items-center gap-2">
         <span className="w-2 h-2 rounded-full bg-cyan-400 animate-pulse" />
         <span className="text-sm font-mono font-bold text-cyan-400">02:45</span>
      </div>

      <div className="w-full max-w-2xl glass rounded-3xl p-12 border border-white/10 relative z-10 text-center">
        <h2 className="text-lg font-semibold text-cyan-400 mb-4 uppercase tracking-widest">Question Prompt</h2>
        <p className="text-2xl font-medium text-indigo-100 leading-relaxed mb-12">
           "Describe your favorite city and explain why it has a special place in your heart."
        </p>

        <div className="relative h-48 flex items-center justify-center mb-12">
           {/* Audio Wave Simulation */}
           <div className="flex gap-1.5 h-16 items-center">
              {[...Array(20)].map((_, i) => (
                <div key={i} className={`w-1.5 rounded-full transition-all duration-300 ${isRecording ? 'bg-cyan-400 animate-pulse' : 'bg-indigo-800'}`}
                     style={{ height: isRecording ? `${Math.random() * 100 + 20}%` : '20%' }} />
              ))}
           </div>

           {isRecording && (
              <div className="absolute inset-0 flex items-center justify-center">
                 <div className="w-40 h-40 rounded-full border border-cyan-500/30 animate-ping" />
              </div>
           )}
        </div>

        <button
          onClick={() => setIsRecording(!isRecording)}
          className={`w-24 h-24 rounded-full flex items-center justify-center transition-all duration-500 ${isRecording ? 'bg-red-500 shadow-[0_0_30px_rgba(239,68,68,0.5)] scale-110' : 'bg-cyan-500 shadow-[0_0_30px_rgba(34,211,238,0.5)] hover:scale-105'}`}
        >
           {isRecording ? (
              <div className="w-8 h-8 bg-white rounded-sm" />
           ) : (
              <div className="w-0 h-0 border-t-[15px] border-t-transparent border-l-[25px] border-l-indigo-950 border-b-[15px] border-b-transparent ml-2" />
           )}
        </button>
        <p className="mt-6 text-indigo-300 font-medium">
          {isRecording ? 'Recording in progress...' : 'Tap to start recording'}
        </p>
      </div>

      <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-4xl">
         <div className="glass rounded-2xl p-6 border border-white/5">
            <h4 className="text-xs font-bold text-indigo-400 uppercase tracking-widest mb-4">Pronunciation</h4>
            <div className="text-2xl font-bold text-cyan-400">{isRecording ? 'Analyzing...' : '88%'}</div>
         </div>
         <div className="glass rounded-2xl p-6 border border-white/5">
            <h4 className="text-xs font-bold text-indigo-400 uppercase tracking-widest mb-4">Fluency</h4>
            <div className="text-2xl font-bold text-cyan-400">{isRecording ? 'Analyzing...' : '92%'}</div>
         </div>
         <div className="glass rounded-2xl p-6 border border-white/5">
            <h4 className="text-xs font-bold text-indigo-400 uppercase tracking-widest mb-4">Vocabulary</h4>
            <div className="text-2xl font-bold text-cyan-400">{isRecording ? 'Analyzing...' : '85%'}</div>
         </div>
      </div>
    </div>
  )
}
