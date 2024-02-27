from sys import stdin
def input():
    return stdin.readline()[:-1]
T = int(input())
for _ in range(T):
    ans = []
    word = input()
    if len(word)>10:
        ans.append(word[0])
        ans.append(str(len(word)-2))
        ans.append(word[len(word)-1])
        print(''.join(ans))
    else:
        print(word)