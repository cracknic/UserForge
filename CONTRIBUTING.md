# Contributing to UserForge

First off, thank you for considering contributing to UserForge! It's people like you that make UserForge such a great tool for the security community.

## Code of Conduct

This project and everyone participating in it is governed by our commitment to ethical security research. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if applicable**
- **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List any alternative solutions you've considered**

### Pull Requests

- Fill in the required template
- Follow the Python style guide (PEP 8)
- Include appropriate test cases
- Update documentation as needed
- End all files with a newline

## Development Setup

```bash
# Clone your fork
git clone https://github.com/cracknic/userforge.git
cd userforge

# Create a branch
git checkout -b feature/your-feature-name

# Make your changes
# ...

# Test your changes
python3 userforge.py -i examples/names.txt -v

# Commit your changes
git add .
git commit -m "Add: your feature description"

# Push to your fork
git push origin feature/your-feature-name

# Create a Pull Request
```

## Style Guidelines

### Python Style Guide

- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and concise
- Use type hints where appropriate

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

**Commit Message Format:**
```
Type: Brief description

Detailed description if needed

Fixes #123
```

**Types:**
- `Add:` New feature
- `Fix:` Bug fix
- `Update:` Update existing feature
- `Remove:` Remove feature
- `Docs:` Documentation changes
- `Style:` Code style changes (formatting, etc.)
- `Refactor:` Code refactoring
- `Test:` Adding or updating tests

## Research Contributions

If you have research on corporate naming conventions, password patterns, or email formats:

1. Document your sources
2. Provide statistical backing
3. Include real-world examples (anonymized)
4. Submit as a GitHub issue with the `research` label

## Pattern Contributions

New pattern suggestions are welcome! Include:

- Pattern description
- Real-world usage examples
- Industry/sector where it's common
- Estimated frequency/probability

## Legal and Ethical Guidelines

- **All contributions must be for authorized security testing purposes**
- Do not include patterns derived from unauthorized access
- Do not include real credentials or sensitive data
- Respect responsible disclosure practices
- Follow all applicable laws and regulations

## Questions?

Feel free to open an issue with the `question` label.

---

Thank you for contributing to UserForge! 
