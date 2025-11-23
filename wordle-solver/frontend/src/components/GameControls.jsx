import React, { useState } from 'react';
import { Play, RotateCcw, Settings, Globe, Zap } from 'lucide-react';

const GameControls = ({ 
  onNewGame, 
  onGetSuggestion,
  languages,
  strategies,
  isPlaying,
  disabled 
}) => {
  const [showSettings, setShowSettings] = useState(false);
  const [selectedLanguage, setSelectedLanguage] = useState('en');
  const [selectedStrategy, setSelectedStrategy] = useState('frequency');

  const handleNewGame = () => {
    onNewGame(selectedLanguage, selectedStrategy);
  };

  return (
    <div className="card">
      <div className="space-y-4">
        {/* Header */}
        <div className="flex items-center justify-between">
          <h2 className="text-xl font-bold">Contrôles</h2>
          <button
            onClick={() => setShowSettings(!showSettings)}
            className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <Settings size={20} />
          </button>
        </div>

        {/* Settings Panel */}
        {showSettings && (
          <div className="space-y-3 p-3 bg-gray-50 rounded-lg">
            <div>
              <label className="flex items-center gap-2 text-sm font-medium text-gray-700 mb-2">
                <Globe size={16} />
                Langue
              </label>
              <select
                value={selectedLanguage}
                onChange={(e) => setSelectedLanguage(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                disabled={isPlaying}
              >
                {languages && languages.map((lang) => (
                  <option key={lang.code} value={lang.code}>
                    {lang.name} ({lang.word_count} mots)
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="flex items-center gap-2 text-sm font-medium text-gray-700 mb-2">
                <Zap size={16} />
                Stratégie
              </label>
              <select
                value={selectedStrategy}
                onChange={(e) => setSelectedStrategy(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                disabled={isPlaying}
              >
                {strategies && strategies.map((strategy) => (
                  <option key={strategy.id} value={strategy.id}>
                    {strategy.name} - {strategy.description}
                  </option>
                ))}
              </select>
            </div>
          </div>
        )}

        {/* Action Buttons */}
        <div className="flex flex-col gap-2">
          <button
            onClick={handleNewGame}
            disabled={disabled}
            className="btn-primary w-full flex items-center justify-center gap-2"
          >
            {isPlaying ? (
              <>
                <RotateCcw size={18} />
                Nouvelle Partie
              </>
            ) : (
              <>
                <Play size={18} />
                Démarrer
              </>
            )}
          </button>

          {isPlaying && (
            <button
              onClick={onGetSuggestion}
              disabled={disabled}
              className="btn-secondary w-full flex items-center justify-center gap-2"
            >
              <Zap size={18} />
              Obtenir une Suggestion
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

export default GameControls;
