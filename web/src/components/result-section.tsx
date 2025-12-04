import { useState } from "react";
import { CheckCircle2, Download, Eye, Loader2, RotateCcw } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";

import type { Resume } from "@/types/types";
import { services } from "@/services/api";

interface ResultSectionProps {
  onReset: () => void;
  data: Resume;
}

export function ResultSection({ onReset, data }: ResultSectionProps) {
  const [isDownloading, setIsDownloading] = useState(false);

  const handleDownload = async () => {
    try {
      setIsDownloading(true);
      const blob = await services.generatePdf(data);
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute(
        "download",
        `Curriculo_${data.basics.name.replace(/\s+/g, "-")}.pdf`
      );
      link.click();
      link.parentNode?.removeChild(link);
      window.URL.revokeObjectURL(url);
    } catch (err) {
      alert(err);
    } finally {
      setIsDownloading(false);
    }
  };

  const handlePreview = async () => {
    try {
      const blob = await services.generatePdf(data);
      const url = window.URL.createObjectURL(blob);
      window.open(url, "_blank");
    } catch (err) {
      alert(err);
    }
  };

  //   const handleReset = () => {
  //     setIsPreviewOpen(false);
  //     onReset();
  //   };

  return (
    <Card className="p-6 border-green-200 bg-green-50/30">
      <div className="flex flex-col items-center gap-4 text-center">
        <div className="flex items-center gap-2 text-green-700 font-semibold">
          <CheckCircle2 className="h-5 w-5" />
          Resume Optimized!
        </div>

        <div className="grid grid-cols-2 gap-3 w-full">
          <Button variant="outline" onClick={handlePreview}>
            <Eye className="mr-2 h-4 w-4" />
            Preview
          </Button>

          <Button onClick={handleDownload} disabled={isDownloading}>
            {isDownloading ? (
              <>
                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                Gerando...
              </>
            ) : (
              <>
                <Download className="mr-2 h-4 w-4" />
                Download PDF
              </>
            )}
          </Button>
        </div>

        <Button
          variant="ghost"
          size="sm"
          onClick={onReset}
          className="text-muted-foreground"
        >
          <RotateCcw className="mr-2 h-3 w-3" />
          Start Over
        </Button>
      </div>
    </Card>
  );
}
