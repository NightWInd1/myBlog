<template>
  <canvas ref="canvas" class="particle-bg" aria-hidden="true"></canvas>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const canvas = ref(null)
let ctx, particles = [], animId
const count = 80

class Particle {
  constructor(w, h) {
    this.x = Math.random() * w
    this.y = Math.random() * h
    this.vx = (Math.random() - 0.5) * 0.5
    this.vy = (Math.random() - 0.5) * 0.5
    this.size = Math.random() * 2 + 0.5
  }
  update(w, h) {
    this.x += this.vx
    this.y += this.vy
    if (this.x < 0) this.x = w
    if (this.x > w) this.x = 0
    if (this.y < 0) this.y = h
    if (this.y > h) this.y = 0
  }
  draw(ctx) {
    ctx.beginPath()
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2)
    ctx.fill()
  }
}

function init() {
  const c = canvas.value
  if (!c) return
  ctx = c.getContext('2d')
  resize()
  particles = Array.from({ length: count }, () => new Particle(c.width, c.height))
  animate()
}

function resize() {
  const c = canvas.value
  if (!c) return
  c.width = window.innerWidth
  c.height = window.innerHeight
}

function animate() {
  const c = canvas.value
  if (!c || !ctx) return
  ctx.clearRect(0, 0, c.width, c.height)
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark'
  const color = isDark ? 'rgba(99, 179, 237, 0.35)' : 'rgba(66, 153, 225, 0.25)'

  particles.forEach((p, i) => {
    p.update(c.width, c.height)
    p.draw(ctx)
    ctx.fillStyle = color

    for (let j = i + 1; j < particles.length; j++) {
      const dx = p.x - particles[j].x
      const dy = p.y - particles[j].y
      const dist = Math.sqrt(dx * dx + dy * dy)
      if (dist < 120) {
        ctx.beginPath()
        ctx.moveTo(p.x, p.y)
        ctx.lineTo(particles[j].x, particles[j].y)
        ctx.strokeStyle = isDark
          ? `rgba(99, 179, 237, ${0.12 * (1 - dist / 120)})`
          : `rgba(66, 153, 225, ${0.08 * (1 - dist / 120)})`
        ctx.stroke()
      }
    }
  })

  animId = requestAnimationFrame(animate)
}

onMounted(init)
onUnmounted(() => cancelAnimationFrame(animId))
window.addEventListener('resize', resize)
</script>

<style scoped>
.particle-bg {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  z-index: 0;
  pointer-events: none;
}
</style>
