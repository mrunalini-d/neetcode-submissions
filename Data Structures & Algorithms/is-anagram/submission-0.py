class Solution:
    def isAnagram(self, string1: str, string2: str) -> bool:
        dict1 = dict()
        dict2 = dict()
        for s in string1:
            if s in dict1:
                dict1[s]+=1
            else:
                dict1[s]=1
        for s in string2:
            if s in dict2:
                dict2[s]+=1
            else:
                dict2[s]=1
        return dict1==dict2
                
        