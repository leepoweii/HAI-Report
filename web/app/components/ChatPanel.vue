<script setup lang="ts">
import { useChat } from '~/composables/useChat'

const { messages, isLoading, sendMessage } = useChat()
const messagesContainer = ref<HTMLElement | null>(null)

// Auto-scroll to bottom when new messages arrive
watch(messages, () => {
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  })
}, { deep: true })

// Handle sending message
function handleSend(content: string) {
  if (content.trim()) {
    sendMessage(content)
  }
}
</script>

<template>
  <div class="flex flex-col h-full bg-space-800/50 backdrop-blur-sm">
    <!-- Header -->
    <div class="px-4 py-3 border-b border-space-700 flex items-center gap-3">
      <div class="w-10 h-10 rounded-full bg-accent/20 flex items-center justify-center">
        <IconsIconRobot class="w-6 h-6 text-accent" />
      </div>
      <div>
        <h2 class="font-semibold text-slate-100">展覽導覽</h2>
        <p class="text-xs text-slate-400">歡迎詢問展覽相關問題！</p>
      </div>
    </div>

    <!-- Messages Area -->
    <div
      ref="messagesContainer"
      class="flex-1 overflow-y-auto p-4 space-y-4"
    >
      <!-- Welcome message if no messages -->
      <div v-if="messages.length === 0" class="text-center py-8">
        <div class="w-16 h-16 rounded-full bg-accent/20 flex items-center justify-center mx-auto mb-4">
          <IconsIconWave class="w-8 h-8 text-accent" />
        </div>
        <h3 class="text-lg font-medium text-slate-200 mb-2">歡迎！</h3>
        <p class="text-slate-400 text-sm max-w-xs mx-auto">
          我是人機互動展覽的導覽助手，歡迎隨時向我提問！
        </p>
      </div>

      <!-- Messages -->
      <ChatMessage
        v-for="(message, index) in messages"
        :key="index"
        :message="message"
        :is-last="index === messages.length - 1"
        :is-loading="isLoading && index === messages.length - 1 && message.role === 'assistant'"
      />
    </div>

    <!-- Input Area -->
    <div class="p-4 border-t border-space-700">
      <ChatInput
        :disabled="isLoading"
        @send="handleSend"
      />
    </div>
  </div>
</template>
