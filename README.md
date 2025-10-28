# UserForge v1.0.0

**The Ultimate Pentesting Tool for Active Directory & Brute-Force Attacks**

UserForge is a powerful and highly configurable tool designed for penetration testers and security professionals to generate comprehensive and realistic username and password wordlists for Active Directory (AD) environments and general brute-force attacks. Based on extensive research, UserForge implements critical corporate password patterns to achieve an exceptionally high success rate in simulated attacks.

This tool is styled after the "Cracknic" programming conventions, inspired by the NmapFlow template, ensuring clean, readable, and maintainable code.

---

## 🎯 Key Features

### CRITICAL Corporate Patterns
Implements highly effective, research-backed password patterns:
- **Incremental Passwords:** `Password1!`, `Password2!`
- **Quarter/Fiscal Patterns:** `Q1-2024`, `FY2024`
- **Department Passwords:** `IT2024!`, `HR2025@`
- **Company + Temporal Patterns:** `CompanyName2024!`

### Advanced Features
- **28 CLI Arguments:** Unprecedented control over wordlist generation
- **Independent Depth Control:** Separate depth levels for usernames (`-ud`) and passwords (`-pd`)
- **5 Generation Levels:** From basic to maximum complexity (`-d 1` to `-d 5`)
- **Dual-Mode Transformations:** Applying prefixes, suffixes, or leet speak generates **BOTH** the original and modified versions for maximum coverage
- **Multiple Export Formats:** TXT, JSON, and XML (applied to all output directories)
- **Organized Output:** Structured `combined/` and `by_person/` directories
- **Multi-Language & Multi-Country Support:** Localized patterns (seasons, months)
- **No External Dependencies:** Runs on standard Python 3.6+

### Code Quality (Phase 3)
- **Modular Architecture:** 40+ specialized functions
- **32 Unit Tests:** 100% passing with 80% code coverage
- **Complete Documentation:** Docstrings with examples for all functions
- **Professional Logging:** Structured logging with file output
- **Progress Indicators:** Real-time visual feedback

---

## 📦 Installation

UserForge is designed to be simple to install and run on any system with Python 3.6+.

```bash
# 1. Clone the repository (or download the source code)
git clone https://github.com/cracknic/UserForge.git
cd UserForge

# 2. Make the installer executable
chmod +x install.sh

# 3. Run the installer
./install.sh

# To uninstall at any time:
./install.sh --uninstall
```

---

## 🚀 Quick Start

### Basic Usage

Generate a standard wordlist for a list of names:

```bash
userforge -i names.txt -d 3
```

### With Passwords

Generate usernames and passwords targeting a specific company:

```bash
userforge -i names.txt -o output_wordlists -d 3 \
  --company-name "TechCorp" \
  --passwords \
  --quarters \
  --departments
```

### Independent Depth Control

Generate many usernames but fewer passwords:

```bash
userforge -i names.txt -ud 5 -pd 2 \
  --passwords \
  --company-name "MegaCorp"
```

### Dual-Mode with Prefixes/Suffixes

Generate both original and modified versions:

```bash
userforge -i names.txt -d 3 \
  --passwords \
  --user-prefix "corp_" \
  --pass-suffix "!"
```

**Result:** Generates `usuario` AND `corp_usuario`, `Password2024` AND `Password2024!`

### All Formats

Export in TXT, JSON, and XML:

```bash
userforge -i names.txt -d 3 \
  --passwords \
  --format all
```

---

## 📋 Full Argument Reference

UserForge provides **28 command-line arguments** for maximum flexibility.

### Core Options

| Argument | Short | Description | Default | Example |
|---|---|---|---|---|
| `--input` | `-i` | Path to the input file with names (one full name per line) | `None` | `-i names.txt` |
| `--depth` | `-d` | Generation depth (1-5). Applies to both usernames and passwords if specific depths are not set | `3` | `-d 4` |
| `--user-depth` | `-ud` | Username generation depth (1-5). **Overrides `--depth` for usernames only** | `None` | `-ud 2` |
| `--pass-depth` | `-pd` | Password generation depth (1-5). **Overrides `--depth` for passwords only** | `None` | `-pd 5` |
| `--passwords` | | Generate password patterns in addition to usernames | `False` | `--passwords` |
| `--emails` | | Generate email addresses for the given domains (comma-separated) | `None` | `--emails example.com` |
| `--company-name` | | Name of the target company for corporate patterns | `None` | `--company-name "Acme Corp"` |
| `--output` | `-o` | Output directory to save the generated wordlists | `userforge_output` | `-o /tmp/wordlists` |

### Output & Display

| Argument | Short | Description | Default | Example |
|---|---|---|---|---|
| `--format` | | Output format (`txt`, `json`, `xml`, `all`). **Applies to both `combined/` and `by_person/` directories** | `txt` | `--format all` |
| `--verbose` | `-v` | Enable verbose logging to see detailed progress | `False` | `-v` |

### Length Filtering

| Argument | Short | Description | Default | Example |
|---|---|---|---|---|
| `--min-user-length` | | Minimum length for generated usernames | `4` | `--min-user-length 6` |
| `--max-user-length` | | Maximum length for generated usernames | `30` | `--max-user-length 20` |
| `--min-pass-length` | | Minimum length for generated passwords | `6` | `--min-pass-length 8` |
| `--max-pass-length` | | Maximum length for generated passwords | `50` | `--max-pass-length 16` |

### Localization

| Argument | Short | Description | Default | Example |
|---|---|---|---|---|
| `--country` | | Country code for localized patterns (e.g., seasons) | `US` | `--country DE` |
| `--language` | | Language for months, seasons, and common words | `EN` | `--language ES` |

### Leet Speak

| Argument | Short | Description | Default | Example |
|---|---|---|---|---|
| `--leet` | | Global leet speak level (0-3). **Generates both the original and leet versions** | `0` | `--leet 2` |
| `--leet-user` | | Leet speak level for usernames only (0-3). **Generates both versions** | `0` | `--leet-user 1` |
| `--leet-password` | | Leet speak level for passwords only (0-3). **Generates both versions** | `0` | `--leet-password 3` |

### Prefix/Suffix
| Argument | Short | Description | Default | Example |
|---|---|---|---|---|
| `--user-prefix` | | Add a prefix to usernames. **Generates both the original and prefixed versions** | `""` | `--user-prefix "test-"` |
| `--user-suffix` | | Add a suffix to usernames. **Generates both the original and suffixed versions** | `""` | `--user-suffix ".adm"` |
| `--pass-prefix` | | Add a prefix to passwords. **Generates both the original and prefixed versions** | `""` | `--pass-prefix "!"` |
| `--pass-suffix` | | Add a suffix to passwords. **Generates both the original and suffixed versions** | `""` | `--pass-suffix "#"` |

### Password Enhancements

| Argument | Short | Description | Default | Example |
|---|---|---|---|---|
| `--years` | | Year range for temporal patterns. Supports range format (`2024-2025`) or comma-separated (`2024,2025,2026`) | Current Year | `--years 2024-2025` or `--years 2024,2025` |
| `--common-words` | | Additional common words for password patterns (comma-separated) | `None` | `--common-words "Project,Secret"` |
| `--keyboard-patterns` | | Include keyboard-based patterns (e.g., `qwerty`, `asdfgh`) | `False` | `--keyboard-patterns` |
| `--numeric-sequences` | | Include common numeric sequences (e.g., `123456`, `987654`) | `False` | `--numeric-sequences` |
| `--rotation-count` | | Number of incremental passwords to generate (e.g., `Password1!` to `PasswordN!`) | `12` | `--rotation-count 24` |

### Corporate Patterns
| Argument | Short | Description | Default | Example |
|---|---|---|---|---|
| `--quarters` | | Include financial quarter patterns (e.g., `Q1-2024`, `FY2024`) | `False` | `--quarters` |
| `--departments` | | Include department-based patterns (e.g., `IT2024`, `HR2024`) | `False` | `--departments` |

---

## 📊 Generation Depth Levels

### Unified Depth (`--depth` / `-d`)

Sets the same depth for both usernames and passwords.

| Level | Usernames | Passwords | Use Case |
|-------|-----------|-----------|----------|
| 1 | ~150 | ~500 | Quick tests |
| 2 | ~500 | ~1,000 | Standard enumeration |
| 3 | ~1,000 | ~2,000 | **Default - Balanced** |
| 4 | ~2,000 | ~5,000 | Comprehensive attacks |
| 5 | ~8,000+ | ~10,000+ | Maximum coverage |

### Independent Depth Control

Use `-ud` and `-pd` for granular control:

```bash
# Many usernames, few passwords
userforge -i names.txt -ud 5 -pd 1 --passwords

# Few usernames, many passwords (known user)
userforge -i admin.txt -ud 1 -pd 5 --passwords
```

---

## 🎨 Personalized Transformations

When applying modifications (prefixes, suffixes, leet speak), UserForge generates **BOTH** versions:

### Example 1: User Prefix

```bash
userforge -i names.txt --user-prefix "corp_"
```

**Generates:**
- `jsmith` (original)
- `corp_jsmith` (prefixed)

### Example 2: Password Suffix

```bash
userforge -i names.txt --passwords --pass-suffix "!"
```

**Generates:**
- `Welcome2024` (original)
- `Welcome2024!` (suffixed)

### Example 3: Leet Speak

```bash
userforge -i names.txt --passwords --leet-password 2
```

**Generates:**
- `Password` (original)
- `P@ssw0rd` (leet)

**Benefit:** Maximum coverage without losing original patterns.

---

## 📁 Output Structure

```
output_directory/
├── combined/
│   ├── all_usernames.txt
│   ├── all_usernames.json
│   ├── all_usernames.xml
│   ├── all_passwords.txt
│   ├── all_passwords.json
│   └── all_passwords.xml
└── by_person/
    ├── john_smith/
    │   ├── usernames.txt
    │   ├── usernames.json
    │   ├── usernames.xml
    │   ├── passwords.txt
    │   ├── passwords.json
    │   └── passwords.xml
    └── maria_garcia/
        └── ...
```

**Note:** The `--format` argument applies to **ALL** output directories.

---

## 📖 Examples

### Example 1: Standard Attack

```bash
userforge -i employees.txt \
  -d 3 \
  --passwords \
  --company-name "TechCorp" \
  --quarters \
  --departments
```

**Result:** Comprehensive wordlists with corporate patterns.

### Example 2: Targeted Attack (Known Username)

```bash
userforge -i admin.txt \
  -ud 1 \
  -pd 5 \
  --passwords \
  --company-name "MegaCorp" \
  --pass-suffix "!"
```

**Result:** Few username variations, maximum password coverage.

### Example 3: Enumeration Focus

```bash
userforge -i names.txt \
  -ud 5 \
  --user-prefix "corp_" \
  --format all
```

**Result:** Maximum username variations in all formats.

### Example 4: Multi-Format Export

```bash
userforge -i names.txt \
  -d 3 \
  --passwords \
  --format all
```

**Result:** TXT, JSON, and XML files in both `combined/` and `by_person/` directories.

---

## 🚀 Performance

### Optimizations

- **Set-based operations** for deduplication (+20% speed)
- **LRU cache** for localized data (+10% speed)
- **Batch processing** for large datasets
- **Efficient filtering** with early returns

### Benchmarks

| Names | Depth | Usernames | Passwords | Time |
|-------|-------|-----------|-----------|------|
| 3 | 3 | 504 | 2,124 | 0.01s |
| 10 | 3 | 1,680 | 7,080 | 0.03s |
| 100 | 3 | 16,800 | 70,800 | 0.3s |
| 1,000 | 3 | 168,000 | 708,000 | 3s |

---

## 📝 License

This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📚 Documentation

- **README.md** - This file (overview and quick reference)
- **docs/MANUAL_EN.md** - Complete English manual
- **docs/MANUAL_ES.md** - Complete Spanish manual
- **CHANGELOG.md** - Version history

---

## 🎯 Credits

**Author:** Cracknic  
**Version:** 1.0.0  
**License:** GNU GPL v3.0  

---

**UserForge v1.0.0** - Professional-grade wordlist generation for security professionals.

