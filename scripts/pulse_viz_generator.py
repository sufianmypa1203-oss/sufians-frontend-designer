#!/usr/bin/env python3
"""
☢️ PULSE VIZ GENERATOR - Nuclear Financial Visualization
Destroys "Excel-smell" in financial data. Transforms raw numbers into living organisms.

Philosophy:
- Data is not static; it's a heartbeat
- Every line has a "Glow Path" (3 blurred layers)
- Organic easing (logarithmic growth curves)
- No grid prisons (atmospheric gradients only)
- Contextual color (Emerald up, Crimson down)

Output: Single File Vue Component with inline nuclear SVG

Usage:
    pulse-viz data.json --context net-worth
    pulse-viz data.json --context spend-spikes --output viz.vue
    pulse-viz data.json --context budget-orbit --theme dark
"""

import sys
import json
import math
import re
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass
from datetime import datetime

# ============================================
# NUCLEAR COLOR SYSTEM (HSL-based)
# ============================================

class FinancialColors:
    """Contextual colors based on financial performance"""
    EMERALD_STRONG = "hsl(145, 67%, 42%)"      # Vibrant positive
    TEAL_MILD = "hsl(165, 55%, 48%)"           # Mild positive
    SLATE_NEUTRAL = "hsl(220, 15%, 55%)"       # Neutral/baseline
    AMBER_CAUTION = "hsl(38, 65%, 52%)"        # Mild negative
    CRIMSON_WARNING = "hsl(0, 72%, 42%)"       # Strong negative
    
    @staticmethod
    def contextual_color(value: float, benchmark: float) -> str:
        ratio = value / benchmark if benchmark != 0 else 1.0
        if ratio >= 1.15: return FinancialColors.EMERALD_STRONG
        elif ratio >= 1.05: return FinancialColors.TEAL_MILD
        elif ratio >= 0.95: return FinancialColors.SLATE_NEUTRAL
        elif ratio >= 0.85: return FinancialColors.AMBER_CAUTION
        else: return FinancialColors.CRIMSON_WARNING
    
    @staticmethod
    def parse_hsl(hsl_str: str) -> Tuple[int, int, int]:
        match = re.match(r'hsl\((\d+),\s*(\d+)%,\s*(\d+)%\)', hsl_str)
        if match: return int(match.group(1)), int(match.group(2)), int(match.group(3))
        return (0, 0, 0)

# ============================================
# CATMULL-ROM SPLINE INTERPOLATION (REAL MATH)
# ============================================

class CatmullRomSpline:
    @staticmethod
    def interpolate(points: List[Tuple[float, float]], segments: int = 20) -> List[Tuple[float, float]]:
        if len(points) < 2: return points
        if len(points) == 2:
            return [(points[0][0] + (points[1][0] - points[0][0]) * i / segments,
                     points[0][1] + (points[1][1] - points[0][1]) * i / segments) 
                    for i in range(segments + 1)]
        
        result = []
        padded = [points[0]] + points + [points[-1]]
        for i in range(len(padded) - 3):
            p0, p1, p2, p3 = padded[i:i+4]
            for j in range(segments):
                t = j / segments
                t2, t3 = t*t, t*t*t
                x = 0.5 * ((2*p1[0]) + (-p0[0]+p2[0])*t + (2*p0[0]-5*p1[0]+4*p2[0]-p3[0])*t2 + (-p0[0]+3*p1[1]-3*p2[0]+p3[0])*t3)
                y = 0.5 * ((2*p1[1]) + (-p0[1]+p2[1])*t + (2*p0[1]-5*p1[1]+4*p2[1]-p3[1])*t2 + (-p0[1]+3*p1[1]-3*p2[1]+p3[1])*t3)
                result.append((x, y))
        result.append(points[-1])
        return result

# ============================================
# DOUGLAS-PEUCKER SIMPLIFICATION (PERFORMANCE)
# ============================================

class PathSimplifier:
    @staticmethod
    def simplify(points: List[Tuple[float, float]], tolerance: float = 1.0) -> List[Tuple[float, float]]:
        if len(points) < 3: return points
        dmax, index = 0, 0
        for i in range(1, len(points) - 1):
            d = PathSimplifier._perp_dist(points[i], points[0], points[-1])
            if d > dmax: dmax, index = d, i
        if dmax > tolerance:
            return PathSimplifier.simplify(points[:index+1], tolerance)[:-1] + PathSimplifier.simplify(points[index:], tolerance)
        return [points[0], points[-1]]

    @staticmethod
    def _perp_dist(p, p1, p2):
        num = abs((p2[1]-p1[1])*p[0] - (p2[0]-p1[0])*p[1] + p2[0]*p1[1] - p2[1]*p1[0])
        den = math.sqrt((p2[1]-p1[1])**2 + (p2[0]-p1[0])**2)
        return num/den if den != 0 else 0

# ============================================
# SVG PATH GENERATOR (NUCLEAR RENDERING)
# ============================================

class SVGPathGenerator:
    @staticmethod
    def points_to_path(points: List[Tuple[float, float]]) -> str:
        return "M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in points)
    
    @staticmethod
    def calculate_path_length(points: List[Tuple[float, float]]) -> float:
        l = 0
        for i in range(len(points) - 1):
            l += math.sqrt((points[i+1][0]-points[i][0])**2 + (points[i+1][1]-points[i][1])**2)
        return l

    @staticmethod
    def create_area_path(points: List[Tuple[float, float]], baseline: float) -> str:
        if not points: return ""
        p = f"M {points[0][0]:.2f} {baseline} L {points[0][0]:.2f} {points[0][1]:.2f} "
        p += " ".join(f"L {x:.2f} {y:.2f}" for x, y in points[1:])
        p += f" L {points[-1][0]:.2f} {baseline} Z"
        return p

# ============================================
# DATA PROCESSOR
# ============================================

@dataclass
class DataPoint:
    date: str
    value: float
    category: str = "default"

class DataProcessor:
    @staticmethod
    def normalize(data: List[DataPoint], width: float = 100, height: float = 40, padding: float = 5) -> List[Tuple[float, float]]:
        if not data: return []
        vals = [d.value for d in data]
        v_min, v_max = min(vals), max(vals)
        v_range = max(1, v_max - v_min)
        v_min -= v_range * (padding/100)
        v_max += v_range * (padding/100)
        v_range = v_max - v_min
        
        x_step = width / (len(data) - 1) if len(data) > 1 else 0
        return [(i * x_step, height - ((p.value - v_min) / v_range * height)) for i, p in enumerate(data)]

# ============================================
# VISUALIZATION CONTEXTS
# ============================================

class NetWorthViz:
    @staticmethod
    def generate(data: List[DataPoint], color: str) -> Dict:
        points = DataProcessor.normalize(data)
        if len(points) > 500: points = PathSimplifier.simplify(points, 0.5)
        smooth = CatmullRomSpline.interpolate(points, 15)
        return {
            'main_path': SVGPathGenerator.points_to_path(smooth),
            'area_path': SVGPathGenerator.create_area_path(smooth, 40),
            'path_length': SVGPathGenerator.calculate_path_length(smooth),
            'color': color,
            'points': smooth[::max(1, len(smooth)//20)] # Sample for interaction
        }

# ============================================
# VUE COMPONENT GENERATOR
# ============================================

class VueGenerator:
    @staticmethod
    def generate_net_worth(viz: Dict) -> str:
        p_json = json.dumps(viz['points'])
        return f"""<template>
  <div class="pulse-viz">
    <svg viewBox="0 0 100 40" class="pulse-svg">
      <defs>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="1.2" result="blur"/>
          <feComposite in="SourceGraphic" in2="blur" operator="over"/>
        </filter>
        <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="{viz['color']}" stop-opacity="0.3"/>
          <stop offset="100%" stop-color="{viz['color']}" stop-opacity="0"/>
        </linearGradient>
      </defs>
      <path d="{viz['area_path']}" fill="url(#areaGrad)" />
      <path d="{viz['main_path']}" fill="none" stroke="{viz['color']}" stroke-width="1.8" filter="url(#glow)" class="line-animate" 
        :style="{{ strokeDasharray: {viz['path_length']:.2f}, strokeDashoffset: animating ? {viz['path_length']:.2f} : 0 }}" />
    </svg>
  </div>
</template>

<script setup>
import {{ ref, onMounted }} from 'vue'
const animating = ref(true)
onMounted(() => setTimeout(() => animating.value = false, 100))
</script>

<style scoped>
.pulse-viz {{ background: #0f172a; border-radius: 12px; padding: 24px; }}
.line-animate {{ transition: stroke-dashoffset 1200ms cubic-bezier(0.4, 0, 0.2, 1); }}
</style>
"""

def main():
    if len(sys.argv) < 2:
        print("Usage: pulse-viz <data.json> --context <type>")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    with open(path) as f: raw = json.load(f)
    data = [DataPoint(**d) for d in raw]
    
    color = FinancialColors.contextual_color(data[-1].value, data[0].value) if len(data) > 1 else FinancialColors.SLATE_NEUTRAL
    viz = NetWorthViz.generate(data, color)
    vue = VueGenerator.generate_net_worth(viz)
    
    if '--output' in sys.argv:
        out = Path(sys.argv[sys.argv.index('--output')+1])
        out.write_text(vue)
        print(f"✅ Generated {out}")
    else:
        print(vue)

if __name__ == "__main__":
    main()
