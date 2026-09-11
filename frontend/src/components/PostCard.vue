<script setup>
import { computed, ref, watch } from 'vue'
import { site } from '../config/site'
import { formatDate } from '../utils/format'
import Icon from './Icon.vue'
const props = defineProps({
  post: { type: Object, required: true },
  index: { type: Number, default: 0 },
})
const failed = ref(false)
watch(
  () => props.post.cover_image,
  () => {
    failed.value = false
  },
)
const cover = computed(() =>
  !failed.value && props.post.cover_image
    ? props.post.cover_image
    : site.heroImage,
)
</script>
<template>
  <article class="post-card panel">
    <div class="post-card-body">
      <div class="post-card-kicker">
        <span v-if="post.is_pinned" class="pin-label">
          <Icon name="pin" :size="12" />
          置顶
        </span>
        <router-link
          v-if="post.category_slug"
          :to="`/category/${post.category_slug}`"
        >
          {{ post.category_name }}
        </router-link>
        <span v-else>未分类</span>
        <span class="kicker-line"></span>
      </div>
      <h2>
        <router-link :to="`/post/${post.slug}`">{{ post.title }}</router-link>
      </h2>
      <div class="post-meta">
        <time>
          <Icon name="calendar" :size="13" />
          {{ formatDate(post.created_at) }}
        </time>
        <span>
          <Icon name="clock" :size="13" />
          {{ post.reading_minutes }} 分钟阅读
        </span>
      </div>
      <p class="post-excerpt">
        {{ post.excerpt || '每一段记录，都是生活留下的回响。' }}
      </p>
      <div class="post-card-footer">
        <span class="post-author">
          <span class="author-dot"></span>
          {{ post.author_name || site.author }}
          <span v-if="post.comment_count" class="post-comment-count">
            <Icon name="message" :size="13" />
            {{ post.comment_count }}
          </span>
        </span>
        <router-link :to="`/post/${post.slug}`" class="read-more">
          阅读全文
          <Icon name="arrow" :size="15" />
        </router-link>
      </div>
    </div>
    <router-link
      :to="`/post/${post.slug}`"
      class="post-card-cover"
      tabindex="-1"
      aria-hidden="true"
    >
      <img
        :src="cover"
        alt=""
        loading="lazy"
        :style="{ objectPosition: `${35 + (index % 3) * 20}% center` }"
        @error="failed = true"
      />
      <span v-if="!post.cover_image || failed" class="cover-caption">
        {{ ['INTO THE QUIET', 'LITTLE THOUGHTS', 'MAKE SOMETHING'][index % 3] }}
      </span>
      <span class="cover-arrow"><Icon name="arrow" :size="20" /></span>
    </router-link>
  </article>
</template>
