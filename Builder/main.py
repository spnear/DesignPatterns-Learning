from cook import Cook
from pizza_builder import MargheritaBuilder

cook = Cook()
margheritha_builder = MargheritaBuilder()

pizza = cook.make_pizza(margheritha_builder)
print(pizza)