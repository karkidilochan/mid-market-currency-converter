import os


def run_migrations():
    output = os.system("cd src/db/ && alembic upgrade head")
    print(output)
