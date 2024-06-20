from typing import List

class meeting:
    def __init__(self,start,end,position):
        self.start = start
        self.end = end
        self.position = position

def maxMeetings(start:List[int],end:List[int],n:int) -> None :

    # Create a list of meeting objects with their start,end and pos
    meetings = [meeting(start[i],end[i],i+1) for i in range(n)]
    
    # Sort the meetings objects using end time as primary and position as secondary key
    sorted(meetings, key= lambda meet : (meet.end,meet.position))
    
    order = []
    order.append(meetings[0].position)
    count = 1
    previous_meeting_end = meetings[0].end
    for i in range(1,n):
        if meetings[i].start > previous_meeting_end:
            count+=1
            order.append(meetings[i].position)
            previous_meeting_end = meetings[i].end
    return count,order
        

if __name__ == '__main__':
    n = 6
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 5, 7, 9, 9]
    count,order = maxMeetings(start, end, n)
    print(f"The max number of meetings which can happen is {count}")
    print(f"The order of the meetings will be : {order}")