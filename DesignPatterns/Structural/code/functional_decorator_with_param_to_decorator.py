import time
import math

def timeit(type_of_call):
	print(type_of_call)
	def inner(func):
		# the parameters to the func can be passed using *args, **kwargs as below.
		def wrapper(*args, **kwargs):
			start = time.time()
			result = func(*args, **kwargs)
			end = time.time()
			print(f"{func.__name__} took {(end - start) * 1000}ms")
			return result
		return wrapper
	return inner


@timeit("timing factorial")
def factorial(num):
	print("operation starts")
	time.sleep(1)
	result = math.factorial(num)
	print("operation ends")
	return result

res = factorial(10)
print(res)