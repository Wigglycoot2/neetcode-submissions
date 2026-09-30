import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mn = 1
        mx = max(piles)
        k = mx

        while mn <= mx:
            mid = (mn+mx)//2

            h2 = 0
            for i in piles:
                h2 += math.ceil(i/mid)

            if h2 > h:
                mn = mid +1
            elif h2 <= h:
                k = mid
                mx = mid -1

        return k
                
