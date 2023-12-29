[[Structural Design Patterns]]

### When to use ?
- When you want to transparently and dynamically ==**add responsibilities to objects without affecting other objects.**==
- When you want to add responsibilities to an object that you may want to change in future.
- Extending functionality by sub-classing is no longer practical.
- To Avoid class explosion
- When we want to add specific features over an object.
- If we anticipate the need to apply the same feature to multiple objects or reuse specific functionality across different parts of our application, decorators promote code reusability.
- Legacy code changes: The **Decorator** pattern can be applied to existing classes, even in legacy code, making it an excellent choice when we need to introduce new functionality without refactoring large portions of the codebase.
- **Separation of Concerns**: If we want to separate different concerns or aspects of an object’s functionality into distinct components for better organization and maintainability, the **Decorator** pattern helps achieve this separation.

### When not to use ?
1. **Static and Simple Behavior**: If an object’s behavior is simple and unlikely to change, and there is no need for dynamic extensions, using decorators might introduce unnecessary complexity.
2. **Performance Considerations**: Adding multiple decorators to an object can introduce a slight performance overhead due to the method delegation involved. If performance is a critical concern, we should evaluate the impact carefully.
3. **Complexity**: Overusing decorators can lead to a complex web of decorators, making the code harder to understand and maintain. In such cases, other design patterns or refactoring may be more appropriate.


### What it is ?

Decorator design pattern is **used to modify the functionality of an object at runtime**. At the same time other instances of the same class will not be affected by this, so individual object gets the modified behaviour.

- Follows [[Open Closed Principle]] and [[Single Responsibility Principle]]

### How it's coming in to the picture ?

We use ***inheritance*** or ***composition*** to extend the behaviour of an object but this is done at compile time and its **applicable to all the instances of the class**. We can’t add any new functionality of remove any existing behaviour at runtime – this is when Decorator pattern comes into picture.

### Motivation
- Want to augment an object with additional functionality
- Do not want to rewrite or alter the existing code. (Open Closed Principle)
- Want to keep the new functionality separate
- Need to be able to interact with existing structures
- Two Options:
	- Inherit
	- Decorator


### Structure

1. **Component**: Declares the common interface for both wrappers and the wrapped objects.
2. **Concrete Component:** Class of objects being wrapped. It defines the basic behaviour, which can be altered by decorators. 
3. **Concrete Decorators**: Defines extra behaviours that can be added to components dynamically. Concrete decorators override methods of Base Decorators and execute their behaviour either before or after calling the parent method. 
4. **Base Decorator**: It has a field for referencing a wrapped object. The field's type should be declared as the component interface. So it can contain both concrete components and decorators. The base decorator delegates all operations to the wrapped object. 
5. **Client**: It wrap components into multiple layers of decorators, as long as it works with all objects via the component interface. 

![[Pasted image 20231227193837.png]]


### Example 1 - Notifier

#### Problem Statement

Imagine that you’re working on a notification library which lets other programs notify their users about important events.

The initial version of the library was based on the `Notifier` class that had only a few fields, a constructor and a single `send` method. The method could accept a message argument from a client and send the message to a list of emails that were passed to the notifier via its constructor. A third-party app which acted as a client was supposed to create and configure the notifier object once, and then use it each time something important happened.

![[Pasted image 20231227190101.png]]

At some point, you realize that users of the library expect more than just email notifications. Many of them would like to receive an SMS about critical issues. Others would like to be notified on Facebook and, of course, the corporate users would love to get Slack notifications.

![[Pasted image 20231227190532.png]]

How hard can that be? You extended the `Notifier` class and put the additional notification methods into new subclasses. Now the client was supposed to instantiate the desired notification class and use it for all further notifications.

But then someone reasonably asked you, “Why can’t you use several notification types at once? If your house is on fire, you’d probably want to be informed through every channel.”

You tried to address that problem by creating special subclasses which combined several notification methods within one class. However, it quickly became apparent that this approach would bloat the code immensely, not only the library code but the client code as well.

![[Pasted image 20231227190627.png]]

#### Solution

Since using inheritance brings in many problems, we can use Aggregation/composition. Aggregation/composition is the key principle behind many design patterns, including [[Decorator Pattern]]

A _wrapper_ is an object that can be linked with some _target_ object. The wrapper contains the same set of methods as the target and delegates to it all requests it receives. However, the wrapper may alter the result by doing something either before or after it passes the request to the target.

![[Pasted image 20231227191441.png]]

In our notification example, Let's leave the simple email notification behaviour inside the base Notifier class, but turn all other notifier to a decorator. 

![[Pasted image 20231227192346.png]]


### Example 2 : 

![[Pasted image 20231226091959.png]]
Here we have the BasePizza class , which costs about 200 rs. Now if we want to add cheese or mushroom we can acheive the same using ToppingDecorator class
like below, 

```
BasePizza pizza = new Mushroom(new ExtraCheese(new FarmHousePizza()))
```


### Implementation in Python

#### Functional Decorator - No parameters

```python
import time


def timeit(func):
	def wrapper():
		start = time.time()
		result = func()
		end = time.time()
		print(f"{func.__name__} took {(end - start) * 1000}ms")
		return result
	return wrapper


@timeit
def some_op():
	print("operation starts")
	time.sleep(1)
	print("operation ends")

# some_op()
timeit(some_op)


```

#### Functional Decorator - With parameters

```python

import time
import math

def timeit(func):
	# the parameters to the func can be passed using *args, **kwargs as below.
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(f"{func.__name__} took {(end - start) * 1000}ms")
		return result
	return wrapper


@timeit
def factorial(num):
	print("operation starts")
	time.sleep(1)
	result = math.factorial(num)
	print("operation ends")
	return result

res = factorial(10)
print(res)

```


#### Functional Decorator - Parameter to the Decorator

```python
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

```

#### Functional Decorators - Stacking

Inner decorators will work first then the outer. 
Inner to outer.

```python
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

  

@double
@square
def some_op(num):
	return num


@square
@double
def some_op_2(num):
	return num

  

print(some_op(3))
print(some_op_2(3))
```

#### Class Decorator

```python
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

```

#### Class Decorator for Pizza 

```python
from abc import ABC

# Abstact class - Interface - Component
class BasePizza(ABC):
    def cost():
        pass

# Concrete Component
class FarmHousePizza(BasePizza):
    def cost(self):
        return 200

# Concrete Component
class MargheritaPizza(BasePizza):
    def cost(self):
        return 100

# Base Decorator
class ToppingDecorator(BasePizza):
    def cost():
        pass

# Concrete Decorator
class ExtraCheese(ToppingDecorator):

    def __init__(self, pizza: BasePizza):
        self.base_pizza = pizza
    
    def cost(self):
        return self.base_pizza.cost() + 10

class Mushroom(ToppingDecorator):

    def __init__(self, pizza: BasePizza):
        self.base_pizza = pizza
    
    def cost(self):
        return self.base_pizza.cost() + 20

farmhouse_pizza = FarmHousePizza()
final_pizza = Mushroom(farmhouse_pizza)

final_pizza = ExtraCheese(Mushroom(farmhouse_pizza))
print('Cost of final pizza', final_pizza.cost())

```


### Advantages
- It provides greater flexibility than static interfaces
- It enhances the extensibility of the object, because changes are made by coding new classes.
- It simplifies the coding by allowing you to develop a series of functionality from targeted classes instead of coding all of the behaviour into the object

### Disadvantages
- Overuse of decorators can lead to a complex nesting. 
- Increased number of classes
- Maintenance Overhead
- Performance Overhead - Due to method delegation
- Limited to interface inheritance - The **Decorator** pattern relies on interface inheritance, which means that it can only extend the behavior of objects through interfaces or abstract classes. It cannot add new data members to the original object.
- Limited support for removing decorators
- In some cases [[Composite]] or Strategy Design pattern might be more efficient. 

### Relations

[[Adapter]] [[Composite]] [[Structural Design Patterns]] 