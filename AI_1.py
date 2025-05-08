from collections import deque

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph.get(node, []):
            dfs(visited, graph, neighbour)

def bfs(visited, graph, node, queue):
    visited.add(node)
    queue.append(node)
    while queue:
        s = queue.popleft()
        print(s, end=" ")
        for neighbour in graph.get(s, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    visited1 = set()  # DFS visited nodes
    visited2 = set()  # BFS visited nodes
    queue = deque()   # For BFS
    graph = {}

    n = int(input("Enter number of nodes: "))
    for i in range(1, n + 1):
        edges = int(input(f"Enter number of edges for node {i}: "))
        graph[i] = []
        for j in range(edges):
            node = int(input(f"Enter edge {j + 1} for node {i}: "))
            graph[i].append(node)

    print("\nThe following is DFS:")
    dfs(visited1, graph, 1)

    print("\n\nThe following is BFS:")
    bfs(visited2, graph, 1, queue)

if __name__ == "__main__":
    main()