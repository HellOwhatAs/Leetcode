#
# @lc app=leetcode.cn id=722 lang=python3
#
# [722] 删除注释
#

# @lc code=start
from typing import List

class Solution:
    @staticmethod
    def new_state(state, char: str):
        if state == '/':
            if char == '/': return char, '//'
            elif char == '*': return char, '/*'
        elif state == '*':
            if char == '/': return char, '*/'
        return char, None

    def removeComments(self, source: List[str]) -> List[str]:
        ret = []
        state, multi_line = None, False
        for line in source:
            if not multi_line:
                if not (ret and not ret[-1]):
                    ret.append([])
            for char in line:
                state, token = self.new_state(state, char)
                if not multi_line and token == '//':
                    ret[-1].pop()
                    state = None
                    break
                elif not multi_line and token == '/*':
                    ret[-1].pop()
                    multi_line = True
                    state = None
                    continue
                elif multi_line and token == '*/':
                    multi_line = False
                    state = None
                    continue
                if not multi_line: ret[-1].append(char)
        return [''.join(i) for i in ret]
                    
# @lc code=end

# print(Solution().removeComments(source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
# print(Solution().removeComments(["a/*comment", "line", "more_comment*/b"]))
# print(Solution().removeComments(["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"]))
print(Solution().removeComments(["a//*b//*c","blank","d*//e*//f"]))
print(Solution().removeComments(["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]))