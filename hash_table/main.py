# Resizing is not supported yet
class HashTable:
    def __init__(self):
        self.capacity = 5
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        key = str(key)
        hashsum = 0
        for i, c in enumerate(key):
            hashsum += (i + len(key)) ** ord(c)
            hashsum %= self.capacity

        return hashsum

    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        self.buckets[index] = Node(key, value, node)

    def remove(self, key):
        node = self.buckets[self.hash(key)]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None
        else:
            value = node.value
            if prev is None:
                node = None
            else:
                prev.next = node.next
            self.size -= 1
            return value

    def find(self, key):
        node = self.buckets[self.hash(key)]
        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

class Node:
    def __init__(self, key, value, node):
        self.key = key
        self.value = value
        self.next = node

if __name__ == "__main__":
    suffixes = HashTable()
    suffixes.insert("python", "py")
    suffixes.insert("javascript", "js")
    suffixes.insert("rust", "rs")
    suffixes.insert("c", "c")

    assert suffixes.find("rust") == "rs"
    assert suffixes.find("javascript") == "js"
    assert suffixes.find("python") == "py"
    assert suffixes.find("c") == "c"
    assert suffixes.find("ruby") is None
