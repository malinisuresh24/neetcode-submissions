class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            if(arr[i]==arr[:-1]):
                arr[i]=-1
                break
            ma=max(arr[i+1:], default=-1)
            
            arr[i]=ma
        return arr
        
