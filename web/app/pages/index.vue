<script setup lang="ts">
// Main page with VIVERSE world and floating chatbot

const isChatOpen = ref(false)
const chatPanelRef = ref<HTMLElement | null>(null)

// Toggle chat open/close
function toggleChat() {
  isChatOpen.value = !isChatOpen.value
}

// Close chat
function closeChat() {
  isChatOpen.value = false
}
</script>

<template>
  <div class="relative h-screen w-screen overflow-hidden">
    <!-- VIVERSE World - Full screen background -->
    <div class="absolute inset-0 z-0">
      <ViverseEmbed />
    </div>

    <!-- Floating Chat Button (when closed) -->
    <Transition name="scale">
      <button
        v-if="!isChatOpen"
        class="fixed bottom-14 right-6 z-50 group"
        style="
          width: 64px;
          height: 64px;
          border-radius: 50%;
          background: linear-gradient(135deg, rgba(0, 212, 255, 0.9) 0%, rgba(8, 145, 178, 0.9) 100%);
          box-shadow: 0 4px 20px rgba(0, 212, 255, 0.4), 0 0 40px rgba(0, 212, 255, 0.2);
          border: 2px solid rgba(255, 255, 255, 0.2);
          cursor: pointer;
          transition: all 0.3s ease;
        "
        @click="toggleChat"
        @touchend.prevent="toggleChat"
      >
        <div class="flex items-center justify-center w-full h-full">
          <IconsIconRobot class="w-8 h-8" style="color: #0a0a10;" />
        </div>

        <!-- Pulse ring animation -->
        <span
          class="absolute inset-0 rounded-full animate-ping opacity-30"
          style="background: rgba(0, 212, 255, 0.5);"
        ></span>

        <!-- Tooltip -->
        <span
          class="absolute bottom-full right-0 mb-2 px-3 py-1.5 rounded-lg text-sm whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none"
          style="background: rgba(0, 0, 0, 0.8); color: #e2e8f0;"
        >
          開啟對話助手
        </span>
      </button>
    </Transition>

    <!-- Chat Panel (when open) -->
    <Transition name="chat-slide">
      <div
        v-if="isChatOpen"
        ref="chatPanelRef"
        class="fixed bottom-14 right-6 z-50 flex flex-col"
        style="
          width: min(400px, calc(100vw - 48px));
          height: min(600px, calc(100vh - 100px));
          border-radius: 20px;
          background: rgba(10, 10, 18, 0.65);
          -webkit-backdrop-filter: blur(24px) saturate(180%);
          backdrop-filter: blur(24px) saturate(180%);
          border: 1px solid rgba(0, 212, 255, 0.15);
          box-shadow:
            0 8px 32px rgba(0, 0, 0, 0.4),
            0 0 0 1px rgba(255, 255, 255, 0.05) inset,
            0 0 80px rgba(0, 212, 255, 0.1);
          overflow: hidden;
        "
      >
        <!-- Chat Header -->
        <div
          class="flex items-center justify-between px-4 py-3 flex-shrink-0"
          style="background: rgba(0, 0, 0, 0.2); border-bottom: 1px solid rgba(255, 255, 255, 0.05);"
        >
          <div class="flex items-center gap-3">
            <div
              class="w-10 h-10 rounded-full flex items-center justify-center"
              style="background: linear-gradient(135deg, rgba(0, 212, 255, 0.2) 0%, rgba(168, 85, 247, 0.1) 100%); border: 1px solid rgba(0, 212, 255, 0.3);"
            >
              <IconsIconRobot class="w-5 h-5" style="color: #22d3ee;" />
            </div>
            <div>
              <h2 class="font-semibold text-sm" style="color: #f1f5f9;">展覽導覽助手</h2>
              <div class="flex items-center gap-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                <span class="text-xs" style="color: #94a3b8;">在線</span>
              </div>
            </div>
          </div>

          <!-- Close button -->
          <button
            class="w-9 h-9 rounded-full flex items-center justify-center transition-all hover:scale-110 active:scale-95"
            style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1);"
            @click="closeChat"
            @touchend.prevent="closeChat"
          >
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5" style="color: #94a3b8;">
              <path fill-rule="evenodd" d="M5.47 5.47a.75.75 0 0 1 1.06 0L12 10.94l5.47-5.47a.75.75 0 1 1 1.06 1.06L13.06 12l5.47 5.47a.75.75 0 1 1-1.06 1.06L12 13.06l-5.47 5.47a.75.75 0 0 1-1.06-1.06L10.94 12 5.47 6.53a.75.75 0 0 1 0-1.06Z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>

        <!-- Chat Content -->
        <div class="flex-1 overflow-hidden">
          <ChatPanel />
        </div>
      </div>
    </Transition>
  </div>
</template>

<style scoped>
/* Scale transition for chat button */
.scale-enter-active,
.scale-leave-active {
  transition: all 0.3s ease;
}

.scale-enter-from,
.scale-leave-to {
  opacity: 0;
  transform: scale(0.8);
}

/* Slide up transition for chat panel */
.chat-slide-enter-active,
.chat-slide-leave-active {
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.chat-slide-enter-from,
.chat-slide-leave-to {
  opacity: 0;
  transform: translateY(20px) scale(0.95);
}

/* Touch-friendly button states */
button:active {
  transform: scale(0.95);
}

@media (hover: hover) {
  button:hover {
    transform: scale(1.05);
  }
}

/* Ensure minimum touch target size */
button {
  min-width: 44px;
  min-height: 44px;
}
</style>
