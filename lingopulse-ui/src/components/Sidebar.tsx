'use client'
import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { useLanguage } from '@/context/LanguageContext'

export const Sidebar = () => {
  const pathname = usePathname()
  const { t } = useLanguage()

  const links = [
    { name: 'Dashboard', icon: '📊', path: '/dashboard' },
    { name: 'Test Center', icon: '📝', path: '/test-center' },
    { name: 'Classroom', icon: '🏫', path: '/classroom' },
    { name: 'Vocabulary', icon: '📚', path: '/vocabulary' },
    { name: 'Media', icon: '🎧', path: '/media-library' },
    { name: 'Leaderboard', icon: '🏆', path: '/leaderboard' },
    { name: 'Profile', icon: '👤', path: '/profile' },
    { name: 'Admin', icon: '🛠️', path: '/admin' },
  ]

  return (
    <aside className="fixed left-0 top-0 h-screen w-20 md:w-64 glass border-r border-white/5 z-50 flex flex-col items-center md:items-start transition-all overflow-hidden group">
       <div className="p-8 w-full border-b border-white/5 flex items-center gap-4">
          <Link href="/" className="flex items-center gap-4">
            <div className="w-10 h-10 rounded-xl bg-cyan-500 shadow-[0_0_20px_rgba(34,211,238,0.5)] flex items-center justify-center text-indigo-950 font-black">LP</div>
            <span className="hidden md:block text-xl font-black text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-indigo-400">LingoPulse</span>
          </Link>
       </div>

       <nav className="flex-1 w-full p-4 space-y-2 overflow-y-auto scrollbar-hide">
          {links.map((link) => {
            const isActive = pathname === link.path || pathname.startsWith(link.path + '/')
            return (
              <Link key={link.path} href={link.path}>
                 <div className={`flex items-center gap-4 p-4 rounded-xl transition-all ${isActive ? 'bg-cyan-500 text-indigo-950 shadow-[0_0_15px_rgba(34,211,238,0.3)]' : 'text-indigo-400 hover:bg-white/5 hover:text-cyan-400'}`}>
                    <span className="text-xl">{link.icon}</span>
                    <span className={`hidden md:block font-bold text-sm ${isActive ? 'text-indigo-950' : ''}`}>{link.name}</span>
                 </div>
              </Link>
            )
          })}
       </nav>

       <div className="p-4 w-full">
          <Link href="/support">
             <div className={`flex items-center gap-4 p-4 rounded-xl ${pathname === '/support' ? 'bg-cyan-500 text-indigo-950' : 'bg-indigo-900/50 border border-indigo-700/50 text-cyan-400 hover:bg-cyan-500 hover:text-indigo-950'} transition-all cursor-pointer`}>
                <span className="text-xl">🤖</span>
                <span className="hidden md:block font-bold text-sm">AI Support</span>
             </div>
          </Link>
       </div>
    </aside>
  )
}
