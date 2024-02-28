from sys import stdin
def input():
    return stdin.readline()[:-1]
N = int(input())
count = 0
for _ in range(N):
    nums = input()
    a, b, c =map(int, nums.split(' '))
    if a + b + c >= 2:
        count +=1
print(count)
