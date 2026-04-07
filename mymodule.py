def myrange(start=None,stop=None,step=1):
    current = start
    while current < stop:
        yield current
        current += step
def incrementer(start=0):
    current = start
    while True:
        yield current
        current += 1