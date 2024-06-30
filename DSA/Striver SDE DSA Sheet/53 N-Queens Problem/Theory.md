# N-Queens Problem

- The n-queens is the problem of placing `n` queens on `n × n` chessboard such that no two queens can attack each other. 
- Given an integer `n`, return all distinct solutions to the n -queens puzzle. 
- Each solution contains a distinct boards configuration of the queen's placement, where ‘Q’ and ‘.’ indicate queen and empty space respectively.
- Examples : 
```
Examples:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
```
![alt text](<pasted image 0.png>)

<br>

## Brute Approach (Back Tracking)

### Algorithm
- [Watch it here](https://youtu.be/i05Ju7AftcM?si=LApUVnGJpB8tbkjJ&t=415)
- check for each col and each row, if we can place a Q there.
- If we find a place, we all the Q to that place and move to the next col
- if we cannot place a Q in any row, then that sequence is wrong and we pop that sequence 
- else if we are able to place all n Q then that is a correct sequence and we can append it into the answer
- Recursive go back and make the stack empty 

### Code

```python

```
- Time complexity : 
- Space complexity : 