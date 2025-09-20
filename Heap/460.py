class LFUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2val = {}
        self.key2freq = {} 
        self.freq2key = defaultdict(OrderedDict)
        self.minf = 0 
        
    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        old_freq = self.key2freq[key] 
        self.key2freq[key] += 1
        self.freq2key[old_freq].pop(key) 
        if not self.freq2key[old_freq]:
            del self.freq2key[old_freq] 
        self.freq2key[old_freq+1][key] =1  
        
        if self.minf not in self.freq2key:
            self.minf += 1 
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        if key in self.key2val:
            self.get(key)
            self.key2val[key] = value
            return 
        if len(self.key2val) == self.capacity:
            delkey, _ = self.freq2key[self.minf].popitem(last=False)
            del self.key2val[delkey]
            del self.key2freq[delkey]
        self.key2val[key] = value
        self.key2freq[key] = 1
        self.freq2key[1][key] = 1
        self.minf = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)