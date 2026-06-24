import os

name = os.environ.get("USER_NAME","Guest")
task = os.environ.get("TASK","No task set")

log_entry = f"{name} added task: {task}\n"

with open("/data/tasks.log", "a") as f:
    f.write(log_entry)

print(f"Task saved for {name}: {task}")

with open("/data/tasks.log", "r") as f:
    print("\nAll saved tasks:")
    print(f.read())

