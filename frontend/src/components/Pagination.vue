<script setup>
import { computed } from 'vue'
import Icon from './Icon.vue'
const props = defineProps({ page: Number, totalPages: Number })
defineEmits(['change'])
const pages = computed(() => {
  const values = []
  for (let i = 1; i <= props.totalPages; i++) {
    if (i === 1 || i === props.totalPages || Math.abs(i - props.page) <= 1)
      values.push(i)
    else if (values.at(-1) !== '…') values.push('…')
  }
  return values
})
</script>
<template>
  <nav class="pagination" v-if="totalPages > 1" aria-label="文章分页">
    <button
      class="icon-button"
      :disabled="page === 1"
      @click="$emit('change', page - 1)"
      aria-label="上一页"
    >
      <Icon name="chevron" class="flip" :size="18" />
    </button>
    <template v-for="(p, i) in pages" :key="i">
      <span v-if="p === '…'">…</span>
      <button
        v-else
        :class="{ current: p === page }"
        :aria-label="`第 ${p} 页`"
        :aria-current="p === page ? 'page' : undefined"
        @click="$emit('change', p)"
      >
        {{ p }}
      </button>
    </template>
    <button
      class="icon-button"
      :disabled="page === totalPages"
      @click="$emit('change', page + 1)"
      aria-label="下一页"
    >
      <Icon name="chevron" :size="18" />
    </button>
  </nav>
</template>
