class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        left = []
        middle = ""

        for i in range(26):
            left.append(chr(i + ord('a')) * (count[i] // 2))

            if count[i] % 2 == 1:
                middle = chr(i + ord('a'))

        left = "".join(left)

        return left + middle + left[::-1]