class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            if(arr[i]==arr[:-1]):
                arr[i]=-1
                break
            ma=-1
            for j in range(i+1,len(arr)):

                if(arr[j]>ma):
                    ma=arr[j]
            
            arr[i]=ma
        return arr
        
