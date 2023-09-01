class Numbers:
    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        factors = self.Factors()
        return sum(factors) == 2 * self.Value  

    def Factors(self):
        factors = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors.append(i)
        return factors

    def SumFactors(self):
        factors = self.Factors()
        return sum(factors)

def main():
    num1 = Numbers(7)
    print(f"Is {num1.Value} prime? {num1.ChkPrime()}")
    print(f"Is {num1.Value} perfect? {num1.ChkPerfect()}")
    print(f"Factors of {num1.Value}: {num1.Factors()}")
    print(f"Sum of factors of {num1.Value}: {num1.SumFactors()}")

    num2 = Numbers(28)
    print(f"Is {num2.Value} prime? {num2.ChkPrime()}")
    print(f"Is {num2.Value} perfect? {num2.ChkPerfect()}")
    print(f"Factors of {num2.Value}: {num2.Factors()}")
    print(f"Sum of factors of {num2.Value}: {num2.SumFactors()}")

if __name__ == "__main__":
    main()
