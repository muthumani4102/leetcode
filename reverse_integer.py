class Solution(object):
    def reverse(self, x):
      neg=1
      if x<0:
        neg=-1
        x=-x

      rev=0
      while x>0:  
        digit=x%10
        rev=rev*10+digit 
        x=x//10
      ans=rev*neg
      if ans<-2147483648 or ans>2147483647:
        return 0
      return ans
      
      
     reverse a integer