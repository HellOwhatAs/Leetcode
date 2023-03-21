class Solution:
    def printBin(self, num: float) -> str:
        ret = []
        while num != 0 and len(ret) <= 30:
            num *= 2
            ret.append(tmp := int(num))
            num -= tmp
        return "0." + "".join(map(str, ret)) if num == 0 else "ERROR"

print(Solution().printBin(0.625))
print(Solution().printBin(0.1))