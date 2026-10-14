class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = nums[:1]
        
        if (len(nums)>1):
            memo.append(nums[1])
        else:
            return memo[0]

        if(len(nums)>2):
            memo.append(nums[2]+memo[0])

        while (len(memo)<len(nums)):
            i = len(memo)

            memo.append(nums[i]+max(memo[i-2],memo[i-3]))

        return max(memo[-1], memo[-2])
