# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

HAI-Report is a Human-Robot Interaction Virtual Exhibition application featuring an embedded VIVERSE 3D world alongside an AI chatbot guide. The project uses a monorepo structure with two main components.

## Architecture

```
HAI-Report/
├── api/          # FastAPI backend (Python)
└── web/          # Nuxt 4 frontend (Vue 3)
```

### Backend (api/)
- **Framework**: FastAPI with uvicorn, uses `uv` for dependency management
- **AI Integration**: OpenAI Responses API (streaming) via `client.responses.create()`
- **Routers**:
  - `/chat` - Streaming chat endpoint for web frontend
  - `/line/webhook` - LINE Bot integration (non-streaming)
- **Prompt System**: System prompt defined in `prompts/guide.py`, loads dynamic context from `context/exhibition.md`
- **Key Pattern**: Chatbot knowledge is externalized to `context/exhibition.md` for easy editing without code changes

### Frontend (web/)
- **Framework**: Nuxt 4 in SPA mode (SSR disabled)
- **Styling**: Tailwind CSS with custom dark "space" theme colors
- **Layout**: Split view - VIVERSE 3D world (70%) + ChatPanel (30%)
- **Chat Composable**: `useChat.ts` handles streaming responses from the API
- **VIVERSE Integration**: Embeds HTC VIVERSE world via iframe in `ViverseEmbed.vue`

## Development Commands

### API Server
```bash
cd api
uv sync                                    # Install dependencies
uv run uvicorn main:app --reload           # Start dev server (port 8000)
```

### Web Frontend
```bash
cd web
npm install                                # Install dependencies
npm run dev                                # Start dev server (port 3000)
```

### Docker (API)
```bash
cd api
docker build -t hai-api .
docker run -p 8000:8000 -e OPENAI_API_KEY=xxx hai-api
```

## Environment Variables

### API (`api/.env`)
- `OPENAI_API_KEY` - Required
- `OPENAI_MODEL` - Defaults to "gpt-5-mini"
- `USE_WEB_SEARCH` - Enable OpenAI web search tool (default: true)
- `LINE_CHANNEL_SECRET` - Optional, for LINE Bot
- `LINE_CHANNEL_ACCESS_TOKEN` - Optional, for LINE Bot

### Web (`web/.env`)
- `NUXT_PUBLIC_API_URL` - API endpoint (default: http://localhost:8000)

## Key Implementation Details

- The chatbot uses OpenAI's Responses API (not Chat Completions), which supports built-in tools like web search
- Streaming is handled differently: backend yields text chunks, frontend reads via `response.body.getReader()`
- The system prompt includes bilingual (English/Chinese) support - chatbot matches user's language
- Exhibition content updates require editing `api/context/exhibition.md` and restarting the API
