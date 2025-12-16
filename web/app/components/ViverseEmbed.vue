<script setup lang="ts">
// VIVERSE World Embed Component
const viverseUrl = 'https://worlds.viverse.com/gda5mZ3?full3d=&no-cookie='
</script>

<template>
  <div class="relative w-full h-full bg-space-900">
    <!-- Loading overlay (shown while iframe loads) -->
    <div class="absolute inset-0 flex items-center justify-center bg-space-900 z-10 transition-opacity duration-500"
         id="viverse-loader">
      <div class="text-center">
        <div class="w-12 h-12 border-4 border-accent border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
        <p class="text-slate-400">Loading Virtual World...</p>
      </div>
    </div>

    <!-- VIVERSE iframe -->
    <iframe
      :src="viverseUrl"
      class="w-full h-full border-0"
      allow="microphone; camera; xr-spatial-tracking; fullscreen; autoplay"
      allowfullscreen
      @load="onIframeLoad"
    />
  </div>
</template>

<script lang="ts">
export default {
  methods: {
    onIframeLoad() {
      // Hide loader when iframe is ready
      const loader = document.getElementById('viverse-loader')
      if (loader) {
        loader.style.opacity = '0'
        setTimeout(() => {
          loader.style.display = 'none'
        }, 500)
      }
    }
  }
}
</script>
