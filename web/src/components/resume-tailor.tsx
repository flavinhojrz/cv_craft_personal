import { useEffect, useState } from "react";
import { Loader2 } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Checkbox } from "@/components/ui/checkbox";
import { Label } from "@/components/ui/label";
import { ResultSection } from "@/components/result-section";
import { services } from "@/services/api";
import type { Resume } from "@/types/types";

const SECTIONS = [
  { id: "summary", label: "Summary" },
  { id: "skills", label: "Skills" },
  { id: "experience", label: "Experience" },
  { id: "projects", label: "Projects" },
] as const;

type SectionId = (typeof SECTIONS)[number]["id"];

export function ResumeTailor() {
  const [jobDescription, setJobDescription] = useState("");
  const [resumeData, setResumeData] = useState<Resume | null>(null);
  const [selectedSections, setSelectedSections] = useState<SectionId[]>([
    "summary",
    "skills",
  ]);
  const [isProcessing, setIsProcessing] = useState(false);
  const [isComplete, setIsComplete] = useState(false);
  const [loadingInitial, setLoadingInitial] = useState(true);

  const toggleSection = (sectionId: SectionId) => {
    setSelectedSections((prev) =>
      prev.includes(sectionId)
        ? prev.filter((id) => id !== sectionId)
        : [...prev, sectionId]
    );
  };

  useEffect(() => {
    async function loadData() {
      try {
        const data = await services.getInitialData();
        setResumeData(data);
      } catch (err) {
        alert(err);
      } finally {
        setLoadingInitial(false);
      }
    }
    loadData();
  }, []);

  const handleOptimize = async () => {
    if (!jobDescription.trim() || selectedSections.length === 0 || !resumeData)
      return;
    setIsProcessing(true);
    setIsComplete(false);

    try {
      const optimizeData = await services.optimizeResume({
        instructions: jobDescription,
        sections: selectedSections,
        data: resumeData,
      });
      setResumeData(optimizeData);
      setIsComplete(true);
    } catch (err) {
      alert(err);
    } finally {
      setIsComplete(false);
    }

    setIsProcessing(false);
    setIsComplete(true);
  };

  const handleReset = () => {
    setIsComplete(false);
  };

  if (loadingInitial) {
    return (
      <div className="flex justify-center p-8">
        <Loader2 className="animate-spin" />
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Input Section */}
      <div className="space-y-2">
        <Label
          htmlFor="job-description"
          className="text-sm font-medium text-foreground"
        >
          Target Job Description
        </Label>
        <Textarea
          id="job-description"
          placeholder="Paste the job description here..."
          className="h-[150px] resize-none border-border bg-background text-foreground placeholder:text-muted-foreground"
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
          disabled={isProcessing}
        />
      </div>

      {/* Configuration Section */}
      <div className="space-y-3">
        <Label className="text-sm font-medium text-foreground">
          Sections to Optimize
        </Label>
        <div className="flex flex-wrap gap-4">
          {SECTIONS.map((section) => (
            <div key={section.id} className="flex items-center gap-2">
              <Checkbox
                id={section.id}
                checked={selectedSections.includes(section.id)}
                onCheckedChange={() => toggleSection(section.id)}
                disabled={isProcessing}
              />
              <Label
                htmlFor={section.id}
                className="text-sm font-normal text-foreground cursor-pointer"
              >
                {section.label}
              </Label>
            </div>
          ))}
        </div>
      </div>

      {/* Action Area */}
      <Button
        className="w-full"
        size="lg"
        onClick={handleOptimize}
        disabled={
          isProcessing ||
          !jobDescription.trim() ||
          selectedSections.length === 0
        }
      >
        {isProcessing ? (
          <>
            <Loader2 className="mr-2 h-4 w-4 animate-spin" />
            Processing...
          </>
        ) : (
          "Optimize Resume"
        )}
      </Button>

      {isComplete && resumeData && (
        <ResultSection data={resumeData} onReset={handleReset} />
      )}
    </div>
  );
}
