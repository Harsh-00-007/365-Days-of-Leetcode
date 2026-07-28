from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}  # key -> (val, freq)
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> OrderedDict of keys

    def _update_freq(self, key: int, val: int = None):
        """Helper to increment frequency of a key."""
        curr_val, freq = self.key_to_val_freq[key]
        if val is not None:
            curr_val = val  # Update value if provided (e.g. during put)
            
        # Remove key from current frequency group
        del self.freq_to_keys[freq][key]
        
        # If the removed key was the last one at min_freq, increment min_freq
        if not self.freq_to_keys[freq] and self.min_freq == freq:
            self.min_freq += 1
            
        # Move key to higher frequency group
        new_freq = freq + 1
        self.key_to_val_freq[key] = (curr_val, new_freq)
        self.freq_to_keys[new_freq][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        
        val, _ = self.key_to_val_freq[key]
        self._update_freq(key)
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # Case 1: Key already exists -> Update value and frequency
        if key in self.key_to_val_freq:
            self._update_freq(key, value)
            return

        # Case 2: Cache is full -> Evict LFU (and LRU tie-breaker)
        if len(self.key_to_val_freq) >= self.capacity:
            # popitem(last=False) pops in FIFO order (least recently used)
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[evict_key]

        # Insert new key with frequency = 1
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1