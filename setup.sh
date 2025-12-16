#!/bin/bash

# Music21 Wrapper Setup Script for macOS
# This script sets up everything needed to run the music composition project

set -e  # Exit on any error

echo "🎵 Music21 Wrapper Setup"
echo "========================"
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if Python 3 is installed
echo "Checking for Python 3..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 is not installed!${NC}"
    echo "Please install Python 3 from https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo -e "${GREEN}✅ Found: $PYTHON_VERSION${NC}"
echo ""

# Check if we're in the right directory
if [ ! -f "wrapper.py" ]; then
    echo -e "${RED}❌ Error: wrapper.py not found!${NC}"
    echo "Please run this script from the project directory."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo -e "${GREEN}✅ Virtual environment created${NC}"
else
    echo -e "${YELLOW}⚠️  Virtual environment already exists, skipping...${NC}"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo -e "${GREEN}✅ Virtual environment activated${NC}"
echo ""

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip --quiet
echo -e "${GREEN}✅ pip upgraded${NC}"
echo ""

# Install music21 and dependencies
echo "Installing music21 and dependencies..."
echo "This may take a minute..."
pip install music21 --quiet
echo -e "${GREEN}✅ music21 installed${NC}"
echo ""

# Verify installation
echo "Verifying installation..."
python3 -c "from music21 import stream, note, tempo, meter, instrument; print('✅ music21 imports successfully')" 2>/dev/null
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Installation verified!${NC}"
else
    echo -e "${RED}❌ Installation verification failed${NC}"
    exit 1
fi
echo ""

# Make test.py executable (optional, but nice)
chmod +x test.py 2>/dev/null || true

echo "========================"
echo -e "${GREEN}🎉 Setup complete!${NC}"
echo ""
echo "To use the project:"
echo "  1. Activate the virtual environment:"
echo "     ${YELLOW}source venv/bin/activate${NC}"
echo ""
echo "  2. Run the example:"
echo "     ${YELLOW}python test.py${NC}"
echo ""
echo "  3. Or use the wrapper in your own scripts:"
echo "     ${YELLOW}from wrapper import *${NC}"
echo ""
echo "The music will open in GarageBand (or your default MIDI player)!"
echo ""

