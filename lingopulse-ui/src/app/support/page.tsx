'use client'
import { useState } from 'react'

export default function SupportPage() {
  const [messages, setMessages] = useState([
    { sender: 'AI Agent', text: 'Hello Ahmed! I am your LingoPulse AI Support assistant. How can I help you today?', time: '10:00 AM' }
  ])

  return (
    <div className="min-h-screen bg-indigo-950 p-8 flex flex-col items-center justify-center">
       <div className="w-full max-w-4xl h-[80vh] glass rounded-3xl border border-white/10 relative z-10 flex flex-col overflow-hidden shadow-2xl">
          <header className="p-8 border-b border-white/5 flex justify-between items-center bg-white/5 backdrop-blur-md">
             <div className="flex items-center gap-4">
                <div className="relative">
                   <div className="w-12 h-12 rounded-full bg-indigo-900 flex items-center justify-center text-2xl shadow-lg">🤖</div>
                   <div className="absolute bottom-0 right-0 w-3 h-3 bg-green-500 rounded-full border-2 border-indigo-950 animate-pulse" />
                </div>
                <div>
                   <h2 className="text-lg font-bold text-indigo-100">AI Support Agent</h2>
                   <p className="text-[10px] text-cyan-400 font-extrabold uppercase tracking-widest">Online & Ready to Help</p>
                </div>
             </div>
             <div className="flex gap-4">
                <button className="px-4 py-2 glass hover:bg-white/5 border border-white/10 rounded-xl text-xs font-bold text-indigo-300 transition-all uppercase">Report Bug</button>
                <button className="px-4 py-2 glass hover:bg-white/5 border border-white/10 rounded-xl text-xs font-bold text-indigo-300 transition-all uppercase">Human Support</button>
             </div>
          </header>

          <main className="flex-1 p-8 overflow-y-auto space-y-8 scrollbar-hide">
             {messages.map((m, i) => (
                <div key={i} className={`flex ${m.sender === 'User' ? 'justify-end' : 'justify-start'}`}>
                   <div className={`max-w-[70%] p-6 rounded-3xl text-sm leading-relaxed ${m.sender === 'User' ? 'bg-cyan-500 text-indigo-950 font-bold rounded-tr-sm' : 'glass border border-white/10 text-indigo-100 rounded-tl-sm'}`}>
                      {m.text}
                      <div className={`mt-2 text-[10px] ${m.sender === 'User' ? 'text-indigo-900' : 'text-indigo-400'} font-bold`}>{m.time}</div>
                   </div>
                </div>
             ))}
          </main>

          <footer className="p-8 bg-indigo-950/50 backdrop-blur-md">
             <div className="mb-4 flex gap-3">
                {['Speaking Tool?', 'Billing Issue', 'Grammar Tip'].map(t => (
                  <button key={t} className="px-4 py-1.5 glass hover:bg-white/10 border border-white/10 rounded-full text-[10px] font-extrabold text-cyan-400 uppercase tracking-widest transition-all">
                     {t}
                  </button>
                ))}
             </div>
             <div className="flex gap-4 items-center glass p-2 rounded-2xl border border-white/10 bg-white/5">
                <button className="w-10 h-10 rounded-xl hover:bg-white/10 flex items-center justify-center text-xl transition-all opacity-50">📎</button>
                <input
                  type="text"
                  placeholder="Type your message here..."
                  className="flex-1 bg-transparent border-none outline-none text-indigo-100 placeholder:text-indigo-700 text-sm py-2"
                />
                <button className="px-6 py-2 bg-cyan-500 hover:bg-cyan-400 text-indigo-950 rounded-xl font-bold transition-all shadow-[0_0_15px_rgba(34,211,238,0.4)]">
                   Send
                </button>
             </div>
          </footer>
       </div>
    </div>
  )
}
