from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i in range(1, len(height)-1):
            # 좌우 기둥에서 가장 큰 기둥
            left = max(height[:i])
            right = max(height[i+1:])

            # 좌우 기둥의 큰 값 중에서 작은 값
            lower_limit_wall = min(left, right)

            if height[i] <= lower_limit_wall:
                water += lower_limit_wall - height[i]

        return water

if __name__ == "__main__":
    arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    print(solution.trap(arr))