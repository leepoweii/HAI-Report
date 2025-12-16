<script setup lang="ts">
const props = defineProps<{
  disabled: boolean
}>()

const emit = defineEmits<{
  send: [content: string]
}>()

const input = ref('')
const textareaRef = ref<HTMLTextAreaElement | null>(null)

// Auto-resize textarea
function autoResize() {
  if (textareaRef.value) {
    textareaRef.value.style.height = 'auto'
    textareaRef.value.style.height = Math.min(textareaRef.value.scrollHeight, 100) + 'px'
  }
}

// Handle send
function handleSend() {
  if (input.value.trim() && !props.disabled) {
    emit('send', input.value)
    input.value = ''
    if (textareaRef.value) {
      textareaRef.value.style.height = 'auto'
    }
  }
}

// Handle key press
function handleKeyDown(e: KeyboardEvent) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault()
    handleSend()
  }
}
</script>

<template>
  <div class="flex gap-2 items-end">
    <!-- Text input -->
    <div class="flex-1">
      <textarea
        ref="textareaRef"
        v-model="input"
        :disabled="disabled"
        placeholder="輸入訊息..."
        rows="1"
        class="w-full px-3 py-2.5 rounded-xl resize-none focus:outline-none disabled:opacity-50 disabled:cursor-not-allowed transition-all"
        style="
          background: rgba(255, 255, 255, 0.08);
          border: 1px solid rgba(255, 255, 255, 0.1);
          color: #f1f5f9;
          font-size: 14px;
          line-height: 1.5;
        "
        @input="autoResize"
        @keydown="handleKeyDown"
      />
    </div>

    <!-- Send button -->
    <button
      :disabled="disabled || !input.trim()"
      class="flex-shrink-0 w-10 h-10 rounded-xl flex items-center justify-center transition-all active:scale-95 disabled:opacity-40 disabled:cursor-not-allowed"
      style="background: linear-gradient(135deg, #00d4ff 0%, #0891b2 100%);"
      @click="handleSend"
      @touchend.prevent="handleSend"
    >
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5" style="color: #0a0a10;">
        <path d="M3.478 2.404a.75.75 0 0 0-.926.941l2.432 7.905H13.5a.75.75 0 0 1 0 1.5H4.984l-2.432 7.905a.75.75 0 0 0 .926.94 60.519 60.519 0 0 0 18.445-8.986.75.75 0 0 0 0-1.218A60.517 60.517 0 0 0 3.478 2.404Z" />
      </svg>
    </button>
  </div>
</template>

<style scoped>
textarea::placeholder {
  color: #64748b;
}

/* Ensure touch-friendly size */
button {
  min-width: 44px;
  min-height: 44px;
}
</style>
