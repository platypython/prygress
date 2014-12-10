import sys
import time
import threading
from functools import wraps

def progress(function):
    """Shows a progress bar while a function runs."""
    @wraps(function)
    def wrap_function(*args, **kwargs):
        stop = False

        def progress_bar():
            while not stop:
                sys.stdout.write('.')
                sys.stdout.flush()
                time.sleep(0.2)
            print '\b\b finished.',
        
        try:
            p = threading.Thread(target=progress_bar)
            p.start()
            return function(*args, **kwargs)
        finally:
            stop = True

    return wrap_function
