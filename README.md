prygress
=======
A threaded progress decorator for python functions.

Give yourself something to watch while your long calls are made. Add the '@progress' decorator to your functions, thats it!

Install it with pip
    pip install prygress

example

    from prygress import progress
    from time import sleep
    
    @progress
    def wait_with_me():
	    sleep(10)
	
	wait_with_me()
    ................................................ finished.

To customize your bar, just add one or all of these params to the decorator:

    @progress(char='.', pause=0.2)

> Written with [StackEdit](https://stackedit.io/).
