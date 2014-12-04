import sys
import time
import threading

class progress_bar(threading.Thread):
     """Draw the dots, bar, or whatever"""

    def run(self):
        while stop != True:
            sys.stdout.write('.'),
            sys.stdout.flush()
            time.sleep(0.2)

        if kill == True:
            print '\b\b\b\b aborted by keystroke!',
        elif has_error == True:
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
        p = progress_bar()
        p.start()

        try:
            function(*args)
            stop = True
        except KeyboardInterrupt:
            kill = True
            stop = True
        except Exception as e:
            stop = True
            has_error = True
            time.sleep(1)
            print "\n" + str(e)

    return wrap_function





