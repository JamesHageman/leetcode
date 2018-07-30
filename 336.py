from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        A = []
        for i in range(len(words)):
            for j in range(len(words)):
                if j == i:
                    continue
                if is_palindrome(words[i], words[j]):
                    A.append([i, j])
        return A


def is_palindrome(a: str, b: str) -> bool:
    if len(a) < len(b):
        if not b.endswith(a[::-1]):
            return False
    else:
        if not a.startswith(b[::-1]):
            return False

    s = a + b
    return s == s[::-1]


if __name__ == "__main__":
    import sys

    s = Solution()
    print(s.palindromePairs(sys.argv[1:]))
