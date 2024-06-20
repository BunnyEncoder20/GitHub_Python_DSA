# Job Sequencing Problem

- You are given a set of `N` jobs where each job comes with a `deadline` and `profit`. 
- The profit can only be earned upon completing the job within its deadline. 
- Find the number of jobs done and the maximum profit that can be obtained. 
- Each job takes a single unit of time and only one job can be performed at a time.

<br>

## The Only Approach 

- Delay the jobs to the end days 
- perform the max profit job

### Algorithm

1. Get the max deadline number. This is the number of days we have.
2. Create a array of max_deadline+1 and initlize to -1 (to indicate empty).
3. Sort all the jobs according to profits. For the highest profit job, try to perform it on it's deadline day.
4. update job count, job profits.
5. If there is already a job on the deadline day, we retract and go to an earlier day.

<br>

### Code 

```python 
from typing import Tuple,List

class job:
    def __init__(self,id,deadline,profit) -> None:
        self.id = id
        self.deadline = deadline
        self.profit = profit
        
def jobScheduling(jobs:List[job])->Tuple[int,int]:
    # sort the jobs according to the profit in decsending order
    jobs.sort(key=lambda x: x.profit,reverse=True)
    
    # Get the number of days we have
    days = -1
    for i in range(1,len(jobs)):
        days = max(days,jobs[i].deadline)
    
    # Create a array of days we can work in
    # +1 to accomodate the end day index
    working_days = [0]*(days+1)

    # Keep adding jobs till working_days are full
    # Remember that the jobs are sorted according to profit
    job_count = 0
    profit_earned = 0
    for job in jobs:
        for day in range(job.deadline,0,-1):
            if not working_days[day]:
                working_days[day]=1
                job_count+=1
                profit_earned+=job.profit
                break 
    
    return job_count,profit_earned

if __name__ == "__main__":
    jobs = [job(1, 4, 20), job(2, 1, 10), job(3, 2, 40), job(4, 2, 30)]
    count, profit = jobScheduling(jobs)
    print(f"We can do {count} jobs, earning a max profit of ₹{profit}")
```
- **Time complexity : O(nlogn) + O(n) + O(n*max_deadline)**
- **Space complexity : O(max_deadline)**