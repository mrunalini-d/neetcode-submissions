class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}       
        for i in nums:
            if i in seen.keys():
                seen[i] += 1
            else:
                seen[i] = 1
        result =  list(sorted(seen.items(), key= lambda e: e[1], reverse = True))
        return [key for key, _ in result[:k]]
              
        