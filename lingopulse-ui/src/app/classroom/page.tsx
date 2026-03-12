'use client'

export default function ClassroomPage() {
  const classes = [
    { name: 'Business Communication 101', teacher: 'Dr. Sarah Wilson', level: 'B2', students: 24, next: 'Tomorrow at 10:00 AM' },
    { name: 'Academic Writing Mastery', teacher: 'Prof. Ahmed Al-Farsi', level: 'C1', students: 18, next: 'Live Now' },
    { name: 'Casual English Fluency', teacher: 'Emma Thompson', level: 'B1', students: 30, next: 'Monday at 2:00 PM' },
  ]

  return (
    <div className="min-h-screen bg-indigo-950 p-8">
      <header className="mb-12 flex justify-between items-center">
        <div>
          <h1 className="text-4xl font-bold text-cyan-400 mb-2">Your Virtual Classrooms</h1>
          <p className="text-indigo-300">Join live sessions, interact with teachers, and complete assignments.</p>
        </div>
        <button className="px-8 py-3 bg-cyan-500 hover:bg-cyan-400 rounded-xl font-bold text-indigo-950 transition-all shadow-lg">
           Join New Class
        </button>
      </header>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
        {classes.map((cls, i) => (
          <div key={i} className="glass rounded-3xl p-8 border border-white/5 group hover:border-cyan-500/30 transition-all cursor-pointer relative overflow-hidden flex flex-col md:flex-row gap-8">
             <div className="w-full md:w-32 h-32 rounded-2xl bg-indigo-900/50 flex items-center justify-center text-4xl shadow-inner group-hover:bg-cyan-500/10 transition-colors">
                🏫
             </div>
             <div className="flex-1 flex flex-col">
                <div className="flex justify-between items-start mb-2">
                   <h3 className="text-2xl font-bold text-indigo-100 leading-tight">{cls.name}</h3>
                   {cls.next === 'Live Now' && (
                     <span className="flex items-center gap-2 px-3 py-1 bg-red-500 text-[10px] font-extrabold rounded-full animate-pulse shadow-lg shadow-red-500/30 uppercase tracking-widest">
                        Live Now
                     </span>
                   )}
                </div>
                <p className="text-indigo-400 font-medium mb-6">Instructor: {cls.teacher}</p>
                <div className="mt-auto flex justify-between items-center">
                   <div className="flex gap-3">
                      <span className="px-3 py-1 bg-indigo-900 border border-indigo-800 text-cyan-400 rounded-lg text-[10px] font-extrabold uppercase">{cls.level}</span>
                      <span className="text-[10px] text-indigo-400 font-bold uppercase flex items-center gap-1">👥 {cls.students} Students</span>
                   </div>
                   <p className="text-xs font-bold text-indigo-300">Next: {cls.next}</p>
                </div>
             </div>
          </div>
        ))}
      </div>

      <section>
         <h2 className="text-2xl font-bold text-indigo-100 mb-8">Recent Class Materials</h2>
         <div className="glass rounded-3xl border border-white/5 overflow-hidden">
            <div className="grid grid-cols-1 divide-y divide-white/5">
               {[
                 { title: 'Lecture Notes: Formal Email Writing', date: 'Oct 12', size: '2.4 MB', icon: '📄' },
                 { title: 'Video: Presentation Skills Workshop', date: 'Oct 10', size: '124 MB', icon: '🎬' },
                 { title: 'Reading: Case Study - Global Trends', date: 'Oct 08', size: '1.1 MB', icon: '📖' },
               ].map((doc, i) => (
                 <div key={i} className="p-6 flex justify-between items-center hover:bg-white/5 transition-colors group cursor-pointer">
                    <div className="flex items-center gap-4">
                       <span className="text-2xl group-hover:scale-125 transition-transform">{doc.icon}</span>
                       <div>
                          <h4 className="font-bold text-indigo-100 group-hover:text-cyan-400 transition-colors">{doc.title}</h4>
                          <span className="text-[10px] text-indigo-500 font-bold uppercase">{doc.date}</span>
                       </div>
                    </div>
                    <div className="text-right">
                       <div className="text-xs font-bold text-indigo-300 mb-1">{doc.size}</div>
                       <button className="text-[10px] font-extrabold text-cyan-500 uppercase tracking-widest hover:underline">Download</button>
                    </div>
                 </div>
               ))}
            </div>
         </div>
      </section>
    </div>
  )
}
