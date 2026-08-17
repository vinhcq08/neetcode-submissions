class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int) #Stores frequency of each letter
        l = 0 #Preset left edge
        maxf = 0 #Preset max frequency
        res = 0
        for r in range(len(s)):
            counter[s[r]] +=1
            maxf = max(maxf, counter[s[r]])
            while (r-l+1)-maxf > k:
                counter[s[l]] -=1
                l += 1
            res = max(res,r-l+1)
        return res
