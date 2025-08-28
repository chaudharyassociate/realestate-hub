# CID Copilot

A modern, scalable monorepo for AI-powered copilot applications with integrated cybersecurity and pentesting tools.

## Overview

CID Copilot is designed as a comprehensive AI-powered platform that combines intelligent copilot functionality with cybersecurity tools and multiple AI model integrations. Built as a monorepo, it enables seamless development, testing, and deployment of interconnected services.

## Features

- **AI-Powered Copilot**: Intelligent assistance using multiple AI models (GPT-OSS, LLaMA 3, Qwen 3)
- **Cybersecurity Tools**: Integrated pentesting frameworks (Sniper, NodeGoat, Reconness)
- **Modular Architecture**: Shared packages for core functionality and LangChain integration
- **Docker Integration**: Containerized services for easy deployment and scaling
- **Workspace Management**: PNPM-based monorepo with efficient dependency management

## Tech Stack

- **Runtime:** Node.js 18+, Python 3.11+
- **Package Manager:** PNPM (recommended) or NPM
- **Frontend/Backend:** Express.js, FastAPI
- **AI Integration:** LangChain, Transformers, Multiple LLM APIs
- **Containerization:** Docker, Docker Compose
- **Cybersecurity:** Custom pentesting tools, OWASP NodeGoat

## Structure

```
cid-copilot/
├── apps/
│   └── cid-app/                 # Main application (Express.js API server)
│       ├── index.js             # Entry point
│       ├── package.json         # App-specific dependencies
│       ├── routes/              # API route handlers
│       └── Dockerfile           # Container configuration
│
├── packages/                    # Shared internal libraries
│   ├── copilotkit/              # Core copilot functionality
│   └── langchainjs/             # AI/LLM integration wrapper
│
├── docker/                      # Containerized external services
│   ├── sniper/                  # Automated pentesting framework
│   ├── nodegoat/                # OWASP vulnerable app for testing
│   ├── reconness/               # Reconnaissance/OSINT framework
│   ├── gpt-oss/                 # GPT-compatible AI service
│   ├── llama3/                  # Meta LLaMA 3 model service
│   └── qwen3/                   # Alibaba Qwen 3 model service
│
├── pnpm-workspace.yaml          # Monorepo workspace configuration
├── package.json                 # Root dependencies and scripts
├── docker-compose.yml           # Multi-service orchestration
└── README.md                    # This file
```

## Getting Started

### Prerequisites

- Node.js 18+ 
- PNPM 8+ (recommended) or NPM
- Docker & Docker Compose
- Git

### Quick Start

1. **Clone and Install:**
    ```bash
    git clone <repository-url>
    cd cid-copilot
    pnpm install
    ```

2. **Start All Services:**
    ```bash
    # Start Docker services (AI models + security tools)
    pnpm docker:up
    
    # Start main application
    pnpm dev
    ```

3. **Access Services:**
    - **Main API:** http://localhost:3000
    - **GPT-OSS:** http://localhost:8001  
    - **LLaMA 3:** http://localhost:8002
    - **Qwen 3:** http://localhost:8003
    - **Sniper:** http://localhost:8080
    - **NodeGoat:** http://localhost:4000
    - **Reconness:** http://localhost:8081

### Development Workflow

```bash
# Install dependencies for all workspaces
pnpm install

# Run main application in development mode
pnpm dev

# Build all packages
pnpm build

# Run tests across all packages
pnpm test

# Lint all code
pnpm lint

# Start specific Docker services
docker compose up gpt-oss llama3 qwen3

# Stop all services
pnpm docker:down
```

## API Endpoints

### Main Application (Port 3000)

- `GET /` - Service status and health check
- `GET /health` - Health endpoint

### Copilot API (`/api/copilot`)
- `GET /api/copilot/status` - Copilot service status
- `POST /api/copilot/chat` - Chat with AI copilot
- `POST /api/copilot/analyze` - Code analysis

### Pentesting API (`/api/pentest`) 
- `GET /api/pentest/tools` - Available pentesting tools
- `POST /api/pentest/scan` - Initiate security scan
- `GET /api/pentest/scan/:id` - Get scan results

### AI Models API (`/api/ai`)
- `GET /api/ai/models` - List available AI models  
- `POST /api/ai/query` - Query AI models
- `POST /api/ai/analyze-vulnerability` - AI vulnerability analysis

## Architecture

### Apps
- **`cid-app`**: Main Express.js application serving the API and coordinating services

### Packages  
- **`@cid-copilot/copilotkit`**: Core copilot intelligence, utilities, and agent management
- **`@cid-copilot/langchainjs`**: LangChain integration for LLM interactions

### Docker Services
- **`gpt-oss`**: OpenAI-compatible GPT service (Port 8001)
- **`llama3`**: Meta LLaMA 3 model service (Port 8002) 
- **`qwen3`**: Alibaba Qwen 3 model service (Port 8003)
- **`sniper`**: Automated pentesting framework (Port 8080)
- **`nodegoat`**: OWASP vulnerable application (Port 4000)
- **`reconness`**: Reconnaissance framework (Port 8081)

## Environment Configuration

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Key environment variables:
- `NODE_ENV` - Application environment
- `PORT` - Main application port (default: 3000)
- `*_ENDPOINT` - Service endpoint URLs
- `ENABLE_*` - Feature flags

## Workspace Commands

### Package Management
```bash
# Install dependencies for all packages
pnpm install

# Install for specific workspace
pnpm --filter cid-app install

# Add dependency to specific package
pnpm --filter @cid-copilot/copilotkit add lodash
```

### Development
```bash
# Start development server
pnpm dev

# Build all packages
pnpm build

# Run tests
pnpm test

# Lint code
pnpm lint
```

### Docker Operations
```bash
# Start all services
pnpm docker:up

# Start specific services
docker compose up gpt-oss llama3

# View logs
docker compose logs -f cid-app

# Stop all services  
pnpm docker:down

# Rebuild containers
pnpm docker:build
```
