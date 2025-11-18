import sys
from datetime import datetime

from display.date import show_current_date
from display.prompts import show_prompts
from display.tasks import show_progress, show_today_tasks
from handlers.prompts import handle_prompts
from handlers.tasks import create_task, get_tasks


def main():
    """Main function to run the daily tracker application."""
    show_current_date()
    tasks = get_tasks(only_today=True)

    if not tasks:
        print("\n\t Oops! No tasks found for today. Wanna add some?")
        title = input("> ")
        create_task(title, date=datetime.now().date())
        return

    show_progress(
        tasks_count=len(get_tasks(only_today=True)),
        completed_count=len(get_tasks(only_today=True, status=True)),
    )
    show_today_tasks()
    show_prompts()

    user_prompt = input("\n>")
    handle_prompts(user_prompt)


if __name__ == "__main__":
    try:
        while True:
            # clear terminal screen
            print("\033c", end="")

            main()
    except KeyboardInterrupt:
        print("\n\n Okay!, next time use Q prompt! 😒")
        sys.exit(0)
