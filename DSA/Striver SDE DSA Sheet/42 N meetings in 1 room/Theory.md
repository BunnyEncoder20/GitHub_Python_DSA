# N Meetings in 1 Room

- There is one meeting room in a firm. 
- You are given two arrays, `start` and `end` each of size `N`.
- For an index `i`, 
  - `start[i]` denotes the starting time of the ith meeting 
  - while `end[i]`  will denote the ending time of the ith meeting. 
- Find the maximum number of meetings that can be accommodated if only one meeting can happen in the room at a  particular time. Print the order in which these meetings will be performed.

<br>

## The Only Approach 

- Arrange the meetings according to their finishing times and see how many you can accomodate into the room

### Algorithm  
- [Watch it here](https://youtu.be/II6ziNnub1Q?si=WC6ZNjgU9WlPOvr_&t=237)
- Sort the given meetings in order their finishing times, also remember the position of the meetings
- **Remember** if the enidng time is same (irrespective of their starting times) add them in order of their positions (smaller position comes first)
- Now keep putting meetings into the room if possible (start of next meeting has to be after the end time of previous meeting)

<br> 

### Code

```python

```
- **Time complexity : O(n)+O(nlogn)+O(n) = O(nlogn)**
- **Space complexity : O(n)**

---