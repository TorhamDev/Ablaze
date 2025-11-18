from configs.constants import PROGRESS
from handlers.tasks import get_tasks


def show_progress(tasks_count: int, completed_count: int):
    """Display the progress of tasks that completed and tasks that are not completed by percentage."""  # noqa: E501
    completed = f"{(completed_count / tasks_count) * 100:.0f}%"
    not_completed = f"{((tasks_count - completed_count) / tasks_count) * 100:.0f}%"
    progress_message = PROGRESS % (completed, not_completed)
    print(progress_message)


def show_today_tasks():
    """Display today's tasks."""

    print("───────────────────────────────")
    todays_tasks = get_tasks(only_today=True)
    for idx, task in enumerate(todays_tasks, start=1):
        task_title = task[1]
        is_completed = task[3]
        status = "✅" if is_completed else "[❔]"
        print(f"{idx}. {task_title} {status}")
