# Connor Murphy         Student ID:001093925      WGU Data Structures and Algorithms 2 C950



class HashMap:
    def __init__(self):
        self.size = 40
        self.map = [None] * self.size





    # Extremly basic hash function for storage since daily package list are increments of one, this saves memory, runtime, and confusion to anyone touching up the code
    def makeHash(self, key):
        hashKey = int(key) - 1
        return hashKey




    def insert(self, key, package):
        hashKey = self.makeHash(key)
        hashValue = [key, package]

        if self.map[hashKey] is None:
            self.map[hashKey] = hashValue
            return True
        else:
            print("Multiple packages with the same ID detected, asses this package visually and contact your supervisor. Package ID's are 1 to 1")
            return False




    def lookUp(self, key):
        hashKey = self.makeHash(key)

        if self.map[hashKey] is not None:
            return self.map[hashKey]
        else:
            return None
