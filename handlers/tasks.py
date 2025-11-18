from datetime import date

from database.db import conn


def get_tasks(only_today: bool = False, status: bool | None = None):
    """
    Fetch tasks from the database. If only_today is True, fetch only today's tasks.

    params:
        only_today: Whether to fetch only today's tasks.
        status: If None fetch all tasks. If True, fetch only completed tasks.
                            If False, fetch only incomplete tasks.
    returns:
        list: A list of tasks matching the criteria.
    """

    cursor = conn.cursor()
    if only_today:
        query = "SELECT * FROM tasks WHERE created_at = CURRENT_DATE"
    else:
        query = "SELECT * FROM tasks"

    # return all if status none otherwise filter by status
    if status is None:
        cursor.execute(query)
    else:
        query += " AND is_completed = ?"
        cursor.execute(query, (status,))
    return cursor.fetchall()


def create_task(title: str, date: date):
    """
    Create a new task with the given title and date.
    """
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, created_at, is_completed) VALUES (?, ?, ?)",
        (title, date, False),
    )
    conn.commit()


def delete_task_by_display_id(display_id: int):
    """
    Delete a task by its display ID (1-based index for today's tasks).
    """

    todays_tasks = get_tasks(only_today=True)
    tasks_map = {idx: task for idx, task in enumerate(todays_tasks, start=1)}

    if display_id not in tasks_map:
        raise ValueError

    task_id = tasks_map[display_id][0]
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()


def edit_task_by_display_id(display_id: int, new_title: str):
    """
    Edit a task's title by its display ID (1-based index for today's tasks).
    """

    todays_tasks = get_tasks(only_today=True)
    tasks_map = {idx: task for idx, task in enumerate(todays_tasks, start=1)}

    if display_id not in tasks_map:
        raise ValueError

    task_id = tasks_map[display_id][0]
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (new_title, task_id))
    conn.commit()


def update_task_status_by_display_id(display_id: int):
    """
    Update a task's completion status by its display ID (1-based index for today's tasks).
    if its none its marked as completed else its marked as incomplete.
    """  # noqa: E501
    todays_tasks = get_tasks(only_today=True)
    tasks_map = {idx: task for idx, task in enumerate(todays_tasks, start=1)}

    if display_id not in tasks_map:
        raise ValueError

    task_id = tasks_map[display_id][0]
    current_status = tasks_map[display_id][3]
    new_status = not current_status  # Toggle status

    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET is_completed = ? WHERE id = ?", (new_status, task_id)
    )
    conn.commit()
