class Example:
    def builtin_operations(self, arr):
        # sorted(): returns you a sorted list, doesn't change the original list
        print(sorted(arr))  # normal sort
        print(sorted(arr, reverse=True))  # descending sort
        print(
            sorted(arr, key=lambda num: abs(num))
        )  # sorting using specific function/logic

        fruits = ["banana", "pineapple", "cherry", "date"]
        print(
            sorted(fruits, key=len)
        )  # NOTE: how the key is just the function with which we sort

        # NOTE: Some other functions which also can have custom keys: min, max
        print(max(fruits, key=len))

        # NOTE: some math funvtions:
        # sum : (also has start=what is the base starting value),
        # prod : same as the sum but multiplication

        # NOTE: for dealing with boolean arrays:
        # any: returns True if any of the values id True
        # all: reutrns True only if all the values of the array are True
        arr = [True, False, True, False]
        print(any(arr))
        print(all(arr))

    def collectionModule(self):
        def dequeExample():
            from collections import deque

            d = deque()
            d.append(1)
            d.append(2)
            d.appendleft(0)
            print(d)  # deque([0, 1, 2])

            d.pop()
            print(d)  # deque([0, 1])

            d.popleft()
            print(d)  # deque([1])


if __name__ == "__main__":
    instance = Example()

    instance.builtin_operations([5, 2, 9, 1, 5, 6])
    instance.collectionModule()
