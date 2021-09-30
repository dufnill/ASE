import calculator as c

class FooCalculator:
    def __init__(self):
        pass

    def sum(self, m, n):
        return c.sum(m,n)

    def divide(self, m, n):
        return c.divide(m,n)

if __name__ == '__main__':
    f = FooCalculator()
    a=input("Insert first number\n")
    b=input("Insert second number\n")
    print("Summation: ", f.sum(a,b))
    print("Division: ", f.divide(a,b))