'use client'

export default function MediaLibraryPage() {
  const content = [
    { title: 'The Future of AI in Education', type: 'Video', source: 'YouTube', level: 'B2', duration: '12 min' },
    { title: 'Mastering English Grammar', type: 'Podcast', source: 'Spotify', level: 'B1', duration: '45 min' },
    { title: 'Modern English Literature', type: 'Article', source: 'Wikipedia', level: 'C1', duration: '20 min' },
  ]

  return (
    <div className="min-h-screen bg-indigo-950 p-8">
      <header className="mb-12 flex justify-between items-center">
        <div>
          <h1 className="text-4xl font-bold text-cyan-400 mb-2">Media Learning Library</h1>
          <p className="text-indigo-300">Learn English from real-world, high-quality content.</p>
        </div>
        <div className="flex gap-4">
           <button className="glass px-6 py-2 rounded-full border border-indigo-700 text-indigo-300 hover:text-cyan-400 transition-all text-sm font-bold">
              My Saved Resources
           </button>
           <button className="px-6 py-2 bg-indigo-800 border border-indigo-700 rounded-full text-indigo-300 hover:text-cyan-400 transition-all text-sm font-bold">
              Filter By Level
           </button>
        </div>
      </header>

      <section className="mb-16">
        <h2 className="text-2xl font-bold text-indigo-100 mb-8">Daily Discovery</h2>
        <div className="glass rounded-3xl p-10 border border-cyan-500/30 grid grid-cols-1 lg:grid-cols-2 gap-10 items-center overflow-hidden">
           <div className="relative aspect-video rounded-2xl overflow-hidden bg-indigo-900 group cursor-pointer shadow-2xl">
              <div className="absolute inset-0 bg-gradient-to-t from-indigo-950/80 to-transparent" />
              <div className="absolute inset-0 flex items-center justify-center">
                 <div className="w-20 h-20 bg-cyan-500 rounded-full flex items-center justify-center text-indigo-950 text-4xl shadow-[0_0_30px_rgba(34,211,238,0.5)] group-hover:scale-110 transition-transform">
                    ▶️
                 </div>
              </div>
           </div>
           <div className="relative z-10">
              <span className="px-4 py-1.5 bg-cyan-500 text-indigo-950 rounded-full text-[10px] font-extrabold mb-4 inline-block tracking-widest uppercase">Video of the Day</span>
              <h3 className="text-3xl font-extrabold text-indigo-100 mb-4 leading-tight">Artificial Intelligence: The New Frontier of Human Learning</h3>
              <p className="text-indigo-300 mb-8 leading-relaxed">Watch this high-level talk and take the AI-generated vocabulary quiz to master 15 new academic words today.</p>
              <div className="flex gap-4">
                 <button className="px-8 py-3 bg-cyan-500 hover:bg-cyan-400 rounded-xl font-bold text-indigo-950 transition-all">
                    Watch & Learn
                 </button>
                 <button className="px-8 py-3 glass hover:bg-white/5 border border-white/10 rounded-xl font-bold text-indigo-200 transition-all">
                    AI Transcription
                 </button>
              </div>
           </div>
        </div>
      </section>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {content.map((item, i) => (
          <div key={i} className="glass rounded-2xl p-6 border border-white/5 group hover:border-cyan-500/30 transition-all cursor-pointer flex flex-col h-full relative overflow-hidden">
            <div className="flex justify-between items-start mb-6">
               <span className="px-3 py-1 bg-white/5 rounded-lg text-[10px] font-bold text-indigo-400 tracking-widest uppercase">{item.type}</span>
               <span className="text-2xl opacity-30 group-hover:opacity-100 transition-opacity">🔗</span>
            </div>
            <h4 className="text-xl font-bold text-indigo-100 mb-4 leading-tight">{item.title}</h4>
            <div className="mt-auto pt-6 flex justify-between items-center border-t border-white/5">
               <div className="flex gap-2">
                  <span className="px-2 py-0.5 bg-indigo-900 text-cyan-400 rounded text-[10px] font-extrabold border border-cyan-500/20">{item.level}</span>
                  <span className="text-[10px] text-indigo-400 font-bold uppercase">{item.duration}</span>
               </div>
               <span className="text-[10px] text-indigo-500 font-bold uppercase">{item.source}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
