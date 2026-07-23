class Solution:
    def isPalindrome(self, string):
        cleaned = "".join(ch.lower() for ch in string if ch.isalnum())
        return cleaned == cleaned[::-1]