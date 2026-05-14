# Simple Calendar Display

A clean, minimalist digital signage solution designed for Raspberry Pi. This project fetches events from a Google Calendar (iCal) and displays the next upcoming event with a beautiful, high-readability interface. The repo runs locally and the index.html file is added as an asset in Anthias.

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features
* **Automated Sync**: Background Python script fetches iCal data every 5 minutes.
* **Robust Architecture**: Saves data as a JS variable to bypass browser CORS and local file restrictions.
* **Modern UI**: High-legibility design optimized for digital signage screens.
* **Auto-Clock**: Real-time digital clock with localized date formatting.
* **Self-Healing**: Automatically reloads to ensure the data is always fresh.

## 🛠 Tech Stack
* **Backend**: Python 3 (with `icalevents`)
* **Frontend**: HTML5, CSS3, Vanilla JavaScript
* **Environment**: Raspberry Pi (Tested on Anthias/Screenly)

## 🚀 Installation

### 1. Clone the repository
\`\`\`bash
git clone https://github.com/sm7urw/simple-calendar-display.git
cd simple-calendar-display
\`\`\`

### 2. Run the Installer
The included script will install system dependencies, setup the Python virtual environment, and configure permissions:
\`\`\`bash
chmod +x install_calendar.sh
./install_calendar.sh
\`\`\`

### 3. Configuration
Open \`update_calendar.py\` and replace the \`ICAL_URL\` with your private Google Calendar iCal link:
\`\`\`bash
nano update_calendar.py
\`\`\`

## 📅 Automation (Cron)
The installation script automatically adds a cronjob to update the calendar every 5 minutes. If you need to add it manually, use:
\`\`\`text
*/5 * * * * cd $HOME/simple-calendar-display && ./venv/bin/python update_calendar.py
\`\`\`

## 🖥 Display Setup
Point your signage player or browser to the Raspberry Pi's IP address on port \`8080\`. 

If using **Anthias**, simply add the local URL as a "Web Asset".

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
EOF
