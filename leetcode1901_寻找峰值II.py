from typing import List

"""
LeetCode1901. 寻找峰值II
"""


class solution:
    def findfindPeakGrid(self, mat: List[List[int]]):
        nums = []
        for arr in mat:
            for num in arr:
                nums.append(num)
        max_num = max(nums)
        return [nums.index(max_num) // len(mat[0]), nums.index(max_num) % len(mat[0])]


if __name__ == "__main__":
    s = solution()
    mat = [[10, 20, 15], [21, 30, 14], [7, 16, 32]]
    result = s.findfindPeakGrid(mat)
    print(result)
