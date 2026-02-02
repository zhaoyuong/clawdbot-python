# ClawdBot Python ---- NEW ONE openclaw-python is ready https://github.com/zhaoyuong/openclaw-python.

> **⚠️ WORK IN PROGRESS**: This project is under active development and approaching production readiness.

A Python implementation of the ClawdBot personal AI assistant platform. This is a port of the [TypeScript version](https://github.com/badlogic/clawdbot), designed to provide a more accessible Python-based alternative with production-grade features.

## Status

| Component | Completion | Status |
|-----------|-----------|--------|
| Agent Runtime | 90% | ✅ Claude & OpenAI, context management, error handling, retry logic |
| Tools System | 85% | ✅ 24+ tools with permissions, rate limiting, timeouts |
| Channel Plugins | 70% | ✅ 4 fully implemented (Telegram, Discord, Slack, WebChat) + 13 stubs |
| REST API | 100% | ✅ Full FastAPI + OpenAI-compatible endpoints |
| Authentication | 100% | ✅ API key management, rate limiting, middleware |
| Monitoring | 90% | ✅ Health checks, metrics, structured logging |
| CLI | 95% | ✅ Full command-line interface with uv support |
| Testing | 60%+ | ✅ 120+ test cases with CI/CD |
| Documentation | 100% | ✅ Comprehensive English documentation |

**Current Development Stage**: Beta - Production MVP ready for testing.

## Quick Start

### Prerequisites

- Python 3.11+
- Poetry (package manager)
- An API key (Anthropic or OpenAI)

### Installation

```bash
# Clone repository
git clone https://github.com/zhaoyuong/clawdbot-python.git
cd clawdbot-python

# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Copy environment template
cp .env.example .env

# Add your API key
echo "ANTHROPIC_API_KEY=your-key-here" >> .env
```

### Basic Usage

```bash
# Chat with agent (one-shot)
uv run clawdbot agent chat "Hello, who are you?"

# Start API server
uv run clawdbot api start

# Check health
uv run clawdbot health check

# View configuration
uv run clawdbot config show
```

### Run Examples

```bash
# Basic agent usage
uv run python examples/01_basic_agent.py

# Agent with tools
uv run python examples/02_with_tools.py

# API server
uv run python examples/04_api_server.py
```

## What's New

### Latest: Multi-Provider Support (v0.4.1)

- **🚀 5 LLM Providers**: Anthropic, OpenAI, Google Gemini, AWS Bedrock, Ollama
- **🆓 Free Options**: Ollama (local), Gemini (free tier)
- **🔒 Privacy**: Run fully local with Ollama
- **⚡ Speed**: Gemini Flash, Claude Haiku
- **🏢 Enterprise**: AWS Bedrock support
- **📦 50+ Models**: Access to massive model ecosystem

### Recent Improvements (v0.4.0)

- **Package Management**: Migrated from Poetry to `uv` for faster, more reliable builds
- **Authentication**: Complete API key management with validation, rotation, and permissions
- **Rate Limiting**: Token bucket rate limiter with per-endpoint controls
- **Error Handling**: Integrated retry logic with exponential backoff and circuit breakers
- **Context Management**: Automatic context window management and message pruning
- **OpenAI Compatibility**: Full `/v1/chat/completions` API compatible with OpenAI SDKs
- **CI/CD**: GitHub Actions workflow with automated testing and Docker builds
- **Documentation**: All documentation converted to English with clear structure
- **Project Structure**: Clean root directory with organized docs/ folder

## Project Structure

```
clawdbot-python/
├── clawdbot/              # Main package
│   ├── agents/            # Agent runtime & tools
│   ├── api/               # REST API server
│   ├── channels/          # Channel plugins
│   ├── config/            # Configuration
│   ├── gateway/           # WebSocket gateway
│   └── monitoring/        # Health & metrics
├── examples/              # Usage examples
├── extensions/            # Channel extensions
├── skills/                # Skill templates
├── tests/                 # Test suite
└── docs/                  # Documentation
```

## Features

### Agent Runtime
- Streaming responses from Claude and OpenAI
- Context window management
- Automatic error handling and retry
- Tool calling support

### Tools
- File operations (read, write, glob, grep)
- Shell command execution
- Web browsing (Playwright)
- Image generation
- And more...

### REST API
- Health check endpoints (`/health`, `/health/live`, `/health/ready`)
- Metrics endpoint (`/metrics`, `/metrics/prometheus`)
- Agent chat API
- Session management
- Channel management

### CLI
- `clawdbot agent chat` - Chat with agent
- `clawdbot api start` - Start API server
- `clawdbot health check` - Run health checks
- `clawdbot config show` - View configuration

## API Documentation

Start the API server and visit:
- Interactive docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development

### Run Tests

```bash
# All tests
poetry run pytest

# With coverage
poetry run pytest --cov=clawdbot --cov-report=html

# Specific test file
poetry run pytest tests/test_runtime.py -v
```

### Code Quality

```bash
# Format code
poetry run black clawdbot/

# Lint
poetry run ruff check clawdbot/

# Type check
poetry run mypy clawdbot/
```

## Docker

```bash
# Build image
docker build -t clawdbot-python .

# Run with docker-compose
docker-compose up

# Run tests in container
./test-docker-safe.sh
```

See [docs/guides/](docs/guides/) for detailed Docker documentation.

## Configuration

Configuration can be set via:
1. Environment variables (`CLAWDBOT_*`)
2. `.env` file
3. JSON config file

Example environment variables:
```bash
CLAWDBOT_AGENT__MODEL=anthropic/claude-sonnet-4-20250514
CLAWDBOT_API__PORT=8000
CLAWDBOT_DEBUG=true
```

## Documentation

- [Quick Start Guide](docs/guides/QUICKSTART.md)
- [Installation](docs/guides/INSTALLATION.md)
- [Architecture](docs/development/ARCHITECTURE.md)
- [Agent Implementation](docs/development/AGENT_IMPLEMENTATION.md)
- [Docker Guide](docs/guides/DOCKER_QUICKSTART.md)

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

This project is a Python port of [ClawdBot](https://github.com/badlogic/clawdbot) by Mario Zechner.

---

**Note**: This is an independent implementation and not affiliated with Anthropic or OpenAI.
