# stock_prices = [
#     ['6-Mar',310],
#     ['7-Mar',340],
#     ['8-Mar',380],
#     ['9-Mar',302],
#     ['10-Mar',297],
#     ['11-Mar',323],
# ]  

# # trying to find that one day (when using a List to store) : 
# # for entry in stock_prices : 
# #     if entry[0] == '9-Mar' :
# #         print(entry[1])              # O(n)

# stock_prices_dict = {
#     '6-Mar':310,
#     '7-Mar':340,
#     '8-Mar':380,
#     '9-Mar':302,
#     '10-Mar':297,
#     '11-Mar':323,
# } 
# # trying to find that one day (when using a dict to store) : 
# # print(stock_prices_dict['9-Mar'])   # O(1)


# Implementing a hashmap in python

class HashTable :
    def __init__(self) :
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]  # adding 100 elements here using list comprehension
    
    def getHash(self, key) : 
        h = 0 
        for char in key : 
            h+=ord(char)        # ord just returns the ASCII value of the character
        return h % self.MAX

    def __setitem__(self,key,value) :
        idx = self.getHash(key)
        self.arr[idx] = value
        

    def __delitem__(self,key) :
        self.arr[self.getHash(key)]=None
        
    
    def __getitem__(self, key) :
        idx = self.getHash(key)
        if self.arr[idx] is not None:
            return self.arr[idx]
        else :
            print("No element on given index")
    



t = HashTable()
print(t.getHash('9-Mar'))

# Inserting elements
t['9-Mar'] = 310    # calls the __setitem__()
print(t['9-Mar'])   # calls the __getitem__()

t['1-Mar'] = 280
t['2-Apr'] = 330
t['3-May'] = 350

# Seeing the entire dictionary
print(t.arr)

# Removing elements 
del t['2-Apr']
print(t.arr)