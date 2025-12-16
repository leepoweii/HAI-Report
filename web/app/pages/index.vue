<script setup lang="ts">
// Main page with VIVERSE world and Chat Panel side by side
</script>

<template>
  <div class="flex flex-col lg:flex-row h-screen">
    <!-- VIVERSE World - Takes 70% on desktop, full width on mobile -->
    <div class="flex-1 lg:flex-[2] min-h-[50vh] lg:min-h-0">
      <ViverseEmbed />
    </div>

    <!-- Chat Panel - Takes 30% on desktop, half height on mobile -->
    <div class="w-full lg:w-[400px] xl:w-[450px] h-[50vh] lg:h-full border-t lg:border-t-0 lg:border-l border-space-700">
      <ChatPanel />
    </div>
  </div>
</template>
