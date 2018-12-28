base = 10


def multiply(number):
    return base * number


def add(number):
    return base + number


print(multiply(5))
print(add(7))

base = 13

print(multiply(5))
print(add(7))


class Calculator:
    def __init__(self, base):
        self.base = base

    def multiply_by(self, number):
        return self.base * number

    def add_to(self, number):
        return self.base + number


base_ten_calc = Calculator(base=10)
print(base_ten_calc.multiply_by(5))
print(base_ten_calc.add_to(7))

