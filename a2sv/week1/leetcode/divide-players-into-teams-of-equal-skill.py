class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right, result = 0, len(skill)-1, 0
        target = skill[left] + skill[right]

        while left < right:
            if skill[left] + skill[right] != target:
                return -1
            result += skill[left]*skill[right]
            left += 1
            right-=1
        return result