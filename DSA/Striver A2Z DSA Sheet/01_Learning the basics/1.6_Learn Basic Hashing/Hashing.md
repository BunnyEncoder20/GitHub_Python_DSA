# Hashing in DSA (Very Important)

- If you don't know about hashing, you wouldn't be able to solve a lot of DSA questions 
>- Hashing in naive way can be defined by **pre-storing** some data and then **fetching** it later when needed. 

<br>

- Take a scenario where we need to find the number of occurrences of each element in a array
  - `Time Complexity`: **O(q x n)** (q = number of elements in the list which count we need)
- This is not a good `Time Complexity` and can very well go up to **O(n<sup>2</sup>)**
- This situation is where something like Hashing is useful.
- Instead of doing the calculations for the count when needed, we can do some pre-calculations by making a **Hashing** (or frequency) **array** and then using it to store the frequency of each element of the original array.
- This is done efficiently by 
    1. Make an Hashing array and initialize all the elements to 0 (length = number of unique numbers in the number array).   
    2. Loop through the number array and for each number 'n', increase the value of at the position HashArray[n].
- This way by a simple O(n) time we have created a pre-fetched Hash array which now has the number of occurrences of each and every element in the Number array.

<br>

- Generally we can declare array size up to 10<sup>6</sup> in main function without memory segmentation errors. (can declare bigger ones as globals)
- Hashing can also be done for characters