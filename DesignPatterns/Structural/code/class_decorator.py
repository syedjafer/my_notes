class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # Code to be executed before the decorated function is called
        print("Decorator setup")

        # Call the decorated function
        result = self.func(*args, **kwargs)

        # Code to be executed after the decorated function is called
        print("Decorator cleanup")

        return result

@MyDecorator
def my_function():
    print("Inside the decorated function")

# Call the decorated function
my_function()
