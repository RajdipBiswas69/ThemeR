#!/bin/bash

echo "=============================="
echo "  Installing ThemeR Tool"
echo "  Made by Rajdip ❤️"
echo "=============================="

# Check root
if [ "$EUID" -ne 0 ]; then
  echo "❌ Please run as root (use sudo)"
  exit
fi

# Check python3
if ! command -v python3 >/dev/null 2>&1; then
  echo "❌ Python3 not found. Installing..."
  apt update && apt install python3 -y
fi

# Copy tool
if [ -f "themer.py" ]; then
    cp themer.py /usr/local/bin/themer
elif [ -f "themer" ]; then
    cp themer /usr/local/bin/themer
else
    echo "❌ Tool file not found!"
    exit 1
fi
chmod +x /usr/local/bin/themer

echo "✅ ThemeR installed successfully!"
echo "👉 Run: themer"

