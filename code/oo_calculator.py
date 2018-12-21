class Calculator:
    def __init__(self, base):
        self.base = base

    def multiply(self, value):
        return self.base * value


calc_ten = Calculator(10)
print(calc_ten.multiply(5))

calc_twelve = Calculator(12)
print(calc_twelve.multiply(10))
