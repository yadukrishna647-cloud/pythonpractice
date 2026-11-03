class staff:
    def __init__(self,name,shift):
        self.name=name
        self.shift=shift

    def start_work(self):
        print(f"{self.name} is starting work on {self.shift} shift.")
    def work(sself):
        print(f"{self.name} is working")
class waiter(staff):
    def take_order(self):
        print(f"{self.name} is taking an order.")

    def work(self):
        print(f"{self.name} is taking order")
class chef(staff):
    def cook_food(self):
        print(f"{self.name} is cooking food.")
    def work(self):
        print(f"{self.name} is cooking food.")
    

raj=waiter("Raj","morning")
amit = chef("Amit","evening")
amit.work()
raj.work()