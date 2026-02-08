#!/usr/bin/env python3
"""
⚡ SPRING PHYSICS CALCULATOR
Calculates real spring animation values using actual physics formulas.

Based on Hooke's Law:
F = -kx (spring force)
F = -bv (damping force)
a = (-kx - bv) / m (acceleration)
"""

import sys
import math
import json
from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class SpringConfig:
    stiffness: float  # k
    damping: float    # b
    mass: float       # m
    name: str = "custom"

PRESETS = {
    'snappy': SpringConfig(stiffness=280, damping=18, mass=0.7, name='snappy'),
    'smooth': SpringConfig(stiffness=110, damping=16, mass=0.9, name='smooth'),
    'bouncy': SpringConfig(stiffness=240, damping=12, mass=0.6, name='bouncy'),
    'wobbly': SpringConfig(stiffness=180, damping=8, mass=0.5, name='wobbly'),
    'stiff': SpringConfig(stiffness=400, damping=25, mass=1.0, name='stiff'),
    'gentle': SpringConfig(stiffness=80, damping=20, mass=1.2, name='gentle'),
}

class SpringPhysics:
    @staticmethod
    def simulate(config: SpringConfig, initial_displacement: float = 100, 
                 duration: float = 2.0, fps: float = 60) -> List[Tuple[float, float, float]]:
        dt = 1.0 / fps
        frames = int(duration * fps)
        x, v = initial_displacement, 0.0
        result = [(0.0, x, v)]
        for frame in range(1, frames):
            a = (-config.stiffness * x - config.damping * v) / config.mass
            v += a * dt
            x += v * dt
            result.append((frame * dt, x, v))
            if abs(x) < 0.01 and abs(v) < 0.01: break
        return result

    @staticmethod
    def analyze(config: SpringConfig) -> dict:
        zeta = config.damping / (2 * math.sqrt(config.stiffness * config.mass))
        simulation = SpringPhysics.simulate(config)
        settle_time = simulation[-1][0]
        return {
            "damping_ratio": round(zeta, 3),
            "settle_time_ms": int(settle_time * 1000),
            "type": "underdamped" if zeta < 1 else "critical" if zeta == 1 else "overdamped"
        }

if __name__ == "__main__":
    preset_name = sys.argv[1] if len(sys.argv) > 1 else "snappy"
    config = PRESETS.get(preset_name, PRESETS['snappy'])
    analysis = SpringPhysics.analyze(config)
    print(f"--- SPRING ANALYSIS: {config.name.upper()} ---")
    print(f"Stiffness: {config.stiffness} | Damping: {config.damping} | Mass: {config.mass}")
    print(f"Ratio: {analysis['damping_ratio']} | Settle: {analysis['settle_time_ms']}ms")
    print(json.dumps({"framer": {"stiffness": config.stiffness, "damping": config.damping, "mass": config.mass}}, indent=2))
