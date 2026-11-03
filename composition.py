class chef:
    def cook_food(self,dish):
        print(f"chef is cooking {dish}.")
class waiter:
    def __init__(self,name,chef):
        self.name = name
        self.chef = chef
    def take_order(self,dish):
        print(f"{self.name} is taking an order for {dish}.")
        self.chef.cook_food(dish)

amit = chef()
raj = waiter("Raj", amit)
raj.take_order("pasta")