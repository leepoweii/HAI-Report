export interface Message {
  role: 'user' | 'assistant'
  content: string
}

export function useChat() {
  const config = useRuntimeConfig()
  const messages = ref<Message[]>([])
  const isLoading = ref(false)

  async function sendMessage(content: string) {
    if (!content.trim() || isLoading.value) return

    // Add user message
    messages.value.push({
      role: 'user',
      content: content.trim()
    })

    // Add empty assistant message (will be filled by streaming)
    messages.value.push({
      role: 'assistant',
      content: ''
    })

    const assistantMessageIndex = messages.value.length - 1
    isLoading.value = true

    try {
      // Prepare messages for API (excluding the empty assistant message)
      const apiMessages = messages.value.slice(0, -1).map(m => ({
        role: m.role,
        content: m.content
      }))

      // Call the FastAPI chat endpoint
      const response = await fetch(`${config.public.apiUrl}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ messages: apiMessages })
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      // Handle streaming response
      const reader = response.body?.getReader()
      const decoder = new TextDecoder()

      if (!reader) {
        throw new Error('No response body')
      }

      while (true) {
        const { done, value } = await reader.read()

        if (done) break

        // Decode the chunk and append to the assistant message
        const chunk = decoder.decode(value, { stream: true })
        messages.value[assistantMessageIndex].content += chunk
      }

    } catch (error) {
      console.error('Chat error:', error)

      // Update the assistant message with error
      messages.value[assistantMessageIndex].content =
        'Sorry, I encountered an error. Please make sure the API server is running and try again.'

    } finally {
      isLoading.value = false
    }
  }

  function clearMessages() {
    messages.value = []
  }

  return {
    messages: readonly(messages),
    isLoading: readonly(isLoading),
    sendMessage,
    clearMessages
  }
}
