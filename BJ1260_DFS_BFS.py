from collections import deque
import sys
input = sys.stdin.readline

deq = deque()

def dfs(graph, start_node):

    ## 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    need_visited, visited = list(), list()
    ## 시작 노드를 시정하기
    need_visited.append(start_node)

    ## 만약 아직도 방문이 필요한 노드가 있다면,
    while need_visited:
        ## 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        node = need_visited.pop()
        ## 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
            ## 방문한 목록에 추가하기
            visited.append(node)
            ## 그래프에 현재 해당 node 값이 없는 경우 함수 종료
            if node not in graph:
                return visited
            ## 그 노드에 연결된 노드를
            need_visited.extend(graph[node])

    return visited

def bfs(graph, start_node):

    ## 기본 항상 두개의 리스트를 별도로 관리
    need_visited, visited = deque(), list()
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.popleft()

        if node not in visited:
            visited.append(node)
            if node in need_visited:
                return visited
            need_visited.extend(graph[node])

    return visited


if __name__=="__main__":

    N, M, V = map(int, input().split())

    graph = dict()

    for _ in range(M):
        key, child = map(int, input().split())
        if key not in graph:
            graph[key] = list()
        if child not in graph:
            graph[child] = list()
        graph[key].append(child)
        graph[child].append(key)

    for elements in graph:
        graph[elements].sort(reverse=True)
    answer_dfs = dfs(graph, V)

    for elements in graph:
        graph[elements].sort(reverse=False)
    answer_bfs = bfs(graph, V)

    for i in answer_dfs:
        print(i, end=" ")
    print()
    for i in answer_bfs:
        print(i, end=" ")
