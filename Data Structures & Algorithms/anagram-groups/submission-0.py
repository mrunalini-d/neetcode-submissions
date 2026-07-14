class Solution:
    def groupAnagrams(self, strs):
        seen = dict()
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in seen.keys():
                seen[sorted_string].append(string)
            else:
                seen[sorted_string] = [string]
        return list(seen.values())