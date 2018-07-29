class Solution:
    def shortestPalindrome(self, s):
        A = self.palindromesByLength(s)
        A = [edge_ps(ps, s) for ps in A]
        A = [ps for ps in A if ps]
        i, j, edge_p = A[-1][0]
        return reverse(s[j:]) + s

    def palindromesByLength(self, s):
        A = [
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

        return [ps for ps in A if ps]


def is_palindrome(s):
    return s == s[::-1]


def edge_ps(ps, s):
    return [p for p in ps if p[0] == 0]


def reverse(s):
    return s[::-1]


"""

 i
 ^
babad

"""

if __name__ == "__main__":
    import sys

    s = Solution()
    print(s.shortestPalindrome(sys.argv[1]))
