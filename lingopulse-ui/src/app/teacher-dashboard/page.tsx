'use client'

export default function TeacherDashboard() {
  const stats = [
    { label: 'Total Students', value: 124, trend: '+12%' },
    { label: 'Avg. Proficiency', value: 'B2', trend: '+5%' },
    { label: 'Completion Rate', value: '92%', trend: '+3%' },
    { label: 'Pending Evaluations', value: 18, trend: 'High' },
  ]

  const students = [
    { name: 'Ahmed Al-Farsi', level: 'B2', progress: 88, status: 'Active', next: 'Speaking Eval' },
    { name: 'Sara Al-Mansoori', level: 'C1', progress: 92, status: 'Active', next: 'Writing Mastery' },
    { name: 'John Doe', level: 'B1', progress: 75, status: 'Inactive', next: 'N/A' },
  ]

  return (
    <div className="min-h-screen bg-indigo-950 p-8">
      <header className="mb-12 flex justify-between items-center">
        <div>
          <h1 className="text-4xl font-bold text-cyan-400 mb-2">Teacher Mission Control</h1>
          <p className="text-indigo-300">Manage your classes, students, and curriculum with AI support.</p>
        </div>
        <div className="flex gap-4">
           <button className="px-6 py-3 bg-indigo-800 hover:bg-indigo-700 border border-indigo-700 rounded-xl font-bold text-indigo-100 transition-all">
              Create New Test
           </button>
           <button className="px-6 py-3 bg-cyan-500 hover:bg-cyan-400 rounded-xl font-bold text-indigo-950 transition-all shadow-lg">
              Start Live Session
           </button>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-12">
        {stats.map((stat, i) => (
          <div key={i} className="glass rounded-3xl p-8 border border-white/5 relative overflow-hidden group hover:border-cyan-500/30 transition-all cursor-pointer">
             <div className="absolute top-0 right-0 p-4 opacity-5 text-4xl group-hover:scale-125 transition-transform">📈</div>
             <h3 className="text-xs font-bold text-indigo-400 uppercase tracking-widest mb-2">{stat.label}</h3>
             <div className="flex items-end gap-3">
                <span className="text-4xl font-extrabold text-indigo-100">{stat.value}</span>
                <span className={`text-[10px] font-bold mb-1 ${stat.trend.includes('+') || stat.trend === 'High' ? 'text-green-500' : 'text-red-500'}`}>
                   {stat.trend}
                </span>
             </div>
          </div>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
         {/* Class Performance Chart Placeholder */}
         <div className="lg:col-span-2 glass rounded-3xl p-10 border border-white/5">
            <h3 className="text-xl font-bold text-cyan-400 mb-8">Class Performance Overview</h3>
            <div className="h-64 flex items-end gap-6 px-4">
               {[
                 { label: 'Class A', val: 85 },
                 { label: 'Class B', val: 72 },
                 { label: 'Class C', val: 90 },
                 { label: 'Class D', val: 65 },
                 { label: 'Class E', val: 88 },
               ].map((c) => (
                 <div key={c.label} className="flex-1 flex flex-col items-center gap-4 group">
                    <div className="w-full bg-cyan-500/10 rounded-xl relative overflow-hidden h-full">
                       <div className="absolute bottom-0 w-full bg-cyan-500 group-hover:bg-cyan-400 transition-all"
                            style={{ height: `${c.val}%` }} />
                    </div>
                    <span className="text-[10px] font-bold text-indigo-400 uppercase">{c.label}</span>
                 </div>
               ))}
            </div>
         </div>

         {/* Pending Evaluations */}
         <div className="glass rounded-3xl p-8 border border-white/5">
            <h3 className="text-xl font-bold text-cyan-400 mb-6">Pending Review</h3>
            <div className="space-y-4">
               {students.filter(s => s.status === 'Active').map((s, i) => (
                 <div key={i} className="flex justify-between items-center p-4 rounded-xl bg-white/5 border border-white/5 hover:border-cyan-500/30 transition-all cursor-pointer">
                    <div className="flex items-center gap-3">
                       <div className="w-8 h-8 rounded-full bg-indigo-800/50 flex items-center justify-center font-bold text-indigo-200 text-xs">{s.name[0]}</div>
                       <div>
                          <div className="text-sm font-bold text-indigo-100">{s.name}</div>
                          <div className="text-[10px] text-indigo-400 font-bold uppercase">{s.next}</div>
                       </div>
                    </div>
                    <button className="px-4 py-1.5 bg-indigo-800 text-cyan-400 rounded-lg text-[10px] font-extrabold uppercase hover:bg-cyan-500 hover:text-indigo-950 transition-all">Review</button>
                 </div>
               ))}
            </div>
            <button className="w-full mt-6 py-2 text-sm font-bold text-indigo-400 hover:text-cyan-400 transition-colors">View All Submissions &rarr;</button>
         </div>
      </div>
    </div>
  )
}
