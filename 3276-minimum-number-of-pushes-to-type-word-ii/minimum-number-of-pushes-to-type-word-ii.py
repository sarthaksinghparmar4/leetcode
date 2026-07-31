class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count frequency of each letter
        freq = [0] * 26

        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        # Most frequent letters should get fewer pushes
        freq.sort(reverse=True)

        pushes = 0

        for i in range(26):
            cost = (i // 8) + 1
            pushes += freq[i] * cost

        return pushes
        