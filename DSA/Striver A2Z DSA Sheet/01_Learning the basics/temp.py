from collections import defaultdict

dd = defaultdict(int)  # int() returns 0
dd['a'] += 1
print(dd)              # Output: defaultdict(<class 'int'>, {'a': 1})
dd['b']                # Output: 0
print(dd)              # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 0})
