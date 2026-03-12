'use client'
import { useState } from 'react'

export default function AdminDashboard() {
  return (
    <div className="min-h-screen bg-indigo-950 p-8">
      <header className="flex justify-between items-center mb-12">
        <h1 className="text-3xl font-bold cyan-glow text-cyan-400">System Mission Control</h1>
        <div className="flex gap-4">
           <div className="glass px-6 py-2 rounded-full border border-green-500/30 text-green-400 flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
              Groq: Online
           </div>
           <div className="glass px-6 py-2 rounded-full border border-green-500/30 text-green-400 flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
              Gemini: Online
           </div>
        </div>
      </header>

      <main className="grid grid-cols-1 md:grid-cols-4 gap-8">
         {/* System Pulse */}
         <div className="md:col-span-3 glass rounded-2xl p-8 border border-white/5">
            <h3 className="text-lg font-semibold mb-8 text-cyan-400">System Pulse Monitor</h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-8">
               <div className="space-y-4">
                  <div className="flex justify-between text-sm text-indigo-300">
                     <span>CPU Usage</span>
                     <span className="text-cyan-400 font-bold">42%</span>
                  </div>
                  <div className="h-2 bg-indigo-900 rounded-full overflow-hidden">
                     <div className="h-full bg-cyan-500 rounded-full" style={{ width: '42%' }} />
                  </div>
               </div>
               <div className="space-y-4">
                  <div className="flex justify-between text-sm text-indigo-300">
                     <span>Memory Usage</span>
                     <span className="text-cyan-400 font-bold">68%</span>
                  </div>
                  <div className="h-2 bg-indigo-900 rounded-full overflow-hidden">
                     <div className="h-full bg-cyan-500 rounded-full" style={{ width: '68%' }} />
                  </div>
               </div>
            </div>
            {/* Visual representation of a chart placeholder */}
            <div className="mt-12 h-48 flex items-end gap-2 px-4">
               {[...Array(30)].map((_, i) => (
                  <div key={i} className="flex-1 bg-cyan-500/30 rounded-t-sm hover:bg-cyan-500 transition-all"
                       style={{ height: `${Math.random() * 80 + 20}%` }} />
               ))}
            </div>
         </div>

         {/* AI Model Management */}
         <div className="glass rounded-2xl p-8 border border-white/5 flex flex-col">
            <h3 className="text-lg font-semibold mb-6 text-cyan-400">AI Engine Control</h3>
            <div className="space-y-6">
               <div className="flex justify-between items-center p-4 rounded-xl bg-white/5 border border-cyan-500/30">
                  <span className="font-bold text-indigo-100">Groq (Llama-3.1)</span>
                  <div className="w-10 h-6 bg-cyan-500 rounded-full relative p-1 cursor-pointer">
                     <div className="w-4 h-4 bg-indigo-950 rounded-full absolute right-1" />
                  </div>
               </div>
               <div className="flex justify-between items-center p-4 rounded-xl bg-white/5 border border-white/10">
                  <span className="font-bold text-indigo-300">Google Gemini</span>
                  <div className="w-10 h-6 bg-indigo-800 rounded-full relative p-1 cursor-pointer">
                     <div className="w-4 h-4 bg-indigo-400 rounded-full absolute left-1" />
                  </div>
               </div>
               <div className="flex justify-between items-center p-4 rounded-xl bg-white/5 border border-white/10">
                  <span className="font-bold text-indigo-300">Local (Ollama)</span>
                  <div className="w-10 h-6 bg-indigo-800 rounded-full relative p-1 cursor-pointer">
                     <div className="w-4 h-4 bg-indigo-400 rounded-full absolute left-1" />
                  </div>
               </div>
            </div>
            <button className="mt-auto py-3 bg-indigo-800/50 border border-indigo-700 rounded-xl text-indigo-200 text-sm font-bold transition-all">
               Global AI Settings
            </button>
         </div>

         {/* User Management */}
         <div className="md:col-span-4 glass rounded-2xl p-8 border border-white/5 overflow-x-auto">
            <h3 className="text-lg font-semibold mb-6 text-cyan-400">User Management</h3>
            <table className="w-full text-left">
               <thead className="text-xs uppercase font-bold text-indigo-400 tracking-widest border-b border-white/5">
                  <tr>
                     <th className="pb-4">Name</th>
                     <th className="pb-4">Role</th>
                     <th className="pb-4">Level</th>
                     <th className="pb-4">Status</th>
                     <th className="pb-4">Action</th>
                  </tr>
               </thead>
               <tbody className="text-sm text-indigo-100 divide-y divide-white/5">
                  {[
                     { name: 'Ahmed Al-Farsi', role: 'Student', level: 'B2', status: 'Active' },
                     { name: 'Dr. Sarah Wilson', role: 'Teacher', level: 'C2', status: 'Active' },
                     { name: 'John Doe', role: 'Student', level: 'A1', status: 'Inactive' },
                  ].map((user, i) => (
                     <tr key={i} className="group hover:bg-white/5 transition-colors">
                        <td className="py-4 font-medium">{user.name}</td>
                        <td className="py-4 text-indigo-400">{user.role}</td>
                        <td className="py-4">
                           <span className="px-2 py-1 rounded bg-indigo-900 border border-indigo-800 text-[10px] font-bold">{user.level}</span>
                        </td>
                        <td className="py-4">
                           <span className={`w-2 h-2 rounded-full inline-block mr-2 ${user.status === 'Active' ? 'bg-green-500' : 'bg-red-500'}`} />
                           {user.status}
                        </td>
                        <td className="py-4">
                           <button className="text-cyan-400 hover:underline font-bold">Manage</button>
                        </td>
                     </tr>
                  ))}
               </tbody>
            </table>
         </div>
      </main>
    </div>
  )
}
