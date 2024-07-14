def sortStack(stack):
    empty_stack(stack)

def empty_stack(stack):
    if len(stack)==0 : return
    else:
        current_element = stack.pop()
        empty_stack(stack)
        place(stack,current_element)
        
def place(stack,curr):
    if len(stack)==0 or stack[-1]<curr:
        stack.append(curr)
    else:
        top = stack.pop()
        place(stack,curr)
        stack.append(top)

if __name__ == "__main__":
    stack = [5 ,-2,9 ,-7 ,3]
    sortStack(stack)
    print(*stack)