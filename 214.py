class Solution:
    def shortestPalindrome(self, s):
        i = 0
        for i in range(len(s), 0, -1):
            p = s[:i]
            if p == p[::-1]:
                break

        return s[i:][::-1] + s


if __name__ == "__main__":
    import sys

    s = Solution()
    print(s.shortestPalindrome(sys.argv[1]))
