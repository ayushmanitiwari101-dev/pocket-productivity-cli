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



















import sqlite3
import sys
import time
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
    table.add_column("Status", style="bold")

    for row in rows:
        task_id, title, status = row
        status_display = f"[green]{status}[/green]" if status == "Done" else f"[yellow]{status}[/yellow]"
        table.add_row(str(task_id), title, status_display)

    console.print(table)

def mark_done(task_id):
    cursor.execute("UPDATE tasks SET status = 'Done' WHERE id = ?", (task_id,))
    conn.commit()
    if cursor.rowcount == 0:
        console.print(f"[bold red]ID {task_id} wala koi task nahi mila.[/bold red]")
    else:
        console.print(f"[bold green]Task #{task_id} Done mark ho gaya![/bold green]")

def focus_timer(minutes):
    seconds = minutes * 60
    console.print(f"[bold cyan]Focus session shuru: {minutes} minute[/bold cyan] (Rokne ke liye CTRL + C dabaa)")
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            console.print(f"\r[bold green]Bacha hua waqt: {mins:02d}:{secs:02d}[/bold green]", end="")
            time.sleep(1)
            seconds -= 1
        console.print("\n[bold green]Shabash! Focus session poora ho gaya![/bold green]")
    except KeyboardInterrupt:
        console.print("\n[yellow]Focus timer rok diya gaya.[/yellow]")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        console.print("[bold red]Use:[/bold red]")
        console.print("  python main.py add 'Task ka naam'")
        console.print("  python main.py list")
        console.print("  python main.py done <ID>")
        console.print("  python main.py focus <minutes>")
    elif sys.argv[1] == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "done" and len(sys.argv) > 2 and sys.argv[2].isdigit():
        mark_done(int(sys.argv[2]))
    elif sys.argv[1] == "focus" and len(sys.argv) > 2 and sys.argv[2].isdigit():
        focus_timer(int(sys.argv[2]))
    else:
        console.print("[bold red]Galat command ya argument![/bold red] Sahi syntax check kar.")
