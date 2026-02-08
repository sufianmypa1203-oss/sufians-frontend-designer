#!/usr/bin/env python3
"""
💬 MICROCOPY HUMANIZER (Elite Skill S5)
Replaces generic button/label text with playful, human alternatives.
"""

import sys
import re
import random
from pathlib import Path
from typing import Dict, List, Tuple
from enum import Enum

class Tone(Enum):
    PLAYFUL = "playful"
    CASUAL = "casual"
    WARM = "warm"
    CONFIDENT = "confident"

REPLACEMENTS = {
    'Submit': { Tone.PLAYFUL: ["Let's go!", "Send it!", "Make magic ✨"], Tone.CASUAL: ["Send it", "Submit", "Go ahead"] },
    'Cancel': { Tone.PLAYFUL: ["Nah", "Never mind!", "Nope"], Tone.CASUAL: ["Cancel", "Not now", "Skip"] },
    'Delete': { Tone.PLAYFUL: ["Bye forever! 💀", "Trash it!", "Yeet"], Tone.CASUAL: ["Delete", "Remove", "Trash"] },
    'Save': { Tone.PLAYFUL: ["Lock it in! 🔒", "Keep it!", "Stash this"], Tone.CASUAL: ["Save it", "Keep this", "Got it"] }
}

class MicrocopyHumanizer:
    def __init__(self, code: str, tone: Tone = Tone.CASUAL):
        self.code = code
        self.tone = tone
        self.replacements_made = []

    def humanize(self, preserve_aria: bool = True) -> str:
        modified_code = self.code
        for generic, variants in REPLACEMENTS.items():
            human = random.choice(variants.get(self.tone, variants[Tone.CASUAL]))
            pattern = rf'>{generic}<'
            if re.search(pattern, modified_code, re.IGNORECASE):
                modified_code = re.sub(pattern, f'>{human}<', modified_code, flags=re.IGNORECASE)
                self.replacements_made.append((generic, human))
        return modified_code

def main():
    if len(sys.argv) < 2: 
        print("Usage: humanize-copy <file>")
        sys.exit(1)
    input_path = Path(sys.argv[1])
    code = input_path.read_text()
    humanizer = MicrocopyHumanizer(code, Tone.PLAYFUL)
    print(humanizer.humanize())
    print(f"\nReplacements: {len(humanizer.replacements_made)}")

if __name__ == "__main__":
    main()
