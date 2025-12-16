<script setup lang="ts">
import { useChat } from '~/composables/useChat'

const { messages, isLoading, sendMessage } = useChat()
const messagesContainer = ref<HTMLElement | null>(null)

// Suggested questions for quick start
const suggestedQuestions = [
  '這個展覽有什麼內容？',
  '如何操作虛擬世界？',
  '人機互動是什麼？',
]

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

// Handle suggested question click
function handleSuggestedClick(question: string) {
  sendMessage(question)
}
</script>

<template>
  <div class="flex flex-col h-full text-white">
    <!-- Messages Area -->
    <div
      ref="messagesContainer"
      class="flex-1 overflow-y-auto px-4 py-3 space-y-4"
    >
      <!-- Welcome message if no messages -->
      <div v-if="messages.length === 0" class="flex flex-col items-center justify-center h-full py-4">
        <!-- Main welcome -->
        <div class="text-center mb-6">
          <div
            class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4"
            style="background: linear-gradient(135deg, rgba(0, 212, 255, 0.15) 0%, rgba(168, 85, 247, 0.1) 100%); border: 1px solid rgba(0, 212, 255, 0.25);"
          >
            <IconsIconWave class="w-8 h-8" style="color: #22d3ee;" />
          </div>

          <h3 class="text-lg font-semibold mb-2" style="color: #f1f5f9;">
            歡迎！
          </h3>
          <p class="text-sm max-w-[260px] mx-auto leading-relaxed" style="color: #94a3b8;">
            我可以回答關於人機互動展覽的任何問題
          </p>
        </div>

        <!-- Suggested questions -->
        <div class="w-full">
          <p class="text-xs text-center mb-3 uppercase tracking-wider" style="color: #64748b;">
            試試這些問題
          </p>
          <div class="flex flex-col gap-2 px-2">
            <button
              v-for="question in suggestedQuestions"
              :key="question"
              class="w-full px-4 py-2.5 text-sm text-left rounded-xl transition-all duration-200 active:scale-[0.98]"
              style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); color: #e2e8f0;"
              @click="handleSuggestedClick(question)"
              @touchend.prevent="handleSuggestedClick(question)"
            >
              {{ question }}
            </button>
          </div>
        </div>
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
    <div
      class="flex-shrink-0 p-3"
      style="background: rgba(0, 0, 0, 0.15); border-top: 1px solid rgba(255, 255, 255, 0.05);"
    >
      <ChatInput
        :disabled="isLoading"
        @send="handleSend"
      />
    </div>
  </div>
</template>
