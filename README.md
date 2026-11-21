# Pocket Productivity CLI

A lightweight Python command-line productivity tool built in Termux using **SQLite** and **Rich** to manage daily tasks and focus sessions.

## Features
- Add tasks (`add`)
- View tasks in a formatted terminal table (`list`)
- Mark tasks as completed (`done`)
- Built-in focus countdown timer (`focus`)
- Local SQLite storage (`tasks.db` ignored via `.gitignore`)

## Setup & Usage
```bash
pip install rich
python main.py add "Study History"
python main.py list
python main.py done 1
python main.py focus 25

