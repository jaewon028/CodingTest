from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        argmax = 0
        pairs = []
        nums.sort()

        for n in nums:
            pairs.append(n)
            if len(pairs) == 2:
                argmax += min(pairs)
                pairs = []

        return argmax


if __name__ == "__main__":
    solution = Solution()
    print(solution.arrayPairSum([1,4,2,3,9,6,5,8,7]))
