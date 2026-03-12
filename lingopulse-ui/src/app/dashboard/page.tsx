'use client'
import { useAuth } from '@/hooks/useAuth'

export default function Dashboard() {
  const { user, loading } = useAuth()

  if (loading) return <div>Loading...</div>

  return (
    <div className="min-h-screen bg-indigo-950 p-8">
      <header className="flex justify-between items-center mb-12">
        <h1 className="text-3xl font-bold cyan-glow text-cyan-400">Student Dashboard</h1>
        <div className="glass px-6 py-2 rounded-full border border-cyan-500/30">
          Hello, {user?.full_name || 'Guest'} | Level: {user?.role === 'student' ? 'B2' : user?.role}
        </div>
      </header>

      <main className="grid grid-cols-1 md:grid-cols-3 gap-8">
        {/* Welcome Section */}
        <div className="md:col-span-2 glass rounded-2xl p-8 border border-white/5 relative overflow-hidden group">
          <div className="absolute inset-0 bg-gradient-to-br from-cyan-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
          <h2 className="text-2xl font-semibold mb-4 text-indigo-100">Quick Start AI Practice</h2>
          <p className="text-indigo-300 mb-8 max-w-md">Continue your journey to English mastery with real-time AI feedback in speaking and writing.</p>
          <button className="px-8 py-3 bg-cyan-500 hover:bg-cyan-400 rounded-xl font-bold text-indigo-950 transition-all scale-100 hover:scale-105">
            Start Speaking Test
          </button>
        </div>

        {/* Vocabulary Progress */}
        <div className="glass rounded-2xl p-8 border border-white/5 flex flex-col items-center justify-center">
          <div className="w-32 h-32 rounded-full border-4 border-cyan-500/30 border-t-cyan-400 flex items-center justify-center mb-4">
            <span className="text-2xl font-bold">85%</span>
          </div>
          <h3 className="text-lg font-medium text-indigo-200">Vocabulary Goal</h3>
          <p className="text-sm text-indigo-400">850 / 1000 words</p>
        </div>

        {/* Recent Activity */}
        <div className="glass rounded-2xl p-8 border border-white/5">
          <h3 className="text-lg font-semibold mb-4 text-cyan-400">Recent Scores</h3>
          <ul className="space-y-4">
            {[
              { skill: 'Speaking', score: 88, date: '2 days ago' },
              { skill: 'Writing', score: 92, date: '4 days ago' },
              { skill: 'Grammar', score: 75, date: '1 week ago' },
            ].map((activity, i) => (
              <li key={i} className="flex justify-between items-center p-3 rounded-lg bg-white/5 hover:bg-white/10 transition-colors">
                <span className="text-indigo-100 font-medium">{activity.skill}</span>
                <div className="text-right">
                   <div className="text-cyan-400 font-bold">{activity.score}%</div>
                   <div className="text-[10px] text-indigo-400">{activity.date}</div>
                </div>
              </li>
            ))}
          </ul>
        </div>

        {/* Upcoming Tasks */}
        <div className="md:col-span-2 glass rounded-2xl p-8 border border-white/5">
           <h3 className="text-lg font-semibold mb-4 text-cyan-400">Upcoming Assignments</h3>
           <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div className="p-4 rounded-xl border border-white/5 bg-white/5 hover:border-cyan-500/30 transition-all cursor-pointer">
                 <h4 className="font-medium text-indigo-100">Business Presentation Task</h4>
                 <p className="text-xs text-indigo-400 mt-1">Due in 2 days | Classroom 101</p>
              </div>
              <div className="p-4 rounded-xl border border-white/5 bg-white/5 hover:border-cyan-500/30 transition-all cursor-pointer">
                 <h4 className="font-medium text-indigo-100">Academic Vocabulary Quiz</h4>
                 <p className="text-xs text-indigo-400 mt-1">Due tomorrow | Self-paced</p>
              </div>
           </div>
        </div>
      </main>
    </div>
  )
}
