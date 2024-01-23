def square(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return wrapper

def double(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

# @double
# @square
# def some_op(num):
#     return num

@square
@double
def some_op_2(num):
    return num

# print(some_op(3))
print(some_op_2(3))