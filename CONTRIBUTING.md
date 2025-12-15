# Contributing to LLM Smart Router

Thank you for considering contributing to LLM Smart Router! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Minimal code example

### Suggesting Features

Feature requests are welcome! Please:
- Check existing issues first
- Clearly describe the use case
- Explain why this would be useful
- Consider if it fits the project scope

### Pull Requests

1. **Fork the repo** and create your branch from `main`
2. **Make your changes** with clear commits
3. **Add tests** for new functionality
4. **Ensure tests pass**: `pytest`
5. **Run linting**: `ruff check smart_router`
6. **Run type checking**: `mypy smart_router`
7. **Update docs** if needed
8. **Submit PR** with clear description

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/llm-smart-router.git
cd llm-smart-router

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Code Style

- Follow PEP 8
- Use type hints
- Write docstrings for public APIs
- Keep functions small and focused
- Line length: 100 characters

### Testing

- Write tests for new features
- Aim for >80% coverage
- Use pytest fixtures
- Mock external LLM calls

```bash
# Run tests
pytest

# With coverage
pytest --cov=smart_router --cov-report=html

# Specific test
pytest tests/test_registry.py::test_register_tool
```

### Commit Messages

- Use present tense: "Add feature" not "Added feature"
- Be concise but descriptive
- Reference issues: "Fix #123: Add caching"

### Code Review Process

1. Maintainer reviews within 3-5 days
2. Address feedback with new commits
3. Once approved, maintainer merges

## Questions?

- Open a [Discussion](https://github.com/yourusername/llm-smart-router/discussions)
- Join our [Discord](https://discord.gg/example) (if applicable)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
