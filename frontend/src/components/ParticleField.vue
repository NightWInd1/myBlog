<script setup>
import { onMounted, onUnmounted, ref } from 'vue'
const canvas = ref(null)
let frame = 0,
  cleanup = () => {}
onMounted(() => {
  const el = canvas.value
  const ctx = el.getContext('2d', { alpha: true })
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)')
  let width = 0,
    height = 0,
    particles = [],
    pointer = { x: -1000, y: -1000 }
  const resize = () => {
    const dpr = Math.min(window.devicePixelRatio || 1, 2)
    width = window.innerWidth
    height = window.innerHeight
    el.width = width * dpr
    el.height = height * dpr
    el.style.width = `${width}px`
    el.style.height = `${height}px`
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0)
    particles = Array.from(
      { length: Math.min(84, Math.max(34, Math.floor(width / 15))) },
      (_, i) => ({
        x: Math.random() * width,
        y: Math.random() * height,
        r: 0.8 + Math.random() * 2.2,
        vx: (Math.random() - 0.5) * 0.16,
        vy: -0.1 - Math.random() * 0.25,
        phase: i,
      }),
    )
  }
  const move = (e) => {
    pointer.x = e.clientX
    pointer.y = e.clientY
  }
  const draw = () => {
    ctx.clearRect(0, 0, width, height)
    for (const p of particles) {
      p.x += p.vx
      p.y += p.vy
      if (p.y < -8) p.y = height + 8
      if (p.x < -8 || p.x > width + 8) p.vx *= -1
      const dx = p.x - pointer.x,
        dy = p.y - pointer.y,
        distance = Math.sqrt(dx * dx + dy * dy)
      if (distance < 120) {
        p.x += (dx / Math.max(distance, 1)) * 0.18
        p.y += (dy / Math.max(distance, 1)) * 0.18
      }
      const glow = 0.24 + Math.sin(Date.now() / 800 + p.phase) * 0.12
      ctx.beginPath()
      ctx.fillStyle = `rgba(236, 116, 160, ${glow})`
      ctx.shadowColor = 'rgba(250, 126, 177, .9)'
      ctx.shadowBlur = 8
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2)
      ctx.fill()
      ctx.shadowBlur = 0
    }
    if (!reduced.matches) frame = requestAnimationFrame(draw)
  }
  resize()
  draw()
  window.addEventListener('resize', resize)
  window.addEventListener('pointermove', move, { passive: true })
  const handleMotionPreference = () => {
    cancelAnimationFrame(frame)
    draw()
  }
  reduced.addEventListener?.('change', handleMotionPreference)
  cleanup = () => {
    cancelAnimationFrame(frame)
    window.removeEventListener('resize', resize)
    window.removeEventListener('pointermove', move)
    reduced.removeEventListener?.('change', handleMotionPreference)
  }
})
onUnmounted(() => cleanup())
</script>
<template>
  <canvas ref="canvas" class="particle-field" aria-hidden="true"></canvas>
</template>
