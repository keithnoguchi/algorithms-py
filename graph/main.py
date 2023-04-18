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

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('you', 'alice')
    graph.add_edge('you', 'bob')
    graph.add_edge('you', 'claire')
    graph.add_edge('bob', 'peggy')
    graph.add_edge('claire', 'peggy')
    print(graph.neighbors('claire'))
