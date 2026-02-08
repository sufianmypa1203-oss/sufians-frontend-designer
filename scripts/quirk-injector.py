#!/usr/bin/env python3
"""
🎭 QUIRK INJECTOR (Elite Skill S4)
Adds intentional imperfections and personality to components.
"""

import sys
import re
import random
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass
from enum import Enum

class QuirkType(Enum):
    ROTATION = "rotation"
    IRREGULAR_BORDER = "irregular_border"
    ORGANIC_SHAPE = "organic_shape"
    HAND_DRAWN_UNDERLINE = "hand_drawn_underline"
    CUSTOM_CURSOR = "custom_cursor"
    IRREGULAR_PADDING = "irregular_padding"
    TEXTURED_SHADOW = "textured_shadow"
    OFFSET_HOVER = "offset_hover"

class QuirkLevel(Enum):
    SUBTLE = "subtle"
    MILD = "mild"
    MODERATE = "moderate"
    BOLD = "bold"

@dataclass
class Quirk:
    type: QuirkType
    code: str
    description: str
    line_hint: str

class QuirkGenerator:
    @staticmethod
    def rotation_quirk() -> Quirk:
        angle = round(random.uniform(-0.8, 0.8), 1)
        return Quirk(type=QuirkType.ROTATION, code=f"rotate-[{angle}deg]", 
                     description=f"Subtle {angle}deg rotation", line_hint="className")
    
    @staticmethod
    def irregular_border_quirk() -> Quirk:
        radii = [random.choice([3, 5, 7, 9, 11, 13, 15, 17]) for _ in range(4)]
        return Quirk(type=QuirkType.IRREGULAR_BORDER, 
                     code=f"border-radius: {radii[0]}px {radii[1]}px {radii[2]}px {radii[3]}px;", 
                     description=f"Irregular corners: {radii}", line_hint="style")

    @staticmethod
    def irregular_padding_quirk() -> Quirk:
        values = [17, 19, 23, 29, 31, 37, 41, 43]
        px, py = random.choice(values), random.choice(values)
        return Quirk(type=QuirkType.IRREGULAR_PADDING, code=f"px-[{px}px] py-[{py}px]", 
                     description=f"Irregular padding: {py}px {px}px", line_hint="className")

class QuirkInjector:
    def __init__(self, code: str):
        self.code = code
        self.quirks_applied = []

    def inject_quirks(self, quirk_types: List[QuirkType], level: QuirkLevel = QuirkLevel.MILD) -> str:
        count = {"subtle": 1, "mild": 2, "moderate": 3, "bold": 4}[level.value]
        modified_code = self.code
        for qt in quirk_types[:count]:
            if qt == QuirkType.ROTATION: q = QuirkGenerator.rotation_quirk()
            elif qt == QuirkType.IRREGULAR_BORDER: q = QuirkGenerator.irregular_border_quirk()
            elif qt == QuirkType.IRREGULAR_PADDING: q = QuirkGenerator.irregular_padding_quirk()
            else: continue
            
            if q.line_hint == "className":
                modified_code = re.sub(r'className="([^"]*)"', rf'className="\1 {q.code}"', modified_code, count=1)
            elif q.line_hint == "style":
                modified_code = re.sub(r'(<\w+)', rf'\1 style={{{{{q.code.replace(";", "")}}}}}', modified_code, count=1)
            self.quirks_applied.append(q)
        return modified_code

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(1)
    input_file = Path(sys.argv[1])
    code = input_file.read_text()
    injector = QuirkInjector(code)
    modified = injector.inject_quirks([QuirkType.ROTATION, QuirkType.IRREGULAR_BORDER, QuirkType.IRREGULAR_PADDING])
    print(modified)
    print(f"\nApplied {len(injector.quirks_applied)} quirks.")
