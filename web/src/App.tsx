import { ResumeTailor } from "@/components/resume-tailor";

function App() {
  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto max-w-[600px] px-4 py-8 md:py-16">
        <header className="mb-8">
          <h1 className="text-2xl font-semibold tracking-tight text-foreground">
            CV Craft
          </h1>
        </header>
        <ResumeTailor />
      </div>
    </main>
  );
}

export default App;
