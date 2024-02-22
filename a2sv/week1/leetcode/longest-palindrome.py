class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic ={}
        c=1
        counter =0
        for i in s:
            if i in dic:
                dic[i]+=1
            else: 
                dic[i]= 1
        for i in dic:
            if dic[i]%2==0:
                counter +=dic[i]
            elif dic[i]==1 and c==1:
                counter +=1
                c=0
            elif dic[i]%2==1 and c==1:
                counter +=dic[i]
                c=0
            elif dic[i]%2==1 and c==0:
                counter += dic[i]-1
        return counter
