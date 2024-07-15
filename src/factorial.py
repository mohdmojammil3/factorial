class Factorial:
    def __init__(self, number):
        self.number = number

    def calculate(self):
        if self.number < 0:
            return "Factorial is not defined for negative numbers"
        elif self.number == 0 or self.number == 1:
            return 1
        else:
            result = 1
            for i in range(2, self.number + 1):
                result *= i
            return result