class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l =0 
        count_vowel =0
        result =0
        seen = {'a', 'e', 'i', 'o', 'u'}

        for  r in range(len(s)):
            
            if s[r] in seen:
                count_vowel +=1

            if r-l+1 > k:
                if s[l] in seen:
                    count_vowel -=1
                l +=1

            result = max(result, count_vowel)
            
        return result