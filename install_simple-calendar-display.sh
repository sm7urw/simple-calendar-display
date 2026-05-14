#!/bin/bash

# --- CONFIGURATION ---
REPO_URL="https://github.com/sm7urw/simple-calendar-display.git"
# Dynamically get the directory where the script is being run
PROJECT_DIR="$(pwd)"

echo "🚀 Starting Simple Calendar Display installation..."

# 1. Update system and install dependencies
echo "📦 Updating system packages..."
sudo apt update && sudo apt install -y git python3 python3-pip python3-venv apache2

# 2. Sync code from GitHub
if [ -d ".git" ]; then
    echo "📂 Local Git repo detected. Pulling latest changes..."
    git pull
else
    echo "🌐 Cloning project from GitHub..."
    # If we are not already in a git repo, clone it into a folder
    git clone "$REPO_URL" simple-calendar-display
    cd simple-calendar-display
    PROJECT_DIR="$(pwd)"
fi

# 3. Setup Virtual Environment (venv)
echo "🐍 Setting up Python venv..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

if [ -f "requirements.txt" ]; then
    echo "📥 Installing Python dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "⚠️ requirements.txt not found, installing icalevents manually..."
    pip install icalevents
fi

# 4. Permissions
echo "🔐 Setting script permissions..."
chmod +x update_calendar.py

# 5. Automation (Cron)
echo "⏰ Setting up automation (Cron)..."
# This checks if the cronjob already exists to avoid duplicates
CRON_JOB="*/5 * * * * cd $PROJECT_DIR && $PROJECT_DIR/venv/bin/python $PROJECT_DIR/update_calendar.py"
(crontab -l 2>/dev/null | grep -Fv "$PROJECT_DIR/update_calendar.py"; echo "$CRON_JOB") | crontab -

echo "-------------------------------------------------------"
echo "✅ Installation Complete!"
echo "📍 Location: $PROJECT_DIR"
echo "🕒 Cronjob: Set to run every 5 minutes."
echo "👉 Next step: Update ICAL_URL in update_calendar.py"
echo "-------------------------------------------------------"
