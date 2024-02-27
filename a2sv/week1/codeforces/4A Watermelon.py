from sys import stdin
def input():
    return stdin.readline()
W = int(input())

if ((W-2)%2)==0 and (W-2>0):
    print("YES")
else:
    print("NO")
