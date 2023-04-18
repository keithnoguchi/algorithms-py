from graph import main

def test():
    graph = main.Graph()
    graph.add_edge('you', 'alice')
    graph.add_edge('you', 'bob')
    graph.add_edge('you', 'claire')
    graph.add_edge('bob', 'peggy')
    graph.add_edge('claire', 'peggy')
    assert graph.neighbors('you') == ['alice', 'bob', 'claire']
    assert graph.neighbors('bob') == ['peggy']
    assert graph.neighbors('claire') == ['peggy']
