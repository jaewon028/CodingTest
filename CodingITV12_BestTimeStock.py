import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        # 최소값과 최댓값을 계속 생신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit


if __name__ == "__main__":
    pricea = [7, 6, 4, 3, 1,5]
    solution = Solution()
    print(solution.maxProfit(prices=pricea))