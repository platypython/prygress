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

        if kill:
            print '\b\b\b\b aborted by keystroke!',
        elif has_error:
            print '\b\b\b\b program error...'
        else:
            print '\b\b finished.',


def progress(function):
    """Shows a progress bar while a function runs."""
    def wrap_function(*args):
        global stop
        global kill
        global has_error
        has_error = False
        kill = False
        stop = False
        p = ProgressBar()
        p.start()

        try:
            ran = function(*args)
            stop = True
        except KeyboardInterrupt:
            kill = True
            stop = True
        except Exception as e:
            stop = True
            has_error = True
            time.sleep(1)
            print
            print e

        return ran

    return wrap_function
