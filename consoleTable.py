from tabulate import tabulate # type: ignore

people = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "David", "age": 28, "city": "Houston"},
    {"name": "Eve", "age": 22, "city": "Phoenix"}
]

print(tabulate(people, headers="keys", tablefmt="grid"))