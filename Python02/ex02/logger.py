import time
from random import randint
import os
#... your definition of log decorator...

def log(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter() - start
        with open("machine.log", "a") as f:
            user = os.getenv('USER', "unknown")
            name = func.__name__.replace('_', ' ').title()
            if end > 0.001:
                f.write(f"({user}) Running: {name:18} [ exec-time = {end:.3f} s  ]\n")
            else:
                f.write(f"({user}) Running: {name:18} [ exec-time = {end * 1000:.3f} ms ]\n")
        return result
    return wrapper


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
 
    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)