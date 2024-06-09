# Pow(x,n)

- given a number x we and a integer n, we need to return x<sup>n</sup>
- x can be a integer or a double 
- **NOTE:** ask if n can be a negative integer. (because we need to handle some edge cases if that is the case)

---

## Brute Force Approach  

- We can simple make a loop and keep multiplying x for n times : 
- **Note** that this will only work if n is `+ve`.
- **If** n is negative then the answer will be 1/x<sup>n</sup>

<br>

- **Time Complexity : O(n)**
- **Space Complexity : O(1)**

<br>

### Code 

```python 
for i in range(abs(n)):
    ans *= x
return ans if n > 0 else 1/ans
```

---

## Better Approach 

- We can split the powers into smaller values until we get n = 0
- Eg: 2<sup>10</sup> = (2x2)<sup>5</sup> = (2x2 x 2)<sup>4</sup> = (2x2 x 2 x 2x2)<sup>2</sup>
- hence we see a pattern here in the powers : 
    - n%2 == 0 : ans *= x*x and n = n/2
    - n%2 == 1 : ans *= x and n = n-1

<br>

- **Time Complexity : O(log<sub>2</sub>n)**

<br>

### Code

```python 
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        nn = n      # original n
        

        if nn < 0 : nn = abs(nn)
    
        while nn > 0 : 
            if nn%2 == 0 :
                x *= x
                nn = nn//2
            else : 
                ans *= x
                nn -= 1
        
        return ans if n > 0 else 1/ans

if __name__ == "__main__":
    i = Solution()
    x1,x2,x3 = 2.00000,2.10000,2.00000
    n1,n2,n3 = 10,3,-2

    print(i.myPow(x1,n1))
    print(i.myPow(x2,n2))
    print(i.myPow(x3,n3))
```