class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        location = [0]*1001

        for person, start, end in trips:
            location[start] += person
            location[end] -= person

        return all(current_passengers <= capacity for current_passengers in accumulate(location)) 