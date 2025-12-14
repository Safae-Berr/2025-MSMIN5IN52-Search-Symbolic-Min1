// frontend/src/components/DarkModeToggle.jsx
import { useState, useEffect } from "react";
import { cn } from "@/lib/utils";

export function DarkModeToggle() {
  const [isDark, setIsDark] = useState(false);

  useEffect(() => {
    const html = document.documentElement;
    setIsDark(html.classList.contains("dark"));
  }, []);

  const toggleDarkMode = () => {
    const html = document.documentElement;
    html.classList.toggle("dark");
    setIsDark(html.classList.contains("dark"));
  };

  return (
    <button
      onClick={toggleDarkMode}
      className="relative w-14 h-7 rounded-full bg-secondary/70 dark:bg-secondary/50 transition-colors"
    >
      <span
        className={cn(
          "absolute top-0.5 left-0.5 w-6 h-6 bg-foreground rounded-full shadow-md transition-transform",
          isDark ? "translate-x-7" : "translate-x-0"
        )}
      />
      <span className="absolute left-2 top-0.5 text-xs pointer-events-none">
        {isDark ? "🌙" : "☀️"}
      </span>
    </button>
  );
}
