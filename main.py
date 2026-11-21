import sqlite3
import sys
from rich.console import Console
from rich.table import Table

console = Console()

# Database setup
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        status TEXT DEFAULT 'Pending'
    )
""")
conn.commit()

def add_task(title):
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    console.print(f"[bold green]Task add ho gaya:[/bold green] {title}")

def list_tasks():
    cursor.execute("SELECT id, title, status FROM tasks")
    rows = cursor.fetchall()
    
    if not rows:
        console.print("[yellow]Abhi koi task nahi hai.[/yellow]")
        return

    table = Table(title="Mere Daily Tasks")
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Task", style="white")
    table.add_column("Status", style="green")

    for row in rows:
        table.add_row(str(row[0]), row[1], row[2])

    console.print(table)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        console.print("[bold red]Use:[/bold red] python main.py add 'Task ka naam'  YA  python main.py list")
    elif sys.argv[1] == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()
    else:
        console.print("[bold red]Galat command![/bold red] 'add' ya 'list' use kar.")
