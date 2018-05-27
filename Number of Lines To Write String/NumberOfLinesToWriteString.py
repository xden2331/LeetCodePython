import collections

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lineSize = 100
        lineUsed = 0
        currentChars = 0

        for c in S:
            if currentChars + widths[ord(c) - 97] <= lineSize:
                currentChars += widths[ord(c) - 97]
            else:
                lineUsed += 1
                currentChars = widths[ord(c) - 97]

        return [lineUsed+1, currentChars]

    # numberOfLines(
    #     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    #     "abcdefghijklmnopqrstuvwxyz")