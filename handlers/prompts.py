import sys
from datetime import datetime

from handlers.tasks import (
    create_task,
    delete_task_by_display_id,
    edit_task_by_display_id,
    update_task_status_by_display_id,
)


def handle_prompts(prompt: str) -> None:
    """Handle user prompts and display available commands."""
    from configs.constants import PROMPTS

    params = prompt.split(" ", 1)[1:]
    prompt = prompt.lower().split(" ")[0]

    if prompt in ["help", "h", "?"]:
        # TODO: needs a more detailed help page
        print(PROMPTS)

    elif prompt in ["exit", "quit", "q"]:
        print("Exiting the application. Goodbye!")
        sys.exit(0)

    elif prompt in ["a", "add"]:
        if not len(params):
            print("Please provide a task title after the 'ADD/A' command.")
            input("Press Enter to continue...")
        else:
            create_task(params[0], date=datetime.now().date())

    elif prompt in ["r", "remove", "d", "delete"]:
        if len(params) != 1:
            print(
                "Please provide the task number to delete after the 'REMOVE/R/DELETE/D' command."  # noqa: E501
            )  # noqa: E501
            input("Press Enter to continue...")
        else:
            try:
                display_id = int(params[0])
                delete_task_by_display_id(display_id)
            except ValueError:
                print("Invalid task number. Please provide a valid task number.")
                input("Press Enter to continue...")

    elif prompt in ["e", "edit"]:
        params = params[0].split(" ", 1)
        if len(params) != 2:
            print(
                "Please provide the task number and new title after the 'EDIT/E' command."  # noqa: E501
            )
            input("Press Enter to continue...")
        else:
            try:
                display_id = int(params[0])
                edit_task_by_display_id(display_id, params[1])
            except ValueError:
                print("Invalid task number. Please provide a valid task number.")
                input("Press Enter to continue...")

    elif prompt in ["t", "toggle"]:
        if len(params) != 1:
            print(
                "Please provide the task number to toggle after the 'TOGGLE/T' command."  # noqa: E501
            )
            input("Press Enter to continue...")
        else:
            try:
                display_id = int(params[0])
                update_task_status_by_display_id(display_id)
            except ValueError:
                print("Invalid task number. Please provide a valid task number.")
                input("Press Enter to continue...")
