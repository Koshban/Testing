'''
Implement a time-based key-value data structure that supports:

Storing multiple values for the same key at specified time stamps
Retrieving the key's value at a specified timestamp
Implement the TimeMap class:

TimeMap() Initializes the object.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".
Note: For all calls to set, the timestamps are in strictly increasing order.

Example 1:
Input:
["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]
Output:
[null, null, "happy", "happy", null, "sad"]

Explanation:
TimeMap timeMap = new TimeMap();
timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
timeMap.get("alice", 1);           // return "happy"
timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
timeMap.get("alice", 3);           // return "sad"

'''
import unittest

class TimeMap:

    def __init__(self):
        self.store = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store.keys():
            self.store[key].append([timestamp, value])
            print(f"1. Key is {key} and Val is {self.store[key]}")
        else:
            self.store[key]= [[timestamp, value]]
            print(f"2. Key is {key} and Val is {self.store[key]}")      

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store.keys():
            return None
        print(self.store)
        values = self.store.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            #print(f"Mid is {mid} and Values are {values} and MIds Val is {values[mid][0]} and its Type is {type(values[mid][0])}")
            if int(values[mid][0]) <= timestamp:
                l = mid + 1
            elif int(values[mid][0]) > timestamp:
                r = mid -1
        if r == -1:
            return None
        return values[r][1]
        
class TestTimeMap(unittest.TestCase):
    def setUp(self):
        self.timeMap = TimeMap()

    def test_example_1(self):
        # Test case from the example
        self.timeMap.set("alice", "happy", 1)
        self.assertEqual(self.timeMap.get("alice", 1), "happy")
        self.assertEqual(self.timeMap.get("alice", 2), "happy")
        self.timeMap.set("alice", "sad", 3)
        self.assertEqual(self.timeMap.get("alice", 3), "sad")

    def test_non_existent_key(self):
        # Test getting a key that doesn't exist
        self.assertEqual(self.timeMap.get("nonexistent", 1), None)

    def test_multiple_values(self):
        # Test multiple values for the same key
        self.timeMap.set("test", "value1", 1)
        self.timeMap.set("test", "value2", 2)
        self.timeMap.set("test", "value3", 3)
        
        self.assertEqual(self.timeMap.get("test", 1), "value1")
        self.assertEqual(self.timeMap.get("test", 2), "value2")
        self.assertEqual(self.timeMap.get("test", 3), "value3")
        self.assertEqual(self.timeMap.get("test", 4), "value3")

    def test_timestamp_between_values(self):
        # Test getting value with timestamp between stored timestamps
        self.timeMap.set("key", "value1", 1)
        self.timeMap.set("key", "value2", 10)
        
        self.assertEqual(self.timeMap.get("key", 5), "value1")

    def test_timestamp_before_first(self):
        # Test getting value with timestamp before first stored timestamp
        self.timeMap.set("key", "value1", 5)
        self.assertEqual(self.timeMap.get("key", 1), None)

    def test_multiple_keys(self):
        # Test handling multiple keys
        self.timeMap.set("key1", "value1", 1)
        self.timeMap.set("key2", "value2", 1)
        
        self.assertEqual(self.timeMap.get("key1", 1), "value1")
        self.assertEqual(self.timeMap.get("key2", 1), "value2")

if __name__ == '__main__':
    unittest.main()
