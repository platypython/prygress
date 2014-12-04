import sys
import time
import threading

class progress_bar(threading.Thread):
    """Draw the dots, bar, or whatever"""

    def run(self):
        while stop != True:
            sys.stdout.write('\b.')
            sys.stdout.flush()
            time.sleep(0.5)

        if kill == True:
            print '\b\b\b\b ERROR!',
        else:
            print '\b\b finished.',

def progress(function):
    """Shows a progress bar while a function runs."""

    def wrap_function(*args):
        global stop
        global kill
        kill = False
        stop = False
        p = progress_bar()
        p.start()

        try:
            function(*args)
            stop = True
        except Exception,e:
            kill = True
            stop = True
            time.sleep(1)
            print "\n" + str(e)

    return wrap_function





