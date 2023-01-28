#
# @lc app=leetcode.cn id=341 lang=python3
#
# [341] 扁平化嵌套列表迭代器
#
# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
def func(nestedList):
    for i in nestedList:
        if i.isInteger():
            yield i.getInteger()
        else:
            for j in func(i.getList()):
                yield j
class NestedIterator:
    def __init__(self, nestedList):
        self.iter=iter(func(nestedList))
        self.tmp=None

    def next(self) -> int:
        if self.tmp==None:return next(self.iter)
        ret=self.tmp
        self.tmp=None
        return ret
    
    def hasNext(self) -> bool:
        if self.tmp!=None:return True
        try:
            self.tmp=next(self.iter)
            return True
        except:
            return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end