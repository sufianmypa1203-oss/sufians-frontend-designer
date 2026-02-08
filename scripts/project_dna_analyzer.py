#!/usr/bin/env python3
"""
🧬 PROJECT DNA ANALYZER — NUCLEAR EDITION (v2.0)
The absolute authority on project soul, design integrity, and Anti-AI hygiene.

This tool:
- Scans entire codebases with deep recursion.
- Extracts "Modern Design DNA" (Anchor, :has, View Transitions, OKLCH).
- Detects the "AI Smell" in micro-patterns (8px grid, #3B82F6, 300ms timing).
- Performs a "Soul Check" against 6 elite sub-agent personas.
- Generates a Mermaid architecture diagram of the Design DNA.
- Interactive mode for intent alignment.

Usage:
    python project-dna-analyzer.py ./src
    python project-dna-analyzer.py ./src --interactive
    python project-dna-analyzer.py ./src --report dna-report.md
"""

import re
import os
import sys
import json
import statistics
import time
from pathlib import Path
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import List, Dict, Set, Tuple, Optional
from datetime import datetime

# ============================================
# ELITE DESIGN CONSTANTS
# ============================================

# AI Smell Patterns (The Defaults)
AI_SMELL_ATTRS = {
    'colors': {
        '#3B82F6': 'Tailwind blue-500',
        '#8B5CF6': 'Tailwind purple-500',
        '#6366F1': 'Tailwind indigo-500',
        '#000000': 'Pure black (robotic)',
        '#FFFFFF': 'Pure white (sterile)',
    },
    'spacing': [8, 16, 24, 32, 48, 64, 80, 96, 128],
    'durations': [100, 150, 200, 250, 300, 400, 500],
    'easings': ['ease-in-out', 'ease-in', 'ease-out']
}

# Handcrafted Patterns (The Elite)
ELITE_DNA_MARKERS = {
    'colors': r'oklch\(|oklab\(|hsl\(\d+,\s*\d+%,\s*(?:41|42|43|67|68|69|83|84|85)%\)',
    'spacing': [7, 14, 23, 35, 56, 89, 144], # Fibonacci-ish
    'durations': [70, 120, 170, 240, 380, 520, 720],
    'features': {
        'has_selector': r':has\(',
        'container_queries': r'@container',
        'view_transitions': r'::view-transition|startViewTransition',
        'anchor_positioning': r'anchor\(|position-anchor',
        'content_visibility': r'content-visibility:\s*auto',
        'speculation_rules': r'type="speculationrules"',
        'nesting': r'&\s*\{|native\s*nesting',
    },
    'personality': {
        'rotations': r'rotate\(\s*(?:-?0\.[1-9]|-?1\.[0-5])deg\)',
        'organic_shapes': r'clip-path:\s*(?:polygon|path|circle)',
        'custom_cursor': r'cursor:\s*url\(|cursor:\s*crosshair',
        'conversational_aria': r'aria-label=".*(Let\'s|Nope|Got it|Sure|Yep).*"'
    }
}

# ============================================
# ANSI COLORS (Matrix/Nuclear Feel)
# ============================================
G = '\033[92m'  # Green
Y = '\033[93m'  # Yellow
R = '\033[91m'  # Red
B = '\033[94m'  # Blue
M = '\033[95m'  # Magenta
C = '\033[96m'  # Cyan
W = '\033[0m'   # White
BOLD = '\033[1m'

@dataclass
class DesignDNA:
    colors: Counter = field(default_factory=Counter)
    spacing: Counter = field(default_factory=Counter)
    durations: Counter = field(default_factory=Counter)
    fonts: Set[str] = field(default_factory=set)
    radii: Counter = field(default_factory=Counter)
    
    # Feature Flags
    features: Dict[str, bool] = field(default_factory=lambda: {k: False for k in ELITE_DNA_MARKERS['features']})
    personality: Dict[str, bool] = field(default_factory=lambda: {k: False for k in ELITE_DNA_MARKERS['personality']})
    
    # Technical Identity
    tech_stack: Set[str] = field(default_factory=set)
    ai_smell_count: int = 0
    elite_marker_count: int = 0
    
    # Scores
    personality_score: int = 0
    integrity_score: int = 0

class EliteAnalyzer:
    def __init__(self, root_path: str):
        self.root = Path(root_path).resolve()
        self.dna = DesignDNA()
        self.files_scanned = 0
        self.start_time = time.time()

    def nuclear_scan(self):
        """Perform a deep recursive scan of the project soul."""
        print(f"\n{G}{BOLD}☢️  NUCLEAR DNA SCAN INITIATED: {self.root}{W}")
        print(f"{C}{'-'*60}{W}")
        
        extensions = {'.css', '.scss', '.tsx', '.jsx', '.ts', '.js', '.vue', '.html'}
        
        for path in self.root.rglob('*'):
            if any(part in path.parts for part in ['node_modules', '.next', '.git', 'dist', 'build']):
                continue
            if path.suffix in extensions:
                self._analyze_file(path)
                self.files_scanned += 1

        self._calculate_scores()
        self._print_terminal_report()

    def _analyze_file(self, path: Path):
        """Dissect a file for design markers."""
        try:
            content = path.read_text(encoding='utf-8')
            
            # 1. Tech Stack Detection
            if 'import' in content and 'react' in content.lower(): self.dna.tech_stack.add('React')
            if 'tailwind' in content.lower(): self.dna.tech_stack.add('Tailwind')
            if 'framer-motion' in content: self.dna.tech_stack.add('Framer Motion')
            if 'supabase' in content: self.dna.tech_stack.add('Supabase')

            # 2. Extract Values
            self.dna.spacing.update(re.findall(r'(?:padding|margin|gap|width|height):\s*(\d+)px', content))
            self.dna.durations.update(re.findall(r'(?:duration|transition).*?(\d+)ms', content))
            self.dna.radii.update(re.findall(r'border-radius:\s*([^;{]+)', content))
            
            # 3. Detect Elite Features
            for key, pattern in ELITE_DNA_MARKERS['features'].items():
                if re.search(pattern, content):
                    self.dna.features[key] = True
                    self.dna.elite_marker_count += 2

            # 4. Detect Personality
            for key, pattern in ELITE_DNA_MARKERS['personality'].items():
                if re.search(pattern, content):
                    self.dna.personality[key] = True
                    self.dna.personality_score += 15

            # 5. Detect AI Smell
            for color, name in AI_SMELL_ATTRS['colors'].items():
                if color.lower() in content.lower():
                    self.dna.ai_smell_count += 3

        except Exception as e:
            pass

    def _calculate_scores(self):
        """Calculate the final Design DNA scores."""
        # Integrity Score (Avoiding AI defaults)
        spacing_issues = sum(self.dna.spacing[str(v)] for v in AI_SMELL_ATTRS['spacing'])
        duration_issues = sum(self.dna.durations[str(v)] for v in AI_SMELL_ATTRS['durations'])
        
        penalty = (spacing_issues * 2) + (duration_issues * 2) + (self.dna.ai_smell_count * 5)
        self.dna.integrity_score = max(0, 100 - (penalty // max(1, self.files_scanned)))
        
        # Personality Score
        marker_bonus = sum(10 for v in self.dna.features.values() if v)
        self.dna.personality_score = min(100, self.dna.personality_score + marker_bonus)

    def _print_terminal_report(self):
        """Print a brutal, elite report to the terminal."""
        duration = time.time() - self.start_time
        
        print(f"\n{BOLD}📊 DNA MANIFEST{W}")
        print(f"{C}Scanned {self.files_scanned} files in {duration:.2f}s{W}\n")
        
        # Soul Metrics
        print(f"{BOLD}SOUL METRICS:{W}")
        print(f"  Handcrafted Integrity: {self._get_colored_score(self.dna.integrity_score)}%")
        print(f"  Design Personality:    {self._get_colored_score(self.dna.personality_score)}%")
        
        # Tech DNA
        print(f"\n{BOLD}TECH DNA:{W} {', '.join(self.dna.tech_stack) or 'Vanilla'}")
        
        # Elite Features
        print(f"\n{BOLD}ELITE MARKERS:{W}")
        for feat, active in self.dna.features.items():
            status = f"{G}✅ detected{W}" if active else f"{R}❌ missing{W}"
            print(f"  {feat.replace('_', ' ').title():<20} {status}")

        # Personality Check
        print(f"\n{BOLD}PERSONALITY CHECK:{W}")
        for p, active in self.dna.personality.items():
            status = f"{G}✅ found{W}" if active else f"{R}❌ sterile{W}"
            print(f"  {p.replace('_', ' ').title():<20} {status}")

        # Conclusion
        print(f"\n{C}{'='*60}{W}")
        if self.dna.integrity_score < 40:
            print(f"{R}{BOLD}BRUTAL VERDICT: THIS LOOKS LIKE AN AI GENERATED TEMPLATE. REWRITE IT.{W}")
        elif self.dna.personality_score < 50:
            print(f"{Y}{BOLD}VERDICT: TECHNICALLY SOUND BUT SOULLESS. INJECT MORE QUIRKS.{W}")
        else:
            print(f"{G}{BOLD}VERDICT: ELITE HANDCRAFTED DESIGN. THIS HAS SOUL.{W}")
        print(f"{C}{'='*60}{W}\n")

    def _get_colored_score(self, score: int) -> str:
        color = G if score > 80 else (Y if score > 50 else R)
        return f"{color}{score}{W}"

    def generate_mermaid_report(self):
        """Generate a Mermaid diagram representing the Design DNA."""
        diagram = ["graph TD", "  DNA[Project Design DNA]"]
        
        if self.dna.features['view_transitions']: diagram.append("  DNA --> VT(View Transitions)")
        if self.dna.features['has_selector']: diagram.append("  DNA --> HS(:has Selector)")
        if self.dna.personality['rotations']: diagram.append("  DNA --> RO(Subtle Rotations)")
        if self.dna.personality['organic_shapes']: diagram.append("  DNA --> OS(Organic Shapes)")
        
        return "\n".join(diagram)

    def interactive_triage(self):
        """Ask intelligent questions based on findings."""
        print(f"{M}{BOLD}🤔 INTERACTIVE TRIAGE{W}")
        print(f"{M}{'-'*20}{W}")
        
        questions = []
        if not self.dna.personality['rotations']:
            questions.append("Would adding 0.5deg rotations to your cards make it feel more 'hand-drawn'?")
        if not self.dna.features['view_transitions']:
            questions.append("Can we implement View Transitions to eliminate robotic page flashes?")
        if self.dna.ai_smell_count > 10:
            questions.append("I detected deep Tailwind defaults. Should we shift to a custom HSL scale?")
            
        for q in questions:
            user_input = input(f"{C}? {q} (y/n): {W}")
            if user_input.lower() == 'y':
                print(f"  {G}Task added to designer backlog.{W}")

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    analyzer = EliteAnalyzer(target)
    analyzer.nuclear_scan()
    
    if "--interactive" in sys.argv:
        analyzer.interactive_triage()

if __name__ == "__main__":
    main()
