<script setup lang="ts">
import { marked } from 'marked'

interface Message {
  role: 'user' | 'assistant'
  content: string
}

const props = defineProps<{
  message: Message
  isLast: boolean
  isLoading: boolean
}>()

// Configure marked for safe rendering
marked.setOptions({
  breaks: true,
  gfm: true,
})

// Render markdown content
const renderedContent = computed(() => {
  if (!props.message.content) return ''
  return marked.parse(props.message.content) as string
})
</script>

<template>
  <div
    class="flex gap-3 animate-fade-in"
    :class="message.role === 'user' ? 'justify-end' : 'justify-start'"
  >
    <!-- Assistant avatar -->
    <div
      v-if="message.role === 'assistant'"
      class="w-8 h-8 avatar-cyber flex-shrink-0 mt-1"
    >
      <IconsIconRobot class="w-4 h-4" style="color: #22d3ee;" />
    </div>

    <!-- Message bubble -->
    <div
      :class="message.role === 'user' ? 'chat-bubble-user' : 'chat-bubble-assistant'"
      class="markdown-content"
    >
      <!-- Rendered markdown content -->
      <div
        v-if="message.content"
        class="prose-chat"
        v-html="renderedContent"
      ></div>

      <!-- Typing indicator for streaming (when no content yet) -->
      <span v-if="isLoading && message.role === 'assistant' && !message.content" class="typing-indicator">
        <span></span>
        <span></span>
        <span></span>
      </span>

      <!-- Cursor for streaming text -->
      <span
        v-if="isLoading && message.role === 'assistant' && message.content"
        class="inline-block w-0.5 h-4 ml-0.5 align-middle animate-pulse"
        style="background: #22d3ee;"
      ></span>
    </div>

    <!-- User avatar -->
    <div
      v-if="message.role === 'user'"
      class="w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 mt-1"
      style="background: linear-gradient(135deg, #00d4ff 0%, #0891b2 100%);"
    >
      <IconsIconUser class="w-4 h-4" style="color: #0a0a10;" />
    </div>
  </div>
</template>

<style scoped>
/* Markdown prose styles for chat */
.prose-chat {
  font-size: 0.875rem;
  line-height: 1.6;
}

.prose-chat :deep(p) {
  margin: 0.5em 0;
}

.prose-chat :deep(p:first-child) {
  margin-top: 0;
}

.prose-chat :deep(p:last-child) {
  margin-bottom: 0;
}

.prose-chat :deep(strong) {
  font-weight: 600;
  color: #f1f5f9;
}

.prose-chat :deep(em) {
  font-style: italic;
}

.prose-chat :deep(code) {
  background: rgba(0, 212, 255, 0.1);
  padding: 0.15em 0.4em;
  border-radius: 4px;
  font-size: 0.85em;
  font-family: 'SF Mono', 'Fira Code', monospace;
  color: #67e8f9;
}

.prose-chat :deep(pre) {
  background: rgba(0, 0, 0, 0.3);
  padding: 0.75em 1em;
  border-radius: 8px;
  overflow-x: auto;
  margin: 0.75em 0;
  border: 1px solid rgba(0, 212, 255, 0.1);
}

.prose-chat :deep(pre code) {
  background: none;
  padding: 0;
  font-size: 0.8em;
  color: #e2e8f0;
}

.prose-chat :deep(ul),
.prose-chat :deep(ol) {
  margin: 0.5em 0;
  padding-left: 1.5em;
}

.prose-chat :deep(li) {
  margin: 0.25em 0;
}

.prose-chat :deep(blockquote) {
  border-left: 3px solid #00d4ff;
  padding-left: 1em;
  margin: 0.75em 0;
  color: #94a3b8;
  font-style: italic;
}

.prose-chat :deep(a) {
  color: #22d3ee;
  text-decoration: underline;
  text-underline-offset: 2px;
}

.prose-chat :deep(a:hover) {
  color: #67e8f9;
}

.prose-chat :deep(h1),
.prose-chat :deep(h2),
.prose-chat :deep(h3),
.prose-chat :deep(h4) {
  font-weight: 600;
  color: #f1f5f9;
  margin: 0.75em 0 0.5em;
}

.prose-chat :deep(h1) { font-size: 1.25em; }
.prose-chat :deep(h2) { font-size: 1.125em; }
.prose-chat :deep(h3) { font-size: 1em; }

.prose-chat :deep(hr) {
  border: none;
  border-top: 1px solid rgba(0, 212, 255, 0.2);
  margin: 1em 0;
}

.prose-chat :deep(table) {
  width: 100%;
  border-collapse: collapse;
  margin: 0.75em 0;
  font-size: 0.85em;
}

.prose-chat :deep(th),
.prose-chat :deep(td) {
  border: 1px solid rgba(0, 212, 255, 0.2);
  padding: 0.5em 0.75em;
  text-align: left;
}

.prose-chat :deep(th) {
  background: rgba(0, 212, 255, 0.1);
  font-weight: 600;
}

/* User message specific overrides */
.chat-bubble-user .prose-chat :deep(code) {
  background: rgba(0, 0, 0, 0.2);
  color: #0a0a10;
}

.chat-bubble-user .prose-chat :deep(strong) {
  color: #0a0a10;
}

.chat-bubble-user .prose-chat :deep(a) {
  color: #0a0a10;
}
</style>
