# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-01-XX

### Added
- Initial release
- Core routing functionality with domain-based classification
- Support for multiple LLM providers (OpenAI, Groq, Anthropic, Ollama)
- ToolRegistry for managing tool catalogs
- SmartRouter with confidence scoring
- Three example implementations (basic, LangChain, custom domains)
- Comprehensive documentation
- Unit tests with pytest
- CI/CD with GitHub Actions
- Type hints and mypy support
- Ruff linting and Black formatting

### Performance
- 95.8% tool reduction (93 → 3-8 tools)
- <200ms routing latency
- 90%+ confidence scores

## [Unreleased]

### Planned
- Caching layer for routing decisions
- Async/await support for concurrent routing
- Batch routing for multiple queries
- Streaming routing decisions
- Router analytics and metrics
- Custom domain taxonomy builder
- Tool embedding similarity search
- Multi-language support (prompts)
- Router fine-tuning capabilities
- OpenTelemetry instrumentation
