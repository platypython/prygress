import sys
import time
import threading
from functools import wraps

def progress(function=None, stream=sys.stdout, char='.', pause=0.2):
    """Shows a progress bar while a function runs."""
    if function is None:
        return lambda func: progress(func, stream, char, pause)

    @wraps(function)
    def wrap_function(*args, **kwargs):
        stop = False

        def progress_bar():
            while not stop:
                stream.write(char)
                stream.flush()
                time.sleep(pause)
            stream.write('\b\b finished.')
            stream.flush()
        
        try:
            p = threading.Thread(target=progress_bar)
            p.start()
            return function(*args, **kwargs)
        finally:
            stop = True

    return wrap_function
