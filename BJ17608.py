# N, h = map(int, input().split())
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    stk = []
    cnt = 0
    highest_block = 0

    N = int(input())

    for _ in range(N):
        stk.append(int(input()))

    for _ in range(N):
        next_block = stk.pop()
        if next_block > highest_block:
            highest_block = next_block
            cnt += 1
    print(cnt)