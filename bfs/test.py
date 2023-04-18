from bfs.main import Graph

def test():
    graph = Graph()
    graph.add_edge('you', 'alice')
    graph.add_edge('you', 'bob')
    graph.add_edge('you', 'nancy')
    graph.add_edge('nancy', 'jessica')
    graph.add_edge('bob', 'jessica')
    assert graph.bfs('you', 'jessica') == 'jessica'
    assert graph.bfs('you', 'david') is None
