import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_sql(question, schema):

    prompt = f"""
You are an expert MySQL SQL generator.

Convert the user's question into a valid MySQL query.

Database Schema:

{schema}

User Question:
{question}

Rules:
1. Generate ONLY the SQL query.
2. Do NOT explain anything.
3. Do NOT add markdown.
4. Use only the tables and columns from the schema.
5. Do NOT generate DROP, DELETE, UPDATE, INSERT, ALTER, or TRUNCATE statements.
6. Generate only SELECT queries.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # Get SQL text from Gemini
    sql = response.text

    # Remove Markdown formatting if present
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql