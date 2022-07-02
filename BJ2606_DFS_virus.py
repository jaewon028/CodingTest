import sys
input = sys.stdin.readline

def dfs_virus(graph, start_node):

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
                return len(visited) - 1
            ## 그 노드에 연결된 노드를
            need_visited.extend(graph[node])

    result_num = len(visited)-1
    return result_num


if __name__=="__main__":

    N = int(input())
    M = int(input())
    V = 1

    graph = dict()

    for _ in range(M):
        key, child = map(int, input().split())
        if key not in graph:
            graph[key] = list()
        if child not in graph:
            graph[child] = list()
        graph[key].append(child)
        graph[child].append(key)
    #
    # for elements in graph:
    #     graph[elements].sort(reverse=True)
    # answer_dfs = dfs(graph, V)

    answer_dfs = dfs_virus(graph, V)
    print(answer_dfs)