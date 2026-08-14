class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2
            hours = self.totalhr(piles, mid)

            if hours <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low

    def totalhr(self, piles, speed):
        ans = 0
        for pile in piles:
            ans += math.ceil(pile / speed)
        return ans