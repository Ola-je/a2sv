class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        ans = []
        dic = Counter(s)  

        for ch in s:
            dic[ch] -=1
            if ch not in seen:
                while ans and dic[ans[-1]]>0 and ch < ans[-1]:
                    seen.remove(ans[-1])
                    ans.pop()
                ans.append(ch)
                seen.add(ch)

        return ''.join(ans)
