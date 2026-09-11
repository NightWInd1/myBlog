<script setup>
import { site } from '../config/site'
import Icon from './Icon.vue'
</script>
<template>
  <footer class="site-footer">
    <div class="footer-brand">
      <Icon name="leaf" :size="19" />
      {{ site.name }}
      <span>记录，是为了更好地出发。</span>
    </div>
    <div class="footer-bottom">
      <span>
        © {{ new Date().getFullYear() }} {{ site.author }} · Made with care.
      </span>
      <span>
        Design inspired by
        <a
          href="https://github.com/CuteLeaf/Firefly"
          target="_blank"
          rel="noopener noreferrer"
        >
          Firefly
        </a>
        <span class="footer-separator">/</span>
        <a href="/feed/">RSS</a>
      </span>
    </div>
  </footer>
</template>
