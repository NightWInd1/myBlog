<script setup>
import { computed, onBeforeUnmount, ref, watch } from 'vue'
import { site } from '../config/site'
import Icon from './Icon.vue'
const audio = ref(null),
  playing = ref(false),
  current = ref(0),
  duration = ref(0),
  volume = ref(0.72),
  expanded = ref(false),
  trackIndex = ref(0)
const tracks = computed(() => site.music?.tracks || [])
const track = computed(() => tracks.value[trackIndex.value] || null)
const hasTracks = computed(() => tracks.value.length > 0)
const progress = computed(() =>
  duration.value ? (current.value / duration.value) * 100 : 0,
)
function sync() {
  if (!audio.value) return
  current.value = audio.value.currentTime
  duration.value = audio.value.duration || 0
}
function toggle() {
  if (!audio.value) return
  if (playing.value) audio.value.pause()
  else
    audio.value.play().catch(() => {
      playing.value = false
    })
}
function setTrack(index, autoplay = false) {
  trackIndex.value = index
  current.value = 0
  if (audio.value) {
    audio.value.load()
    if (autoplay) audio.value.play().catch(() => {})
  }
}
function next() {
  if (hasTracks.value)
    setTrack((trackIndex.value + 1) % tracks.value.length, playing.value)
}
function prev() {
  if (hasTracks.value)
    setTrack(
      (trackIndex.value - 1 + tracks.value.length) % tracks.value.length,
      playing.value,
    )
}
function seek(event) {
  if (audio.value && duration.value)
    audio.value.currentTime =
      (Number(event.target.value) / 100) * duration.value
}
function formatTime(value) {
  if (!Number.isFinite(value)) return '0:00'
  return `${Math.floor(value / 60)}:${String(Math.floor(value % 60)).padStart(2, '0')}`
}
watch(volume, (value) => {
  if (audio.value) audio.value.volume = value
})
onBeforeUnmount(() => audio.value?.pause())
</script>
<template>
  <section
    class="panel music-player"
    :class="{ expanded, 'has-track': hasTracks }"
  >
    <div class="music-heading">
      <span>
        <Icon name="music" :size="18" />
        BGM 音乐角
      </span>
      <button
        class="music-expand"
        @click="expanded = !expanded"
        :aria-expanded="expanded"
        aria-label="展开音乐播放器"
      >
        <Icon :name="expanded ? 'up' : 'down'" :size="15" />
      </button>
    </div>
    <template v-if="hasTracks">
      <audio
        ref="audio"
        :src="track.src"
        preload="metadata"
        @timeupdate="sync"
        @loadedmetadata="sync"
        @play="playing = true"
        @pause="playing = false"
        @ended="next"
      />
      <div class="music-main">
        <div class="music-disc" :class="{ spinning: playing }">
          <span>♪</span>
        </div>
        <div class="music-info">
          <strong>{{ track.title }}</strong>
          <span>{{ track.artist || 'Nightwind playlist' }}</span>
        </div>
      </div>
      <input
        class="music-progress"
        type="range"
        min="0"
        max="100"
        :value="progress"
        aria-label="播放进度"
        @input="seek"
      />
      <div class="music-time">
        <span>{{ formatTime(current) }}</span>
        <span>{{ formatTime(duration) }}</span>
      </div>
      <div class="music-controls">
        <button @click="prev" aria-label="上一首">
          <Icon name="prev" :size="15" />
        </button>
        <button
          class="music-play"
          @click="toggle"
          :aria-label="playing ? '暂停' : '播放'"
        >
          <Icon :name="playing ? 'pause' : 'play'" :size="17" />
        </button>
        <button @click="next" aria-label="下一首">
          <Icon name="next" :size="15" />
        </button>
      </div>
      <div v-if="expanded" class="music-extra">
        <label>
          <Icon name="volume" :size="14" />
          <input
            v-model.number="volume"
            type="range"
            min="0"
            max="1"
            step=".01"
            aria-label="音量"
          />
        </label>
        <button
          v-for="(item, index) in tracks"
          :key="item.src"
          class="music-track"
          :class="{ active: index === trackIndex }"
          @click="setTrack(index, playing)"
        >
          {{ item.title }}
          <small>{{ item.artist }}</small>
        </button>
      </div>
    </template>
    <div v-else class="music-empty">
      <div class="music-note"><Icon name="music" :size="22" /></div>
      <p>此处留给喜欢的旋律</p>
      <small>
        在
        <code>config/site.js</code>
        的
        <code>music.tracks</code>
        中填入音频地址即可播放。
      </small>
    </div>
  </section>
</template>
