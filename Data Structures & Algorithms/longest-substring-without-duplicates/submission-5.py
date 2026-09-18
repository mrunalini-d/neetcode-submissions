class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        seen = set()
        left = 0
        right = 0
        longest = 0
        while right < len(string):
            while string[right] in seen:
                seen.remove(string[left])
                left += 1
            seen.add(string[right])
            longest = max(longest, right - left + 1)
            right += 1
        return longest