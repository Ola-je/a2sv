class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = s.rindex(s[0])
        first = 0
        result = []
        for i in range(len(s)):
            if i == last:
                result.append(last - first + 1)
                first = last +1
                if i < len(s)-1:
                    last = s.rindex(s[i+1])
                
            if s.rindex(s[i]) > last:
                last = s.rindex(s[i])

        return result
