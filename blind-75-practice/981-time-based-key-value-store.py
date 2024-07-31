import bisect
class TimeMap:

    def __init__(self):
        self.my_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.my_map:
            self.my_map[key] = []
        self.my_map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_map:
            return ""
        values = self.my_map[key]
        i = bisect.bisect_right (values, (timestamp, chr(255))) -1
        return values[i][1] if i >= 0 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)