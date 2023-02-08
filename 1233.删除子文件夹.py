#
# @lc app=leetcode.cn id=1233 lang=python3
#
# [1233] 删除子文件夹
#

# @lc code=start
from typing import List
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        filesys, ret = {}, []
        folder.sort(key=len)
        for path in folder:
            p = filesys
            for folder in path[1:].split('/'):
                if folder in p and not p[folder]: break
                else:
                    if not folder in p: p[folder] = {}
                    p = p[folder]
            else:
                ret.append(path)
        return ret
# @lc code=end

print(Solution().removeSubfolders(folder = ["/a/b/c","/a/b/ca","/a/b/d"]))