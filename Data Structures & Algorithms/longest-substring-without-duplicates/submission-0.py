class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        verify = set() #No dulpicates
        l = 0 #Left edge
        res = 0 #Initialize result
        for r in range(len(s)):
            while s[r] in verify:
                verify.remove(s[l])
                l += 1
            verify.add(s[r])
            res = max(res, r-l+1)
        return res