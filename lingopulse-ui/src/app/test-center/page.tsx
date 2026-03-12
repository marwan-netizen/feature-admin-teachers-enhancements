'use client'
import { useLanguage } from '@/context/LanguageContext'

export default function TestCenter() {
  const { t } = useLanguage()

  const skills = [
    { id: 'reading', icon: '📖', level: 'B2', duration: '20 min' },
    { id: 'listening', icon: '🎧', level: 'B1', duration: '15 min' },
    { id: 'writing', icon: '✍️', level: 'B2', duration: '30 min' },
    { id: 'speaking', icon: '🎙️', level: 'B2', duration: '10 min' },
  ]

  return (
    <div className="min-h-screen bg-indigo-950 p-8">
      <header className="mb-12">
        <h1 className="text-4xl font-bold text-cyan-400 mb-2">Test Center</h1>
        <p className="text-indigo-300">Choose a skill to assess your current proficiency.</p>
      </header>

      <section className="mb-12">
        <div className="glass rounded-3xl p-10 border border-cyan-500/30 relative overflow-hidden">
           <div className="absolute top-0 right-0 p-8 opacity-10 text-8xl">🚀</div>
           <h2 className="text-2xl font-bold text-indigo-100 mb-4">Recommended for You</h2>
           <p className="text-indigo-300 mb-6 max-w-lg">Based on your recent activity, we recommend taking the **Business English Speaking Test** to improve your fluency in professional settings.</p>
           <button className="px-8 py-3 bg-cyan-500 hover:bg-cyan-400 rounded-xl font-bold text-indigo-950 transition-all">
              Start Recommended Test
           </button>
        </div>
      </section>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        {skills.map((skill) => (
          <div key={skill.id} className="glass rounded-2xl p-8 border border-white/5 group hover:border-cyan-500/30 transition-all cursor-pointer flex flex-col items-center">
            <span className="text-5xl mb-6 group-hover:scale-110 transition-transform">{skill.icon}</span>
            <h3 className="text-xl font-bold text-indigo-100 mb-2 capitalize">{skill.id}</h3>
            <div className="flex gap-2 mb-6">
              <span className="px-3 py-1 bg-indigo-900 rounded-full text-xs font-bold text-cyan-400 border border-cyan-500/20">{skill.level}</span>
              <span className="px-3 py-1 bg-white/5 rounded-full text-xs font-medium text-indigo-400 border border-white/5">{skill.duration}</span>
            </div>
            <button className="w-full py-2 bg-indigo-800/50 hover:bg-indigo-800 border border-indigo-700 rounded-lg text-indigo-200 text-sm font-bold transition-all">
              View Tests
            </button>
          </div>
        ))}
      </div>
    </div>
  )
}
