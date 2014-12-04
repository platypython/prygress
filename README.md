prygress
=======
A threaded progress decorator for python functions.

Give yourself something to watch while your long calls are made. Add the '@progress' decorator to your functions, thats it!

    from prygress import progress
    from time import sleep
    
    @progress
    def wait_with_me():
	    sleep(10)
	
	wait_with_me()
    ................................................ finished.

I'm sure there are bugs, do me a **HUGE** favor and report them!

> Written with [StackEdit](https://stackedit.io/).
