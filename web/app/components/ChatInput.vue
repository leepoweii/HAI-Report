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
    textareaRef.value.style.height = Math.min(textareaRef.value.scrollHeight, 150) + 'px'
  }
}

// Handle send
function handleSend() {
  if (input.value.trim() && !props.disabled) {
    emit('send', input.value)
    input.value = ''
    // Reset textarea height
    if (textareaRef.value) {
      textareaRef.value.style.height = 'auto'
    }
  }
}

// Handle key press (Enter to send, Shift+Enter for new line)
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
    <div class="flex-1 relative">
      <textarea
        ref="textareaRef"
        v-model="input"
        :disabled="disabled"
        placeholder="請輸入您的問題..."
        rows="1"
        class="w-full px-4 py-3 bg-space-700 border border-space-600 rounded-xl
               text-slate-100 placeholder-slate-500
               focus:outline-none focus:border-accent focus:ring-1 focus:ring-accent
               disabled:opacity-50 disabled:cursor-not-allowed
               resize-none transition-all duration-200"
        @input="autoResize"
        @keydown="handleKeyDown"
      />
    </div>

    <!-- Send button -->
    <button
      :disabled="disabled || !input.trim()"
      class="btn-glow p-3 rounded-xl"
      @click="handleSend"
    >
      <!-- Send icon -->
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 24 24"
        fill="currentColor"
        class="w-5 h-5"
      >
        <path
          d="M3.478 2.404a.75.75 0 0 0-.926.941l2.432 7.905H13.5a.75.75 0 0 1 0 1.5H4.984l-2.432 7.905a.75.75 0 0 0 .926.94 60.519 60.519 0 0 0 18.445-8.986.75.75 0 0 0 0-1.218A60.517 60.517 0 0 0 3.478 2.404Z"
        />
      </svg>
    </button>
  </div>

  <!-- Helper text -->
  <p class="text-xs text-slate-500 mt-2 text-center">
    按 Enter 發送，Shift+Enter 換行
  </p>
</template>
