#!/bin/bash

#############################################################
# UserForge v1.0.0 - Installation Script
# Author: Cracknic
# License: GNU GPL v3.0
#############################################################

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# Installation paths
INSTALL_DIR="/opt/userforge"
BIN_LINK="/usr/local/bin/userforge"
SCRIPT_NAME="userforge.py"

print_banner() {
    echo -e "${CYAN}"
    echo "██╗   ██╗███████╗███████╗██████╗ ███████╗ ██████╗ ██████╗  ██████╗ ███████╗"
    echo "██║   ██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝"
    echo "██║   ██║███████╗█████╗  ██████╔╝█████╗  ██║   ██║██████╔╝██║  ███╗█████╗  "
    echo "██║   ██║╚════██║██╔══╝  ██╔══██╗██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  "
    echo "╚██████╔╝███████║███████╗██║  ██║██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗"
    echo " ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝"
    echo -e "${NC}"
    echo -e "${BLUE}Version: 1.0 | Author: Cracknic${NC}"
    echo -e "${YELLOW}⚠  FOR AUTHORIZED PENETRATION TESTING ONLY ⚠${NC}"
    echo ""
}

# Check root
check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo -e "${RED}[ERROR]${NC} This script must be run as root (use sudo)"
        exit 1
    fi
}

# Check version
check_python() {
    echo -e "${BLUE}[INFO]${NC} Checking Python installation..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
        PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
        PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
        
        if [ "$PYTHON_MAJOR" -ge 3 ] && [ "$PYTHON_MINOR" -ge 6 ]; then
            echo -e "${GREEN}[OK]${NC} Python $PYTHON_VERSION found"
            PYTHON_CMD="python3"
            return 0
        fi
    fi
    
    echo -e "${RED}[ERROR]${NC} Python 3.6+ is required but not found"
    echo -e "${YELLOW}[INFO]${NC} Please install Python 3.6 or higher:"
    echo "  Ubuntu/Debian: sudo apt install python3"
    echo "  CentOS/RHEL:   sudo yum install python3"
    echo "  Fedora:        sudo dnf install python3"
    echo "  Arch:          sudo pacman -S python"
    exit 1
}

# Install UserForge
install_userforge() {
    print_banner
    check_root
    check_python
    
    echo ""
    echo -e "${CYAN}*============================================================${NC}"
    echo -e "${CYAN} INSTALLING USERFORGE${NC}"
    echo -e "${CYAN}*============================================================${NC}"
    echo ""
    
    # Installation directory
    echo -e "${BLUE}[INFO]${NC} Creating installation directory..."
    mkdir -p "$INSTALL_DIR"
    
    # Copy files
    echo -e "${BLUE}[INFO]${NC} Copying files to $INSTALL_DIR..."
    cp -r ./* "$INSTALL_DIR/"
    
    if [ -f "$INSTALL_DIR/$SCRIPT_NAME" ]; then
        chmod +x "$INSTALL_DIR/$SCRIPT_NAME"
    fi
    
    # Symbolic link
    echo -e "${BLUE}[INFO]${NC} Creating symbolic link..."
    ln -sf "$INSTALL_DIR/$SCRIPT_NAME" "$BIN_LINK"
    
    if [ -L "$BIN_LINK" ]; then
        chmod +x "$BIN_LINK" 2>/dev/null || true
    fi
    
    # Output directory
    echo -e "${BLUE}[INFO]${NC} Creating output directory..."
    mkdir -p "$HOME/UserForge_Output"
    
    # Verify
    echo ""
    echo -e "${BLUE}[INFO]${NC} Verifying installation..."
    
    if [ -f "$INSTALL_DIR/$SCRIPT_NAME" ] && [ -L "$BIN_LINK" ]; then
        echo -e "${GREEN}[SUCCESS]${NC} UserForge installed successfully!"
        echo ""
        echo -e "${CYAN}============================================================${NC}"
        echo -e "${GREEN}✓ INSTALLATION COMPLETE${NC}"
        echo -e "${CYAN}============================================================${NC}"
        echo ""
        echo -e "${BLUE}Installation Details:${NC}"
        echo -e "  • Installation directory: ${GREEN}$INSTALL_DIR${NC}"
        echo -e "  • Binary link: ${GREEN}$BIN_LINK${NC}"
        echo -e "  • Output directory: ${GREEN}$HOME/UserForge_Output${NC}"
        echo -e "  • Python: ${GREEN}$PYTHON_CMD ($PYTHON_VERSION)${NC}"
        echo ""
        echo -e "${BLUE}Usage:${NC}"
        echo -e "  ${GREEN}userforge -i names.txt${NC}"
        echo -e "  ${GREEN}userforge -h${NC} (for help)"
        echo ""
        echo -e "${BLUE}Documentation:${NC}"
        echo -e "  • README: ${GREEN}$INSTALL_DIR/README.md${NC}"
        echo -e "  • Manual (EN): ${GREEN}$INSTALL_DIR/docs/MANUAL_EN.md${NC}"
        echo -e "  • Manual (ES): ${GREEN}$INSTALL_DIR/docs/MANUAL_ES.md${NC}"
        echo ""
        echo -e "${YELLOW}To uninstall:${NC} sudo $0 --uninstall"
        echo ""
    else
        echo -e "${RED}[ERROR]${NC} Installation failed"
        exit 1
    fi
}

# Uninstall
uninstall_userforge() {
    print_banner
    check_root
    
    echo ""
    echo -e "${CYAN}============================================================${NC}"
    echo -e "${CYAN}UNINSTALLING USERFORGE${NC}"
    echo -e "${CYAN}============================================================${NC}"
    echo ""
    
    if [ ! -d "$INSTALL_DIR" ]; then
        echo -e "${YELLOW}[WARNING]${NC} UserForge is not installed"
        exit 0
    fi
    
    echo -e "${YELLOW}[WARNING]${NC} This will remove UserForge from your system"
    echo -e "${YELLOW}[WARNING]${NC} Output files in $HOME/UserForge_Output will NOT be deleted"
    echo ""
    read -p "Are you sure you want to uninstall? (y/N): " -n 1 -r
    echo ""
    
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${BLUE}[INFO]${NC} Uninstallation cancelled"
        exit 0
    fi
    
    echo -e "${BLUE}[INFO]${NC} Removing installation directory..."
    rm -rf "$INSTALL_DIR"
    
    echo -e "${BLUE}[INFO]${NC} Removing symbolic link..."
    rm -f "$BIN_LINK"
    
    # Verify uninstallation
    if [ ! -d "$INSTALL_DIR" ] && [ ! -L "$BIN_LINK" ]; then
        echo ""
        echo -e "${GREEN}[SUCCESS]${NC} UserForge uninstalled successfully!"
        echo ""
        echo -e "${BLUE}[INFO]${NC} Output files remain in: $HOME/UserForge_Output"
        echo -e "${BLUE}[INFO]${NC} To remove output files: rm -rf $HOME/UserForge_Output"
        echo ""
    else
        echo -e "${RED}[ERROR]${NC} Uninstallation failed"
        exit 1
    fi
}

# Usage
show_usage() {
    echo "Usage: $0 [OPTION]"
    echo ""
    echo "Options:"
    echo "  (no option)      Install UserForge"
    echo "  --uninstall      Uninstall UserForge"
    echo "  --help           Show this help message"
    echo ""
    echo "Examples:"
    echo "  sudo $0                    # Install"
    echo "  sudo $0 --uninstall        # Uninstall"
    echo ""
}

case "${1:-}" in
    --uninstall)
        uninstall_userforge
        ;;
    --help|-h)
        print_banner
        show_usage
        ;;
    "")
        install_userforge
        ;;
    *)
        echo -e "${RED}[ERROR]${NC} Unknown option: $1"
        echo ""
        show_usage
        exit 1
        ;;
esac

