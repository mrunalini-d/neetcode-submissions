class Solution:
    def characterReplacement(self, string: str, k: int) -> int:
        left = 0
        right = 0
        answer = 0
        count = {}
        while right < len(string):
            count[string[right]] = count.get(string[right], 0) + 1
            max_freq = max(count.values())
            replacements = (right - left + 1) - max_freq
            while replacements > k: 
                count[string[left]] -= 1
                left += 1
                replacements = (right - left + 1) - max_freq
            answer = max(answer, right - left + 1)
            right += 1
        return answer