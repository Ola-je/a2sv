class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l =0
        s1dic = Counter(s1)
        count = 0
        for r in range(len(s2)):
            if s2[r] in s1dic:
                count +=1
                s1dic[s2[r]] -=1

                while s1dic[s2[r]] <0:
                    count -=1
                    s1dic[s2[l]] +=1
                    l +=1
                if count == len(s1):
                    return True
            
            else:
                while l <r:
                    count -=1
                    s1dic[s2[l]] +=1
                    l +=1
                l= r+1
            
        return False
