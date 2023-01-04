

def mydecorater(function):
    def wrapper():
        print("I am decorating your function")
        function()
    return wrapper

@mydecorater
def hello_world():
    print("Hello World")

hello_world()

#Older way of doing things
#y=mydecorater(hello_world)
#y()

#########################################################################################

# what to do when you have parameters

def mydecorater(function):
    def wrapper(*args,**kwargs):
        print("I am decorating your function")
        return function(*args,**kwargs)
    return wrapper

@mydecorater
def hello(person):
    return f"Hello {person}"

print(hello("mike"))

##############################################################################################

# if your original function is returning something as well, then that needs to be returned as well from wrapper
# as we might need to catch in a cvariable associated with the caller

def mydecorater(function):
    def wrapper(*args,**kwargs):
        return_value = function(*args,**kwargs)
        print("I am decorating your function")
        return return_value
    return wrapper

@mydecorater
def hello(person):
    return f"Hello {person}"

print(hello("mike"))
