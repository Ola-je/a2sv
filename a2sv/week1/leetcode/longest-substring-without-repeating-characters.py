class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        dic = Counter(s[0])
        count = 0
        l = 0
        r= 1

        while r < len(s):
            if s[r] in dic and dic[s[r]] >=1:
                dic[s[l]] -=1
                l+=1
            else:
                dic[s[r]] +=1
                r+=1
            count = max(count, r-l)
        return count
