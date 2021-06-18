class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = 0
        count = 0
        timestamp = []
        for interval in intervals:
            start, end = interval[0], interval[1]
            timestamp.append((start, 1))
            timestamp.append((end, -1))
        
        timestamp.sort()
        
        for i in range(len(timestamp)):
            if i == 0:
                count += 1
            else:
                if timestamp[i][1] == 1:
                    count += 1
                else:
                    count -= 1
            res = max(res, count)
        
        return res
        
