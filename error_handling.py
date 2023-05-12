import sys
import traceback

def handle_exception(exc_type, exc_value, exc_traceback):
    """ This function handles all uncaught exceptions """
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    print("Uncaught exception:", exc_type, exc_value)
    print("Traceback:")
    traceback.print_tb(exc_traceback)

# Set the function to handle uncaught exceptions
sys.excepthook = handle_exception
