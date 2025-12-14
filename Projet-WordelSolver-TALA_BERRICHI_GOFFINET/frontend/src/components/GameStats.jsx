// frontend/src/components/GameStats.jsx
import React from "react";
import { Trophy, RotateCcw, Clock } from "lucide-react";
import { Button } from "@/components/ui/button";

export function GameStats({ isGameOver, isWon, targetWord, attempts, onNewGame }) {
  if (!isGameOver) return null;

  return (
    <div className="fixed inset-0 bg-background/80 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div className="bg-card rounded-2xl border border-border p-6 sm:p-8 max-w-sm w-full text-center">
        {isWon ? (
          <>
            <div className="w-16 h-16 mx-auto mb-4 rounded-full bg-primary/20 flex items-center justify-center">
              <Trophy className="w-8 h-8 text-primary" />
            </div>
            <h2 className="text-2xl font-bold text-foreground mb-2">Félicitations !</h2>
            <p className="text-muted-foreground mb-4">
              Vous avez trouvé le mot en {attempts} tentative{attempts > 1 ? "s" : ""} !
            </p>
          </>
        ) : (
          <>
            <div className="w-16 h-16 mx-auto mb-4 rounded-full bg-destructive/20 flex items-center justify-center">
              <Clock className="w-8 h-8 text-destructive" />
            </div>
            <h2 className="text-2xl font-bold text-foreground mb-2">Partie terminée</h2>
            <p className="text-muted-foreground mb-2">Le mot était :</p>
            <p className="text-3xl font-bold font-mono text-primary tracking-widest mb-4">
              {targetWord}
            </p>
          </>
        )}

        <Button onClick={onNewGame} className="w-full gap-2">
          <RotateCcw className="w-4 h-4" />
          Nouvelle partie
        </Button>
      </div>
    </div>
  );
}
