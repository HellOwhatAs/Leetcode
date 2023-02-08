#
# @lc app=leetcode.cn id=1233 lang=python3
#
# [1233] 删除子文件夹
#

# @lc code=start
from typing import List
class Solution:
    @staticmethod
    def getleafs(root, prefix = ''):
        if not root: yield prefix
        for folder in root: yield from Solution.getleafs(root[folder], f'{prefix}/{folder}')
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        filesys = {}
        for path in folder:
            p = filesys
            for folder in path[1:].split('/'):
                if folder in p and not p[folder]: break
                else:
                    if not folder in p: p[folder] = {}
                    p = p[folder]
            else: p.clear()
        return list(Solution.getleafs(filesys))
# @lc code=end

print(Solution().removeSubfolders(folder = ["/a","/a/b/c","/a/b/d"]))