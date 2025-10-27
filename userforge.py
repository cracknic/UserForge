#!/usr/bin/env python3
"""
██╗   ██╗███████╗███████╗██████╗ ███████╗ ██████╗ ██████╗  ██████╗ ███████╗
██║   ██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
██║   ██║███████╗█████╗  ██████╔╝█████╗  ██║   ██║██████╔╝██║  ███╗█████╗  
██║   ██║╚════██║██╔══╝  ██╔══██╗██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
╚██████╔╝███████║███████╗██║  ██║██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝

UserForge v1.0 - Corporate Username & Password Generator
Author: Cracknic
License: GNU GPL v3.0
⚠ FOR AUTHORIZED PENETRATION TESTING ONLY ⚠
"""

import argparse
import os
import sys
import json
import re
import logging
import time
from datetime import datetime
from pathlib import Path
from typing import List, Set, Dict, Tuple, Optional
from collections import Counter
from functools import lru_cache

class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


# ============================================================ #
# LOCALIZATION DATA                                            #
# ============================================================ #

LOCALIZATION = {
    'ES': {
        'seasons': ['Primavera', 'Verano', 'Otono', 'Invierno'],
        'months': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                   'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        'days': ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'],
        'common_words': ['Bienvenido', 'Hola', 'Adios', 'Gracias', 'Porfavor']
    },
    'EN': {
        'seasons': ['Spring', 'Summer', 'Autumn', 'Fall', 'Winter'],
        'months': ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December'],
        'days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'common_words': ['Welcome', 'Hello', 'Goodbye', 'Thanks', 'Please']
    },
    'FR': {
        'seasons': ['Printemps', 'Ete', 'Automne', 'Hiver'],
        'months': ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin',
                   'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre'],
        'days': ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'],
        'common_words': ['Bienvenue', 'Bonjour', 'Aurevoir', 'Merci', 'Silvouplait']
    },
    'DE': {
        'seasons': ['Fruhling', 'Sommer', 'Herbst', 'Winter'],
        'months': ['Januar', 'Februar', 'Marz', 'April', 'Mai', 'Juni',
                   'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'],
        'days': ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag'],
        'common_words': ['Willkommen', 'Hallo', 'AufWiedersehen', 'Danke', 'Bitte']
    },
    'IT': {
        'seasons': ['Primavera', 'Estate', 'Autunno', 'Inverno'],
        'months': ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno',
                   'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre'],
        'days': ['Lunedi', 'Martedi', 'Mercoledi', 'Giovedi', 'Venerdi', 'Sabato', 'Domenica'],
        'common_words': ['Benvenuto', 'Ciao', 'Arrivederci', 'Grazie', 'Perfavore']
    },
    'PT': {
        'seasons': ['Primavera', 'Verao', 'Outono', 'Inverno'],
        'months': ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho',
                   'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        'days': ['Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo'],
        'common_words': ['Bemvindo', 'Ola', 'Adeus', 'Obrigado', 'Porfavor']
    }
}

COUNTRY_CODES = {
    'ES': ['es', 'cat', 'gal', 'eus'],
    'US': ['us', 'usa'],
    'GB': ['uk', 'gb'],
    'FR': ['fr'],
    'DE': ['de'],
    'IT': ['it'],
    'PT': ['pt', 'br'],
    'PL': ['pl'],
    'NL': ['nl'],
    'BE': ['be']
}

# Role patterns
ROLES = {
    'ceo': ['ceo', 'chief', 'executive'],
    'cto': ['cto', 'tech', 'technology'],
    'cfo': ['cfo', 'finance', 'financial'],
    'admin': ['admin', 'administrator', 'sysadmin', 'root'],
    'manager': ['mgr', 'manager', 'lead', 'supervisor'],
    'developer': ['dev', 'developer', 'engineer', 'programmer'],
    'analyst': ['analyst', 'data', 'business'],
    'support': ['support', 'helpdesk', 'service'],
    'sales': ['sales', 'account', 'rep'],
    'hr': ['hr', 'human', 'resources', 'people'],
    'marketing': ['marketing', 'mkt', 'promo'],
    'intern': ['intern', 'trainee', 'junior']
}

# Targeted company data
COMPANY_TARGETS = {
    'microsoft': {
        'products': ['windows', 'office', 'azure', 'teams', 'outlook'],
        'locations': ['redmond', 'seattle'],
        'common': ['msft', 'ms']
    },
    'google': {
        'products': ['gmail', 'drive', 'chrome', 'android', 'cloud'],
        'locations': ['mountain', 'view', 'palo', 'alto'],
        'common': ['goog', 'alphabet']
    },
    'amazon': {
        'products': ['aws', 'prime', 'alexa', 'kindle'],
        'locations': ['seattle'],
        'common': ['amzn']
    },
    'apple': {
        'products': ['iphone', 'ipad', 'mac', 'ios', 'safari'],
        'locations': ['cupertino'],
        'common': ['aapl']
    }
}

# Complexity rules
COMPLEXITY_RULES = {
    'low': {
        'min_length': 4,
        'max_length': 20,
        'require_upper': False,
        'require_lower': False,
        'require_digit': False,
        'require_special': False
    },
    'medium': {
        'min_length': 8,
        'max_length': 30,
        'require_upper': False,
        'require_lower': True,
        'require_digit': True,
        'require_special': False
    },
    'high': {
        'min_length': 12,
        'max_length': 40,
        'require_upper': True,
        'require_lower': True,
        'require_digit': True,
        'require_special': True
    }
}


# ============================================================ #
# UTILITY FUNCTIONS                                            #
# ============================================================ #

def print_banner():
    banner = f"""{Colors.CYAN}
██╗   ██╗███████╗███████╗██████╗ ███████╗ ██████╗ ██████╗  ██████╗ ███████╗
██║   ██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
██║   ██║███████╗█████╗  ██████╔╝█████╗  ██║   ██║██████╔╝██║  ███╗█████╗  
██║   ██║╚════██║██╔══╝  ██╔══██╗██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
╚██████╔╝███████║███████╗██║  ██║██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
{Colors.RESET}
{Colors.BOLD}Version:{Colors.RESET} 1.0 | {Colors.BOLD}Author:{Colors.RESET} Cracknic
{Colors.YELLOW}⚠  FOR AUTHORIZED PENETRATION TESTING ONLY ⚠{Colors.RESET}
"""
    print(banner)


# ============================================================ #
# LOGGING                                                      #      
# ============================================================ #

class ColoredFormatter(logging.Formatter):
    
    COLORS = {
        'DEBUG': Colors.CYAN,
        'INFO': Colors.BLUE,
        'WARNING': Colors.YELLOW,
        'ERROR': Colors.RED,
        'CRITICAL': Colors.RED + Colors.BOLD,
        'SUCCESS': Colors.GREEN
    }
    
    def format(self, record):
        levelname = record.levelname
        if levelname in self.COLORS:
            record.levelname = f"{self.COLORS[levelname]}{levelname}{Colors.RESET}"
        return super().format(record)


def setup_logging(verbose: bool = False, log_file: str = None):
    level = logging.DEBUG if verbose else logging.INFO
    
    logger = logging.getLogger('UserForge')
    logger.setLevel(level)
    
    logger.handlers.clear()
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_formatter = ColoredFormatter('[%(levelname)s] %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    # File handler (if specified)
    if log_file:
        log_dir = os.path.dirname(log_file)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    
    return logger


# Add SUCCESS to logging
logging.SUCCESS = 25
logging.addLevelName(logging.SUCCESS, 'SUCCESS')

def success(self, message, *args, **kwargs):
    if self.isEnabledFor(logging.SUCCESS):
        self._log(logging.SUCCESS, message, args, **kwargs)

logging.Logger.success = success


def log(message: str, level: str = "INFO"):

    logger = logging.getLogger('UserForge')
    
    if level == "SUCCESS":
        logger.success(message)
    elif level == "WARNING":
        logger.warning(message)
    elif level == "ERROR":
        logger.error(message)
    elif level == "DEBUG":
        logger.debug(message)
    else:
        logger.info(message)


def show_progress(current: int, total: int, prefix: str = 'Progress', bar_length: int = 40):
    """Progress bar"""
    if total == 0:
        return
    
    filled_length = int(bar_length * current / total)
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    percent = 100 * current / total
    
    # Use carriage return to overwrite the same line
    print(f'\r{Colors.CYAN}{prefix}:{Colors.RESET} |{Colors.GREEN}{bar}{Colors.RESET}| {percent:.1f}% ({current}/{total})', end='')
    
    # Print newline when complete
    if current == total:
        print()


def validate_name(name: str) -> bool:
    """Validate name format"""
    if not name or len(name.strip()) == 0:
        return False
    
    if not re.match(r"^[a-zA-ZÀ-ÿ\s\-']+$", name):
        log(f"Invalid name format (contains special characters): {name}", "WARNING")
        return False
    
    # Check length
    if len(name) > 100:
        log(f"Name too long (>100 chars): {name[:50]}...", "WARNING")
        return False
    
    return True


def load_input_names(filepath: str) -> List[str]:
    """Load and validate names from input"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            names = [line.strip() for line in f if line.strip()]
        
        if not names:
            log(f"No names found in file: {filepath}", "ERROR")
            sys.exit(1)
        
        valid_names = [n for n in names if validate_name(n)]
        
        if len(valid_names) < len(names):
            skipped = len(names) - len(valid_names)
            log(f"Skipped {skipped} invalid name(s)", "WARNING")
        
        if not valid_names:
            log("No valid names to process", "ERROR")
            sys.exit(1)
        
        return valid_names
    
    except FileNotFoundError:
        log(f"Input file not found: {filepath}", "ERROR")
        sys.exit(1)
    except UnicodeDecodeError:
        log(f"Invalid file encoding. Please use UTF-8.", "ERROR")
        sys.exit(1)
    except PermissionError:
        log(f"Permission denied: {filepath}", "ERROR")
        sys.exit(1)
    except Exception as e:
        log(f"Error reading file: {e}", "ERROR")
        sys.exit(1)


def interactive_mode() -> Dict:
    """Interactive mode"""
    print(f"\n{Colors.CYAN}{'='*60}")
    print("USERFORGE INTERACTIVE MODE")
    print(f"{'='*60}{Colors.RESET}\n")
    
    config = {}
    
    # Input file
    config['input'] = input(f"{Colors.BOLD}Input file with names:{Colors.RESET} ").strip()
    
    # Depth levels
    print(f"\n{Colors.BOLD}Depth levels:{Colors.RESET}")
    print("  1 = Basic (~150 patterns)")
    print("  2 = Standard (~500 patterns)")
    print("  3 = Advanced (~1000 patterns) [RECOMMENDED]")
    print("  4 = Extensive (~2000 patterns)")
    print("  5 = Maximum (~8000+ patterns)")
    
    use_separate_depth = input(f"\n{Colors.BOLD}Use separate depth for users/passwords? (y/n) [n]:{Colors.RESET} ").strip().lower() or "n"
    
    if use_separate_depth == 'y':
        user_depth = input(f"{Colors.BOLD}User depth (1-5) [3]:{Colors.RESET} ").strip() or "3"
        config['user_depth'] = int(user_depth)
        pass_depth = input(f"{Colors.BOLD}Password depth (1-5) [3]:{Colors.RESET} ").strip() or "3"
        config['pass_depth'] = int(pass_depth)
    else:
        depth = input(f"{Colors.BOLD}Select depth (1-5) [3]:{Colors.RESET} ").strip() or "3"
        config['depth'] = int(depth)
    
    # Passwords
    gen_pass = input(f"\n{Colors.BOLD}Generate passwords? (y/n) [y]:{Colors.RESET} ").strip().lower() or "y"
    config['passwords'] = gen_pass == 'y'
    
    if config['passwords']:
        company = input(f"{Colors.BOLD}Company name (optional):{Colors.RESET} ").strip()
        if company:
            config['company_name'] = company
        
        # Years
        years = input(f"{Colors.BOLD}Years (e.g., 2024-2025 or 2024,2025) [empty]:{Colors.RESET} ").strip()
        if years:
            config['years'] = years
        
        # Quarters
        quarters = input(f"{Colors.BOLD}Add quarters (Q1, Q2, Q3, Q4)? (y/n) [n]:{Colors.RESET} ").strip().lower() or "n"
        if quarters == 'y':
            config['quarters'] = True
        
        # Departments
        departments = input(f"{Colors.BOLD}Add departments (IT, HR, Sales, etc.)? (y/n) [n]:{Colors.RESET} ").strip().lower() or "n"
        if departments == 'y':
            config['departments'] = True
    
    # Emails
    gen_email = input(f"\n{Colors.BOLD}Generate emails? (y/n) [n]:{Colors.RESET} ").strip().lower() or "n"
    if gen_email == 'y':
        domains = input(f"{Colors.BOLD}Email domains (comma-separated):{Colors.RESET} ").strip()
        if domains:
            config['emails'] = domains
    
    # Language
    print(f"\n{Colors.BOLD}Language for seasons/months:{Colors.RESET}")
    print("  ES=Spanish, EN=English, FR=French, DE=German, IT=Italian, PT=Portuguese")
    lang = input(f"{Colors.BOLD}Select language [EN]:{Colors.RESET} ").strip().upper() or "EN"
    config['language'] = lang
    
    # Country
    print(f"\n{Colors.BOLD}Country code for location patterns:{Colors.RESET}")
    print("  ES, US, GB, FR, DE, IT, PT, PL, NL, BE")
    country = input(f"{Colors.BOLD}Select country [US]:{Colors.RESET} ").strip().upper() or "US"
    config['country'] = country
    
    # Leet speak
    use_leet = input(f"\n{Colors.BOLD}Use leet speak? (y/n) [n]:{Colors.RESET} ").strip().lower() or "n"
    if use_leet == 'y':
        separate_leet = input(f"{Colors.BOLD}Separate leet levels for users/passwords? (y/n) [n]:{Colors.RESET} ").strip().lower() or "n"
        if separate_leet == 'y':
            leet_user = input(f"{Colors.BOLD}Leet speak level for USERS (0-3) [0]:{Colors.RESET} ").strip() or "0"
            config['leet_user'] = int(leet_user)
            leet_pass = input(f"{Colors.BOLD}Leet speak level for PASSWORDS (0-3) [0]:{Colors.RESET} ").strip() or "0"
            config['leet_password'] = int(leet_pass)
        else:
            leet = input(f"{Colors.BOLD}Leet speak level (0-3) [0]:{Colors.RESET} ").strip() or "0"
            config['leet'] = int(leet)
    
    # Prefix/Suffix
    add_prefix_suffix = input(f"\n{Colors.BOLD}Add prefixes/suffixes? (y/n) [n]:{Colors.RESET} ").strip().lower() or "n"
    if add_prefix_suffix == 'y':
        separate_prefix = input(f"{Colors.BOLD}Separate prefix/suffix for users/passwords? (y/n) [n]:{Colors.RESET} ").strip().lower() or "n"
        
        if separate_prefix == 'y':
            user_prefix = input(f"{Colors.BOLD}User prefix (optional):{Colors.RESET} ").strip()
            if user_prefix:
                config['user_prefix'] = user_prefix
            
            user_suffix = input(f"{Colors.BOLD}User suffix (optional):{Colors.RESET} ").strip()
            if user_suffix:
                config['user_suffix'] = user_suffix
            
            if config.get('passwords'):
                pass_prefix = input(f"{Colors.BOLD}Password prefix (optional):{Colors.RESET} ").strip()
                if pass_prefix:
                    config['pass_prefix'] = pass_prefix
                
                pass_suffix = input(f"{Colors.BOLD}Password suffix (optional):{Colors.RESET} ").strip()
                if pass_suffix:
                    config['pass_suffix'] = pass_suffix
        else:
            prefix = input(f"{Colors.BOLD}Prefix (optional):{Colors.RESET} ").strip()
            if prefix:
                config['prefix'] = prefix
            
            suffix = input(f"{Colors.BOLD}Suffix (optional):{Colors.RESET} ").strip()
            if suffix:
                config['suffix'] = suffix
    
    # Length filters
    add_filters = input(f"\n{Colors.BOLD}Add length filters? (y/n) [n]:{Colors.RESET} ").strip().lower() or "n"
    if add_filters == 'y':
        min_user = input(f"{Colors.BOLD}Min username length [3]:{Colors.RESET} ").strip() or "3"
        config['min_user_length'] = int(min_user)
        
        max_user = input(f"{Colors.BOLD}Max username length [50]:{Colors.RESET} ").strip() or "50"
        config['max_user_length'] = int(max_user)
        
        if config.get('passwords'):
            min_pass = input(f"{Colors.BOLD}Min password length [8]:{Colors.RESET} ").strip() or "8"
            config['min_pass_length'] = int(min_pass)
            
            max_pass = input(f"{Colors.BOLD}Max password length [50]:{Colors.RESET} ").strip() or "50"
            config['max_pass_length'] = int(max_pass)
    
    # Roles
    add_roles = input(f"\n{Colors.BOLD}Add role-based patterns? (y/n) [n]:{Colors.RESET} ").strip().lower() or "n"
    if add_roles == 'y':
        print(f"{Colors.BOLD}Available roles:{Colors.RESET} ceo, admin, manager, developer, analyst, support, sales, hr, marketing")
        roles = input(f"{Colors.BOLD}Select roles (comma-separated):{Colors.RESET} ").strip()
        if roles:
            config['roles'] = roles
    
    # Target company
    add_target = input(f"\n{Colors.BOLD}Add target company patterns? (y/n) [n]:{Colors.RESET} ").strip().lower() or "n"
    if add_target == 'y':
        print(f"{Colors.BOLD}Available targets:{Colors.RESET} microsoft, google, apple, amazon, facebook, oracle, cisco, ibm")
        target = input(f"{Colors.BOLD}Select target company:{Colors.RESET} ").strip().lower()
        if target:
            config['target_company'] = target
    
    # Format
    print(f"\n{Colors.BOLD}Output format:{Colors.RESET}")
    print("  txt  = Text files only")
    print("  json = JSON files only")
    print("  xml  = XML files only")
    print("  all  = All formats")
    fmt = input(f"{Colors.BOLD}Select format [txt]:{Colors.RESET} ").strip().lower() or "txt"
    config['format'] = fmt
    
    # Optimize
    optimize = input(f"\n{Colors.BOLD}Optimize wordlists (remove duplicates, sort)? (y/n) [y]:{Colors.RESET} ").strip().lower() or "y"
    config['optimize'] = optimize == 'y'
    
    # Smart mode
    smart = input(f"{Colors.BOLD}Enable smart mode (auto-adjust depth)? (y/n) [n]:{Colors.RESET} ").strip().lower() or "n"
    config['smart'] = smart == 'y'
    
    print(f"\n{Colors.GREEN}✓ Configuration complete!{Colors.RESET}\n")
    
    return config



class LeetSpeakConverter:
    """Convert text to leet speak with multiple levels"""
    
    LEET_MAP = {
        1: {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'},
        2: {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7', 'l': '1', 'g': '9', 'b': '8'},
        3: {'a': '@', 'e': '3', 'i': '!', 'o': '0', 's': '$', 't': '7', 'l': '1', 'g': '9', 'b': '8', 'z': '2'}
    }
    
    @staticmethod
    def apply_leet(text: str, level: int) -> Set[str]:
        """Leet speak transformations"""
        if level == 0 or level not in LeetSpeakConverter.LEET_MAP:
            return {text}
        
        result = {text}
        leet_map = LeetSpeakConverter.LEET_MAP[level]
        
        # Full leet
        leet_text = ''.join(leet_map.get(c.lower(), c) for c in text)
        if leet_text != text:
            result.add(leet_text)
        
        # Partial leet (first occurrence only)
        for char, replacement in leet_map.items():
            if char in text.lower():
                partial = text.lower().replace(char, replacement, 1)
                result.add(partial)
        
        return result


# ============================================================ #
# COMPLEXITY CHECKER                                           #
# ============================================================ #

class ComplexityChecker:
    """Check complexity requirements"""
    
    @staticmethod
    def meets_requirements(pattern: str, rules: Dict) -> bool:
        # Length check
        if len(pattern) < rules['min_length'] or len(pattern) > rules['max_length']:
            return False
        
        # Character requirements
        if rules['require_upper'] and not any(c.isupper() for c in pattern):
            return False
        
        if rules['require_lower'] and not any(c.islower() for c in pattern):
            return False
        
        if rules['require_digit'] and not any(c.isdigit() for c in pattern):
            return False
        
        if rules['require_special'] and not any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in pattern):
            return False
        
        return True


# ============================================================ #
# PATTERN GENERATOR (MAIN CLASS)                               #
# ============================================================ #

class PatternGenerator:
    """Generate patterns"""
    
    def __init__(self, depth: int = 3, user_depth: int = None, pass_depth: int = None, leet_level: int = 0, company_size: str = "medium",
                 min_user_length: int = 3, max_user_length: int = 50,
                 min_pass_length: int = 8, max_pass_length: int = 50,
                 country: str = 'US', language: str = 'EN',
                 leet_user: int = 0, leet_password: int = 0,
                 user_prefix: str = '', user_suffix: str = '',
                 pass_prefix: str = '', pass_suffix: str = '',
                 roles: List[str] = None, target_company: str = '',
                 complexity: str = 'low', smart_mode: bool = False,
                 years: List[int] = None, common_words: List[str] = None,
                 keyboard_patterns: bool = False, numeric_sequences: bool = False,
                 symbol_positions: str = None, seasons_only: bool = False,
                 rotation_count: int = 12, quarters: bool = False, departments: bool = False):
        """Initialize generator with parameters"""
        self.user_depth = min(max(user_depth if user_depth is not None else depth, 1), 5)
        self.pass_depth = min(max(pass_depth if pass_depth is not None else depth, 1), 5)
        self.depth = depth 
        self.leet_level = leet_level
        self.company_size = company_size
        self.min_user_length = min_user_length
        self.max_user_length = max_user_length
        self.min_pass_length = min_pass_length
        self.max_pass_length = max_pass_length
        self.country = country.upper()
        self.language = language.upper()
        self.leet_user = leet_user
        self.leet_password = leet_password
        self.user_prefix = user_prefix
        self.user_suffix = user_suffix
        self.pass_prefix = pass_prefix
        self.pass_suffix = pass_suffix
        self.roles = roles or []
        self.target_company = target_company.lower() if target_company else ''
        self.complexity = complexity
        self.smart_mode = smart_mode
        self.year = str(datetime.now().year)
        self.year_short = self.year[2:]
        self.years = years or [datetime.now().year]
        self.common_words = common_words or []
        self.keyboard_patterns = keyboard_patterns
        self.numeric_sequences = numeric_sequences
        self.symbol_positions = symbol_positions
        self.rotation_count = rotation_count
        self.quarters = quarters
        self.departments = departments
        self.seasons_only = seasons_only
        
        # Localization data
        self.loc_data = LOCALIZATION.get(self.language, LOCALIZATION['EN'])
        self.country_codes = COUNTRY_CODES.get(self.country, COUNTRY_CODES['US'])
        
        # Complexity rules
        self.complexity_rules = COMPLEXITY_RULES.get(self.complexity, COMPLEXITY_RULES['low'])
        
        # Common separators
        self.separators = ['.', '_', '-', '']
        
        # Department
        self.dept_prefixes = ['admin', 'svc', 'ext', 'temp', 'test', 'dev', 'prod', 'qa']
        self.dept_suffixes = ['admin', 'dev', 'prod', 'test', 'qa', 'staging', 'backup']
        
        # Location codes
        self.locations = ['ny', 'la', 'sf', 'chi', 'bos', 'dc', 'sea', 'aus', 'den', 'atl',
                         'mia', 'dal', 'hou', 'phx', 'por', 'sd', 'lv', 'nash', 'char', 'ind']
        
        # Country-specific locations
        self.locations.extend(self.country_codes)
        
        # Years
        self.years = [self.year, self.year_short, str(int(self.year)-1), str(int(self.year_short)-1)]
        
        # Smart mode
        if self.smart_mode:
            self._apply_smart_optimizations()
    
    def _apply_smart_optimizations(self):
        """Smart mode optimizations"""
        # Auto-adjust depth
        if self.roles or self.target_company:
            self.user_depth = min(self.user_depth + 1, 5)
            self.pass_depth = min(self.pass_depth + 1, 5)
            self.depth = min(self.depth + 1, 5)
        
        # Auto-enable leet
        if self.leet_user == 0 and self.leet_password == 0 and self.leet_level == 0:
            self.leet_level = 1
    
    @lru_cache(maxsize=128)
    def _get_localized_seasons(self, language: str) -> List[str]:
        """Localized season names with language args"""
        return LOCALIZATION.get(language, LOCALIZATION['EN']).get('seasons', [])
    
    @lru_cache(maxsize=128)
    def _get_localized_months(self, language: str) -> List[str]:
        """Localized month names with language args"""
        return LOCALIZATION.get(language, LOCALIZATION['EN']).get('months', [])
    
    @lru_cache(maxsize=128)
    def _get_localized_common_words(self, language: str) -> List[str]:
        """Get localized common words"""
        return LOCALIZATION.get(language, LOCALIZATION['EN']).get('common_words', [])
    
    def parse_name(self, fullname: str) -> Tuple[str, str, str]:
        """Parse full name into components"""
        parts = fullname.strip().split()
        if len(parts) == 0:
            return ("", "", "")
        elif len(parts) == 1:
            return (parts[0], "", parts[0])
        elif len(parts) == 2:
            return (parts[0], "", parts[1])
        else:
            return (parts[0], parts[1], parts[-1])
    
    def _apply_prefix_suffix(self, pattern: str, pattern_type: str = 'user') -> Set[str]:
        """Apply prefix and suffix"""
        result = {pattern}  # Always include original
        
        if pattern_type == 'user':
            modified = pattern
            if self.user_prefix:
                modified = self.user_prefix + modified
            if self.user_suffix:
                modified = modified + self.user_suffix
            if modified != pattern:  # Only add if actually modified
                result.add(modified)
        elif pattern_type == 'pass':
            modified = pattern
            if self.pass_prefix:
                modified = self.pass_prefix + modified
            if self.pass_suffix:
                modified = modified + self.pass_suffix
            if modified != pattern:  # Only add if actually modified
                result.add(modified)
        
        return result
    
    def _filter_by_length(self, patterns: Set[str], min_len: int, max_len: int) -> Set[str]:
        """Filter by length"""
        return {p for p in patterns if min_len <= len(p) <= max_len}
    
    def _filter_by_complexity(self, patterns: Set[str]) -> Set[str]:
        """Filter by complexity rules"""
        if self.complexity == 'low':
            return patterns
        
        return {p for p in patterns if ComplexityChecker.meets_requirements(p, self.complexity_rules)}
    
    def _apply_leet_to_usernames(self, patterns: Set[str]) -> Set[str]:
        """Leet speak to users"""
        if self.leet_user > 0:
            result = set()
            for pattern in patterns:
                result.add(pattern)
                leet_variations = LeetSpeakConverter.apply_leet(pattern, self.leet_user)
                result.update(leet_variations)
            return result
        return patterns
    
    def _apply_leet_to_passwords(self, patterns: Set[str]) -> Set[str]:
        """Leet speak to passwords"""
        if self.leet_password > 0:
            result = set()
            for pattern in patterns:
                result.add(pattern)
                leet_variations = LeetSpeakConverter.apply_leet(pattern, self.leet_password)
                result.update(leet_variations)
            return result
        return patterns

    # ============================================================ #
    # USERNAME GENERATION - HELPER FUNCTIONS                       #
    # ============================================================ #
    
    def _generate_username_basic_components(self, first: str, middle: str, last: str) -> Dict[str, str]:
        """Generate basic username components"""
        return {
            'f': first.lower(),
            'l': last.lower() if last else "",
            'm': middle.lower() if middle else "",
            'f_cap': first.capitalize(),
            'l_cap': last.capitalize() if last else ""
        }
    
    def _generate_usernames_level1(self, components: Dict[str, str]) -> Set[str]:
        """Level 1 username patterns (~150 patterns)"""
        patterns = set()
        f = components['f']
        l = components['l']
        f_cap = components['f_cap']
        l_cap = components['l_cap']
        
        # Full names
        patterns.add(f"{f}{l}")
        patterns.add(f"{f}.{l}")
        patterns.add(f"{f}_{l}")
        patterns.add(f"{f}-{l}")
        patterns.add(f"{l}{f}")
        patterns.add(f"{l}.{f}")
        patterns.add(f"{l}_{f}")
        patterns.add(f"{l}-{f}")
        
        # Initials
        if l:
            patterns.add(f"{f[0]}{l}")
            patterns.add(f"{f[0]}.{l}")
            patterns.add(f"{f[0]}_{l}")
            patterns.add(f"{f[0]}-{l}")
            patterns.add(f"{f}{l[0]}")
            patterns.add(f"{f}.{l[0]}")
            patterns.add(f"{f}_{l[0]}")
            patterns.add(f"{f}-{l[0]}")
            patterns.add(f"{f[0]}{l[0]}")
            patterns.add(f"{f[0]}.{l[0]}")
            patterns.add(f"{f[0]}_{l[0]}")
            patterns.add(f"{f[0]}-{l[0]}")
        
        # Capitalized variations
        patterns.add(f_cap)
        patterns.add(l_cap)
        patterns.add(f"{f_cap}{l_cap}")
        patterns.add(f"{f_cap}.{l_cap}")
        
        # Numbers
        for num in ['1', '01', '2', '02', '123', '2025', '25']:
            patterns.add(f"{f}{num}")
            patterns.add(f"{f}{l}{num}")
            if l:
                patterns.add(f"{l}{num}")
        
        return patterns
    
    def _generate_usernames_level2(self, components: Dict[str, str], level1_patterns: Set[str]) -> Set[str]:
        """Level 2 username patterns (~500 patterns)"""
        patterns = level1_patterns.copy()
        f = components['f']
        l = components['l']
        m = components['m']
        
        # Middle name patterns
        if m:
            patterns.add(f"{f}{m}{l}")
            patterns.add(f"{f}.{m}.{l}")
            patterns.add(f"{f}_{m}_{l}")
            patterns.add(f"{f[0]}{m[0]}{l[0]}")
            patterns.add(f"{f}{m[0]}{l}")
        
        # More number variations
        for num in ['00', '10', '20', '99', '21', '22', '23', '24', '2024']:
            patterns.add(f"{f}{num}")
            patterns.add(f"{f}{l}{num}")
            patterns.add(f"{f}.{l}{num}")
            patterns.add(f"{f}_{l}{num}")
        
        # Reversed patterns
        patterns.add(f[::-1])
        if l:
            patterns.add(l[::-1])
            patterns.add(f"{f[::-1]}{l[::-1]}")
        
        return patterns
    
    def _generate_usernames_level3(self, components: Dict[str, str], level2_patterns: Set[str]) -> Set[str]:
        """Level 3 username patterns (~1000 patterns)"""
        patterns = level2_patterns.copy()
        f = components['f']
        l = components['l']
        
        # Department-based patterns
        for dept in self.dept_prefixes:
            patterns.add(f"{dept}_{f}")
            patterns.add(f"{dept}.{f}")
            patterns.add(f"{dept}-{f}")
            if l:
                patterns.add(f"{dept}_{f}{l}")
                patterns.add(f"{dept}.{f}.{l}")
        
        for dept in self.dept_suffixes:
            patterns.add(f"{f}_{dept}")
            patterns.add(f"{f}.{dept}")
            if l:
                patterns.add(f"{f}{l}_{dept}")
                patterns.add(f"{f}.{l}.{dept}")
        
        # Year-based patterns
        for year in self.years:
            patterns.add(f"{f}{year}")
            patterns.add(f"{f}_{year}")
            patterns.add(f"{f}.{year}")
            if l:
                patterns.add(f"{f}{l}{year}")
                patterns.add(f"{f}.{l}.{year}")
        
        return patterns
    
    def _generate_usernames_level4(self, components: Dict[str, str], level3_patterns: Set[str]) -> Set[str]:
        """Level 4 username patterns (~2000 patterns)"""
        patterns = level3_patterns.copy()
        f = components['f']
        l = components['l']
        
        # Location-based patterns
        for loc in self.locations[:10]:
            patterns.add(f"{f}_{loc}")
            patterns.add(f"{f}.{loc}")
            patterns.add(f"{f}-{loc}")
            patterns.add(f"{loc}_{f}")
            patterns.add(f"{loc}.{f}")
            if l:
                patterns.add(f"{f}{l}_{loc}")
                patterns.add(f"{f}.{l}.{loc}")
        
        # Extended number patterns
        for i in range(0, 30):
            patterns.add(f"{f}{i:02d}")
            if l:
                patterns.add(f"{f}{l}{i:02d}")
        
        return patterns
    
    def _generate_usernames_level5(self, components: Dict[str, str], level4_patterns: Set[str]) -> Set[str]:
        """Level 5 username patterns (~8000+ patterns)"""
        patterns = level4_patterns.copy()
        f = components['f']
        l = components['l']
        
        # All locations
        for loc in self.locations:
            patterns.add(f"{f}_{loc}")
            patterns.add(f"{f}.{loc}")
            patterns.add(f"{f}-{loc}")
            patterns.add(f"{loc}_{f}")
            if l:
                patterns.add(f"{f}{l}_{loc}")
        
        # Extended numbers
        for i in range(0, 100):
            patterns.add(f"{f}{i}")
            if l:
                patterns.add(f"{f}{l}{i}")
        
        # All separator combinations
        for sep1 in self.separators:
            for sep2 in self.separators:
                if l:
                    patterns.add(f"{f}{sep1}{l}{sep2}{self.year_short}")
                    patterns.add(f"{f}{sep1}{l[0]}{sep2}{self.year_short}")
        
        return patterns
    
    def _generate_username_role_patterns(self, components: Dict[str, str]) -> Set[str]:
        """Role username patterns"""
        patterns = set()
        
        if not self.roles:
            return patterns
        
        f = components['f']
        l = components['l']
        
        for role in self.roles:
            role_patterns = ROLES.get(role.lower(), [role.lower()])
            for rp in role_patterns:
                patterns.add(f"{rp}_{f}")
                patterns.add(f"{rp}.{f}")
                patterns.add(f"{rp}-{f}")
                patterns.add(f"{f}_{rp}")
                patterns.add(f"{f}.{rp}")
                if l:
                    patterns.add(f"{rp}_{f}{l}")
                    patterns.add(f"{rp}.{f}.{l}")
                    patterns.add(f"{f}{l}_{rp}")
        
        return patterns
    
    def _generate_username_company_patterns(self, components: Dict[str, str]) -> Set[str]:
        """Company-specific username patterns"""
        patterns = set()
        
        if not self.target_company or self.target_company not in COMPANY_TARGETS:
            return patterns
        
        f = components['f']
        l = components['l']
        target_data = COMPANY_TARGETS[self.target_company]
        
        # Product-based patterns
        for product in target_data.get('products', []):
            patterns.add(f"{f}_{product}")
            patterns.add(f"{f}.{product}")
            patterns.add(f"{product}_{f}")
            if l:
                patterns.add(f"{f}{l}_{product}")
        
        # Company-specific patterns
        for common in target_data.get('common', []):
            patterns.add(f"{f}_{common}")
            patterns.add(f"{common}_{f}")
            patterns.add(f"{f}{common}")
        
        return patterns



    def generate_usernames(self, fullname: str) -> List[str]:
        """Username patterns with role and targeted patterns"""
        # Parse name
        first, middle, last = self.parse_name(fullname)
        if not first:
            return []
        
        # Basic components
        components = self._generate_username_basic_components(first, middle, last)
        
        # Based on depth level
        if self.user_depth == 1:
            patterns = self._generate_usernames_level1(components)
        elif self.user_depth == 2:
            level1 = self._generate_usernames_level1(components)
            patterns = self._generate_usernames_level2(components, level1)
        elif self.user_depth == 3:
            level1 = self._generate_usernames_level1(components)
            level2 = self._generate_usernames_level2(components, level1)
            patterns = self._generate_usernames_level3(components, level2)
        elif self.user_depth == 4:
            level1 = self._generate_usernames_level1(components)
            level2 = self._generate_usernames_level2(components, level1)
            level3 = self._generate_usernames_level3(components, level2)
            patterns = self._generate_usernames_level4(components, level3)
        else:
            level1 = self._generate_usernames_level1(components)
            level2 = self._generate_usernames_level2(components, level1)
            level3 = self._generate_usernames_level3(components, level2)
            level4 = self._generate_usernames_level4(components, level3)
            patterns = self._generate_usernames_level5(components, level4)
        
        # Role-based patterns
        role_patterns = self._generate_username_role_patterns(components)
        patterns.update(role_patterns)
        
        # Company-specific patterns
        company_patterns = self._generate_username_company_patterns(components)
        patterns.update(company_patterns)
        
        # Apply filters
        patterns = self._apply_filters(patterns, is_username=True)
        
        return sorted(list(patterns))


    def _generate_temporal_patterns(self, years: list, years_short: list, seasons: list, 
                                    months: list, months_abbr: list) -> set:
        """CATEGORY 1: TEMPORAL PATTERNS"""
        passwords = set()
        
        # Seasons + Year 
        for season in seasons:
            season_cap = season.capitalize()
            for year in years:
                passwords.add(f"{season_cap}{year}")
                passwords.add(f"{season.lower()}{year}")
                passwords.add(f"{season_cap}{str(year)[2:]}")
                passwords.add(f"{season.lower()}{str(year)[2:]}")
                
                # With symbols
                if self.user_depth >= 2:
                    passwords.add(f"{season_cap}{year}!")
                    passwords.add(f"{season_cap}{year}@")
                    passwords.add(f"{season_cap}!{year}")
                    passwords.add(f"{season_cap}@{str(year)[2:]}")
        
        # 1.2 Months + Year
        for i, month in enumerate(months):
            month_cap = month.capitalize()
            month_abbr = months_abbr[i] if i < len(months_abbr) else month[:3]
            
            for year in years:
                passwords.add(f"{month_cap}{year}")
                passwords.add(f"{month.lower()}{year}")
                passwords.add(f"{month_cap}{str(year)[2:]}")
                passwords.add(f"{month_abbr.capitalize()}{year}")
                passwords.add(f"{month_abbr.capitalize()}{str(year)[2:]}")
                
                # With symbols
                if self.user_depth >= 2:
                    passwords.add(f"{month_cap}{year}!")
                    passwords.add(f"{month_cap}{year}@")
                    passwords.add(f"{month_cap}!{year}")
        
        # 1.3 Year alone
        for year in years:
            passwords.add(str(year))
            passwords.add(str(year)[2:])
            if self.user_depth >= 2:
                passwords.add(f"@{year}")
                passwords.add(f"!{year}")
                passwords.add(f"#{year}")
        
        return passwords
    
    def _generate_name_based_mutations(self, f: str, l: str, f_cap: str, l_cap: str,
                                       first: str, middle: str, last: str,
                                       years: list, seasons: list, months: list) -> set:
        """CATEGORY 2: NAME-BASED MUTATIONS"""
        passwords = set()
        
        # 2.1 Name + Temporal
        for year in years:
            year_short = str(year)[2:]
            passwords.add(f"{f_cap}{year}")
            passwords.add(f"{f_cap}{year_short}")
            passwords.add(f"{f.lower()}{year}")
            
            if self.user_depth >= 2:
                passwords.add(f"{f_cap}{year}!")
                passwords.add(f"{f_cap}!{year}")
                passwords.add(f"{f_cap}@{year}")
                passwords.add(f"{f_cap}#{year}")
                passwords.add(f"{f_cap}{year_short}!")
            
            if l:
                passwords.add(f"{l_cap}{year}")
                passwords.add(f"{l_cap}{year_short}")
                if self.user_depth >= 2:
                    passwords.add(f"{l_cap}{year}!")
                    passwords.add(f"{l_cap}!{year}")
        
        # 2.2 Name + Season
        if self.user_depth >= 2:
            for season in seasons:
                season_cap = season.capitalize()
                passwords.add(f"{f_cap}{season_cap}")
                passwords.add(f"{f_cap}{season_cap}{self.year_short}")
                for year in years:
                    passwords.add(f"{f_cap}{season_cap}{str(year)[2:]}")
                
                if l:
                    passwords.add(f"{l_cap}{season_cap}")
                    passwords.add(f"{l_cap}{season_cap}{self.year_short}")
        
        # 2.3 Name + Month
        if self.user_depth >= 3:
            for month in months[:6]:
                month_cap = month.capitalize()
                passwords.add(f"{f_cap}{month_cap}")
                passwords.add(f"{f_cap}{month_cap}{self.year_short}")
                
                if l:
                    passwords.add(f"{l_cap}{month_cap}")
        
        # 2.4 Initials + Temporal
        if l and self.user_depth >= 2:
            initials = f"{first[0]}{last[0]}".upper()
            if middle:
                initials_full = f"{first[0]}{middle[0]}{last[0]}".upper()
                for year in years:
                    passwords.add(f"{initials_full}{year}")
                    passwords.add(f"{initials_full}{str(year)[2:]}")
                    if self.user_depth >= 3:
                        passwords.add(f"{initials_full}{year}!")
                        passwords.add(f"{initials_full}!{year}")
            
            for year in years:
                passwords.add(f"{initials}{year}")
                passwords.add(f"{initials}{str(year)[2:]}")
                if self.user_depth >= 3:
                    passwords.add(f"{initials}{year}!")
                    passwords.add(f"{initials}!{year}")
        
        # 2.5 Full name combinations
        if l:
            passwords.add(f"{f_cap}{l_cap}")
            passwords.add(f"{f_cap}{l_cap}1")
            passwords.add(f"{f_cap}{l_cap}!")
            passwords.add(f"{f_cap}{l_cap}{self.year_short}")
            passwords.add(f"{l_cap}{f_cap}")
            passwords.add(f"{l_cap}{self.year}")
            
            if self.user_depth >= 3:
                for year in years:
                    passwords.add(f"{f_cap}{l_cap}{str(year)[2:]}")
                    passwords.add(f"{l_cap}{f_cap}{str(year)[2:]}")
        
        # 2.6 Name + Sequences
        if self.user_depth >= 2:
            passwords.add(f"{f_cap}123")
            passwords.add(f"{f_cap}1234")
            passwords.add(f"{f_cap}12345")
            passwords.add(f"{f_cap}123!")
            passwords.add(f"{f_cap}@123")
            passwords.add(f"{f_cap}#123")
            
            if l:
                passwords.add(f"{l_cap}123")
                passwords.add(f"{l_cap}456")
                passwords.add(f"{l_cap}123!")
                passwords.add(f"{l_cap}@123")
        
        return passwords
    
    def _generate_corporate_common_patterns(self, years: list, f_cap: str, company: str) -> set:
        """CATEGORY 3: CORPORATE COMMON PATTERNS"""
        passwords = set()
        
        # 3.1 Common words + Year
        common_words = ['Welcome', 'Password', 'Admin', 'Secret', 'Company']
        
        # Custom common words
        if hasattr(self, 'common_words') and self.common_words:
            common_words.extend([w.capitalize() for w in self.common_words])
        
        for word in common_words:
            for year in years:
                passwords.add(f"{word}{year}")
                passwords.add(f"{word}{str(year)[2:]}")
                
                if self.depth >= 2:
                    passwords.add(f"{word}{year}!")
                    passwords.add(f"{word}!{year}")
                    passwords.add(f"{word}@{year}")
                    passwords.add(f"{word}#{year}")
                    passwords.add(f"{word}{str(year)[2:]}!")
        
        # 3.2 Company name + Year
        if company:
            comp_cap = company.capitalize()
            comp_lower = company.lower()
            
            for year in years:
                passwords.add(f"{comp_cap}{year}")
                passwords.add(f"{comp_cap}{str(year)[2:]}")
                passwords.add(f"{comp_lower}{year}")
                
                if self.depth >= 2:
                    passwords.add(f"{comp_cap}{year}!")
                    passwords.add(f"{comp_cap}!{year}")
                    passwords.add(f"{comp_cap}@{year}")
            
            # Company + name
            passwords.add(f"{comp_cap}{f_cap}")
            passwords.add(f"{comp_cap}{f_cap}1")
            passwords.add(f"{comp_cap}{f_cap}!")
            passwords.add(f"{comp_cap}123")
            passwords.add(f"{comp_cap}123!")
            passwords.add(f"{comp_cap}@123")
        
        # 3.3 Role + Year
        if self.roles and self.depth >= 2:
            for role in self.roles:
                role_cap = role.capitalize()
                for year in years:
                    passwords.add(f"{role_cap}{year}")
                    passwords.add(f"{role_cap}{str(year)[2:]}")
                    
                    if self.depth >= 3:
                        passwords.add(f"{role_cap}{year}!")
                        passwords.add(f"{role_cap}!{year}")
                
                passwords.add(f"{role_cap}123")
                passwords.add(f"{role_cap}123!")
        
        return passwords
    
    def _generate_numeric_sequences(self) -> set:
        """CATEGORY 4: COMMON NUMERIC SEQUENCES"""
        passwords = set()
        
        if hasattr(self, 'numeric_sequences') and self.numeric_sequences:
            # 4.1 Basic sequences
            sequences = [
                "123456", "1234567", "12345678", "123456789", "1234567890",
                "654321", "987654321",
                "111111", "222222", "000000",
                "123123", "321321"
            ]
            passwords.update(sequences)
            
            # 4.2 Sequences + symbols
            if self.depth >= 2:
                for seq in ["123456", "123456789", "12345678"]:
                    passwords.add(f"{seq}!")
                    passwords.add(f"{seq}@")
                    passwords.add(f"{seq}#")
                    passwords.add(f"!{seq}")
                    passwords.add(f"@{seq}")
            
            # 4.3 Sequences + letters
            if self.depth >= 2:
                passwords.add("abc123")
                passwords.add("abc1234")
                passwords.add("abc12345")
                passwords.add("password123")
                passwords.add("password1")
                passwords.add("qwerty123")
                passwords.add("qwerty1234")
        
        return passwords
    
    def _generate_keyboard_patterns(self) -> set:
        """CATEGORY 5: KEYBOARD PATTERNS"""
        passwords = set()
        
        if hasattr(self, 'keyboard_patterns') and self.keyboard_patterns and self.depth >= 2:
            # 5.1 QWERTY sequences
            keyboard = [
                "qwerty", "qwerty123", "qwerty1234", "Qwerty123", "Qwerty123!",
                "asdfgh", "asdfgh123", "Asdfgh123", "Asdfgh123!",
                "zxcvbn", "zxcvbn123", "Zxcvbn123", "Zxcvbn123!"
            ]
            passwords.update(keyboard)
            
            # 5.2 Diagonal patterns
            if self.depth >= 3:
                diagonal = [
                    "1qaz2wsx", "1qaz2wsx3edc",
                    "qazwsx", "qazwsx123", "Qazwsx123!",
                    "1q2w3e4r", "1q2w3e4r5t"
                ]
                passwords.update(diagonal)
        
        return passwords
    
    def _generate_symbol_mutations(self, f_cap: str, l_cap: str, l: str, symbols: list) -> set:
        """CATEGORY 6: SYMBOL MUTATIONS"""
        passwords = set()
        
        if self.depth >= 3:
            # 6.1 Name + Symbol + Number
            for sym in symbols[:3]:  # !, @, #
                passwords.add(f"{f_cap}{sym}23")
                passwords.add(f"{f_cap}{sym}24")
                passwords.add(f"{f_cap}{sym}25")
                passwords.add(f"{f_cap}{sym}123")
                passwords.add(f"{f_cap}{sym}{self.year}")
                
                if l:
                    passwords.add(f"{l_cap}{sym}123")
                    passwords.add(f"{l_cap}{sym}{self.year}")
            
            # 6.2 Word + Symbol + Year
            for word in ['Welcome', 'Password', 'Summer']:
                for sym in symbols[:3]:
                    passwords.add(f"{word}{sym}{self.year}")
                    passwords.add(f"{word}{sym}{self.year_short}")
        
        return passwords
    
    def _generate_capitalization_variations(self) -> set:
        """CATEGORY 7: CAPITALIZATION VARIATIONS"""
        passwords = set()
        
        if self.depth >= 4:
            # Create variations of key passwords
            key_passwords = [
                f"welcome{self.year}",
                f"password{self.year}",
                f"summer{self.year}"
            ]
            
            for pwd in key_passwords:
                # All uppercase
                passwords.add(pwd.upper())
                # First letter uppercase
                # CamelCase
                if len(pwd) > 6:
                    camel = pwd[:3] + pwd[3].upper() + pwd[4:]
                    passwords.add(camel)
        
        return passwords
    
    def _generate_targeted_company_patterns(self, years: list) -> set:
        """CATEGORY 8: TARGETED COMPANY PATTERNS"""
        passwords = set()
        
        if self.target_company and self.target_company in COMPANY_TARGETS and self.depth >= 3:
            target_data = COMPANY_TARGETS[self.target_company]
            
            # Product-based passwords
            for product in target_data.get('products', [])[:5]:
                product_cap = product.capitalize()
                passwords.add(f"{product_cap}123")
                passwords.add(f"{product_cap}123!")
                for year in years:
                    passwords.add(f"{product_cap}{year}")
                    passwords.add(f"{product_cap}{str(year)[2:]}")
        
        return passwords
    
    def _generate_common_weak_passwords(self) -> set:
        """CATEGORY 9: COMMON WEAK PASSWORDS"""
        passwords = set()
        
        common_weak = [
            "P@ssw0rd", "P@ssw0rd!", "P@ssword123",
            "Admin123", "Admin123!", "admin123",
            "Welcome1", "Welcome1!", "welcome1"
        ]
        passwords.update(common_weak)
        
        return passwords
    
    def _generate_incremental_passwords(self, years: list, company: str) -> set:
        """CATEGORY 10: INCREMENTAL PASSWORDS"""
        passwords = set()
        
        if self.depth >= 2:
            base_words = ['Welcome', 'Password', 'Admin', company.capitalize() if company else 'Company']
            
            for word in base_words:
                for i in range(1, self.rotation_count + 1):
                    # Word + Number + Symbol
                    passwords.add(f"{word}{i}!")
                    passwords.add(f"{word}{i}@")
                    passwords.add(f"{word}{i}#")
                    
                    if self.depth >= 3:
                        passwords.add(f"{word}{i}$")
                        passwords.add(f"{word}{i}%")
        
        return passwords
    
    def _generate_quarter_fiscal_patterns(self, years: list) -> set:
        """CATEGORY 11: QUARTER/FISCAL YEAR PATTERNS"""
        passwords = set()
        
        if self.depth >= 2 and self.quarters:
            quarters = ['Q1', 'Q2', 'Q3', 'Q4', 'FY']
            
            for q in quarters:
                for year in years:
                    year_str = str(year)
                    year_short = year_str[2:]
                    
                    # Basic formats
                    passwords.add(f"{q}{year_str}")
                    passwords.add(f"{q}{year_short}")
                    passwords.add(f"{q}-{year_str}")
                    passwords.add(f"{q}-{year_short}")
                    
                    # With symbols
                    passwords.add(f"{q}{year_str}!")
                    passwords.add(f"{q}{year_short}!")
                    
                    if self.depth >= 3:
                        # Quarter + Year combinations
                        passwords.add(f"Quarter{q[-1]}{year_str}")
                        passwords.add(f"Quarter{q[-1]}-{year_str}")
                        
                        # Fiscal year ranges (for FY)
                        if q == 'FY' and year < max(years):
                            next_year = str(int(year_str) + 1)[2:]
                            passwords.add(f"FY{year_str}-{next_year}")
                            passwords.add(f"FY{year_short}-{next_year}")
        
        return passwords
    
    def _generate_department_passwords(self, years: list) -> set:
        """CATEGORY 12: DEPARTMENT-BASED PASSWORDS"""
        passwords = set()
        
        if self.depth >= 2 and self.departments:
            departments = [
                'IT', 'HR', 'Finance', 'Sales', 'Marketing', 
                'Legal', 'Support', 'Admin', 'Accounting', 'Operations'
            ]
            
            for dept in departments:
                for year in years:
                    year_str = str(year)
                    year_short = year_str[2:]
                    
                    # Basic formats
                    passwords.add(f"{dept}{year_str}")
                    passwords.add(f"{dept}{year_short}")
                    
                    # With symbols
                    passwords.add(f"{dept}{year_str}!")
                    passwords.add(f"{dept}{year_short}!")
                    
                    if self.depth >= 3:
                        passwords.add(f"{dept}{year_str}@")
                        passwords.add(f"{dept}{year_str}#")
                        
                        # Department + Team/Dept suffix
                        passwords.add(f"{dept}Team{year_str}")
                        passwords.add(f"{dept}Dept{year_str}")
        
        return passwords
    
    def _generate_company_temporal_enhanced(self, company: str, years: list, seasons: list) -> set:
        """CATEGORY 13: ENHANCED COMPANY + TEMPORAL"""
        passwords = set()
        
        if company and self.depth >= 2:
            company_cap = company.capitalize()
            
            # Company + Season + Year
            for season in seasons[:4]:
                season_cap = season.capitalize()
                for year in years:
                    year_str = str(year)
                    year_short = year_str[2:]
                    
                    passwords.add(f"{company_cap}{season_cap}{year_str}")
                    passwords.add(f"{company_cap}{season_cap}{year_short}")
                    
                    if self.depth >= 3:
                        passwords.add(f"{company_cap}{season_cap}{year_str}!")
            
            # Company + Year
            for year in years:
                year_str = str(year)
                year_short = year_str[2:]
                
                passwords.add(f"{company_cap}{year_str}")
                passwords.add(f"{company_cap}{year_short}")
                passwords.add(f"{company_cap}{year_str}!")
                passwords.add(f"{company_cap}{year_str}@")
                
                if self.depth >= 3:
                    passwords.add(f"{company_cap}{year_str}#")
        
        return passwords
    
    def generate_passwords(self, fullname: str, company: str = "") -> List[str]:
        """Generate password patterns"""
        first, middle, last = self.parse_name(fullname)
        if not first:
            return []
        
        passwords = set()
        
        # Basic components
        f = first.lower()
        l = last.lower() if last else ""
        f_cap = first.capitalize()
        l_cap = last.capitalize() if last else ""
        
        # Get localized data
        seasons = self._get_localized_seasons(self.language)
        months = self._get_localized_months(self.language)
        months_abbr = months[:12]  # First 12 as abbreviations
        
        # Year variations based on --years
        years = self.years if hasattr(self, 'years') and self.years else [self.year]
        years_short = [str(y)[2:] for y in years]
        
        # Symbols for mutations
        symbols = ['!', '@', '#', '$', '%']
        
        # ============================================================ #
        # LLAMADAS A FUNCIONES ESPECIALIZADAS                          #
        # ============================================================ #
        
        # CATEGORY 1: Temporal patterns
        passwords.update(self._generate_temporal_patterns(
            years, years_short, seasons, months, months_abbr
        ))
        
        # CATEGORY 2: Name-based mutations
        passwords.update(self._generate_name_based_mutations(
            f, l, f_cap, l_cap, first, middle, last, years, seasons, months
        ))
        
        # CATEGORY 3: Corporate common patterns
        passwords.update(self._generate_corporate_common_patterns(years, f_cap, company))
        
        # CATEGORY 4: Numeric sequences
        passwords.update(self._generate_numeric_sequences())
        
        # CATEGORY 5: Keyboard patterns
        passwords.update(self._generate_keyboard_patterns())
        
        # CATEGORY 6: Symbol mutations
        passwords.update(self._generate_symbol_mutations(f_cap, l_cap, l, symbols))
        
        # CATEGORY 7: Capitalization variations
        passwords.update(self._generate_capitalization_variations())
        
        # CATEGORY 8: Targeted company patterns
        passwords.update(self._generate_targeted_company_patterns(years))
        
        # CATEGORY 9: Common weak passwords
        passwords.update(self._generate_common_weak_passwords())
        
        # CATEGORY 10: Incremental passwords (CRITICAL - 85% success)
        passwords.update(self._generate_incremental_passwords(years, company))
        
        # CATEGORY 11: Quarter/Fiscal year patterns (CRITICAL - 55% in finance)
        passwords.update(self._generate_quarter_fiscal_patterns(years))
        
        # CATEGORY 12: Department-based passwords (CRITICAL - 48% success)
        passwords.update(self._generate_department_passwords(years))
        
        # CATEGORY 13: Enhanced company + temporal (CRITICAL - 72% in targeted)
        passwords.update(self._generate_company_temporal_enhanced(company, years, seasons))
        
        # Apply filters (length, complexity, leet speak)
        passwords = self._apply_filters(passwords, is_username=False)
        
        return sorted(list(passwords))
    def generate_emails(self, fullname: str, domains: List[str]) -> List[str]:
        """Email patterns"""
        first, middle, last = self.parse_name(fullname)
        if not first or not last or not domains:
            return []
        
        emails = set()
        
        f = first.lower()
        l = last.lower()
        m = middle.lower() if middle else ""
        
        for domain in domains:
            domain = domain.strip()
            
            # Basic patterns
            emails.add(f"{f}@{domain}")
            emails.add(f"{l}@{domain}")
            emails.add(f"{f}{l}@{domain}")
            emails.add(f"{f}.{l}@{domain}")
            emails.add(f"{f}_{l}@{domain}")
            emails.add(f"{f}-{l}@{domain}")
            emails.add(f"{l}{f}@{domain}")
            emails.add(f"{l}.{f}@{domain}")
            
            # Initials
            emails.add(f"{f[0]}{l}@{domain}")
            emails.add(f"{f}{l[0]}@{domain}")
            emails.add(f"{f[0]}{l[0]}@{domain}")
            emails.add(f"{f[0]}.{l[0]}@{domain}")
            
            # Middle name patterns
            if m:
                emails.add(f"{f}.{m}.{l}@{domain}")
                emails.add(f"{f}{m}{l}@{domain}")
                emails.add(f"{f[0]}{m[0]}{l[0]}@{domain}")
            
            # Company size optimizations
            if self.company_size == "enterprise":
                # Large companies often use first.last
                emails.add(f"{f}.{l}@{domain}")
                emails.add(f"{f[0]}.{l}@{domain}")
            elif self.company_size == "startup":
                # Firstname
                emails.add(f"{f}@{domain}")
            
            # Role emails
            if self.roles:
                for role in self.roles:
                    role_patterns = ROLES.get(role.lower(), [role.lower()])
                    for rp in role_patterns[:5]:
                        emails.add(f"{rp}@{domain}")
                        emails.add(f"{f}.{rp}@{domain}")
                        emails.add(f"{rp}.{f}@{domain}")
        
        return sorted(list(emails))
    
    def _apply_filters(self, patterns: Set[str], is_username: bool = True) -> Set[str]:
        """Apply filters to patterns"""
        # Leet speak
        if is_username and self.leet_user > 0:
            patterns = self._apply_leet_to_usernames(patterns)
        elif not is_username and self.leet_password > 0:
            patterns = self._apply_leet_to_passwords(patterns)
        
        # Apply general leet
        if self.leet_level > 0:
            leet_patterns = set()
            for pattern in list(patterns)[:100]:
                leet_variants = LeetSpeakConverter.apply_leet(pattern, self.leet_level)
                leet_patterns.update(leet_variants)
            patterns.update(leet_patterns)
        
        # Apply prefix/suffix
        pattern_type = 'user' if is_username else 'pass'
        if (is_username and (self.user_prefix or self.user_suffix)) or \
           (not is_username and (self.pass_prefix or self.pass_suffix)):
            new_patterns = set()
            for p in patterns:
                new_patterns.update(self._apply_prefix_suffix(p, pattern_type))
            patterns = new_patterns
        
        # Filter by length
        if is_username:
            patterns = self._filter_by_length(patterns, self.min_user_length, self.max_user_length)
        else:
            patterns = self._filter_by_length(patterns, self.min_pass_length, self.max_pass_length)
        
        # Filter by complexity
        if not is_username and self.complexity != 'low':
            patterns = self._filter_by_complexity(patterns)
        
        return patterns


# ============================================================ #
# WORDLIST OPTIMIZER                                           #
# ============================================================ #

class WordlistOptimizer:
    """Optimize wordlists"""
    
    @staticmethod
    def optimize(wordlist: List[str], min_length: int = 3, max_length: int = 50) -> List[str]:
        """Remove duplicates"""
        unique = {}
        for word in wordlist:
            key = word.lower()
            if key not in unique:
                unique[key] = word
        
        # Filter by length
        filtered = [w for w in unique.values() if min_length <= len(w) <= max_length]
        
        return sorted(filtered)


# ============================================================ #
# WORDLIST ANALYZER                                            #
# ============================================================ #

class WordlistAnalyzer:
    """Analyze wordlists and generate statistics"""
    
    @staticmethod
    def analyze(wordlist: List[str]) -> Dict:
        """Generate statistics"""
        if not wordlist:
            return {}
        
        lengths = [len(w) for w in wordlist]
        
        stats = {
            'total_count': len(wordlist),
            'unique_count': len(set(w.lower() for w in wordlist)),
            'min_length': min(lengths),
            'max_length': max(lengths),
            'avg_length': sum(lengths) / len(lengths),
            'char_frequency': Counter(''.join(wordlist).lower()),
            'length_distribution': Counter(lengths)
        }
        
        return stats


# ============================================================ #
# FILE WRITERS                                                 #
# ============================================================ #

def write_output_files(usernames: List[str], passwords: List[str], emails: List[str],
                      output_dir: Path, format_type: str = 'txt'):
    """Output files in specified format"""
    
    # Create directories
    (output_dir / 'combined').mkdir(parents=True, exist_ok=True)
    
    formats = [format_type] if format_type != 'all' else ['txt', 'json', 'xml']
    
    for fmt in formats:
        if fmt == 'txt':
            _write_txt(usernames, output_dir / 'combined' / 'all_usernames.txt')
            if passwords:
                _write_txt(passwords, output_dir / 'combined' / 'all_passwords.txt')
            if emails:
                _write_txt(emails, output_dir / 'combined' / 'all_emails.txt')
        
        elif fmt == 'json':
            _write_json(usernames, output_dir / 'combined' / 'all_usernames.json')
            if passwords:
                _write_json(passwords, output_dir / 'combined' / 'all_passwords.json')
            if emails:
                _write_json(emails, output_dir / 'combined' / 'all_emails.json')
        
        elif fmt == 'xml':
            _write_xml(usernames, output_dir / 'combined' / 'all_usernames.xml', 'usernames')
            if passwords:
                _write_xml(passwords, output_dir / 'combined' / 'all_passwords.xml', 'passwords')
            if emails:
                _write_xml(emails, output_dir / 'combined' / 'all_emails.xml', 'emails')

def write_individual_files(usernames: List[str], passwords: List[str], emails: List[str],
                          output_dir: Path, format_type: str = 'txt'):
    """Write individual output files"""
    # Create directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    formats = [format_type] if format_type != 'all' else ['txt', 'json', 'xml']
    
    for fmt in formats:
        if fmt == 'txt':
            _write_txt(usernames, output_dir / 'usernames.txt')
            if passwords:
                _write_txt(passwords, output_dir / 'passwords.txt')
            if emails:
                _write_txt(emails, output_dir / 'emails.txt')
        
        elif fmt == 'json':
            _write_json(usernames, output_dir / 'usernames.json')
            if passwords:
                _write_json(passwords, output_dir / 'passwords.json')
            if emails:
                _write_json(emails, output_dir / 'emails.json')
        
        elif fmt == 'xml':
            _write_xml(usernames, output_dir / 'usernames.xml', 'usernames')
            if passwords:
                _write_xml(passwords, output_dir / 'passwords.xml', 'passwords')
            if emails:
                _write_xml(emails, output_dir / 'emails.xml', 'emails')

def _write_txt(data: List[str], filepath: Path):
    """Write data to text file"""
    try:
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(data) + '\n')
    except PermissionError:
        log(f"Permission denied: {filepath}", "ERROR")
        raise
    except OSError as e:
        log(f"Failed to write {filepath}: {e}", "ERROR")
        raise


def _write_json(data: List[str], filepath: Path):
    """Write data to JSON file"""
    try:
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except PermissionError:
        log(f"Permission denied: {filepath}", "ERROR")
        raise
    except OSError as e:
        log(f"Failed to write {filepath}: {e}", "ERROR")
        raise


def _write_xml(data: List[str], filepath: Path, root_name: str):
    """Write data to XML file"""
    try:
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write(f'<{root_name}>\n')
            for item in data:
                # Escape XML special characters
                item_escaped = item.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                f.write(f'  <item>{item_escaped}</item>\n')
            f.write(f'</{root_name}>\n')
    except PermissionError:
        log(f"Permission denied: {filepath}", "ERROR")
        raise
    except OSError as e:
        log(f"Failed to write {filepath}: {e}", "ERROR")
        raise


def show_detailed_summary(stats: Dict, args, elapsed_time: float):
    """Show detailed execution summary"""
    logger = logging.getLogger('UserForge')
    
    print(f"\n{Colors.GREEN}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}UserForge v1.0 - Execution Summary{Colors.RESET}")
    print(f"{'='*60}")
    
    # Generation Statistics
    print(f"\n{Colors.CYAN}📊 Generation Statistics:{Colors.RESET}")
    print(f"  ├─ Names processed: {stats.get('names_processed', 0)}")
    print(f"  ├─ Usernames generated: {stats.get('total_usernames', 0):,}")
    
    if stats.get('total_passwords', 0) > 0:
        print(f"  ├─ Passwords generated: {stats.get('total_passwords', 0):,}")
    
    if stats.get('total_emails', 0) > 0:
        print(f"  ├─ Emails generated: {stats.get('total_emails', 0):,}")
    
    total_patterns = stats.get('total_usernames', 0) + stats.get('total_passwords', 0) + stats.get('total_emails', 0)
    print(f"  └─ Total patterns: {total_patterns:,}")
    
    # Configuration
    print(f"\n{Colors.CYAN}⚙️  Configuration:{Colors.RESET}")
    user_depth = getattr(args, 'user_depth', None) or getattr(args, 'depth', 3)
    pass_depth = getattr(args, 'pass_depth', None) or getattr(args, 'depth', 3)
    print(f"  ├─ User depth: {user_depth}")
    print(f"  ├─ Pass depth: {pass_depth}")
    print(f"  ├─ Output format: {getattr(args, 'format', 'txt')}")
    print(f"  └─ Output directory: {getattr(args, 'output', 'N/A')}")
    
    # Performance
    print(f"\n{Colors.CYAN}⏱️  Performance:{Colors.RESET}")
    print(f"  ├─ Execution time: {elapsed_time:.2f}s")
    
    if elapsed_time > 0:
        patterns_per_sec = total_patterns / elapsed_time
        names_per_sec = stats.get('names_processed', 0) / elapsed_time
        print(f"  ├─ Patterns/second: {patterns_per_sec:.0f}")
        print(f"  └─ Names/second: {names_per_sec:.1f}")
    
    # Output Files
    output_dir = getattr(args, 'output', 'N/A')
    print(f"\n{Colors.CYAN}💾 Output Files:{Colors.RESET}")
    print(f"  ├─ Combined directory: {output_dir}/combined/")
    print(f"  └─ Individual directories: {output_dir}/by_person/")
    
    print(f"\n{Colors.GREEN}{'='*60}{Colors.RESET}")
    
    logger.success("✓ UserForge v1.0 completed successfully!")


def validate_arguments(args) -> bool:
    """Validate arguments"""
    logger = logging.getLogger('UserForge')
    
    # Check input file
    if not hasattr(args, 'input') or not args.input:
        logger.error("Input file is required. Use -i/--input or --interactive mode.")
        return False
    if not os.path.exists(args.input):
        logger.error(f"Input file not found: {args.input}")
        return False
    
    # Check depth values
    if hasattr(args, 'depth'):
        if args.depth < 1 or args.depth > 5:
            logger.error(f"Invalid depth value: {args.depth}. Must be between 1 and 5.")
            return False
    
    if hasattr(args, 'user_depth') and args.user_depth:
        if args.user_depth < 1 or args.user_depth > 5:
            logger.error(f"Invalid user-depth value: {args.user_depth}. Must be between 1 and 5.")
            return False
    
    if hasattr(args, 'pass_depth') and args.pass_depth:
        if args.pass_depth < 1 or args.pass_depth > 5:
            logger.error(f"Invalid pass-depth value: {args.pass_depth}. Must be between 1 and 5.")
            return False
    
    # Check leet speak
    if hasattr(args, 'leet') and args.leet:
        if args.leet < 0 or args.leet > 3:
            logger.error(f"Invalid leet level: {args.leet}. Must be between 0 and 3.")
            return False
    
    return True


def prepare_output_directory(args) -> Path:
    """Prepare output directory"""
    logger = logging.getLogger('UserForge')
    
    if args.output:
        output_dir = Path(args.output)
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = Path.home() / 'UserForge_Output' / f'UserForge_Output_{timestamp}'
    
    output_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"Output directory: {output_dir}")
    
    return output_dir


def create_pattern_generator(args) -> 'PatternGenerator':
    """Create PatternGenerator instance"""
    logger = logging.getLogger('UserForge')
    
    if args.verbose:
        logger.info("Initializing pattern generator...")
        # Check if user used separate depths
        if hasattr(args, 'user_depth') and hasattr(args, 'pass_depth') and args.user_depth != args.pass_depth:
            logger.info(f"  ├─ User Depth: {args.user_depth}")
            logger.info(f"  ├─ Pass Depth: {args.pass_depth}")
        elif hasattr(args, 'depth') and args.depth is not None:
            logger.info(f"  ├─ Depth Level: {args.depth}")
        else:
            logger.info(f"  ├─ Depth Level: {args.user_depth}")
        logger.info(f"  ├─ Leet Speak: Level {args.leet}")
        logger.info(f"  ├─ Company Size: {args.company_size}")
        logger.info(f"  ├─ Language: {args.language}")
        logger.info(f"  └─ Country: {args.country}")
    
    # Prepare years list
    years = []
    if hasattr(args, 'years') and args.years:
        if '-' in args.years and ',' not in args.years:
            parts = args.years.split('-')
            if len(parts) == 2:
                start_year = int(parts[0].strip())
                end_year = int(parts[1].strip())
                years = list(range(start_year, end_year + 1))
            else:
                logger.error(f"Invalid year range format: {args.years}. Use '2024-2025' or '2024,2025'")
                years = []
        else:
            years = [int(y.strip()) for y in args.years.split(',')]
    
    # Prepare common words
    common_words = []
    if hasattr(args, 'common_words') and args.common_words:
        common_words = [w.strip() for w in args.common_words.split(',')]
    
    # Prepare roles
    roles = []
    if hasattr(args, 'roles') and args.roles:
        if isinstance(args.roles, str):
            roles = [r.strip() for r in args.roles.split(',')]
        else:
            roles = args.roles
    
    # Create generator
    generator = PatternGenerator(
        depth=getattr(args, 'depth', None),
        user_depth=getattr(args, 'user_depth', None),
        pass_depth=getattr(args, 'pass_depth', None),
        leet_level=args.leet,
        company_size=args.company_size,
        min_user_length=args.min_user_length,
        max_user_length=args.max_user_length,
        min_pass_length=args.min_pass_length,
        max_pass_length=args.max_pass_length,
        country=args.country,
        language=args.language,
        leet_user=args.leet_user,
        leet_password=args.leet_password,
        user_prefix=args.user_prefix,
        user_suffix=args.user_suffix,
        pass_prefix=args.pass_prefix,
        pass_suffix=args.pass_suffix,
        roles=roles,
        target_company=args.target_company,
        complexity=args.complexity,
        smart_mode=args.smart,
        years=years if years else None,
        common_words=common_words if common_words else None,
        keyboard_patterns=getattr(args, 'keyboard_patterns', False),
        numeric_sequences=getattr(args, 'numeric_sequences', False),
        symbol_positions=getattr(args, 'symbol_positions', None),
        seasons_only=getattr(args, 'seasons_only', False),
        rotation_count=getattr(args, 'rotation_count', 12),
        quarters=getattr(args, 'quarters', False),
        departments=getattr(args, 'departments', False)
    )
    
    return generator


def process_all_names(names: List[str], generator: 'PatternGenerator', args) -> Dict:
    """Process and generate patterns"""
    logger = logging.getLogger('UserForge')
    
    all_usernames = []
    all_passwords = []
    all_emails = []
    
    # Process each name
    logger.info(f"Processing {len(names)} name(s)...")
    
    # Store individual results for by_person output
    individual_results = []
    
    for i, name in enumerate(names, 1):
        # Show progress bar
        if not args.verbose:
            show_progress(i, len(names), 'Processing names')
        else:
            logger.info(f"  [{i}/{len(names)}] Processing: {name}")
        
        # Generate usernames
        usernames = generator.generate_usernames(name)
        all_usernames.extend(usernames)
        
        # Generate passwords
        passwords = []
        if args.passwords:
            company_name = args.company_name if hasattr(args, 'company_name') and args.company_name else ""
            passwords = generator.generate_passwords(name, company_name)
            all_passwords.extend(passwords)
        
        # Generate emails
        emails = []
        if args.emails:
            domains = [d.strip() for d in args.emails.split(',')]
            emails = generator.generate_emails(name, domains)
            all_emails.extend(emails)
        
        # Store individual results
        individual_results.append({
            'name': name,
            'usernames': sorted(list(set(usernames))),
            'passwords': sorted(list(set(passwords))),
            'emails': sorted(list(set(emails)))
        })
    
    # Remove duplicates and sort
    all_usernames = sorted(list(set(all_usernames)))
    all_passwords = sorted(list(set(all_passwords)))
    all_emails = sorted(list(set(all_emails)))
    
    return {
        'usernames': all_usernames,
        'passwords': all_passwords,
        'emails': all_emails,
        'names_processed': len(names),
        'total_usernames': len(all_usernames),
        'total_passwords': len(all_passwords),
        'total_emails': len(all_emails),
        'individual_results': individual_results
    }


def write_all_outputs(results: Dict, output_dir: Path, args):
    """Write all output files
    
    Args:
        results: Dictionary with generated patterns
        output_dir: Output directory path
        args: Command-line arguments
    """
    logger = logging.getLogger('UserForge')
    
    logger.info("Writing combined outputs...")
    
    # Write combined files
    write_output_files(
        results['usernames'],
        results['passwords'],
        results['emails'],
        output_dir,
        args.format
    )
    
    # Write individual files (by_person)
    if 'individual_results' in results and results['individual_results']:
        logger.info("Writing individual outputs (by_person)...")
        
        for person_data in results['individual_results']:
            # Create directory name
            name = person_data['name']
            dir_name = name.lower().replace(' ', '_')
            dir_name = ''.join(c for c in dir_name if c.isalnum() or c == '_')
            
            # Create person directory
            person_dir = output_dir / 'by_person' / dir_name
            person_dir.mkdir(parents=True, exist_ok=True)
            
            # Write files for each person
            write_individual_files(
                person_data['usernames'],
                person_data['passwords'],
                person_data['emails'],
                person_dir,
                args.format
            )
    
    # Show results
    if results['total_usernames'] > 0:
        logger.success(f"✓ Generated {results['total_usernames']} unique usernames")
    
    if results['total_passwords'] > 0:
        logger.success(f"✓ Generated {results['total_passwords']} unique passwords")
    
    if results['total_emails'] > 0:
        logger.success(f"✓ Generated {results['total_emails']} unique emails")



def main():
    """Main function - Refactored for better maintainability"""
    # Start timing
    start_time = time.time()
    print_banner()
    
    # Check for interactive
    if '--interactive' in sys.argv or '-I' in sys.argv:
        config = interactive_mode()
        # Convert config to objects
        class Args:
            pass
        args = Args()
        for key, value in config.items():
            setattr(args, key, value)
        # Set defaults for missing args
        defaults = {
            'output': None, 'format': 'txt', 'company_size': 'medium', 'verbose': True,
            'min_user_length': 3, 'max_user_length': 50,
            'min_pass_length': 8, 'max_pass_length': 50,
            'leet': 0, 'leet_user': 0, 'leet_password': 0,
            'user_prefix': '', 'user_suffix': '',
            'pass_prefix': '', 'pass_suffix': '',
            'target_company': '', 'complexity': 'low', 'smart': False, 'roles': []
        }
        # User_depth/pass_depth 
        if not hasattr(args, 'user_depth'):
            if hasattr(args, 'depth'):
                setattr(args, 'user_depth', args.depth)
            else:
                setattr(args, 'user_depth', 3)
        if not hasattr(args, 'pass_depth'):
            if hasattr(args, 'depth'):
                setattr(args, 'pass_depth', args.depth)
            else:
                setattr(args, 'pass_depth', 3)
        # Set depth if not set
        if not hasattr(args, 'depth'):
            setattr(args, 'depth', args.user_depth)
        if not hasattr(args, 'pass_depth'):
            if hasattr(args, 'depth'):
                setattr(args, 'pass_depth', args.depth)
            else:
                setattr(args, 'pass_depth', 3)
        # Set depth if not set
        if not hasattr(args, 'depth'):
            setattr(args, 'depth', args.user_depth)
        for key, value in defaults.items():
            if not hasattr(args, key):
                setattr(args, key, value)
        if hasattr(args, 'roles') and isinstance(args.roles, str):
            args.roles = [r.strip() for r in args.roles.split(',')]
    else:
        # Parse arguments
        parser = argparse.ArgumentParser(
            description='UserForge v1.0 - Corporate Username & Password Generator',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog='''
Examples:
  userforge.py -i names.txt -d 3
  userforge.py -i names.txt -d 5 --passwords --emails company.com
  userforge.py -i names.txt --leet 2 --optimize --analyze
  userforge.py -i names.txt --language ES --country ES --roles admin,dev
  userforge.py -i names.txt --target-company microsoft --smart
  userforge.py --interactive
            '''
        )
        
        # Required
        parser.add_argument('-i', '--input', required=False,
                           help='Input file with full names (one per line)')
        
        # Basic options
        parser.add_argument('-d', '--depth', type=int, choices=[1, 2, 3, 4, 5], default=None,
                           help='Depth level: 1=Basic ~100, 2=Standard ~400, 3=Advanced ~800, 4=Extensive ~1500, 5=Maximum ~2500+ (default: 3)')
        parser.add_argument('-ud', '--user-depth', type=int, choices=[1, 2, 3, 4, 5], default=None,
                           help='Username generation depth (overrides --depth for usernames)')
        parser.add_argument('-pd', '--pass-depth', type=int, choices=[1, 2, 3, 4, 5], default=None,
                           help='Password generation depth (overrides --depth for passwords)')
        parser.add_argument('--passwords', action='store_true',
                           help='Generate password patterns')
        parser.add_argument('--emails', type=str, metavar='DOMAINS',
                           help='Generate email patterns (comma-separated domains, e.g., company.com,corp.local)')
        parser.add_argument('--company-name', type=str, metavar='NAME',
                           help='Company name for password generation')
        parser.add_argument('--company-size', choices=['startup', 'smb', 'enterprise', 'medium'], default='medium',
                           help='Company size for email pattern optimization (default: medium)')
        
        # Leet speak options
        parser.add_argument('--leet', type=int, choices=[0, 1, 2, 3], default=0, metavar='LEVEL',
                           help='Leet speak level: 0=Off, 1=Basic, 2=Medium, 3=Advanced (default: 0)')
        parser.add_argument('--leet-user', type=int, choices=[0, 1, 2, 3], default=0, metavar='LEVEL',
                           help='Leet speak level for usernames only (overrides --leet)')
        parser.add_argument('--leet-password', type=int, choices=[0, 1, 2, 3], default=0, metavar='LEVEL',
                           help='Leet speak level for passwords only (overrides --leet)')
        
        # Prefix/Suffix options
        parser.add_argument('--user-prefix', type=str, default='', metavar='PREFIX',
                           help='Prefix to add to usernames')
        parser.add_argument('--user-suffix', type=str, default='', metavar='SUFFIX',
                           help='Suffix to add to usernames')
        parser.add_argument('--pass-prefix', type=str, default='', metavar='PREFIX',
                           help='Prefix to add to passwords')
        parser.add_argument('--pass-suffix', type=str, default='', metavar='SUFFIX',
                           help='Suffix to add to passwords')
        
        # Optimization options
        parser.add_argument('--optimize', action='store_true',
                           help='Optimize wordlists (remove duplicates, filter by length)')
        parser.add_argument('--analyze', action='store_true',
                           help='Generate statistical analysis of wordlists')
        
        # Output options
        parser.add_argument('-o', '--output', type=str, metavar='DIR',
                           help='Output directory (default: ~/UserForge_Output/UserForge_Output_TIMESTAMP)')
        parser.add_argument('--format', choices=['txt', 'json', 'xml', 'all'], default='txt',
                           help='Output format (default: txt)')
        parser.add_argument('-v', '--verbose', action='store_true',
                           help='Verbose output')
        
        # Length filtering
        parser.add_argument('--min-user-length', type=int, default=3, metavar='N',
                           help='Minimum username length (default: 3)')
        parser.add_argument('--max-user-length', type=int, default=50, metavar='N',
                           help='Maximum username length (default: 50)')
        parser.add_argument('--min-pass-length', type=int, default=8, metavar='N',
                           help='Minimum password length (default: 8)')
        parser.add_argument('--max-pass-length', type=int, default=50, metavar='N',
                           help='Maximum password length (default: 50)')
        
        # Localization
        parser.add_argument('--country', type=str, default='US', metavar='CODE',
                           help='Country code for localization (default: US)')
        parser.add_argument('--language', type=str, default='EN', metavar='CODE',
                           help='Language code for localization (default: EN)')
        
        # Advanced options
        parser.add_argument('--target-company', type=str, default='', metavar='NAME',
                           help='Target company for advanced patterns')
        parser.add_argument('--complexity', choices=['low', 'medium', 'high'], default='low',
                           help='Password complexity level (default: low)')
        parser.add_argument('--smart', action='store_true',
                           help='Enable smart mode (auto-adjust parameters)')
        parser.add_argument('--roles', type=str, default='', metavar='ROLES',
                           help='Comma-separated list of roles/titles')
        
        # Password generation
        parser.add_argument('--years', type=str, metavar='YEARS',
                           help='Comma-separated years for password patterns')
        parser.add_argument('--common-words', type=str, metavar='WORDS',
                           help='Comma-separated common words for passwords')
        parser.add_argument('--keyboard-patterns', action='store_true',
                           help='Include keyboard patterns (qwerty, asdf, etc.)')
        parser.add_argument('--numeric-sequences', action='store_true',
                           help='Include numeric sequences (123, 456, etc.)')
        parser.add_argument('--symbol-positions', type=str, choices=['start', 'end', 'both'], default=None,
                           help='Where to place symbols in passwords')
        parser.add_argument('--seasons-only', action='store_true',
                           help='Use only season-based patterns')
        parser.add_argument('--rotation-count', type=int, default=12, metavar='N',
                           help='Number of password rotation cycles (default: 12)')
        parser.add_argument('--quarters', action='store_true',
                           help='Include quarterly patterns (Q1, Q2, etc.)')
        parser.add_argument('--departments', action='store_true',
                           help='Include department patterns (IT, HR, etc.)')
        
        # Interactive mode
        parser.add_argument('-I', '--interactive', action='store_true',
                           help='Interactive mode')
        
        args = parser.parse_args()

    if not hasattr(args, 'user_depth') or args.user_depth is None:
        if hasattr(args, 'depth') and args.depth is not None:
            args.user_depth = args.depth
        else:
            args.user_depth = 3
    if not hasattr(args, 'pass_depth') or args.pass_depth is None:
        if hasattr(args, 'depth') and args.depth is not None:
            args.pass_depth = args.depth
        else:
            args.pass_depth = 3

    if not hasattr(args, 'depth') or args.depth is None:
        args.depth = args.user_depth

    # Setup logging
    log_file = None
    if hasattr(args, 'output') and args.output:
        log_file = os.path.join(args.output, 'userforge.log')
    setup_logging(verbose=args.verbose, log_file=log_file)
    
    logger = logging.getLogger('UserForge')
    
    try:
        # Validate arguments
        if not validate_arguments(args):
            sys.exit(1)
        
        # Load and validate names
        if args.verbose:
            logger.info(f"Input file: {args.input}")
            logger.info("Reading input file...")
        
        names = load_input_names(args.input)
        
        if args.verbose:
            logger.info(f"Loaded {len(names)} valid name(s)")
        
        # Output directory
        output_dir = prepare_output_directory(args)
        
        # Pattern generator
        generator = create_pattern_generator(args)
        
        # Process names
        results = process_all_names(names, generator, args)
        
        # Write outputs
        write_all_outputs(results, output_dir, args)
        
        # Calculate time
        elapsed_time = time.time() - start_time
        
        # Detailed summary
        logger.success("="*60)
        show_detailed_summary(results, args, elapsed_time)
        
    except KeyboardInterrupt:
        logger.warning("\\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        if args.verbose:
            import traceback
            logger.error(traceback.format_exc())
        sys.exit(1)



if __name__ == "__main__":
    main()

