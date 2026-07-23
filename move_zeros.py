class Solution():
    def moveZeroes(self, nums):
      s=[]
      for i in nums:
        if i!=0:
            s.append(i)
      
      for i in nums:
        if i==0:
            s.append(i)
      for i in range(len(nums)):
         nums[i]=s[i]


     