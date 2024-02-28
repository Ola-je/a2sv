class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left= result = 0
        right = len(skill) - 1
        target = skill[-1] + skill[0]
        
        while left < right:
            if skill[left] + skill[right] != target:
                return -1
            result += skill[left] * skill[right]
            left += 1
            right -=1
        return result
            
        