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

class MargheritaPizzaWithExraOnion(BasePizza):
    def cost(self):
        return 140

pizza = MargheritaPizzaWithExraOnion()
print("Pizza cost is ", pizza.cost())
