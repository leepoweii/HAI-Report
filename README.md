# HAI-Report

Human-Robot Interaction Virtual Exhibition - 人機互動虛擬展覽應用

結合 VIVERSE 3D 虛擬世界與 AI 導覽員的互動式展覽平台。

## Features

- **3D Virtual World**: 嵌入 HTC VIVERSE 虛擬展覽空間
- **AI Chatbot Guide**: 基於 OpenAI GPT-5 的智慧導覽員，支援即時串流回應
- **Bilingual Support**: 自動偵測並回應中英文
- **Web Search**: AI 可即時搜尋網路資訊輔助回答

## Architecture

```
HAI-Report/
├── api/          # FastAPI backend (Python)
└── web/          # Nuxt 4 frontend (Vue 3)
```

## Quick Start

### Prerequisites

- Python 3.11+
- Node.js 20+
- [uv](https://docs.astral.sh/uv/) (Python package manager)

### API Server

```bash
cd api
cp .env.example .env          # 設定環境變數
uv sync                       # 安裝依賴
uv run uvicorn main:app --reload  # 啟動 (port 8000)
```

### Web Frontend

```bash
cd web
npm install                   # 安裝依賴
npm run dev                   # 啟動 (port 3000)
```

## Environment Variables

### API (`api/.env`)

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | Yes | OpenAI API Key |
| `OPENAI_MODEL` | No | Model name (default: `gpt-5-mini`) |
| `USE_WEB_SEARCH` | No | Enable web search (default: `true`) |
| `LINE_CHANNEL_SECRET` | No | LINE Bot integration |
| `LINE_CHANNEL_ACCESS_TOKEN` | No | LINE Bot integration |

### Web (`web/.env`)

| Variable | Required | Description |
|----------|----------|-------------|
| `NUXT_PUBLIC_API_URL` | No | API endpoint (default: `http://localhost:8000`) |

## Tech Stack

**Backend**
- FastAPI + Uvicorn
- OpenAI Responses API (streaming)
- Python 3.11+

**Frontend**
- Nuxt 4 (Vue 3, SPA mode)
- Tailwind CSS
- TypeScript

## License

MIT
