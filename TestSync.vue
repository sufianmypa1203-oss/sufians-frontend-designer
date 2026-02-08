<template>
  <div class="sync-ui" @click="handlePoke">
    <div class="sync-ui__glow"></div>
    <div class="sync-ui__logo">
       <svg width="48" height="48" viewBox="0 0 24 24" fill="hsl(165, 67%, 42%)">
         <path d="M12 2L2 7v10c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-10-5z" />
       </svg>
    </div>
    <div class="sync-ui__status">{{ currentMessage }}</div>
    <div class="sync-ui__progress">
      <div class="sync-ui__progress-bar" :style="{ width: progressPercent + '%', background: 'hsl(165, 67%, 42%)' }"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
const phases = [
  {
    "name": "initiation",
    "duration": 3000,
    "delay": 0,
    "messages": [
      "Establishing secure connection...",
      "Finding your bank's digital vault...",
      "Initiating encrypted handshake...",
      "Verifying security protocols..."
    ]
  },
  {
    "name": "active_scan",
    "duration": 12000,
    "delay": 3000,
    "messages": [
      "Scanning transaction history...",
      "Analyzing spending patterns...",
      "Organizing your coffee habit...",
      "Categorizing groceries vs. late-night snacks...",
      "Detecting your favorite restaurants...",
      "Mapping your financial DNA..."
    ]
  },
  {
    "name": "synthesis",
    "duration": 5000,
    "delay": 15000,
    "messages": [
      "Building your financial dashboard...",
      "Crafting insights from data...",
      "Connecting the dots...",
      "Finalizing your money story..."
    ]
  },
  {
    "name": "resolution",
    "duration": 1000,
    "delay": 20000,
    "messages": [
      "Welcome to clarity.",
      "Your finances, visualized.",
      "Ready to explore."
    ]
  }
]
const currentPhaseIndex = ref(0)
const messageIndex = ref(0)
const progressPercent = ref(0)

const currentMessage = computed(() => {
  const phase = phases[currentPhaseIndex.value]
  return phase ? phase.messages[messageIndex.value % phase.messages.length] : ''
})

const handlePoke = () => { /* Particle logic injected here */ }

onMounted(() => {
  let start = Date.now()
  const total = phases.reduce((s, p) => s + p.duration, 0)
  const update = () => {
    const elapsed = Date.now() - start
    progressPercent.value = Math.min((elapsed / total) * 100, 100)
    
    // Phase logic
    let cur = 0, acc = 0
    for(let i=0; i<phases.length; i++) {
      acc += phases[i].duration
      if(elapsed < acc) { cur = i; break; }
      cur = phases.length - 1
    }
    currentPhaseIndex.value = cur
    messageIndex.value = Math.floor(elapsed / 2000)
    
    if(progressPercent.value < 100) requestAnimationFrame(update)
  }
  update()
})
</script>

<style scoped>
.sync-ui { background: #0f172a; height: 300px; display: flex; flex-direction: column; align-items: center; justify-content: center; border-radius: 12px; position: relative; overflow: hidden; }
.sync-ui__status { color: #f8fafc; margin-top: 20px; font-family: sans-serif; }
.sync-ui__progress { position: absolute; bottom: 0; width: 100%; height: 4px; background: #1e293b; }
.sync-ui__progress-bar { height: 100%; transition: width 0.3s; }
</style>
