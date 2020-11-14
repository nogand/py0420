class Decorator(object):
    """Simple decorator class."""
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        print('Before the function call.')
        res = self.func(*args, **kwargs)
        print('After the function call.')
        return res

@Decorator
def testfunc():
    print('Inside the function.')

@Decorator
def otrafunc(a, b):
    print('A la grande le puse cuca')
    return a+b
    
testfunc()
# Before the function call.
# Inside the function.
# After the function call.

print(otrafunc(2, 3))