class myHashTable():
    def __init__(self, length):
        self.data = [None] * length

    def __hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % len(self.data)
        return hash

    def add(self, key, value):
        index = self.__hash(key)
        if not self.data[index]:
            self.data[index] = []
            self.data[index].append([key, value])
        else:
            self.data[index].append([key, value])
        return self.data

    def get(self, key):
        index = self.__hash(key)
        for key,value in self.data[index]:
            if key == key:
                return value

    def keys(self):
        keys = []
        for key in self.data:
            if key and len(key) > 0:
                for key,value in key:
                    keys.append(key)
        return keys

    def values(self):
        values = []
        for value in self.data:
            if value and len(value) > 0:
                for key,value in value:
                    values.append(value)
        return values

h = myHashTable(10)
h.add("size", 11)
h.add("size1", 11)
h.add("size2", 11)
h.add("size3", 11)
h.add("size4", 11)
h.add("size5", 11)
print(h.get("size"))
print(h.values())
print(h.keys())
print(h.data)