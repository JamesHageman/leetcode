class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        A = []
        for i in range(len(words)):
            for j in range(len(words)):
                if j == i:
                    continue
                if is_palindrome(words[i] + words[j]):
                    A.append([i, j])
        return A


def is_palindrome(s):
    return s == s[::-1]


if __name__ == "__main__":
    import sys

    s = Solution()
    print(s.palindromePairs(sys.argv[1:]))
