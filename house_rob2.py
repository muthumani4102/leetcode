class Solution:
    def rob(self, nums):

        

        if len(nums) == 1:
            return nums[0]
        def helper(mani):
            prev2=0
            prev1=0
            for num in mani:
                 current=max(prev1,prev2+num)
                 prev2=prev1
                 prev1=current
            return prev1
        return max(helper(nums[:-1]),helper(nums[1:]))