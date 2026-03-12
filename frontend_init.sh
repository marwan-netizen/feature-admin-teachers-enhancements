# Check if Next.js is installed, if not, create a placeholder structure and instructions
# Since I cannot run interactive 'npx create-next-app', I will simulate the structure
mkdir -p lingopulse-ui/src/app
mkdir -p lingopulse-ui/src/components
mkdir -p lingopulse-ui/src/lib
mkdir -p lingopulse-ui/src/hooks
mkdir -p lingopulse-ui/public

# Create basic layout and page for verification
cat <<LAYOUT > lingopulse-ui/src/app/layout.tsx
import './globals.css'
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-indigo-950 text-white font-sans">{children}</body>
    </html>
  )
}
LAYOUT

cat <<PAGE > lingopulse-ui/src/app/page.tsx
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-gradient-to-br from-indigo-950 to-indigo-900">
      <h1 className="text-6xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-indigo-400">
        LingoPulse AI
      </h1>
      <p className="mt-4 text-xl text-indigo-200">The Future of English Learning</p>
      <div className="mt-8 flex gap-4">
        <button className="px-6 py-3 bg-cyan-500 hover:bg-cyan-400 rounded-lg font-semibold transition-all shadow-[0_0_15px_rgba(34,211,238,0.5)]">
          Start Journey
        </button>
        <button className="px-6 py-3 bg-indigo-800/50 hover:bg-indigo-800/70 border border-indigo-700 rounded-lg font-semibold backdrop-blur-sm transition-all">
          Learn More
        </button>
      </div>
    </main>
  )
}
PAGE

# Global CSS for glassmorphism
cat <<CSS > lingopulse-ui/src/app/globals.css
@tailwind base;
@tailwind components;
@tailwind utilities;

.glass {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.cyan-glow {
  box-shadow: 0 0 20px rgba(34, 211, 238, 0.3);
}
CSS
