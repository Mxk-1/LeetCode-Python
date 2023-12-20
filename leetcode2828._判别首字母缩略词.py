from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return "".join(word[0] for word in words) == s


if __name__ == "__main__":
    solution = Solution()

    words = ["an", "apple"]
    s = "aa"
    print(solution.isAcronym(words, s))
