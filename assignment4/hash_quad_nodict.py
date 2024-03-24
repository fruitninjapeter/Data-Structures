class HashTable:

    def __init__(self, table_size):  # can add additional attributes
        self.table_size = table_size  # initial table size
        self.hash_table = [None] * table_size  # hash table
        self.num_items = 0  # empty.txt hash table
        self.key_storage = []    # hold keys which have been quadratically probed to index not original hash value

    def insert(self, key, value=None):  # Inserts an entry into the hash table
        # Value can be any object but when used with the concordance it's a Python List of line numbers.
        h = self.horner_hash(key)  # Use Horner hash function to determine index
        inserted = self.insert_helper(key, h, value)
        if inserted == -1:  # Use quadratic probing to resolve collisions
            newhash = self.quadratic_probe_helper(key, h)    # index of key on hash table
            self.key_storage.append([key, newhash])
            self.insert_helper(key, newhash, value)
        if self.get_load_factor() > 0.5:  # If load factor is greater than 0.5 after an insertion
            self.reset_hash_table()  # resize hash table and rearrange all values

    def quadratic_probe_helper(self, key, h):   # helper function for quadratic probing, returns new index
        i = 1
        while self.hash_table[(h + (i * i)) % self.table_size] is not None and \
                self.hash_table[(h + (i * i)) % self.table_size][0] != key:  # if key stored in index is duplicate
            i += 1
        return (h + (i * i)) % self.table_size

    def insert_helper(self, key, hashindex, value=None):    # helper function for insert
        if self.hash_table[hashindex] is None:  # If the key is not already in table it's inserted along with the value
            self.hash_table[hashindex] = (key, value)  # The key is a string and value is any object (ex: Python List)
            self.num_items += 1
        elif self.hash_table[hashindex][0] == key:  # If the key is in the table, new value replaces existing value.
            self.hash_table[hashindex] = (key, value)
        else:
            return -1   # Collision: resort to quadratic sorting

    def key_index_store(self, key):  # looks in self.key_storage for quadratically sorted key's index
        for element in self.key_storage:
            if element[0] == key:
                return element[1]  # return index
        return None  # no key? no index!

    def reset_hash_table(self):  # helper function to resize and reset hash table whenever load factor gets too high
        oldhashtable = self.hash_table  # store old hashable
        self.table_size = (self.table_size * 2) + 1  # hash table size should be increased (doubled + 1).
        self.hash_table = [None] * self.table_size
        self.num_items = 0
        self.key_storage = []
        for element in oldhashtable:  # iterate through all elements in old hash table
            if element is not None:  # if there is a key value pair in old hash table
                self.insert(element[0], element[1])  # Reinstall key value pairs

    def horner_hash(self, key):  # Compute the hash value by using Horner’s rule, as described in project specification.
        if len(key) < 8:  # n is minimum of len(key) and 8
            n = len(key)
        else:
            n = 8
        h = 0
        for i in range(0, n):  # Compute and return an integer from 0 to the (size of the hash table) - 1
            h += ord(key[i]) * 31 ** (n - 1 - i)
        return h % self.table_size

    def in_table(self, key):  # Returns True if key is in an entry of the hash table, False otherwise. Must be O(1).
        h = self.horner_hash(key)
        if self.hash_table[h] is not None:  # Must be 0(1) when there are no collisions
            if self.hash_table[h][0] == key:
                return True
            if self.key_index_store(key) is not None:
                return True
        return False

    def get_index(self, key):  # Returns the index of the hash table entry containing the provided key.
        h = self.horner_hash(key)
        if self.hash_table[h] is not None:  # Must be O(1) if there ain't a collision
            if self.hash_table[h][0] == key:
                return h
            return self.key_index_store(key)    # returns index after quadratic probe or None
        return None  # If there is not an entry with the provided key, returns None.

    def get_all_keys(self):  # Returns a Python list of all keys in the hash table.
        keylist = []
        for element in self.hash_table:  # iterate through each element in hash table
            if element is not None:  # if element isn't none...
                keylist.append(element[0])    # put key in list
        return keylist

    def get_value(self, key):  # Returns the value (for concordance, list of line numbers) associated with the key.
        h = self.horner_hash(key)
        if self.hash_table[h]:
            if self.hash_table[h][0] == key:    # Must be O(1) when there are no collisions
                return self.hash_table[h][1]
            newhash = self.key_index_store(key)
            if newhash is not None:
                return self.hash_table[newhash][1]
        return None  # If key is not in hash table, returns None.

    def get_num_items(self):  # Returns the number of entries (words) in the table. Must be O(1).
        return self.num_items

    def get_table_size(self):  # Returns the size of the hash table.
        return self.table_size

    def get_load_factor(self):  # Returns the load factor of the hash table (entries / table_size).
        return float(self.num_items / self.table_size)
