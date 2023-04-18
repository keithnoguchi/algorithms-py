from collections import deque

class Graph:
    def __init__(self):
        self.adjacencies = {}

    def add_edge(self, a, b):
        if a in self.adjacencies:
            self.adjacencies[a].append(b)
        else:
            self.adjacencies[a] = [b]

    def neighbors(self, a):
        return self.adjacencies[a]

    def bfs(self, a, b):
        queue = deque(self.neighbors(a))
        visited = set()
        while queue:
            item = queue.pop()
            if item == b:
                return b
            elif item in visited:
                continue
            else:
                visited.add(item)
                queue += self.neighbors(item)

        return None

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('you', 'alice')
    graph.add_edge('you', 'bob')
    graph.add_edge('you', 'nancy')
    graph.add_edge('jessica', 'david')
    graph.add_edge('nancy', 'jessica')
    graph.add_edge('bob', 'jessica')
    print(graph.bfs('you', 'jessica'))
    print(graph.bfs('you', 'david'))
