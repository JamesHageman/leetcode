from typing import List, Tuple


class Solution:
    def longestPalindromeSlow(self, s):
        # brute force :(
        x = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                p = s[i:j]
                if p == p[::-1] and len(p) > len(x):
                    x = p
        return x

    def longestPalindrome(self, s: str) -> str:
        A: List[List[Tuple[int, int, str]]] = [
            [(0, 0, "")],
            [(i, i + 1, s[i : i + 1]) for i in range(len(s))],
            [(i, i + 2, s[i : i + 2]) for i in range(len(s) - 1) if s[i] == s[i + 1]],
        ]
        for size in range(3, len(s) + 1):
            new_palindromes = [
                (i - 1, j + 1, s[i - 1 : j + 1])
                for i, j, _ in A[size - 2]
                if is_palindrome(s[i - 1 : j + 1]) and i > 0 and j < len(s)
            ]
            A.append(new_palindromes)
            if new_palindromes:
                A[size - 2] = []  # save that memory

        return [ps for ps in A if ps][-1][0][2]


def is_palindrome(s):
    return s == s[::-1]


"""

 i
 ^
babad

"""

if __name__ == "__main__":
    import sys

    s = Solution()
    print(s.longestPalindrome(sys.argv[1]))
