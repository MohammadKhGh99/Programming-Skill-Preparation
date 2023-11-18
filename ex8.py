from typing import Union, List, Tuple, Any


# 1 - Implement a hash table and write functions to insert, delete, and search for elements.
# there is two types of hashing, open hashing and closed hashing, I will use closed one
class HashTable:
    def __init__(self, size):
        self.size = size
        # self.table: List[None, List[Tuple[Any, Any]]] = [None] * size
        self.table = [None] * size
    
    def _hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        # take the hash code and clap it to fit in table
        i = self._hash_function(key)
        # if the i'th place in table is occupied then add it to the list in it, if not make new list in i'th place
        if self.table[i] is None:
            self.table[i] = [(key, value)]
        else:
            self.table[i].append((key, value))
    
    def delete(self, key):
        i = self._hash_function(key)
        if self.table[i] is not None:
            for pair in self.table[i]:
                if pair[0] == key:
                    self.table[i].remove(pair)
    
    def search(self, key):
        i = self._hash_function(key)
        if self.table[i] is not None:
            for pair in self.table[i]:
                if pair[0] == key:
                    return pair[1]
        return None


if __name__ == '__main__':
    # Question 1
    hash_table = HashTable(10)
    hash_table.insert("key1", "value1")
    hash_table.insert("key2", "value2")
    hash_table.insert("key3", "value3")
    
    print("Searching For \"key1\": " + str(hash_table.search("key1")))
    hash_table.delete("key1")
    print("Searching For \"key1\": " + str(hash_table.search("key1")))
