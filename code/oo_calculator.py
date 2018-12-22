class Calculator:
    def __init__(self, base):
        self.base = base

    def multiply_by(self, value):
        return self.base * value


calc_ten = Calculator(base=10)
print(calc_ten.multiply_by(5))

calc_twelve = Calculator(base=12)
print(calc_twelve.multiply_by(10))
