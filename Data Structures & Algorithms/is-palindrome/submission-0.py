class Solution:
    def isPalindrome(self, string):
        chars = []
        for ch in string:
            if ch.isalnum():
                chars.append(ch.lower())
        cleaned = "".join(chars)
        start = 0
        end = len(cleaned) - 1
        while start < end:
            if cleaned[start] == cleaned[end]:
                start += 1
                end -= 1
            else:
                return False
        return True