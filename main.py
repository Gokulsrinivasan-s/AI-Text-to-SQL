from schema import get_schema
from gemini_sql import generate_sql
from execute_sql import execute_sql
from tabulate import tabulate

question = input("Ask a question: ")

schema = get_schema()

sql = generate_sql(question, schema)

print("\nGenerated SQL:")
print(sql)

rows, columns = execute_sql(sql)

print("\nResults:\n")

print(tabulate(rows, headers=columns, tablefmt="grid"))