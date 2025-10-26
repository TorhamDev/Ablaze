import duckdb

# creating a connection to duckdb file database
conn = duckdb.connect("database.db")

# creating tables if they do not exist

# creating sequences
conn.execute("""
CREATE SEQUENCE IF NOT EXISTS task_id_seq START 1
""")
conn.execute("""
CREATE SEQUENCE IF NOT EXISTS days_log_id_seq START 1
""")

# creating tasks table
conn.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY DEFAULT NEXTVAL('task_id_seq'),
    title TEXT NOT NULL
)
""")

# creating days_log table
conn.execute("""
CREATE TABLE IF NOT EXISTS days_log (
    id INTEGER PRIMARY KEY DEFAULT NEXTVAL('days_log_id_seq'),
    date DATE NOT NULL,
    completed_tasks INTEGER NOT NULL,
    uncompleted_tasks INTEGER NOT NULL,
    tasks JSON NOT NULL
)
""")


# commit table creations and pass the connection object to be used elsewhere
conn.commit()


def get_connection():
    return conn
