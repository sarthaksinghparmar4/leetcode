from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = [0] * 26
        middle = ""

        for ch, cnt in freq.items():
            idx = ord(ch) - ord('a')
            half[idx] = cnt // 2
            if cnt % 2:
                middle = ch

        def countWays(cnt):
            total = sum(cnt)
            ways = 1
            remain = total

            for x in cnt:
                if x:
                    ways *= comb(remain, x)
                    if ways > k:
                        return ways
                    remain -= x

            return ways

        if countWays(half) < k:
            return ""

        left = []

        while sum(half):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = countWays(half)

                if ways >= k:
                    left.append(chr(i + ord('a')))
                    break
                else:
                    k -= ways
                    half[i] += 1

        left = "".join(left)
        return left + middle + left[::-1]