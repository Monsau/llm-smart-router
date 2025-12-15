# Publishing LLM Smart Router to GitHub & PyPI

## 📋 Prerequisites

1. **GitHub Account**: `monsau`
2. **PyPI Account**: Create at https://pypi.org/account/register/
3. **GitHub Personal Access Token**: Create at https://github.com/settings/tokens
4. **PyPI API Token**: Create at https://pypi.org/manage/account/token/

## 🚀 Step 1: Create GitHub Repository

### Option A: Via GitHub Web Interface (Recommended)

1. Go to https://github.com/new
2. Fill in:
   - **Owner**: monsau
   - **Repository name**: `llm-smart-router`
   - **Description**: `⚡ Domain-based tool selection for LLMs. Reduce 100+ tools to 3-8 relevant ones. 95.8% reduction, <200ms latency.`
   - **Visibility**: ✅ Public
   - **Add README**: ❌ NO (we already have one)
   - **Add .gitignore**: ❌ NO
   - **License**: ❌ NO (we have MIT license)
3. Click **Create repository**

### Option B: Via GitHub CLI (if installed)

```bash
# Install GitHub CLI first: winget install --id GitHub.cli
gh auth login
gh repo create llm-smart-router --public --source=. --remote=origin --push
```

## 📤 Step 2: Push to GitHub

After creating the repo on GitHub, run in PowerShell:

```powershell
cd C:\projets\llm-smart-router

# Add remote
git remote add origin https://github.com/monsau/llm-smart-router.git

# Push code
git branch -M main
git push -u origin main
```

If prompted for credentials:
- **Username**: monsau
- **Password**: Use your Personal Access Token (not your GitHub password)

## 🏷️ Step 3: Create GitHub Release

1. Go to https://github.com/monsau/llm-smart-router/releases/new
2. Fill in:
   - **Tag**: `v0.1.0`
   - **Release title**: `v0.1.0 - Initial Release`
   - **Description**:
     ```markdown
     ## 🎉 Initial Release
     
     Domain-based tool selection for Large Language Models.
     
     ### ✨ Features
     - 95.8% tool reduction (93 → 3-8 tools)
     - <200ms routing latency
     - 90%+ confidence scores
     - Multi-provider support (OpenAI, Groq, Anthropic, Ollama)
     - LangChain compatible
     - Type-safe with Pydantic
     
     ### 📦 Installation
     ```bash
     pip install llm-smart-router
     ```
     
     ### 📚 Documentation
     See [README.md](README.md) for quick start and examples.
     ```
3. Click **Publish release**

## 📦 Step 4: Publish to PyPI

### Setup

1. Create PyPI account: https://pypi.org/account/register/
2. Create API token: https://pypi.org/manage/account/token/
   - Token name: `llm-smart-router`
   - Scope: `Entire account` (for first upload)
   - Copy the token (starts with `pypi-...`)

### Build Package

```powershell
cd C:\projets\llm-smart-router

# Install build tools
pip install build twine

# Build distribution
python -m build
```

This creates:
- `dist/llm_smart_router-0.1.0-py3-none-any.whl`
- `dist/llm-smart-router-0.1.0.tar.gz`

### Upload to PyPI

```powershell
# Upload
twine upload dist/*

# When prompted:
# Username: __token__
# Password: <paste your PyPI token>
```

### Verify Installation

```powershell
# Create test environment
python -m venv test_env
.\test_env\Scripts\activate
pip install llm-smart-router

# Test import
python -c "from smart_router import SmartRouter; print('✅ Success!')"
```

## 🎨 Step 5: Add GitHub Badges (Optional)

After publishing to PyPI, update README.md badges:

```markdown
[![PyPI version](https://badge.fury.io/py/llm-smart-router.svg)](https://pypi.org/project/llm-smart-router/)
[![Downloads](https://pepy.tech/badge/llm-smart-router)](https://pepy.tech/project/llm-smart-router)
[![GitHub stars](https://img.shields.io/github/stars/monsau/llm-smart-router.svg)](https://github.com/monsau/llm-smart-router/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
```

## ✅ Verification Checklist

- [ ] GitHub repo created: https://github.com/monsau/llm-smart-router
- [ ] Code pushed to GitHub
- [ ] GitHub release v0.1.0 published
- [ ] Package published to PyPI: https://pypi.org/project/llm-smart-router/
- [ ] Installation test successful
- [ ] README badges updated
- [ ] CI/CD workflows running

## 🔄 Future Updates

For version 0.2.0:

```powershell
# Update version in pyproject.toml
# Update CHANGELOG.md

git add .
git commit -m "Release v0.2.0"
git tag v0.2.0
git push origin main --tags

# Rebuild and upload
python -m build
twine upload dist/*
```

## 🆘 Troubleshooting

### GitHub Authentication Failed
- Use Personal Access Token instead of password
- Token needs `repo` scope

### PyPI Upload Failed
```powershell
# Check package validity
twine check dist/*

# Use test PyPI first
twine upload --repository testpypi dist/*
```

### CI/CD Not Running
- Check .github/workflows/ files exist
- Ensure PYPI_API_TOKEN secret is set in GitHub repo settings

## 📞 Support

- **Issues**: https://github.com/monsau/llm-smart-router/issues
- **Discussions**: https://github.com/monsau/llm-smart-router/discussions
