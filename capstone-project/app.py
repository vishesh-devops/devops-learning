import os
import time
import psycopg2

# Get env vars
name = os.environ.get("USER_NAME", "Guest")
task = os.environ.get("TASK", "No task set")

# Wait for Postgres to be ready
time.sleep(5)

# Connect to Postgres
conn = psycopg2.connect(
    host=os.environ.get("DB_HOST", "db"),
    database=os.environ.get("DB_NAME", "tasksdb"),
    user=os.environ.get("DB_USER", "postgres"),
    password=os.environ.get("DB_PASSWORD", "postgres")
)

cur = conn.cursor()

# Create table if not exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        task VARCHAR(255)
    )
""")

# Insert task
cur.execute("INSERT INTO tasks (name, task) VALUES (%s, %s)", (name, task))
conn.commit()

# Read all tasks
cur.execute("SELECT id, name, task FROM tasks")
rows = cur.fetchall()

print(f"Task saved for {name}: {task}")
print("\nAll saved tasks:")
for row in rows:
    print(f"  [{row[0]}] {row[1]}: {row[2]}")

cur.close()
conn.close()
