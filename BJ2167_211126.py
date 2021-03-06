'''
2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 배열의 (i, j) 위치는 i행 j열을 나타낸다.

[입력]
첫째 줄에 배열의 크기 N, M(1 ≤ N, M ≤ 300)이 주어진다.
 다음 N개의 줄에는 M개의 정수로 배열이 주어진다.
 배열에 포함되어 있는 수는 절댓값이 10,000보다 작거나 같은 정수이다.
 그 다음 줄에는 합을 구할 부분의 개수 K(1 ≤ K ≤ 10,000)가 주어진다.
 다음 K개의 줄에는 네 개의 정수로 i, j, x, y가 주어진다(1 ≤ i ≤ x ≤ N, 1 ≤ j ≤ y ≤ M).

2 3
1 2 4
8 16 32
3
1 1 2 3
1 2 1 2
1 3 2 3

[출력]
K개의 줄에 순서대로 배열의 합을 출력한다. 배열의 합은 2**31-1보다 작거나 같다.

63
2
36

'''


# 시간초과
# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     list_array = [list(map(int, input().split())) for _ in range(n)]
#
#     k = int(input())
#     for _ in range(k):
#         answer=0
#         i,j,x,y = map(int, input().split())
#
#         for a in range(i-1, x):
#             for b in range(j-1, y):
#                 answer += list_array[a][b]
#
#         print(answer)

if __name__ == "__main__":
    # 문제 입력 값 받기
    n, m = map(int, input().split())
    list_array = [list(map(int, input().split())) for _ in range(n)]

    # dp table 초기화
    dp = [[0] * (m+1) for _ in range(n+1)]

    # dp table 생성
    for a in range(1, n+1):
        for b in range(1, m+1):
            dp[a][b] = list_array[a-1][b-1] + dp[a][b-1] + dp[a-1][b] - dp[a-1][b-1]

    # 문제 닶 계산
    k = int(input())
    for _ in range(k):
        i,j,x,y = map(int, input().split())
        answer = dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1]
        print(answer)