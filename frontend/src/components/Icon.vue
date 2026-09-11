<script setup>
defineProps({ name: String, size: { type: [Number, String], default: 20 } })
const paths = {
  home: 'm3 10 9-7 9 7v10a1 1 0 0 1-1 1h-5v-7H9v7H4a1 1 0 0 1-1-1Z',
  leaf: 'M20 4C9 1 2 8 6 15c7 6 16-1 14-11ZM4 21l11-11M8 17v-6m0 6h6',
  search: 'M21 21l-5-5M18 10a8 8 0 1 1-16 0 8 8 0 0 1 16 0',
  sun: 'M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.5 1.5m11 11L19 19M5 19l1.5-1.5m11-11L19 5',
  moon: 'M20.9 13A9 9 0 0 1 11 3.1 9 9 0 1 0 20.9 13Z',
  monitor: 'M3 4h18v13H3ZM8 21h8m-4-4v4',
  palette:
    'M12 3a9 9 0 1 0 0 18h1a2 2 0 0 0 1-3.7 1 1 0 0 1 .5-1.8H17a4 4 0 0 0 4-4A9 9 0 0 0 12 3ZM7 10h.01M10 6h.01M15 7h.01M18 11h.01',
  menu: 'M4 6h16M4 12h16M4 18h16',
  close: 'm6 6 12 12M6 18 18 6',
  arrow: 'M5 12h14m-6-6 6 6-6 6',
  chevron: 'm9 5 7 7-7 7',
  down: 'm6 9 6 6 6-6',
  up: 'm6 14 6-6 6 6',
  calendar: 'M4 5h16v16H4ZM8 3v4m8-4v4M4 11h16',
  folder: 'M3 6V4h6l2 3h10v13H3Z',
  archive: 'M3 3h18v5H3Zm2 5v13h14V8M10 12h4',
  book: 'M12 5C9 3 5 3 2 4v16c3-1 7-1 10 1 3-2 7-2 10-1V4c-3-1-7-1-10 1Zm0 0v16',
  clock: 'M12 8v5l3 2M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0',
  message: 'M21 3H3v14h4v4l5-4h9ZM7 8h10M7 12h6',
  pin: 'm9 3 6 0-1 6 4 4v2H6v-2l4-4ZM12 15v7',
  grid: 'M3 3h7v7H3Zm11 0h7v7h-7ZM3 14h7v7H3Zm11 0h7v7h-7Z',
  list: 'M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01',
  info: 'M12 11v6m0-10h.01M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0',
  mail: 'M3 5h18v14H3Zm0 0 9 8 9-8',
  rss: 'M4 11a9 9 0 0 1 9 9M4 4a16 16 0 0 1 16 16M5 19h.01',
  github:
    'M9 19c-4 1-4-2-6-2m12 5v-4c0-1-.3-1.7-1-2 4-.5 6-2 6-6 0-1.5-.5-2.7-1.5-3.7.2-1 .2-2-.2-3.3-1.6 0-3 1-4 1.5a14 14 0 0 0-5 0C8.3 4 7 3 5.5 3c-.5 1.3-.5 2.3-.2 3.3C4.3 7.3 4 8.5 4 10c0 4 2 5.5 6 6-.7.3-1 1-1 2v4',
  heart:
    'M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8Z',
  spark: 'm12 3 2.5 6.5L21 12l-6.5 2.5L12 21l-2.5-6.5L3 12l6.5-2.5Z',
  coffee:
    'M4 7h12v10a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4Zm12 1h2a3 3 0 0 1 0 6h-2M7 1v2m5-2v2',
}
</script>
<template>
  <svg
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    stroke-width="1.7"
    stroke-linecap="round"
    stroke-linejoin="round"
    aria-hidden="true"
  >
    <path :d="paths[name] || paths.leaf" />
  </svg>
</template>
