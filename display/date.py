from datetime import datetime

from configs.constants import DATE_TITLE


def show_current_date():
    """Display the current date in a formatted manner."""
    result = DATE_TITLE % datetime.now().strftime("%Y-%M-%d")
    print(result.center(80))
