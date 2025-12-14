// frontend/src/components/SolverPanel.jsx
import React from "react";
import { Brain, Lightbulb, Target, Zap } from "lucide-react";
import { cn } from "@/lib/utils";

export function SolverPanel({ solverData, isLoading = false, aiSuggestion, onRequestAI }) {
  // solverData = { remainingCount, topSuggestions, entropy, bestGuess, possibleWords }

  const remainingCount = solverData?.remainingCount ?? 0;
  const topSuggestions = solverData?.topSuggestions ?? [];
  const entropy = solverData?.entropy ?? 0;
  const bestGuess = solverData?.bestGuess ?? null;
  const possibleWords = solverData?.possibleWords ?? [];

  return (
    <div className="flex flex-col gap-4 p-4 bg-card rounded-xl border border-border">
      {/* Header */}
      <div className="flex items-center gap-2">
        <div className="p-2 rounded-lg bg-solver-bg glow-accent">
          <Brain className="w-5 h-5 text-accent" />
        </div>
        <div>
          <h3 className="font-semibold text-foreground">Solveur CSP</h3>
          <p className="text-xs text-muted-foreground">Résolution par contraintes</p>
        </div>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-2 gap-3">
        <div className="p-3 rounded-lg bg-secondary/50">
          <div className="flex items-center gap-2 text-muted-foreground text-xs mb-1">
            <Target className="w-3 h-3" />
            Mots possibles
          </div>
          <div className="text-2xl font-bold text-foreground font-mono">
            {remainingCount}
          </div>
        </div>
        <div className="p-3 rounded-lg bg-secondary/50">
          <div className="flex items-center gap-2 text-muted-foreground text-xs mb-1">
            <Zap className="w-3 h-3" />
            Entropie
          </div>
          <div className="text-2xl font-bold text-foreground font-mono">
            {entropy.toFixed(1)}
          </div>
        </div>
      </div>

      {/* Best Guess */}
      {bestGuess && (
        <div className="p-3 rounded-lg bg-primary/10 border border-primary/30">
          <div className="flex items-center gap-2 text-primary text-xs mb-2">
            <Lightbulb className="w-3 h-3" />
            Meilleure suggestion CSP
          </div>
          <div className="text-xl font-bold text-primary font-mono tracking-widest">
            {bestGuess}
          </div>
        </div>
      )}

      {/* AI Suggestion */}
      <button
        onClick={onRequestAI}
        disabled={isLoading}
        className={cn(
          "p-3 rounded-lg border transition-all",
          "bg-accent/10 border-accent/30 hover:bg-accent/20",
          isLoading && "animate-pulse"
        )}
      >
        <div className="flex items-center gap-2 text-accent text-xs mb-2">
          <Brain className="w-3 h-3" />
          {isLoading ? "Analyse LLM en cours..." : "Suggestion IA"}
        </div>
        {aiSuggestion ? (
          <div className="text-xl font-bold text-accent font-mono tracking-widest">
            {aiSuggestion}
          </div>
        ) : (
          <div className="text-sm text-muted-foreground">
            Cliquer pour obtenir une suggestion IA
          </div>
        )}
      </button>

      {/* Top Suggestions */}
      <div>
        <h4 className="text-xs text-muted-foreground mb-2 flex items-center gap-1">
          <Target className="w-3 h-3" />
          Top suggestions
        </h4>
        <div className="flex flex-wrap gap-2">
          {topSuggestions.map(({ word, score }) => (
            <div
              key={word}
              className="px-2 py-1 rounded bg-secondary text-foreground text-sm font-mono"
              title={`Score: ${score.toFixed(0)}`}
            >
              {word}
            </div>
          ))}
        </div>
      </div>

      {/* Remaining Words Preview */}
      {remainingCount <= 20 && remainingCount > 0 && (
        <div>
          <h4 className="text-xs text-muted-foreground mb-2">
            Mots restants ({remainingCount})
          </h4>
          <div className="flex flex-wrap gap-1 max-h-24 overflow-y-auto">
            {possibleWords.map((word) => (
              <span
                key={word}
                className="px-1.5 py-0.5 rounded bg-muted text-muted-foreground text-xs font-mono"
              >
                {word}
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
