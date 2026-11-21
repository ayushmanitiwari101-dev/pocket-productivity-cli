# Pocket Productivity CLI

A lightweight Python command-line productivity tool built in Termux using **SQLite** and **Rich** to manage daily tasks, track completion stats, and run focus sessions.

## Features
- Add tasks (`add`)
- View tasks in a formatted terminal table (`list`)
- Mark tasks as completed (`done`)
- Delete tasks by ID (`delete`)
- View task completion statistics (`stats`)
- Built-in focus countdown timer (`focus`)
- Local SQLite storage (`tasks.db` ignored via `.gitignore`)

## Setup & Usage
```bash
pip install rich
python main.py add "Study History"
python main.py list
python main.py done 1
python main.py delete 1
python main.py stats
python main.py focus 25


