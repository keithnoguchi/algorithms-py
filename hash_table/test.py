from hash_table.main import HashTable

def test():
    numbers = HashTable()
    for n in range(0, 10000):
        numbers.insert(n, n)

    for n in range(0, 10000):
        assert numbers.find(n) == n
