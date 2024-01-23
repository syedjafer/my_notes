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
