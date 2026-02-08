#!/usr/bin/env python3
"""
🎯 HUMAN VS AI SCORER (Elite Skill S6)
Final validation - scores how human vs AI-generated your code feels.
"""

import sys
import re
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass, field
from collections import Counter

@dataclass
class ScoreCard:
    color_score: float = 0.0
    spacing_score: float = 0.0
    animation_score: float = 0.0
    personality_score: float = 0.0
    microcopy_score: float = 0.0
    verdict: str = ""

AI_COLORS = ['#3B82F6', '#8B5CF6', '#6366F1']
PERFECT_SPACING = [8, 16, 24, 32, 48, 64]

class HumanVsAIScorer:
    def __init__(self, project_path: Path):
        self.project_path = project_path
        self.scorecard = ScoreCard()

    def score(self) -> ScoreCard:
        content = ""
        for f in self.project_path.rglob('*'):
            if f.suffix in ['.css', '.tsx', '.jsx'] and 'node_modules' not in str(f):
                content += f.read_text(errors='ignore')
        
        # Simple scoring logic
        ai_colors = sum(1 for c in AI_COLORS if c.lower() in content.lower())
        perfect_spacing = sum(1 for s in PERFECT_SPACING if f"{s}px" in content)
        
        self.scorecard.color_score = max(0, 100 - (ai_colors * 30))
        self.scorecard.spacing_score = max(0, 100 - (perfect_spacing * 10))
        self.scorecard.personality_score = 100 if 'rotate(' in content else 0
        
        total = (self.scorecard.color_score + self.scorecard.spacing_score + self.scorecard.personality_score) / 3
        if total > 80: self.scorecard.verdict = "HANDCRAFTED"
        elif total > 50: self.scorecard.verdict = "MIXED"
        else: self.scorecard.verdict = "AI-GENERATED"
        
        return self.scorecard

def main():
    if len(sys.argv) < 2: 
        print("Usage: soul-score <project_path>")
        sys.exit(1)
    scorer = HumanVsAIScorer(Path(sys.argv[1]))
    card = scorer.score()
    print(f"SCORE: {card.verdict}")
    print(f"Colors: {card.color_score} | Spacing: {card.spacing_score} | Personality: {card.personality_score}")

if __name__ == "__main__":
    main()
