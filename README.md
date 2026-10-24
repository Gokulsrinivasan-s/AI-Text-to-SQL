# 🤖 AI Text-to-SQL using Gemini & MySQL

## Overview

This project converts natural language questions into SQL queries using Google's Gemini AI and executes them on a MySQL database.

## Features

- Natural Language to SQL
- Automatic Database Schema Reading
- MySQL Integration
- AI-generated SQL
- SQL Execution
- Table-formatted Results

## Technologies

- Python
- MySQL
- Google Gemini
- mysql-connector-python
- python-dotenv
- tabulate

## Project Structure

```
NLP_to_SQL/
│
├── database.py
├── schema.py
├── gemini_sql.py
├── execute_sql.py
├── main.py
├── requirements.txt
└── README.md
```

## Example

Question:

```
Show employees in Sales department
```

Generated SQL:

```sql
SELECT *
FROM employees
WHERE Department = 'Sales';
```

## Future Improvements

- FastAPI Web App
- Chat Interface
- Data Visualization
- Export to CSV/Excel
- SQL Validation