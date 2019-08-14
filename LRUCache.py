class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class LRUCache:

    def __init__(self, capacity: int):
        self.length = 0
        self.capacity = capacity
        self.cache = None
        

    def get(self, key: int) -> int:
        if self.cache.key == key:
            return self.cache.value

        temp = self.cache
        value = -1
        while temp != None and temp.key != key:
            temp = temp.right
        
        if temp != None:
            value = temp.value

            temp.left.right = temp.right
            if temp.right != None:
                temp.right.left = temp.left
            
            temp.left = None
            temp.right = self.cache
            self.cache.left = temp
            self.cache = temp
    
        return value
        
        

    def put(self, key: int, value: int) -> None:
        if self.cache == None:
            self.cache = Node(key, value)
        else:
            if self.length == self.capacity:
                temp = self.cache
                while temp.right != None:
                    temp = temp.right
                temp.left.right = None
                temp.left = None
                del temp
                self.length -= 1
                
            new_node = Node(key, value)
            new_node.right = self.cache
            self.cache.left = new_node
            self.cache = new_node
        self.length += 1
        

cache = LRUCache(2);

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)    
print(cache.get(2))      
cache.put(4, 4)    
print(cache.get(1))    
print(cache.get(3))      
print(cache.get(4))