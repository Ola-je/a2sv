class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        temp = [0]*(len(s)+1)
        for i in range(len(shifts)):
            if shifts[i][2] == 0:
                temp [shifts[i][0]] += -1
                temp[shifts[i][1]+1] += 1
            else:
                temp[shifts[i][0]] += 1
                temp[shifts[i][1]+1] += -1

        result = list(accumulate(temp))
        ans =[]

        for j in range(len(s)):
           ans.append(chr(((ord(s[j]) -97+result[j])%26)+97))
        
        return ''.join(ans)
