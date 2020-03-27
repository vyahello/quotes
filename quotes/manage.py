"""Django's command-line utility for administrative tasks."""
import os
import sys

try:
    from django.core.management import execute_from_command_line
except ImportError as exception:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from exception


def __launch_management_tool() -> None:
    """Runs main manager management tool."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "manager.settings")
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    __launch_management_tool()
