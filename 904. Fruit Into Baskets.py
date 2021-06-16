"""
basket to hold at most two labels 
use a counter 
sliding window beginning from 0,0
increase the window length until the 3rd kind of tree appears
then shrink window size
window size is the number of fruit we can collect
"""

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        basket = Counter()
        left, right = 0, 0
        ans = 0
        while right < len(tree):
            basket[tree[right]] += 1
            while len(basket.keys()) > 2:
                basket[tree[left]] -= 1
                if basket[tree[left]] == 0:
                    del basket[tree[left]]
                left += 1
            ans = max(ans, right-left+1)
            right += 1
        return ans
