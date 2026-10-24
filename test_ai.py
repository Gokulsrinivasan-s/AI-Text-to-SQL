from schema import get_schema
from gemini_sql import generate_sql


schema = get_schema()


question = "Show employees in Sales department"


sql = generate_sql(question, schema)


print(sql)