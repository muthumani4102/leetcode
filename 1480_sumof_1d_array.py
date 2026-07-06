class Solution(object):
    def runningSum(self, nums):
      a=[]
      sum=0
      for i in nums:
          
          sum+=i
          c=a.append(sum)
      return a 