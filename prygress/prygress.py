import sys
import time
import threading

def progress(function):
    """Shows a progress bar while a function runs."""
    def wrap_function(*args):
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
            return function(*args)
        finally:
            stop = True
            # p.join()

    return wrap_function
