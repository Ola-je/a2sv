class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        result = ""
        if len(s)<2:
            return ""

        def good(start, end):
            seen = set(s[start:end])

            for x in seen:
                if (x.lower() in seen)!= (x.upper() in seen):
                    return False
            return True

        for start in range(len(s)):
            for end in range(start+1, len(s)+1):
                if good(start, end) and end - start > len(result):
                    result = s[start:end]

        return result  