class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        if b < 0:
            b = 0 - b
            a = 0 - a
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        if (a < 0 and b >= 0) or \
        (b < 0 and a >= 0):
            step = -1
            if b < 0:
                b = 0 - b
            else:
                a = 0 - a
        else:
            step = 1
        result = 0
        if a >= b:
            while a >= b:
                a = self.subtract(a, b)
                result += step
            return result
        else:
            while a <= b:
                a = self.subtract(a, b)
                result += step
            return result
    
    def modulo(self, a, b):
        n = self.divide(a, b)
        result = a - self.multiply(b, n)
        if result < 0:
            result = 0 - result
        return result

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, -3))
    print("Example: division: ", calc.divide(-10, -2))
    print("Example: modulo: ", calc.modulo(-10, 3))