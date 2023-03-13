from typing import List
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        index = {0: -1}
        diff, ret = 0, 0
        retl, retr = 0, 0
        for idx, elem in enumerate(array):
            diff += 1 if elem.isdigit() else -1
            if diff in index and (l := idx - index[diff]) > ret:
                ret, retl, retr = l, index[diff], idx
            if not diff in index:
                index[diff] = idx
        return array[retl + 1:retr + 1]


print(Solution().findLongestSubarray(["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]))
print(Solution().findLongestSubarray(["A","A"]))
print(Solution().findLongestSubarray(list("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a")))