class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) -1

        maxWater = 0
        while p1 != p2:
            area = (p2-p1) * min(heights[p1],heights[p2])
            # print(area)

            if area>maxWater:
                maxWater = area

            if heights[p1]<heights[p2]:
                p1+=1
            else:
                p2-=1

            # print(f"{p1} {p2}")
        
        return maxWater
        