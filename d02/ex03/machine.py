import beverages
import random


class CoffeeMachine:

    class EmptyCup(beverages.HotBeverage):
        def __init__(self) -> None:
            self.name = "empty cup"
            self.price = 0.90

        def Description(self) -> str:
            description = "An empty cup?! Gimme my money back!"
            return description

    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self) -> None:
        self.bronkenMachine = 10

    def repair(self) -> None:
        self.bronkenMachine = 10

    def server(self, cup: beverages.HotBeverage) -> beverages.HotBeverage():

        if self.bronkenMachine < 10:
            raise self.BrokenMachineException
        self.bronkenMachine -= 1

        if random.randint(0, 5) == 0:
            return CoffeeMachine.EmptyCup()
        return cup()


def test():
    coffee_machine = CoffeeMachine()
    for _ in range(23):
        try:
            print(coffee_machine.server(random.choice(
                [beverages.Coffee, beverages.Tea, beverages.Cappuccino, beverages.Chocolate])))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            coffee_machine.repair()


if __name__ == '__main__':
    test()

