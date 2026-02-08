#!/usr/bin/env python3
"""
☢️ SYNC-UI ORCHESTRATOR - Nuclear Loading Experience Generator
Eliminates "Sync Anxiety." Transforms backend delays into brand-building moments.

Philosophy:
- Waiting = failure of backend, OPPORTUNITY for frontend
- Progress is a story (not percentage)
- Ghost motion (never stop moving)
- Interactive distraction (poke to trigger particles)

Output: Production-ready Vue/React components with Framer Motion orchestration

Usage:
    sync-ui --context flinks-initial --output SyncUI.vue
    sync-ui --context daily-refresh --framework react
    sync-ui --context error-recovery --theme dark
    
Contexts:
    flinks-initial   - First-time connection (grand, secure, impressive)
    daily-refresh    - Background sync (efficient, smart, helpful)
    error-recovery   - Retry after failure (empathetic, resilient, warm)
"""

import sys
import json
import random
import math
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass
from enum import Enum

# ============================================
# STATUS NARRATIVE SYSTEM
# ============================================

class SyncContext(Enum):
    FLINKS_INITIAL = "flinks-initial"
    DAILY_REFRESH = "daily-refresh"
    ERROR_RECOVERY = "error-recovery"

# Status chapters - NOT percentages!
STATUS_NARRATIVES = {
    SyncContext.FLINKS_INITIAL: [
        {
            'phase': 'initiation',
            'duration': 3000,  # ms
            'messages': [
                "Establishing secure connection...",
                "Finding your bank's digital vault...",
                "Initiating encrypted handshake...",
                "Verifying security protocols...",
            ]
        },
        {
            'phase': 'active_scan',
            'duration': 12000,
            'messages': [
                "Scanning transaction history...",
                "Analyzing spending patterns...",
                "Organizing your coffee habit...",
                "Categorizing groceries vs. late-night snacks...",
                "Detecting your favorite restaurants...",
                "Mapping your financial DNA...",
            ]
        },
        {
            'phase': 'synthesis',
            'duration': 5000,
            'messages': [
                "Building your financial dashboard...",
                "Crafting insights from data...",
                "Connecting the dots...",
                "Finalizing your money story...",
            ]
        },
        {
            'phase': 'resolution',
            'duration': 1000,
            'messages': [
                "Welcome to clarity.",
                "Your finances, visualized.",
                "Ready to explore.",
            ]
        }
    ],
    
    SyncContext.DAILY_REFRESH: [
        {
            'phase': 'quick_check',
            'duration': 2000,
            'messages': [
                "Checking for updates...",
                "Scanning new activity...",
                "Looking for changes...",
            ]
        },
        {
            'phase': 'process',
            'duration': 3000,
            'messages': [
                "Processing new transactions...",
                "Updating balances...",
                "Refreshing insights...",
            ]
        },
        {
            'phase': 'complete',
            'duration': 1000,
            'messages': [
                "All caught up.",
                "Fresh data loaded.",
                "You're current.",
            ]
        }
    ],
    
    SyncContext.ERROR_RECOVERY: [
        {
            'phase': 'acknowledge',
            'duration': 2000,
            'messages': [
                "Encountered a hiccup...",
                "Bank didn't respond as expected...",
                "Connection interrupted...",
            ]
        },
        {
            'phase': 'retry',
            'duration': 8000,
            'messages': [
                "Trying a different route...",
                "Reconnecting with patience...",
                "Finding alternative path...",
                "Banks can be moody, we get it...",
                "Almost there, hang tight...",
            ]
        },
        {
            'phase': 'resolution',
            'duration': 2000,
            'messages': [
                "Connection restored.",
                "Back on track.",
                "Crisis averted.",
            ]
        }
    ]
}

# ============================================
# ANIMATION TIMELINES
# ============================================

@dataclass
class AnimationPhase:
    """Single phase in animation timeline"""
    name: str
    duration: int  # ms
    delay: int  # ms from start
    animations: Dict[str, any]
    messages: List[str]

class TimelineGenerator:
    """Generates Framer Motion timeline configurations"""
    
    @staticmethod
    def generate_timeline(context: SyncContext) -> List[AnimationPhase]:
        """Generate complete animation timeline for context"""
        phases = []
        cumulative_delay = 0
        
        narratives = STATUS_NARRATIVES[context]
        
        for narrative in narratives:
            phase_name = narrative['phase']
            duration = narrative['duration']
            
            # Generate animations based on phase
            animations = TimelineGenerator._get_phase_animations(phase_name, context)
            
            phases.append(AnimationPhase(
                name=phase_name,
                duration=duration,
                delay=cumulative_delay,
                animations=animations,
                messages=narrative['messages']
            ))
            
            cumulative_delay += duration
        
        return phases
    
    @staticmethod
    def _get_phase_animations(phase_name: str, context: SyncContext) -> Dict:
        """Get specific animations for each phase"""
        
        if phase_name in ['initiation', 'quick_check', 'acknowledge']:
            return {
                'pulse_ring': {
                    'scale': [1, 1.2, 1],
                    'opacity': [0, 1, 1],
                    'transition': { 'duration': 1.2, 'ease': 'easeOut' }
                },
                'logo': {
                    'scale': [0.8, 1.05, 1],
                    'opacity': [0, 1, 1],
                    'transition': { 'duration': 0.8, 'ease': [0.34, 1.56, 0.64, 1] }
                }
            }
        elif phase_name in ['active_scan', 'process', 'retry']:
            return {
                'sweep_light': { 'enabled': True },
                'particles': { 'enabled': True, 'count': 20 }
            }
        elif phase_name in ['synthesis']:
            return {
                'particles': { 'enabled': True, 'converge': True, 'count': 30 }
            }
        elif phase_name in ['resolution', 'complete']:
            return {
                'container': { 'scale': [1, 1.05, 1] },
                'success_burst': { 'enabled': True }
            }
        return {}

# ============================================
# VUE COMPONENT GENERATOR
# ============================================

class VueComponentGenerator:
    @staticmethod
    def generate(context: SyncContext, theme: str = 'dark') -> str:
        timeline = TimelineGenerator.generate_timeline(context)
        phases_json = json.dumps([{
            'name': p.name,
            'duration': p.duration,
            'delay': p.delay,
            'messages': p.messages
        } for p in timeline], indent=2)
        
        primary_color = "hsl(165, 67%, 42%)" if context == SyncContext.FLINKS_INITIAL else "hsl(220, 85%, 52%)"
        
        return f'''<template>
  <div class="sync-ui" @click="handlePoke">
    <div class="sync-ui__glow"></div>
    <div class="sync-ui__logo">
       <svg width="48" height="48" viewBox="0 0 24 24" fill="{primary_color}">
         <path d="M12 2L2 7v10c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-10-5z" />
       </svg>
    </div>
    <div class="sync-ui__status">{{{{ currentMessage }}}}</div>
    <div class="sync-ui__progress">
      <div class="sync-ui__progress-bar" :style="{{ width: progressPercent + '%', background: '{primary_color}' }}"></div>
    </div>
  </div>
</template>

<script setup>
import {{ ref, computed, onMounted }} from 'vue'
const phases = {phases_json}
const currentPhaseIndex = ref(0)
const messageIndex = ref(0)
const progressPercent = ref(0)

const currentMessage = computed(() => {{
  const phase = phases[currentPhaseIndex.value]
  return phase ? phase.messages[messageIndex.value % phase.messages.length] : ''
}})

const handlePoke = () => {{ /* Particle logic injected here */ }}

onMounted(() => {{
  let start = Date.now()
  const total = phases.reduce((s, p) => s + p.duration, 0)
  const update = () => {{
    const elapsed = Date.now() - start
    progressPercent.value = Math.min((elapsed / total) * 100, 100)
    
    // Phase logic
    let cur = 0, acc = 0
    for(let i=0; i<phases.length; i++) {{
      acc += phases[i].duration
      if(elapsed < acc) {{ cur = i; break; }}
      cur = phases.length - 1
    }}
    currentPhaseIndex.value = cur
    messageIndex.value = Math.floor(elapsed / 2000)
    
    if(progressPercent.value < 100) requestAnimationFrame(update)
  }}
  update()
}})
</script>

<style scoped>
.sync-ui {{ background: #0f172a; height: 300px; display: flex; flex-direction: column; align-items: center; justify-content: center; border-radius: 12px; position: relative; overflow: hidden; }}
.sync-ui__status {{ color: #f8fafc; margin-top: 20px; font-family: sans-serif; }}
.sync-ui__progress {{ position: absolute; bottom: 0; width: 100%; height: 4px; background: #1e293b; }}
.sync-ui__progress-bar {{ height: 100%; transition: width 0.3s; }}
</style>
'''

def main():
    context = SyncContext.FLINKS_INITIAL
    if '--context' in sys.argv:
        try: context = SyncContext(sys.argv[sys.argv.index('--context') + 1])
        except: pass
    
    vue = VueComponentGenerator.generate(context)
    
    if '--output' in sys.argv:
        out = Path(sys.argv[sys.argv.index('--output') + 1])
        out.write_text(vue)
        print(f"✅ Generated {{out}}")
    else:
        print(vue)

if __name__ == "__main__":
    main()
