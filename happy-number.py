class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n: int) -> int:
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit**2
            return total_sum
        
        walker = n
        runner = get_next(n)
        while runner != 1 and walker != runner:
            walker = get_next(walker)
            runner = get_next(get_next(runner))
        return runner == 1
