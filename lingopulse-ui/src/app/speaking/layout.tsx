import { LanguageToggle } from '@/components/LanguageToggle'

export default function SpeakingLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="relative min-h-screen">
      <div className="absolute top-8 right-8 z-50">
         <LanguageToggle />
      </div>
      {children}
    </div>
  )
}
