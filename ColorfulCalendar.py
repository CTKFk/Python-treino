import calendar
from rich.console import Console # type: ignore
from rich.table import Table # type: ignore

def colourful_calendar(year):
    console = Console()
    months = [calendar.monthcalendar(year, month) for month in range(1, 13)] 

    for month in range(12):
        month_name = calendar.month_name[month + 1]
    
        table = Table(title=f"[bold cyan]{month_name} \\ {year}[/bold cyan]", show_lines=True)
        table.add_column("Dom", style="red", width=4)
        table.add_column("Seg", style="yellow", width=4)
        table.add_column("Ter", style="green", width=4)
        table.add_column("Qua", style="blue", width=4)
        table.add_column("Qui", style="magenta", width=4)
        table.add_column("Sex", style="cyan", width=4)
        table.add_column("Sab", style="white", width=4)
    
        for week in months[month]:
            table.add_row(
                *(str(day).rjust(2) if day != 0 else "  " for day in week)
            )
        console.print(table)
        console.print(table)
colourful_calendar(2025)
        