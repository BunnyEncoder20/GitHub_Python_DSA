class Example:
    def __init__(self) -> None:
        self.counter = 0

    def recursiveFunc(self):
        self.counter += 1
        print(f"Recursion count: {self.counter}")

        # Base case / condition to stop recursion
        if self.counter == 5:
            return
        self.recursiveFunc()

    def printingNumbers1ToN(self, n):
        # base case
        if n == 0:
            return

        # go to the end first before printing anything
        # cause we want to print 1 to N
        self.printingNumbers1ToN(n - 1)

        print(n)

    def printingNumbersNto1(self, N):
        if N == 0:
            return
        print(N)
        self.printingNumbersNto1(N - 1)


if __name__ == "__main__":
    Example().recursiveFunc()
    Example().printingNumbers1ToN(5)
    Example().printingNumbersNto1(5)
