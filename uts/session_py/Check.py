import sys
sys.stdin = open("input.txt", "r")
#sys.stdout = open("output.txt", "w")

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

n = int(input())
mas = [list(map(int, input().split())) for i in range(n)]
visit = []

print(mas)