#!/bin/bash

# Quick start script for AI Interviewer Streamlit App

echo "🤖 AI Interviewer - Quick Start"
echo "================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo "📥 Installing dependencies..."
pip install -r requirements.txt

echo "✅ Setup complete!"
echo ""
echo "🚀 Starting Streamlit app..."
echo "The app will open in your browser automatically."
echo ""

streamlit run app.py
