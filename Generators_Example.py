#range function has some limitations as there is a start and there is an end
# better to use yield, on demand usage rather than instant or coolective use

def xrange():
    n=1
    while True:
        yield n
        n=n+1


# A generator in python makes use of the 'yield' keyword. A python iterator doesn't. ' \
# Python generator saves the states of the local variables every time 'yield' pauses the loop in python. ' \
# An iterator does not make use of local variables, all it needs is iterable to iterate on.
