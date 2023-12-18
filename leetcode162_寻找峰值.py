from typing import List

"""
LeetCode162. 寻找峰值
"""


class solution:
    def findPeakElement1(self, nums: List[int]) -> int:
        return nums.index(max(nums))

    def findPeakElement2(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1
        return l


if __name__ == "__main__":
    s = solution()
    list = [1, 2, 4, 5, 6, 4]
    print(s.findPeakElement1(list))
