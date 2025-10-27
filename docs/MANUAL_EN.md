# UserForge v1.0.0 - Official Manual in English

Welcome to the official UserForge manual. This document provides a comprehensive guide to every feature, argument, and workflow available in UserForge v1.0.0. For a quick summary, please refer to the [README.md](../README.md) file.

## Table of Contents

1.  [Introduction](#introduction)
2.  [Key Concepts](#key-concepts)
3.  [Installation](#installation)
4.  [Complete Argument Reference](#complete-argument-reference)
5.  [Detailed Feature Guides](#detailed-feature-guides)
    -   [CRITICAL Corporate Password Patterns](#critical-corporate-password-patterns)
    -   [Generation Depth](#generation-depth)
    -   [Localization](#localization)
    -   [Leet Speak Control](#leet-speak-control)
    -   [Prefix/Suffix Management](#prefixsuffix-management)
6.  [Workflows and Practical Examples](#workflows-and-practical-examples)
7.  [Output Formats](#output-formats)
8.  [License](#license)

---

## 1. Introduction

UserForge is a command-line tool designed for pentesters and security professionals. Its primary purpose is to generate highly realistic and effective username and password lists for attacking Active Directory (AD) environments and other authentication systems.

## 2. Key Concepts

-   **Pattern-Based Generation:** UserForge does not use random characters. It combines base information (names, company, year) with hundreds of predefined patterns (e.g., `firstname.lastname`, `companyAAAA!`, `SeasonAAAA@`).
-   **Depth Levels:** The complexity and size of the output are controlled by a simple depth level (`-d 1` to `-d 5`). Level 1 is fast and small, while Level 5 is exhaustive.
-   **Research-Based Patterns:** The most effective patterns, marked as **CRITICAL**, are derived from the analysis of massive password dumps, targeting common corporate policies such as password rotation every 90 days.

## 3. Installation

UserForge is a standalone Python script with no external dependencies. It requires Python 3.6 or higher.

```bash
# 1. Clone the repository from GitHub
git clone https://github.com/cracknic/userforge.git
cd userforge

# 2. (Optional) Run the installer to create a symbolic link in /usr/local/bin
# This allows you to run 'userforge' from any directory.
chmod +x install.sh
sudo ./install.sh

# To uninstall the symbolic link:
sudo ./install.sh --uninstall

# 3. If you prefer not to install it system-wide, you can run it directly:
python3 userforge.py [arguments]
```

## 4. Complete Argument Reference

This table details the **40 arguments** available in UserForge v1.0.0.

| Argument | Short | Description | Default | Example |
|---|---|---|---|---|
| **Main Options** | | | |
| `--input` | `-i` | Path to the input file with names (one full name per line). | `None` | `-i names.txt` |
| `--depth` | `-d` | Generation depth (1-5). Higher is more comprehensive. | `3` | `-d 4` |
| `--passwords` | | Generate password patterns in addition to usernames. | `False` | `--passwords` |
| `--emails` | | Generate email addresses for given domains (comma-separated). | `None` | `--emails example.com` |
| `--company-name` | | Target company name for corporate patterns. | `None` | `--company-name "Acme Corp"` |
| `--output` | `-o` | Output directory to save the generated wordlists. | `userforge_output` | `-o /tmp/lists` |
| `--format` | | Output format: `txt`, `json`, `xml`, or `all`. | `txt` | `--format all` |
| `--verbose` | `-v` | Enable detailed logging to see progress. | `False` | `-v` |
| **Length Filters** | | | |
| `--min-user-length` | | Minimum length for generated usernames. | `4` | `--min-user-length 6` |
| `--max-user-length` | | Maximum length for generated usernames. | `30` | `--max-user-length 20` |
| `--min-pass-length` | | Minimum length for generated passwords. | `6` | `--min-pass-length 8` |
| `--max-pass-length` | | Maximum length for generated passwords. | `50` | `--max-pass-length 16` |
| **Localization** | | | |
| `--country` | | Country code for localized patterns (e.g., seasons). | `US` | `--country DE` |
| `--language` | | Language for months, seasons, and common words. | `EN` | `--language ES` |
| **Leet Speak** | | | |
| `--leet` | | Global leet speak level (0-3). | `0` | `--leet 2` |
| `--leet-user` | | Leet speak level only for usernames (0-3). | `0` | `--leet-user 1` |
| `--leet-password` | | Leet speak level only for passwords (0-3). | `0` | `--leet-password 3` |
| **Prefixes/Suffixes** | | | |
| `--user-prefix` | | Add a prefix to all generated usernames. | `""` | `--user-prefix "test-"` |
| `--user-suffix` | | Add a suffix to all generated usernames. | `""` | `--user-suffix ".adm"` |
| `--pass-prefix` | | Add a prefix to all generated passwords. | `""` | `--pass-prefix "!"` |
| `--pass-suffix` | | Add a suffix to all generated passwords. | `""` | `--pass-suffix "#"` |
| **Password Enhancements** | | | |
| `--years` | | Year range for temporal patterns (e.g., "2023-2026"). | Current Year | `--years 2020-2025` |
| `--common-words` | | Additional common words for password patterns (comma-separated). | `None` | `--common-words "Project,Secret"` |
| `--keyboard-patterns` | | Include keyboard-based patterns (e.g., `qwerty`, `asdfgh`). | `False` | `--keyboard-patterns` |
| `--numeric-sequences` | | Include common numeric sequences (e.g., `123456`, `987654`). | `False` | `--numeric-sequences` |
| `--rotation-count` | | Number of incremental passwords to generate (e.g., `Password1!` to `PasswordN!`). | `12` | `--rotation-count 24` |
| `--quarters` | | Include fiscal quarter patterns (e.g., `Q1-2024`, `FY2024`). | `False` | `--quarters` |
| `--departments` | | Include department-based patterns (e.g., `IT2024`, `HR2024`). | `False` | `--departments` |
| `--user-depth` | `-ud` | Generation depth only for usernames (1-5). Overrides `--depth` for usernames. | `None` | `-ud 2` |
| `--pass-depth` | `-pd` | Generation depth only for passwords (1-5). Overrides `--depth` for passwords. | `None` | `-pd 5` |
| **Advanced Options** | | | |
| `--company-size` | | Company size for pattern optimization: `startup`, `smb`, `enterprise`, `medium`. | `medium` | `--company-size enterprise` |
| `--complexity` | | Password complexity level: `low`, `medium`, `high`. | `low` | `--complexity high` |
| `--optimize` | | Enable smart pattern optimization. | `False` | `--optimize` |
| `--smart` | | Intelligent mode with contextual analysis. | `False` | `--smart` |
| `--analyze` | | Generate statistical analysis of the wordlists. | `False` | `--analyze` |
| `--target-company` | | Target company for advanced and specific patterns. | `""` | `--target-company "Microsoft"` |
| `--roles` | | List of custom roles/titles (comma-separated). | `""` | `--roles "CEO,CTO,Admin"` |
| `--symbol-positions` | | Where to place symbols in passwords: `start`, `end`, `both`, `random`. | `None` | `--symbol-positions end` |
| `--seasons-only` | | Use only patterns based on seasons of the year. | `False` | `--seasons-only` |
| **Interactive Mode** | | | |
| `--interactive` | `-I` | Enable interactive mode for guided configuration. | `False` | `-I` |


# 5. Detailed Feature Guides


### 5.2 Independent Depth

UserForge v1.0.0 allows granular control over generation depth through separate arguments for usernames and passwords.

#### `--user-depth` / `-ud`

**Description:** Controls generation depth only for usernames (1-5).

**Default value:** `None` (uses the value of `--depth`)

**Use cases:**
- Exhaustive user enumeration with few passwords
- When you know the passwords but need to discover users

**Example:**
```bash
# Many usernames, few passwords
userforge -i names.txt -ud 5 -pd 1 --passwords
```

**Result:** ~8,000 usernames, ~500 passwords

---

#### `--pass-depth` / `-pd`

**Description:** Controls generation depth only for passwords (1-5).

**Default value:** `None` (uses the value of `--depth`)

**Use cases:**
- Attack with known user (e.g., admin)
- Password spraying with a reduced user list

**Example:**
```bash
# Few usernames, many passwords
userforge -i admin.txt -ud 1 -pd 5 --passwords
```

**Result:** ~150 usernames, ~10,000 passwords

---

### 5.3 Advanced Options

#### `--company-size`

**Description:** Specifies the size of the target company to optimize email patterns and organizational structure.

**Values:** `startup`, `smb`, `enterprise`, `medium`

**Default value:** `medium`

**Impact:**
- `startup`: Simple patterns, few departments
- `smb`: Basic structure
- `medium`: Balance between simplicity and complexity
- `enterprise`: Complex structure, many departments

**Example:**
```bash
userforge -i employees.txt --emails company.com --company-size enterprise
```

---

#### `--complexity`

**Description:** Complexity level for password generation.

**Values:** `low`, `medium`, `high`

**Default value:** `low`

**Impact:**
- `low`: Basic patterns (Password123!)
- `medium`: Standard combinations (Welcome@2024)
- `high`: Complex patterns (C0mp@nyN@me2024!)

**Example:**
```bash
userforge -i names.txt --passwords --complexity high -d 4
```

---

#### `--optimize`


**Description:** Activates intelligent optimization that reduces redundant patterns and prioritizes the most effective ones.

**Default value:** `False`

**Benefits:**
- Reduces wordlist size by ~30%
- Maintains the most effective patterns
- Eliminates advanced duplicates

**Example:**
```bash
userforge -i names.txt --passwords -d 5 --optimize
```

---

#### `--smart`

**Description:** Intelligent mode with contextual analysis and pattern adaptation.

**Default value:** `False`

**Features:**
- Analyzes the company context
- Adjusts patterns according to the sector
- Prioritizes patterns based on statistics

**Example:**
```bash
userforge -i names.txt --passwords --company-name "TechCorp" --smart
```

---

#### `--analyze`

**Description:** Generates a complete statistical analysis of the generated wordlists.

**Default value:** `False`

**Generated information:**
- Length distribution
- Most common characters
- Identified patterns
- Complexity metrics

**Example:**
```bash
userforge -i names.txt --passwords -d 3 --analyze
```

---

#### `--target-company`

**Description:** Specifies a target company to generate specific and contextual patterns.

**Default value:** `""`

**Usage:**
- Patterns based on the company’s products
- Acronyms and abbreviations
- Sector-specific terms

**Example:**
```bash
userforge -i names.txt --passwords --target-company "Microsoft" -d 4
```

**Generated patterns:**
- `Azure2024!`
- `Office365@`
- `Windows2024`
- `MSFT2024!`

---

#### `--roles`

**Description:** Custom list of roles/titles to generate specific patterns.

**Default value:** `""`

**Format:** Comma-separated

**Example:**
```bash
userforge -i names.txt --passwords --roles "CEO,CTO,Admin,Manager" -d 3
```

**Generated patterns:**
- `JohnCEO2024`
- `SmithAdmin!`
- `MariaManager@2024`

---

#### `--symbol-positions`
**Description:** Controls where symbols are placed in passwords.

**Values:** `start`, `end`, `both`, `random`

**Default value:** `None` (automatic)

**Example:**
```bash
userforge -i nombres.txt --passwords --symbol-positions end -d 3
```

**Result:**
- `Password2024!` (end)
- `!Password2024` (start)
- `!Password2024!` (both)

---

#### `--seasons-only`

**Description:** Generates only patterns based on seasons of the year.

**Default value:** `False`

**Usage:** Useful for targeted attacks when it is known that the policy uses seasons.

**Example:**
```bash
userforge -i nombres.txt --passwords --seasons-only --language ES
```

**Generated patterns:**
- `Primavera2024`
- `Verano2024!`
- `Otoño2024@`
- `Invierno2024#`

---

### 5.4 Interactive Mode

#### `--interactive` / `-I`

**Description:** Enables interactive mode that guides the user through all available options.

**Default value:** `False`

**Features:**
- Contextual questions
- Suggested default values
- Input validation
- Explanations of each option

**Example:**
```bash
userforge -i nombres.txt -I
```

**Interactive flow:**
1. Generate passwords? (y/n)
2. Unified or separate depth?
3. Company name?
4. Use leet speak?
5. Add prefixes/suffixes?
6. ... (and more)

**Benefit:** Ideal for new users or when you don’t remember all the arguments.



This section provides a comprehensive guide to each available argument in UserForge v1.0.0, organized by functional categories.

---

## 5.1 Main Options

### 5.1.1 `--input` / `-i` (REQUIRED)

**Description:** Specifies the path to the input file containing full names.

**File format:**
- One full name per line
- Format: `FirstName LastName` or `FirstName LastName1 LastName2`
- Supports UTF-8 characters (accents, ñ, etc.)
- Empty lines are ignored

**Example file (`nombres.txt`):**
```
John Michael Smith
María García López
Emilio Dahl Herce
Jean-Pierre Dubois
李明 (Li Ming)
```

**Usage:**
```bash
userforge -i nombres.txt
userforge --input /full/path/nombres.txt
```

**Validation:**
- Names with invalid special characters are omitted with a warning
- Names with fewer than 2 words are accepted but generate fewer patterns
- The number of valid names loaded is recorded

**Tips:**
- Use OSINT (LinkedIn, corporate website) to gather names
- Include name variations (with/without middle name)
- For large organizations, focus on specific departments

---

### 5.1.2 `--depth` / `-d`

**Description:** Controls the generation depth for usernames and passwords in a unified way.

**Values:** 1-5 (Default: 3)

**Breakdown by level:**

#### Level 1 - Basic (~150 patterns per name)
**Generated patterns:**
- Simple names: `john`, `smith`
- Initials: `js`, `jms`
- Basic combinations: `johnsmith`, `smithjohn`
- Simple numbers: `john1`, `smith2`

**Recommended use:** Quick initial enumeration

**Example:**
```bash
userforge -i nombres.txt -d 1
```

**Expected output for "John Smith":**
```
john
smith
jsmith
smithj
js
john1
smith1
```

---

#### Level 2 - Standard (~500 patterns per name)
**Additional patterns:**
- Separators: `john.smith`, `john-smith`, `john_smith`
- Reversals: `smithjohn`, `smith.john`
- Numbers at the end: `jsmith01`, `jsmith99`
- Extended initials: `j.smith`, `john.s`

**Recommended use:** Standard AD attacks

**Example:**
```bash
userforge -i nombres.txt -d 2 --passwords
```

**Expected output:**
```
# Usernames
john.smith
j.smith
smith.john
jsmith01
jsmith2024

# Passwords
Welcome2024
Password123
JohnSmith2024
```

---

#### Level 3 - Advanced (~1,000 patterns per name) **[DEFAULT]**
**Additional patterns:**
- Years: `jsmith2024`, `john2025`
- Seasons: `JohnWinter2024`, `SmithSummer`
- Months: `JohnJanuary`, `SmithDecember2024`
- Basic corporate patterns: `JohnCompany`, `SmithCorp2024`

**Recommended use:** Balanced corporate attacks

**Example:**
```bash
userforge -i nombres.txt -d 3 --passwords --company-name "TechCorp"
```

**Expected output:**
```
# Usernames
jsmith2024
john.smith2025
j.smith.tech
```
# Passwords
Welcome2024!
TechCorp2024
JohnSmithWinter2024
TechCorpJanuary2025
```

---

#### Level 4 - Extensive (~2,000 patterns per name)
**Additional patterns:**
- Basic leet speak: `j0hn`, `sm1th`
- Complex combinations: `JohnSmithTechCorp2024`
- Capitalization variations: `JOHN`, `JoHn`, `jOhN`
- Rotations: `Welcome1!`, `Welcome2!`, ..., `Welcome12!`

**Recommended use:** Exhaustive attacks on specific targets

**Example:**
```bash
userforge -i nombres.txt -d 4 --passwords --company-name "MegaCorp" --quarters
```

**Expected output:**
```
# Passwords
Welcome1!
Welcome2!
MegaCorpQ1-2024
JohnSmith@MegaCorp
M3g4Corp2024!
Q1-2024!
FY2024MegaCorp
```

---

#### Level 5 - Maximum (~8,000+ patterns per name)
**Additional patterns:**
- All possible combinations
- Advanced leet speak: `j0hn$m1th`
- Keyboard patterns: `qwerty`, `asdfgh`
- Numeric sequences: `123456`, `987654`
- All variations of departments, quarters, roles

**Recommended use:** Last resort attacks or exhaustive audits

**⚠️ WARNING:** May generate large files

**Example:**
```bash
userforge -i nombres.txt -d 5 --passwords --company-name "GlobalCorp" --departments --quarters --rotation-count 24
```

**Expected output:** Thousands of patterns per name

---

### 5.1.3 `--user-depth` / `-ud` and `--pass-depth` / `-pd`

**Description:** Independent depth control for usernames and passwords.

**Advantages:**
- Greater flexibility in targeted attacks
- Resource optimization (generate many users, few passwords or vice versa)
- Useful when you know the username but not the password

**Use cases:**

#### Case 1: Known user, unknown password
```bash
userforge -i admin.txt -ud 1 -pd 5 --passwords --company-name "TechCorp"
```
**Result:**
- Few usernames (only basic variations of "admin")
- Thousands of passwords (exhaustive)

---

#### Case 2: User enumeration
```bash
userforge -i nombres.txt -ud 5 --format all
```
**Result:**
- Thousands of usernames (maximum coverage)
- No passwords (no `--passwords` specified)

---

#### Case 3: Balanced attack with priority on passwords
```bash
userforge -i nombres.txt -ud 3 -pd 5 --passwords
```
**Result:**
- ~1,000 usernames per name (advanced)
- ~8,000 passwords per name (maximum)

---

### 5.1.4 `--passwords`

**Description:** Activates the generation of password patterns.

**Without this flag:** Only usernames are generated

**Generated password patterns:**
- Based on names: `JohnSmith2024`, `SmithJohn!`
- Based on company: `TechCorp2024!`, `CompanyName@2025`
- Temporal: `Welcome2024`, `Password2025!`
- Departments: `IT2024!`, `Sales2025@`
- Quarters: `Q1-2024`, `FY2025!`
- Rotations: `Welcome1!` to `Welcome12!`

**Basic example:**
```bash
userforge -i nombres.txt --passwords
```

**Advanced example:**
```bash
userforge -i nombres.txt --passwords \
  --company-name "MegaCorp" \
  --quarters \
  --departments \
  --rotation-count 24 \
  --years 2020-2025
```

---

### 5.1.5 `--emails`

**Description:** Generates email addresses for the specified domains.

**Format:** Domains separated by commas

**Generated patterns:**
- `john.smith@company.com`
- `jsmith@company.com`
- `j.smith@company.com`
- `smithj@company.com`
- `john@company.com`

**Example with one domain:**
```bash
userforge -i nombres.txt --emails company.com
```

**Example with multiple domains:**
```bash
userforge -i nombres.txt --emails company.com,corp.local,company.net
```

**Output:**
```
john.smith@company.com
john.smith@corp.local
john.smith@company.net
jsmith@company.com
jsmith@corp.local
jsmith@company.net
```

**Practical use:**
- Phishing attacks
- Office 365 enumeration
- Password spraying against web services

---

### 5.1.6 `--company-name`

**Description:** Target company name to generate corporate patterns.

**Impact:** Generates hundreds of additional patterns combining the company name with:
- Usernames
- Years
- Seasons
- Departments
- Quarters

**Example:**
```bash
userforge -i nombres.txt --passwords --company-name "TechCorp"
```

**Generated patterns:**
```
# Usernames
john.techcorp
jsmith@techcorp
techcorp.john

# Passwords
TechCorp2024!
JohnTechCorp2024
TechCorpWelcome!
TechCorpQ1-2024
TechCorpIT2024
Welcome@TechCorp
```
```

**Tips:**
- Use the full name: "TechCorp Inc"
- Try variations: "TechCorp", "Tech Corp", "TC"
- Include common company acronyms

---

### 5.1.7 `--output` / `-o`

**Description:** Output directory to save the generated files.

**Default:** `UserForge_Output/UserForge_Output_YYYYMMDD_HHMMSS`

**Output structure:**
```
output_directory/
├── combined/
│   ├── all_usernames.txt
│   ├── all_passwords.txt
│   ├── all_usernames.json  (if --format all)
│   ├── all_passwords.json
│   ├── all_usernames.xml
│   └── all_passwords.xml
├── by_person/
│   ├── john_smith/
│   │   ├── usernames.txt
│   │   ├── passwords.txt
│   │   ├── usernames.json  (if --format all)
│   │   └── passwords.json
│   └── maria_garcia/
│       └── ...
└── userforge.log
```

**Example:**
```bash
userforge -i nombres.txt --passwords -o /tmp/ataque_techcorp
```

---

### 5.1.8 `--format`

**Description:** Format of the output files.

**Options:** `txt`, `json`, `xml`, `all`

**Default:** `txt`

#### TXT Format
```
john.smith
jsmith
j.smith
```

#### JSON Format
```json
{
  "usernames": [
    "john.smith",
    "jsmith",
    "j.smith"
  ],
  "metadata": {
    "count": 3,
    "generated_at": "2024-10-27T10:30:00",
    "source": "John Smith"
  }
}
```

#### XML Format
```xml
<?xml version="1.0" encoding="UTF-8"?>
<wordlist>
  <usernames>
    <username>john.smith</username>
    <username>jsmith</username>
    <username>j.smith</username>
  </usernames>
  <metadata>
    <count>3</count>
    <generated_at>2024-10-27T10:30:00</generated_at>
  </metadata>
</wordlist>
```

**Example:**
```bash
userforge -i nombres.txt --passwords --format all
```

---

### 5.1.9 `--verbose` / `-v`

**Description:** Enables detailed logging.
```
**Displayed Information:**
- Input file and number of loaded names
- Generator configuration (depth, leet, etc.)
- Processing progress with progress bar
- Final statistics (usernames/passwords generated)
- Execution time
- Output files location

**Example without verbose:**
```bash
$ userforge -i nombres.txt --passwords
✓ Generated 504 usernames
✓ Generated 2,124 passwords
```

**Example with verbose:**
```bash
$ userforge -i nombres.txt --passwords -v

[INFO] Input file: nombres.txt
[INFO] Reading input file...
[INFO] Loaded 3 valid name(s)
[INFO] Output directory: /home/user/UserForge_Output/UserForge_Output_20241027_103000
[INFO] Initializing pattern generator...
[INFO]   ├─ Depth Level: 3
[INFO]   ├─ Leet Speak: Level 0
[INFO]   ├─ Company Size: medium
[INFO]   ├─ Language: EN
[INFO]   └─ Country: US
[INFO] Processing 3 name(s)...
Processing names: |████████████████████████████████████████| 100.0% (3/3)
[INFO]   [1/3] Processing: John Smith
[INFO]   [2/3] Processing: Maria Garcia
[INFO]   [3/3] Processing: Emilio Dahl
[SUCCESS] ✓ Generated 504 unique usernames
[SUCCESS] ✓ Generated 2,124 unique passwords
[INFO] Writing output files...
[SUCCESS] ✓ Output written to: /home/user/UserForge_Output/UserForge_Output_20241027_103000

=== SUMMARY ===
📊 Statistics:
  • Total Names Processed: 3
  • Unique Usernames: 504
  • Unique Passwords: 2,124
  • Output Directory: /home/user/UserForge_Output/UserForge_Output_20241027_103000
  • Execution Time: 2.34 seconds
```

---

## 5.2 Length Filters

### 5.2.1 `--min-user-length`

**Description:** Minimum length for generated usernames.

**Default:** 3

**Usage:** Filter out usernames that are too short and do not comply with corporate policies.

**Example:**
```bash
userforge -i nombres.txt --min-user-length 6
```

**Result:**
- ✅ `jsmith` (6 characters)
- ✅ `john.smith` (10 characters)
- ❌ `js` (2 characters - filtered)
- ❌ `john` (4 characters - filtered)

---

### 5.2.2 `--max-user-length`

**Description:** Maximum length for generated usernames.

**Default:** 50

**Usage:** Avoid excessively long usernames that may be rejected by systems.

**Example:**
```bash
userforge -i nombres.txt --max-user-length 20
```

**Result:**
- ✅ `jsmith` (6 characters)
- ✅ `john.smith.techcorp` (19 characters)
- ❌ `john.smith.techcorp.2024` (24 characters - filtered)

---

### 5.2.3 `--min-pass-length`

**Description:** Minimum length for generated passwords.

**Default:** 8
**Usage:** Comply with corporate password policies.

**Example:**
```bash
userforge -i nombres.txt --passwords --min-pass-length 12
```

**Result:**
- ✅ `Welcome2024!` (12 characters)
- ✅ `TechCorp@2024` (13 characters)
- ❌ `Pass123!` (8 characters - filtered)
- ❌ `Welcome!` (8 characters - filtered)

---

### 5.2.4 `--max-pass-length`

**Description:** Maximum length for generated passwords.

**Default:** 50

**Usage:** Avoid excessively long passwords.

**Example:**
```bash
userforge -i nombres.txt --passwords --max-pass-length 16
```

**Result:**
- ✅ `Welcome2024!` (12 characters)
- ❌ `JohnSmithTechCorp2024!` (23 characters - filtered)

---

## 5.3 Localization

### 5.3.1 `--country`

**Description:** Country code for localized patterns.

**Default:** `US`

**Supported countries:** US, UK, CA, AU, DE, FR, ES, IT, PT, MX

**Impact:**
- Date formats (DD/MM/YYYY vs MM/DD/YYYY)
- National holidays
- Cultural patterns

**Example:**
```bash
userforge -i nombres.txt --passwords --country ES --language ES
```

**Generated patterns (Spain):**
```
# Seasons in Spanish
JohnVerano2024
SmithInvierno2025

# Spanish holidays
12Octubre2024  (Día de la Hispanidad)
6Enero2025     (Día de Reyes)

# Spanish date format
25122024       (DD/MM/YYYY)
```

---

### 5.3.2 `--language`

**Description:** Language for months, seasons, and common words.

**Default:** `EN`

**Supported languages:** EN, ES, FR, DE, IT, PT

**Impact:**
- Month names: `January` vs `Enero` vs `Janvier`
- Seasons: `Summer` vs `Verano` vs `Été`
- Common words: `Password` vs `Contraseña` vs `Mot de passe`

**Example with Spanish:**
```bash
userforge -i nombres.txt --passwords --language ES
```

**Generated patterns:**
```
# Months in Spanish
JohnEnero2024
SmithFebrero2025
MariaMarzo2024

# Seasons
JohnVerano2024
SmithOtoño2025

# Common words
```
Password2024!
Welcome2025@
```

**Example with French:**
```bash
userforge -i nombres.txt --passwords --language FR --country FR
```

**Generated patterns:**
```
# Months in French
JohnJanvier2024
SmithFévrier2025

# Seasons
JohnÉté2024
SmithHiver2025

# Common words
MotDePasse2024!
Bienvenue2025@
```

---

## 5.4 Leet Speak

### 5.4.1 `--leet`

**Description:** Global leet speak level applied to usernames and passwords.

**Values:** 0-3 (Default: 0)

**Levels:**

#### Level 0 - Disabled
No transformation.

#### Level 1 - Basic
**Substitutions:**
- `e → 3`
- `a → 4`
- `o → 0`
- `i → 1`

**Example:**
```bash
userforge -i nombres.txt --passwords --leet 1
```

**Output:**
```
# Original
john.smith
Welcome2024

# Leet Level 1
j0hn.sm1th
W3lc0m32024
```

---

#### Level 2 - Medium
**Additional substitutions:**
- `s → 5`
- `t → 7`
- `l → 1`

**Example:**
```bash
userforge -i nombres.txt --passwords --leet 2
```

**Output:**
```
# Original
john.smith
TechCorp2024

# Leet Level 2
j0hn.5m17h
73chC0rp2024
```

---

#### Level 3 - Advanced
**Additional substitutions:**
- `s → $`
- `a → @`
- `i → !`

**Example:**
```bash
userforge -i nombres.txt --passwords --leet 3
```

**Output:**

```
# Original
john.smith
Password2024

# Leet Level 3
j0hn.$m!7h
P@$$w0rd2024
```

---

### 5.4.2 `--leet-user`

**Description:** Leet speak level applied ONLY to usernames.

**Usage:** When you only want to transform usernames.

**Example:**
```bash
userforge -i nombres.txt --passwords --leet-user 2
```

**Output:**
```
# Usernames with leet
j0hn.5m17h
m@r14.g4rc14

# Passwords without leet
Welcome2024
TechCorp2024
```

---

### 5.4.3 `--leet-password`

**Description:** Leet speak level applied ONLY to passwords.

**Usage:** When you only want to transform passwords (more common).

**Example:**
```bash
userforge -i nombres.txt --passwords --leet-password 3
```

**Output:**
```
# Usernames without leet
john.smith
maria.garcia

# Passwords with leet
W3lc0m3@2024
T3chC0rp$2024
P@$$w0rd!
```

---

## 5.5 Prefixes and Suffixes (Dual Mode)

### 5.5.1 `--user-prefix`

**Description:** Adds a prefix to all generated usernames.

**Dual Mode:** Generates BOTH versions (with and without prefix).

**Example:**
```bash
userforge -i nombres.txt --user-prefix "corp_"
```

**Output:**
```
# Original version
john.smith
jsmith
j.smith

# Version with prefix
corp_john.smith
corp_jsmith
corp_j.smith
```

**Practical use:**
- Corporate naming conventions
- Department prefixes: `it_`, `admin_`, `dev_`
- Location prefixes: `us_`, `eu_`, `asia_`

---

### 5.5.2 `--user-suffix`

**Description:** Adds a suffix to all generated usernames.

**Dual Mode:** Generates BOTH versions (with and without suffix).


**Example:**
```bash
userforge -i nombres.txt --user-suffix ".adm"
```

**Output:**
```
# Original version
john.smith
jsmith

# Version with suffix
john.smith.adm
jsmith.adm
```

**Practical use:**
- Administrative accounts: `.adm`, `.admin`, `_admin`
- Service accounts: `.svc`, `.service`
- Test accounts: `.test`, `.dev`

---

### 5.5.3 `--pass-prefix`

**Description:** Adds a prefix to all generated passwords.

**Dual Mode:** Generates BOTH versions (with and without prefix).

**Example:**
```bash
userforge -i nombres.txt --passwords --pass-prefix "P@"
```

**Output:**
```
# Original version
Welcome2024
TechCorp2024

# Version with prefix
P@Welcome2024
P@TechCorp2024
```

**Practical use:**
- Comply with policies requiring a symbol at the start
- Specific corporate patterns

---

### 5.5.4 `--pass-suffix`

**Description:** Adds a suffix to all generated passwords.

**Dual Mode:** Generates BOTH versions (with and without suffix).

**Example:**
```bash
userforge -i nombres.txt --passwords --pass-suffix "!"
```

**Output:**
```
# Original version
Welcome2024
TechCorp2024

# Version with suffix
Welcome2024!
TechCorp2024!
```

**Practical use:**
- Comply with policies requiring a symbol at the end
- Very common pattern in corporate passwords

---

## 5.6 Password Enhancements

### 5.6.1 `--years`

**Description:** Year range for temporal patterns.

**Format:** `YYYY-YYYY` (range) or `YYYY,YYYY,YYYY` (list)

**Default:** Current year

**Example with range:**
```bash
userforge -i nombres.txt --passwords --years 2020-2025
```

**Generated patterns:**
```
Welcome2020
Welcome2021
Welcome2022
Welcome2023
```
Welcome2024
Welcome2025
TechCorp2020!
TechCorp2021!
...
```

**Example with list:**
```bash
userforge -i names.txt --passwords --years 2020,2023,2024,2025
```

**Generated patterns:**
```
Welcome2020
Welcome2023
Welcome2024
Welcome2025
```

**Practical use:**
- Annual password rotation
- Audits of old passwords
- Targeted attacks on specific years

---

### 5.6.2 `--common-words`

**Description:** Additional common words for password patterns.

**Format:** Words separated by commas

**Example:**
```bash
userforge -i names.txt --passwords --common-words "Project,Secret,Confidential"
```

**Generated patterns:**
```
Project2024!
Secret2025@
Confidential2024
JohnProject2024
SmithSecret!
ProjectTechCorp2024
```

**Practical use:**
- Industry-specific words
- Internal project names
- Corporate jargon

---

### 5.6.3 `--keyboard-patterns`

**Description:** Includes patterns based on keyboard layout.

**Generated patterns:**
```
qwerty
asdfgh
zxcvbn
qwerty123
asdfgh2024
qwertyTechCorp
```

**Example:**
```bash
userforge -i names.txt --passwords --keyboard-patterns
```

**Practical use:**
- Common weak passwords
- Users who use keyboard patterns for convenience

---

### 5.6.4 `--numeric-sequences`

**Description:** Includes common numeric sequences.

**Generated patterns:**
```
123456
654321
111111
123456789
987654321
12345678
```

**Example:**
```bash
userforge -i names.txt --passwords --numeric-sequences
```

**Combinations with other patterns:**

```
Welcome123456
TechCorp654321
Password123456789
```

---

### 5.6.5 `--rotation-count`

**Description:** Number of incremental passwords to generate.

**Default:** 12 (for quarterly rotation of 90 days)

**Pattern:** The MOST SUCCESSFUL pattern in corporate environments.

**Explanation:** When employees are forced to change their password every 90 days, most simply increment a number:
- Month 1: `Welcome1!`
- Month 4: `Welcome2!`
- Month 7: `Welcome3!`
- etc.

**Example with 12 rotations (3 years):**
```bash
userforge -i nombres.txt --passwords --rotation-count 12
```

**Generated patterns:**
```
Welcome1!
Welcome2!
Welcome3!
...
Welcome12!

Password1@
Password2@
...
Password12@

TechCorp1!
TechCorp2!
...
TechCorp12!
```

**Example with 24 rotations (6 years):**
```bash
userforge -i nombres.txt --passwords --rotation-count 24
```

**Practical use:**
- Attacks against 90-day rotation policies
- Audits of old passwords
- Detection of incremental patterns

---

### 5.6.6 `--quarters`

**Description:** Includes fiscal quarter patterns.

**Generated patterns:**
```
Q1-2024
Q2-2024
Q3-2024
Q4-2024
FY2024
FY2025
Fiscal2024
Q1-2024!
Q1FY2024
```

**Example:**
```bash
userforge -i nombres.txt --passwords --quarters --years 2023-2025
```

**Generated patterns:**
```
Q1-2023
Q2-2023
Q3-2023
Q4-2023
Q1-2024
Q2-2024
Q3-2024
Q4-2024
Q1-2025
Q2-2025
FY2023
FY2024
FY2025
TechCorpQ1-2024
Q1-2024TechCorp!
```

**Practical use:**
- Financial companies  
- Accounting firms  
- Publicly traded companies  
- Finance departments  

---

### 5.6.7 `--departments`

**Description:** Includes patterns based on corporate departments.

**Included departments:**  
- IT, HR, Sales, Marketing, Finance, Legal  
- Accounting, Admin, Support, Engineering, Operations  
- Management, Executive, Security, Audit  

**Generated patterns:**  
```
IT2024!
HR2025@
Sales2024
Marketing2025!
Finance2024@
ITDept2024
HRTeam2025
SalesTeam!
ITTechCorp2024
HRTechCorp2025
```

**Example:**  
```bash
userforge -i nombres.txt --passwords --departments --company-name "TechCorp"
```

**Generated patterns:**  
```
IT2024!
ITTechCorp2024
TechCorpIT2024
ITDept2024!
HR2024@
HRTechCorp2025
TechCorpHR2025
HRTeam2025!
```

**Practical use:**  
- Shared department passwords  
- Departmental service accounts  
- Shared mailboxes  

---

## 5.7 Interactive Mode

### `--interactive` / `-I`

**Description:** Enables guided interactive mode.

**Features:**  
- Step-by-step questions  
- Suggested default values  
- Input validation  
- Contextual explanations  

**Session example:**  
```bash
$ userforge -i nombres.txt -I

=== UserForge Interactive Mode ===

[1/15] Generate passwords? (y/n) [n]: y
[2/15] Generate emails? (y/n) [n]: y
[3/15] Email domains (comma-separated): techcorp.com,corp.local

[4/15] Use separate depth for users/passwords? (y/n) [n]: y
[5/15] User depth (1-5) [3]: 2
[6/15] Password depth (1-5) [3]: 5

[7/15] Company name []: TechCorp
[8/15] Country code (US/UK/CA/AU/DE/FR/ES/IT/PT/MX) [US]: US
[9/15] Language (EN/ES/FR/DE/IT/PT) [EN]: EN

[10/15] Enable leet speak? (y/n) [n]: y
[11/15] Leet level for users (0-3) [0]: 0
[12/15] Leet level for passwords (0-3) [0]: 2

[13/15] Enable quarters patterns? (y/n) [n]: y
[14/15] Enable departments patterns? (y/n) [n]: y
[15/15] Output format (txt/json/xml/all) [txt]: all

=== Configuration Summary ===
✓ Input: nombres.txt
✓ Passwords: Yes
✓ Emails: techcorp.com, corp.local
✓ User Depth: 2
✓ Pass Depth: 5
✓ Company: TechCorp
✓ Quarters: Yes

✓ Departments: Yes  
✓ Leet (passwords): Level 2  
✓ Format: all  

Proceed? (y/n) [y]: y

[INFO] Processing...
```

---

## 5.8 Tips

### For User Enumeration
1. Start with `-d 2` for speed
2. Use `--emails` if you know the domains
3. Increase to `-d 3` or `-d 4` if unsuccessful
4. Use `--format all` for integration with other tools

### For Password Spraying
1. Use `-d 3` as a starting point
2. **ALWAYS** include `--quarters` and `--departments`
3. Use `--rotation-count 12` at minimum
4. Specify `--company-name` if known
5. Adjust `--min-pass-length` according to detected policy
6. Use `--leet-password 1` or `2` for broader coverage

### For Targeted Attacks
1. Use `-ud 2 -pd 5` if you know the username
2. Research the company (OSINT) for `--common-words`
3. Use `--years` with a wide range (e.g., 2018-2025)
4. Combine `--quarters`, `--departments`, and `--rotation-count 24`

### For Audits
1. Use `-d 5` for maximum coverage
2. Include ALL enhancement flags
3. Use `--format all` for later analysis
4. Document generation time

### Resource Optimization
1. Use length filters to reduce size
2. Start with low depth and increase gradually
3. Use independent `-ud` and `-pd` for fine control
4. Monitor output size with `-v`

---


## 6. Workflows and Practical Examples

-   **Initial Enumeration:** Start with low depth to quickly find common usernames.
    -   `userforge -i nombres.txt -d 2 -o usuarios_iniciales`

-   **Standard Password Spray:** A balanced attack for a typical corporate target.
    -   `userforge -i nombres.txt -d 3 --passwords --company-name "MegaCorp" --quarters -o listas_spray`

-   **High Security Target:** For environments with strict password policies.
    -   `userforge -i nombres.txt -d 4 --passwords --min-pass-length 12 --leet-password 2 -o listas_seguras`

-   **Full Attack (Maximum Coverage):** When you need to try everything.
    -   `userforge -i nombres.txt -d 5 --passwords --format all --company-name "GlobalCorp" --departments --quarters --rotation-count 24 --leet-password 1 -o ataque_total`


### Example 1: Basic Enumeration
```bash
userforge -i nombres.txt -d 2 -o usuarios_basicos
```

### Example 2: Standard Password Spray
```bash
userforge -i nombres.txt -d 3 --passwords \
  --company-name "MegaCorp" \
  --quarters \
  --rotation-count 12 \
  -o spray_megacorp
```

### Example 3: Targeted Attack with Leet Speak
```bash
userforge -i nombres.txt -d 4 --passwords \
  --company-name "TechCorp" \
  --leet-password 2 \
  --min-pass-length 12 \
  --years 2022-2025 \
  -o ataque_techcorp
```

### Example 4: Exhaustive Attack
```bash
userforge -i nombres.txt -ud 5 -pd 5 --passwords \
  --company-name "GlobalCorp" \
  --departments \
  --quarters \
  --rotation-count 24 \
  --keyboard-patterns \
  --numeric-sequences \
  --common-words "Project,Secret,Internal" \
  --years 2020-2025 \
  --format all \
  -v \
```
  -o total_attack
```

### Example 5: Spanish Localization
```bash
userforge -i names.txt -d 3 --passwords \
  --company-name "Empresa SA" \
  --language ES \
  --country ES \
  --quarters \
  --departments \
  -o attack_spain
```

### Example 6: Emails + Usernames
```bash
userforge -i names.txt -d 3 \
  --emails company.com,corp.local,company.net \
  --format all \
  -o email_enumeration
```

### Example 7: Prefixes/Suffixes
```bash
userforge -i names.txt -d 3 --passwords \
  --user-prefix "corp_" \
  --user-suffix ".adm" \
  --pass-prefix "P@" \
  --pass-suffix "!" \
  --company-name "TechCorp" \
  -o dual_mode
```



### Example 8: Attack on Financial Infrastructure
**Scenario:** Pentesting at a bank or financial institution with strict password policies.

**Features:**
- Intensive use of fiscal quarter patterns
- High complexity
- Recent years (quarterly rotation policies)
- Financial departments

```bash
userforge -i cfo_names.txt -pd 5 --passwords \
  --company-name "BankCorp" \
  --quarters \
  --departments \
  --years 2023-2025 \
  --complexity high \
  --min-pass-length 12 \
  --rotation-count 16 \
  --format json \
  -v \
  -o financial_attack
```

**Generated patterns:**
- `BankCorpQ1-2024!`
- `FinanceQ2-2024@`
- `FY2024BankCorp#`
- `Q3-2024Finance!`

**Expected success rate:** ~55% in financial environments

---

### Example 9: Enterprise Active Directory Enumeration
**Scenario:** Discovery of user accounts in a large enterprise AD.

**Features:**
- High username depth
- Email generation with multiple domains
- Large company size
- No passwords (enumeration only)

```bash
userforge -i employees_500.txt -ud 5 \
  --emails company.local,corp.company.com,company.net \
  --company-size enterprise \
  --format txt \
  -o ad_enumeration
```

**Expected result:**
- ~8,000 username variants per person
- Emails in 3 domains
- Total: ~12,000,000 combinations for 500 employees

**Use:** Feed tools like `kerbrute` or `ldapsearch`

---

### Example 10: Password Spraying with Corporate Patterns
**Scenario:** Password spraying attack against AD with a reduced list of known users.

**Features:**
- Known users (admin, service accounts)
- High password depth

- Critical corporate patterns
- Smart mode

```bash
userforge -i admin_accounts.txt -ud 1 -pd 4 --passwords \
  --departments \
  --quarters \
  --rotation-count 24 \
  --target-company "TechCorp" \
  --smart \
  --optimize \
  --min-pass-length 8 \
  -o spray_corporativo
```

**Generated patterns:**
- `IT2024!`, `IT2024@`, `IT2024#`
- `Q1-2024!`, `Q2-2024!`
- `TechCorp1!`, `TechCorp2!`, ..., `TechCorp24!`

**Advantage:** Reduces lockouts with highly effective patterns

---

### Example 11: Targeted Attack with OSINT Intelligence
**Scenario:** Attack on a specific executive using information from LinkedIn/social networks.

**Features:**
- Single target (CEO, CTO)
- Custom roles
- OSINT keywords
- Maximum depth

```bash
userforge -i ceo.txt -pd 5 --passwords \
  --roles "CEO,President,Director,Founder" \
  --common-words "Vision,Strategy,Growth,Innovation,Leadership" \
  --company-name "StartupXYZ" \
  --target-company "Google" \
  --years 2024-2025 \
  --leet-password 2 \
  --complexity high \
  -o ataque_ceo
```

**Generated patterns:**
- `JohnCEO2024!`
- `VisionStartupXYZ@`
- `L3@d3rship2024!`
- `GoogleFounder2025#`

**Useful OSINT information:**
- Projects mentioned on LinkedIn
- Keywords from tweets
- Personal interests

---

### Example 12: Massive Generation for Hashcat
**Scenario:** Create a massive wordlist for offline cracking with Hashcat/John.

**Features:**
- Maximum depth
- All patterns enabled
- Optimization disabled (we want volume)
- Plain text format

```bash
userforge -i all_employees_1000.txt -ud 3 -pd 5 --passwords \
  --keyboard-patterns \
  --numeric-sequences \
  --quarters \
  --departments \
  --years 2020-2025 \
  --rotation-count 36 \
  --leet-password 3 \
  --common-words "Company,Project,Secret,Internal,Confidential" \
  --format txt \
  -v \
  -o wordlist_hashcat
```

**Expected result:**
- ~15,000 passwords per person
- Total: ~15,000,000 passwords for 1,000 employees
- Size: ~200-300 MB

**Usage with Hashcat:**
```bash
hashcat -m 1000 -a 0 hashes.txt wordlist_hashcat/combined/all_passwords.txt
```

---

### Example 13: Password Policy Audit
**Scenario:** Verify if the organization's passwords comply with the policy.

**Features:**
- Statistical analysis enabled
- Length filters according to policy
- Defined complexity  
- Report generation

```bash
userforge -i sample_users.txt -pd 3 --passwords \
  --analyze \
  --min-pass-length 12 \
  --max-pass-length 20 \
  --complexity high \
  --company-name "SecureCorp" \
  --format all \
  -o audit_policies
```

**Generated analysis:**  
- Length distribution  
- Average complexity  
- Most common patterns  
- Recommendations

---

### Example 14: Multi-Language Attack  
**Scenario:** Multinational company with employees from different countries.

**Features:**  
- Multiple runs with different languages  
- Localized patterns  
- Combination of results

```bash
# Spain
userforge -i nombres_es.txt -d 3 --passwords \
  --language ES --country ES \
  --company-name "GlobalCorp" \
  -o attack_es

# France
userforge -i nombres_fr.txt -d 3 --passwords \
  --language FR --country FR \
  --company-name "GlobalCorp" \
  -o attack_fr

# Germany
userforge -i nombres_de.txt -d 3 --passwords \
  --language DE --country DE \
  --company-name "GlobalCorp" \
  -o attack_de

# Combine results
cat attack_*/combined/all_passwords.txt | sort -u > multinational_wordlist.txt
```

**Patterns by language:**  
- ES: `Primavera2024`, `Verano2024`  
- FR: `Printemps2024`, `Été2024`  
- DE: `Frühling2024`, `Sommer2024`

---

### Example 15: Interactive Mode for Beginners  
**Scenario:** New user who is not familiar with all the arguments.

```bash
userforge -i nombres.txt -I
```

**Interactive flow:**  
```
UserForge v1.0.0 - Interactive Mode

1. Generate passwords? (y/n) [n]: y
2. Use separate depth for users/passwords? (y/n) [n]: y
3. User depth (1-5) [3]: 2
4. Password depth (1-5) [3]: 5
5. Company name [None]: TechCorp
6. Use leet speak? (y/n) [n]: y
7. Leet level for passwords (0-3) [0]: 2
8. Add prefixes/suffixes? (y/n) [n]: n
9. Include quarters? (y/n) [n]: y
10. Include departments? (y/n) [n]: y
11. Output format (txt/json/xml/all) [txt]: all
12. Verbose mode? (y/n) [n]: y

Generating wordlists...
✓ Generated 264 usernames
✓ Generated 7,375 passwords
✓ Output saved to: UserForge_Output_20241027_123456
```

**Advantage:** Step-by-step guide with explanations

---

## Summary Table of Use Cases

| Use Case                | Depth      | Key Arguments                | Expected Result     |
|-------------------------|------------|------------------------------|---------------------|
| **Basic Enumeration**   | `-d 2`     | None                         | ~500 usernames      |
| **Standard Password Spray** | `-d 3` | `--quarters`, `--company-name` | ~2,000 passwords    |
| **Financial Infrastructure** | `-pd 5` | `--quarters`, `--complexity high` | ~10,000 passwords |
| **AD Enumeration** | `-ud 5` | `--emails`, `--company-size` | ~8,000 usernames |
| **OSINT Attack** | `-pd 5` | `--roles`, `--common-words` | ~12,000 passwords |
| **Massive Hashcat** | `-pd 5` | All patterns | ~15,000 passwords/person |
| **Audit** | `-pd 3` | `--analyze`, `--complexity` | Statistical report |
| **Multi-Language** | `-d 3` | `--language`, `--country` | Localized patterns |

---


## 7. Output Formats

Use the `--format` argument to specify the desired output.

-   `--format txt`: Default. Creates plain text files (`.txt`).
-   `--format json`: Creates structured JSON files (`.json`), useful for integration with other tools.
-   `--format xml`: Creates XML files (`.xml`).
-   `--format all`: Generates output in all three formats simultaneously.

## 8. License

UserForge is licensed under the GNU General Public License v3.0. You are free to use, modify, and distribute it under the terms of the license. See the [LICENSE](../LICENSE) file for the full text.