'use client'
import { Sidebar } from '@/components/Sidebar'
import { usePathname } from 'next/navigation'

export default function LayoutClient({ children }: { children: React.ReactNode }) {
  const pathname = usePathname()

  const sidebarPaths = [
    '/dashboard',
    '/test-center',
    '/classroom',
    '/vocabulary',
    '/media-library',
    '/leaderboard',
    '/profile',
    '/support',
    '/speaking',
    '/writing',
    '/results',
    '/onboarding',
    '/pricing',
    '/admin',
    '/teacher-dashboard'
  ]

  const hasSidebar = sidebarPaths.some(p => pathname === p || pathname.startsWith(p + '/'))

  return (
    <div className="flex min-h-screen">
      {hasSidebar && <Sidebar />}
      <main className={`flex-1 transition-all ${hasSidebar ? 'md:ml-64 ml-20' : ''}`}>
         {children}
      </main>
    </div>
  )
}
