class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    # need a way: 
    # swap any node to the least recently used 
    # lookup key -> value 

    # hashmap key: key, value: pointer to value in double linked list 
    # pointer on left (lru) and right (most recent) of dll 
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right  
        self.right.prev = self.left 
    
    def remove(self, node: Node) -> None:
        prev = node.prev
        nxt = node.next
        prev.next = nxt 
        nxt.prev = prev
    
    def insert(self, node: Node) -> None:
        prev = self.right.prev 
        nxt = self.right 
        prev.next = nxt.prev = node 
        node.next = nxt
        node.prev = prev 

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove key 
            self.remove(self.cache[key])
            # reinsert key 
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove key 
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        # insert key
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
