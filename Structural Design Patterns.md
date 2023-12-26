Its a way to combine or arrange different classes and objects to form a complex or bigger structure to solve a particular requirement. 

Types:
1. Decorator
2. Proxy
3. Composite
4. Adapter
5. Bridge
6. Facade
7. Flyweight

**Decorator Pattern**
This helps to add more functionality to existing object, without changing its structure. 
![[Pasted image 20231226091959.png]]
Here we have the BasePizza class , which costs about 200 rs. Now if we want to add cheese or mushroom we can acheive the same using ToppingDecorator class
like below, 

```
BasePizza pizza = new Mushroom(new ExtraCheese(new FarmHousePizza()))
```


**Proxy Pattern**

This pattern helps to provide control access to **original object.** 

![[Pasted image 20231226110053.png]]

**Composite Pattern**

This helps in scenarios where we have OBJECT inside OBJECT (tree like structure)

![[Pasted image 20231226110835.png]]

![[Pasted image 20231226110854.png]]


Bridge Pattern

Facade Pattern: Hides the complexity. 
