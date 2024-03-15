class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*(n+1)

        for f, l, s in bookings:
            res[f-1] += s
            res[l] -= s
        res = list (accumulate(res))
        res.pop(-1)
        return res