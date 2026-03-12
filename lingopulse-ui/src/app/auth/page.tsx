'use client'
import { useState } from 'react'

export default function AuthPage() {
  const [isLogin, setIsLogin] = useState(true)

  return (
    <div className="min-h-screen bg-indigo-950 flex items-center justify-center p-4">
      <div className="absolute inset-0 bg-gradient-to-br from-indigo-950 via-indigo-900 to-cyan-900/20" />
      <div className="absolute inset-0 opacity-20 pointer-events-none" style={{
        backgroundImage: 'radial-gradient(circle at 50% 50%, rgba(34,211,238,0.15) 0%, transparent 50%)',
      }} />

      <div className="glass w-full max-w-md rounded-3xl p-10 border border-white/10 relative z-10 shadow-[0_25px_50px_-12px_rgba(0,0,0,0.5)]">
        <div className="text-center mb-10">
          <h2 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-indigo-400">
            LingoPulse AI
          </h2>
          <p className="mt-2 text-indigo-300">Join the Future of Learning</p>
        </div>

        <div className="flex bg-white/5 p-1.5 rounded-2xl mb-8 relative">
          <div className={`absolute inset-y-1.5 w-[calc(50%-6px)] bg-cyan-500 rounded-xl transition-all duration-300 ${isLogin ? 'left-1.5' : 'left-[calc(50%+3px)]'}`} />
          <button onClick={() => setIsLogin(true)} className={`flex-1 py-2 text-sm font-bold relative z-10 transition-colors ${isLogin ? 'text-indigo-950' : 'text-indigo-300'}`}>
            Login
          </button>
          <button onClick={() => setIsLogin(false)} className={`flex-1 py-2 text-sm font-bold relative z-10 transition-colors ${!isLogin ? 'text-indigo-950' : 'text-indigo-300'}`}>
            Register
          </button>
        </div>

        <form className="space-y-6">
          {!isLogin && (
             <div>
                <label className="block text-sm font-medium text-indigo-200 mb-2">Full Name</label>
                <input type="text" className="w-full bg-white/5 border border-white/10 rounded-xl px-5 py-3 text-indigo-100 focus:border-cyan-500/50 focus:ring-1 focus:ring-cyan-500/50 outline-none transition-all placeholder:text-indigo-500/50" placeholder="Ahmed Al-Farsi" />
             </div>
          )}
          <div>
            <label className="block text-sm font-medium text-indigo-200 mb-2">Email Address</label>
            <input type="email" className="w-full bg-white/5 border border-white/10 rounded-xl px-5 py-3 text-indigo-100 focus:border-cyan-500/50 focus:ring-1 focus:ring-cyan-500/50 outline-none transition-all placeholder:text-indigo-500/50" placeholder="ahmed@example.com" />
          </div>
          <div>
            <label className="block text-sm font-medium text-indigo-200 mb-2">Password</label>
            <input type="password" className="w-full bg-white/5 border border-white/10 rounded-xl px-5 py-3 text-indigo-100 focus:border-cyan-500/50 focus:ring-1 focus:ring-cyan-500/50 outline-none transition-all placeholder:text-indigo-500/50" placeholder="••••••••" />
          </div>

          <button className="w-full py-4 bg-cyan-500 hover:bg-cyan-400 text-indigo-950 font-extrabold rounded-2xl transition-all shadow-[0_0_20px_rgba(34,211,238,0.4)] hover:shadow-[0_0_30px_rgba(34,211,238,0.6)]">
            {isLogin ? 'Sign In' : 'Create Account'}
          </button>
        </form>

        <div className="mt-8 flex items-center gap-4">
           <div className="flex-1 h-px bg-white/10" />
           <span className="text-xs text-indigo-500 uppercase font-bold tracking-widest">or continue with</span>
           <div className="flex-1 h-px bg-white/10" />
        </div>

        <div className="mt-8 grid grid-cols-2 gap-4">
           <button className="flex items-center justify-center gap-2 py-3 bg-white/5 border border-white/10 rounded-xl hover:bg-white/10 transition-all font-medium text-indigo-200">
              <span className="text-lg">G</span>
              Google
           </button>
           <button className="flex items-center justify-center gap-2 py-3 bg-white/5 border border-white/10 rounded-xl hover:bg-white/10 transition-all font-medium text-indigo-200">
              <span className="text-lg">A</span>
              Apple
           </button>
        </div>
      </div>
    </div>
  )
}
