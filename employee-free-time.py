"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        h = []
        for i in range(len(schedule)):
            # heap element: employee i's first schedule start time, employee index, this employee's j-th schedule
            heappush(h, (schedule[i][0].start, i, 0))
        
        pre = h[0][0]
        freetime = []
        while h:
            curr_start, curr_employee, curr_j = heappop(h)
            if curr_start > pre:
                freetime.append(Interval(pre, curr_start))
            pre = max(pre, schedule[curr_employee][curr_j].end)
            if curr_j + 1 < len(schedule[curr_employee]):
                heappush(h, (schedule[curr_employee][curr_j+1].start, curr_employee, curr_j+1))
        return freetime
