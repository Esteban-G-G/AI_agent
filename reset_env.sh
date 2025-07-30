#!/bin/bash

echo "🔍 Checking system architecture..."

ARCH=$(uname -m)

if [[ "$ARCH" == "arm64" ]]; then
  echo "❌ You are currently running a terminal in ARM64 mode."
  echo "💡 Boot.dev likely expects x86_64 architecture."
  echo "👉 Please do this first:"
  echo "   1. Open Finder and go to /Applications > Utilities."
  echo "   2. Right-click on 'Terminal.app' > Get Info."
  echo "   3. Check 'Open using Rosetta'."
  echo "   4. Open that Terminal and run this script again."
  exit 1
else
  echo "✅ Terminal is running under x86_64 (Rosetta) mode."
fi

echo "🧹 Removing existing virtual environment..."
rm -rf venv

echo "🐍 Creating new virtual environment..."
python3 -m venv venv

echo "✅ Activating virtual environment..."
source venv/bin/activate

echo "⬆️ Upgrading pip, setuptools, and wheel..."
pip install --upgrade pip setuptools wheel

echo "📦 Installing dependencies with architecture-safe builds..."
pip install --no-binary=:all: -r requirements.txt

echo "✅ Environment setup complete!"
echo "👉 Run your script using: source venv/bin/activate && python main.py"
