class HotBeverage:
    price = 0.30
    name = "hot beverage"

    def __str__(self) -> str:
        template = ("name : {name}\n"
                    "price: {price:0.2f}\n"
                    "description: {description}")
        return template.format(name=self.name, price=self.price, description=self.Description())

    def Description(self) -> str:
        description = "Just some hot water in a cup"
        return description


class Coffee(HotBeverage):
    def __init__(self) -> None:
        self.name = "coffee"
        self.price = 0.40

    def Description(self) -> str:
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    def __init__(self) -> None:
        self.name = "tea"
        self.price = 0.30


class Chocolate(HotBeverage):
    def __init__(self) -> None:
        self.name = "chocolate"
        self.price = 0.50

    def Description(self) -> str:
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    def __init__(self) -> None:
        self.name = "cappuccino"
        self.price = 0.45

    def Description(self) -> str:
        return "Un po’ di Italia nella sua tazza!"


def test():
    print(HotBeverage())
    print(Coffee())
    print(Tea())
    print(Chocolate())
    print(Cappuccino())


if __name__ == "__main__":
    test()