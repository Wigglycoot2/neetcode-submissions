class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        min = None
        while left <= right:
            mid = (left+right)//2

            if (nums[mid]>nums[right]):
                if (mid == right-1):
                    return nums[right]
                left = mid
            elif (nums[mid]<nums[left]):
                if (mid==left+1):
                    return nums[mid]

                right = mid

            else:
                return nums[left]
