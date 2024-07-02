# Sudoku Solver

Given a 9x9 incomplete sudoku, solve it such that it becomes valid sudoku. Valid sudoku has the following properties.
1. All the rows should be filled with numbers(1 - 9) exactly once.
2. All the columns should be filled with numbers(1 - 9) exactly once.
3. Each 3x3 submatrix should be filled with numbers(1 - 9) exactly once.

**Note: Character '.' indicates empty cell.**

Input -> Output: 
![alt text](suduko2.png)

<br>

## The Only Approach 

### Algorithm
- Traverse through the matrix and check for a empty place ('.')
- For numbers 1-9 check if you can place any of it in that location.
- If yes, recursively add the next elements until 
  - you reached end of the board (return true without removing the placed numbers) or 
  - cannot place any number on the baord in which case return false, removing the number which we last placed.
- As we only need to find one solution, we stop after our first true.


### Code 

```python

```
- Time complexity : 
- Space complexity : 