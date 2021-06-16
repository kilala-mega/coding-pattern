class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = Counter()
        left, right = 0, 0
        res = 0
        while right < len(s):
            count[s[right]] += 1
            while len(count.keys()) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res
        
