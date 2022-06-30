import sys
input = sys.stdin.readline

if __name__ == "__main__":
    stk = []
    result_sum = 0

    K = int(input())

    for _ in range(K):
        stk.append(int(input()))
        if stk[-1] == 0:
            stk.pop()
            stk.pop()

    for i in range(len(stk)):
        result_sum += stk[i]

    print(result_sum)