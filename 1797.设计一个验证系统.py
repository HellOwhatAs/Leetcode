#
# @lc app=leetcode.cn id=1797 lang=python3
#
# [1797] 设计一个验证系统
#

# @lc code=start

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.data = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.data[tokenId] = currentTime + self.timeToLive


    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.data and self.data[tokenId] > currentTime: self.data[tokenId] = currentTime + self.timeToLive


    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.data = {k: v for k, v in self.data.items() if v > currentTime}
        return len(self.data)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
# @lc code=end

obj = AuthenticationManager(5)
print(obj.generate("aaa", 1))
print(obj.renew("aaa", 2))
print(obj.countUnexpiredTokens(6))
print(obj.generate("bbb", 7))
print(obj.renew("aaa", 8))
print(obj.renew("bbb", 10))
print(obj.countUnexpiredTokens(15))