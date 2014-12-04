import sys
import time
import threading

class ProgressBar(threading.Thread):
    """Draw the dots, bar, or whatever"""
    def run(self):
        while not stop:
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(0.2)

        print '\b\b finished.',


def progress(function):
    """Shows a progress bar while a function runs."""
    def wrap_function(*args):
        global stop
        stop = False
        p = ProgressBar()
        p.start()

        try:
            ran = function(*args)
        except:
            raise
        finally:
            stop = True

        return ran

    return wrap_function
