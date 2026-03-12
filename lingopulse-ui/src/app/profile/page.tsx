'use client'

export default function ProfilePage() {
  return (
    <div className="min-h-screen bg-indigo-950 p-8 flex flex-col items-center justify-center">
       <div className="w-full max-w-4xl glass rounded-3xl p-12 border border-white/10 relative z-10">
          <header className="flex flex-col md:flex-row items-center gap-10 mb-12">
             <div className="relative">
                <div className="w-40 h-40 rounded-full border-4 border-cyan-400 overflow-hidden shadow-[0_0_30px_rgba(34,211,238,0.3)]">
                   <div className="w-full h-full bg-indigo-900 flex items-center justify-center text-6xl">👨‍💻</div>
                </div>
                <div className="absolute bottom-2 right-2 w-10 h-10 rounded-full bg-cyan-500 border-4 border-indigo-950 flex items-center justify-center text-xs font-bold text-indigo-950">B2</div>
             </div>
             <div className="text-center md:text-left">
                <h1 className="text-4xl font-extrabold text-indigo-100 mb-2">Ahmed Al-Farsi</h1>
                <p className="text-indigo-400 font-medium mb-4 italic">ahmed@lingopulse.ai</p>
                <div className="flex gap-4 justify-center md:justify-start">
                   <span className="px-4 py-1 bg-indigo-900 rounded-full text-xs font-bold text-cyan-400 border border-cyan-500/20">Student Account</span>
                   <span className="px-4 py-1 bg-white/5 rounded-full text-xs font-medium text-indigo-300 border border-white/5">Since Oct 2024</span>
                </div>
             </div>
             <button className="md:ml-auto px-8 py-3 glass hover:bg-white/5 border border-white/10 text-white rounded-xl font-bold transition-all text-sm">
                Edit Profile
             </button>
          </header>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-10">
             <section className="glass rounded-2xl p-8 border border-white/5">
                <h3 className="text-lg font-bold text-cyan-400 mb-6 uppercase tracking-widest">AI Learning Preferences</h3>
                <div className="space-y-6">
                   <div className="flex justify-between items-center">
                      <span className="font-bold text-indigo-100">Business English</span>
                      <div className="w-10 h-6 bg-cyan-500 rounded-full relative p-1">
                         <div className="w-4 h-4 bg-indigo-950 rounded-full absolute right-1" />
                      </div>
                   </div>
                   <div className="flex justify-between items-center">
                      <span className="font-bold text-indigo-300">Academic Writing</span>
                      <div className="w-10 h-6 bg-indigo-800 rounded-full relative p-1">
                         <div className="w-4 h-4 bg-indigo-400 rounded-full absolute left-1" />
                      </div>
                   </div>
                   <div className="flex justify-between items-center">
                      <span className="font-bold text-indigo-100">Daily Vocabulary</span>
                      <div className="w-10 h-6 bg-cyan-500 rounded-full relative p-1">
                         <div className="w-4 h-4 bg-indigo-950 rounded-full absolute right-1" />
                      </div>
                   </div>
                </div>
             </section>

             <section className="glass rounded-2xl p-8 border border-white/5">
                <h3 className="text-lg font-bold text-cyan-400 mb-6 uppercase tracking-widest">Goal Tracker</h3>
                <div className="space-y-8">
                   <div>
                      <div className="flex justify-between text-xs font-bold text-indigo-400 uppercase mb-2">
                         <span>Daily Study Minutes</span>
                         <span className="text-cyan-400">30 / 45m</span>
                      </div>
                      <div className="h-1.5 bg-indigo-900 rounded-full overflow-hidden">
                         <div className="h-full bg-cyan-500 rounded-full shadow-[0_0_10px_rgba(34,211,238,0.5)]" style={{ width: '66%' }} />
                      </div>
                   </div>
                   <div>
                      <div className="flex justify-between text-xs font-bold text-indigo-400 uppercase mb-2">
                         <span>Vocabulary Target</span>
                         <span className="text-cyan-400">15 / 20 words</span>
                      </div>
                      <div className="h-1.5 bg-indigo-900 rounded-full overflow-hidden">
                         <div className="h-full bg-cyan-500 rounded-full shadow-[0_0_10px_rgba(34,211,238,0.5)]" style={{ width: '75%' }} />
                      </div>
                   </div>
                </div>
             </section>

             <section className="md:col-span-2 glass rounded-2xl p-8 border border-white/5">
                <h3 className="text-lg font-bold text-red-400 mb-6 uppercase tracking-widest">Account Security</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                   <div className="flex justify-between items-center p-4 bg-white/5 rounded-xl border border-white/5">
                      <span className="font-bold text-indigo-200">Two-Factor Auth</span>
                      <button className="text-xs font-bold text-cyan-400 hover:underline uppercase tracking-widest">Enable Now</button>
                   </div>
                   <div className="flex justify-between items-center p-4 bg-white/5 rounded-xl border border-white/5">
                      <span className="font-bold text-indigo-200">Change Password</span>
                      <button className="text-xs font-bold text-indigo-400 hover:underline uppercase tracking-widest">Update</button>
                   </div>
                </div>
             </section>
          </div>
       </div>
    </div>
  )
}
