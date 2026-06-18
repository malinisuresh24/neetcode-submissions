class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # for i in range(len(arr)):
        #     if(arr[i]==arr[:-1]):
        #         arr[i]=-1
        #         break
        #     ma=max(arr[i+1:], default=-1)    
        #     arr[i]=ma
        # return arr
        ar=[-1]
        ma=arr[-1]
        
        for i in range(len(arr)-1,0,-1):
           
            if(ma<arr[i]):
                ma=arr[i]
            ar.append(ma)
            
        return ar[ : :-1]

        
