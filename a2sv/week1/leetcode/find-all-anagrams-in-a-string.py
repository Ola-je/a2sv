class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        right = len(p)
        target = Counter(p)
        window = Counter(s[:right])
        ans = []

        while right < len(s):
            if target == window:
                ans.append(left)
            window[s[left]] -=1
            
            left +=1
            window[s[right]] += 1
            right +=1
        if target == window:
                ans.append(left)
        return ans  