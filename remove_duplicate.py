class Solution:
    def removeDuplicates(self, nums):
      
      l1=[]
      for i in nums:
         if i not in l1:
            l1.append(i)
      for i in range(len(l1)):
        nums[i]=l1[i]
      return len(l1)