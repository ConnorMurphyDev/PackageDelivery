# Connor Murphy, WGU C950, Data structures and algorithms 2
# Referencing this:
# https://www.youtube.com/watch?v=9HFbhPscPU0


class hashMap:
    def __init__(self):
        self.size = 40 #change this to be adaptive
        self.map = [None] * self.size


    """Right now each packageID is just 1,2,3,4,5. add better hash function"""
    def makeHash(self, key):
        hashKey = int(key) - 1
        return hashKey


    def insert(self, key, value):
        hashKey = self.makeHash(key)
        hashValue = [key, value]

        if self.map[hashKey] is None:
            #self.map[hashKey] = list([hashValue])
            self.map[hashKey] = hashValue
            return True
        else:
            print("Ohh shit. How did that happen? This is 1 to 1")
            #update with collision correction
            return False


    def lookUp(self, key):
        hashKey = self.makeHash(key)

        if self.map[hashKey] is not None:
            return self.map[hashKey]
        else:
            return None