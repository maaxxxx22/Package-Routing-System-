# Self adjusting HashMap class data structure. 
class HashMap:

    # HashMap Constructor function
    # Space-Time complexity: O(1)
    def __init__(self, hash_len=10):
        self.size = hash_len
        self.map = [None] * self.size
        
    # Self adjusting index getter that assigns index to packages inserted into the hashmap according to their package id by using the modulus operator performed against the size (length) of the hashmap. For this project, the hashmap length is set to 10
    # Space-Time complexity: O(1)
    def _get_bucket_index(self, id):
        index = int(id) % self.size
        return index

    # Space-Time complexity: O(1)
    def insert(self, id, row):
        hashIndex = self._get_bucket_index(id)
        hashValue = {id: row}
        if self.map[hashIndex] is None:
            self.map[hashIndex] = hashValue
        else:
            self.map[hashIndex][id] = row
        return True

    # Space-Time complexity: O(1)   
    def get(self, id):
        hashIndex = self._get_bucket_index(id)
        if self.map[hashIndex] is not None:
            return self.map[hashIndex][id]
        return None

    # Space-Time complexity: O(1)   
    def lookup(self, id, attribute):
        hashIndex = self._get_bucket_index(id)
        row = self.map[hashIndex][id]
        return row[attribute]

    # Space-Time complexity: O(1)   
    def delete(self, id):
        hashIndex = self._get_bucket_index(id)
        self.map[hashIndex].pop(id, "Package Not Found")
        return True

    # Space-Time complexity: O(n)   
    def print(self, id):
        hashIndex = self._get_bucket_index(id)
        print(f"\nPackage {id}: ")
        values = self.map[hashIndex][id]
        for i in values.keys():
            if i != "Pkg ID":
                print(f"{i}: {values[i]}")
