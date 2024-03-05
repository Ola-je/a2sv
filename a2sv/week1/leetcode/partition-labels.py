class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occur = {char: i for i, char in enumerate(s)}
        part = []
        first = last = 0
        for i, char in enumerate(s):
            last = max(last, occur[char])
            if i == last:
                part.append(last - first + 1)
                first = i + 1
        return part 