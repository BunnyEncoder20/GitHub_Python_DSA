# LifoQueue is a stack in python
from queue import LifoQueue

def isValid(s):
    stack = LifoQueue()

    for bracket in s:
        if bracket in "([{":
            stack.put(bracket)
        else:
            if stack.empty(): return False
            else:
                stack_top = stack.get()
                if (bracket==')' and stack_top=='(') or (bracket==']' and stack_top=='[') or (bracket=='}' and stack_top=='{'):
                    continue
                else:
                    return False
    
    return True if stack.empty() else False


if __name__ == '__main__':
    strings = ["()[{}()]","((([]{}{)))"]
    for s in strings:
        if isValid(s):
            print("True")
        else:
            print("False")