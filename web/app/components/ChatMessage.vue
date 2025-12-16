<script setup lang="ts">
interface Message {
  role: 'user' | 'assistant'
  content: string
}

defineProps<{
  message: Message
  isLast: boolean
  isLoading: boolean
}>()
</script>

<template>
  <div
    class="flex"
    :class="message.role === 'user' ? 'justify-end' : 'justify-start'"
  >
    <!-- Assistant avatar -->
    <div
      v-if="message.role === 'assistant'"
      class="w-8 h-8 rounded-full bg-accent/20 flex items-center justify-center mr-2 flex-shrink-0 mt-1"
    >
      <IconsIconRobot class="w-4 h-4 text-accent" />
    </div>

    <!-- Message bubble -->
    <div
      :class="message.role === 'user' ? 'chat-bubble-user' : 'chat-bubble-assistant'"
    >
      <!-- Message content -->
      <div class="whitespace-pre-wrap break-words">
        {{ message.content }}

        <!-- Typing indicator for streaming -->
        <span v-if="isLoading && message.role === 'assistant'" class="typing-indicator ml-1">
          <span></span>
          <span></span>
          <span></span>
        </span>
      </div>
    </div>

    <!-- User avatar -->
    <div
      v-if="message.role === 'user'"
      class="w-8 h-8 rounded-full bg-accent flex items-center justify-center ml-2 flex-shrink-0 mt-1"
    >
      <IconsIconUser class="w-4 h-4 text-white" />
    </div>
  </div>
</template>
