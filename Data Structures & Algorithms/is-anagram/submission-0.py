class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s)!=len(t)):
            return False
        else:

            di={}
            #add
            for i in s:
                if(i in di):
                    di[i]+=1
                else:
                    di[i]=1
            #remove
            for i in t:
                if(i not in di):
                    return False

                di[i]-=1
                if(di[i]<0):
                    return False
           
        return True
       
        
        
        