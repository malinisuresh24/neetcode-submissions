class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        c=0
        m=0
        for i in nums:
            if(i!=0):
                c+=1
                
            else:
                if(c>m):
                    m=c 
                c=0               
        if(c>m):
            m=c
        return m
        