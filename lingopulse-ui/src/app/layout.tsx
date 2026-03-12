import './globals.css'
import { LanguageProvider } from '@/context/LanguageContext'
import LayoutClient from './LayoutClient'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-indigo-950 text-white font-sans">
        <LanguageProvider>
          <LayoutClient>{children}</LayoutClient>
        </LanguageProvider>
      </body>
    </html>
  )
}
