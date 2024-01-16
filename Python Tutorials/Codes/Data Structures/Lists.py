# Lists - used to store multiple items in a single array (kinda like a array)

food = ["🍕", "🍔", "🌭", "🍝", "🥛"]

# Accessing elements by idx
print("Before Editing")
print(food[0])
print(food[1])
print(food[2])
print(food[3])

# Editing a list :
food[0] = "🍣"

# iterating a list :
print("After Editing")
for i in food:
    print(i)


# Some useful functions of Lists :
# 1) .append(item) - adds a new item to the end of list
food.append("🍨")
print("After Editing")
for i in food:
    print(i, end="")
print()

# 2) .pop() - removes the last element from the list
food.pop()
for i in food:
    print(i, end="")
print()

# 3) .insert(idx , item) - adds the element in a specific position
food.insert(1, "🥞")
for i in food:
    print(i, end="")
print()

# 4) .remove(item) - removes specific item from the list
food.remove("🌭")
for i in food:
    print(i, end="")
print()

# 5) .sort() - sorts the elements of  list
food.sort()
for i in food:
    print(i, end="")
print()

# 6) .clear() - removes all the elements of a array :
food.clear
for i in food:
    print(i, end="")
