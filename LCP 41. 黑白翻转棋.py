from typing import List, Tuple, Iterable
from itertools import product
class Solution:
    def directed_update(self, chessboard: List[List[str]], it: Iterable[Tuple[int, int]]):
        childs = []
        for x, y in it:
            if chessboard[x][y] == 'O': childs.append((x, y))
            elif chessboard[x][y] == '.': break
            else:
                for a, b in childs: chessboard[a][b] = 'X'
                return childs
        return []

    def update(self, chessboard: List[List[str]], i: int, j: int):
        all_childs = []
        all_childs.extend(self.directed_update(chessboard, ((_, j) for _ in range(i - 1, -1, -1))))
        all_childs.extend(self.directed_update(chessboard, ((_, j) for _ in range(i + 1, self.m))))
        all_childs.extend(self.directed_update(chessboard, ((i, _) for _ in range(j - 1, -1, -1))))
        all_childs.extend(self.directed_update(chessboard, ((i, _) for _ in range(j + 1, self.n))))
        all_childs.extend(self.directed_update(chessboard, zip(range(i - 1, -1, -1), range(j - 1, -1, -1))))
        all_childs.extend(self.directed_update(chessboard, zip(range(i + 1, self.m), range(j - 1, -1, -1))))
        all_childs.extend(self.directed_update(chessboard, zip(range(i + 1, self.m), range(j + 1, self.n))))
        all_childs.extend(self.directed_update(chessboard, zip(range(i - 1, -1, -1), range(j + 1, self.n))))
        for a, b in all_childs:
            self.update(chessboard, a, b)

    def func(self, chessboard: List[List[str]], i: int, j: int):
        before = sum(i.count('O') for i in chessboard)
        self.update(chessboard, i, j)
        after = sum(i.count('O') for i in chessboard)
        return before - after

    def flipChess(self, chessboard: List[str]) -> int:
        self.m, self.n = len(chessboard), len(chessboard[0])
        return max(
            self.func(
                [
                    ['X' if (i == i0 and j == j0) else elem1 for j0, elem1 in enumerate(elem)]
                    for i0, elem in enumerate(chessboard)
                ], 
                i, j
            ) 
            for i, j in product(range(self.m), range(self.n))
            if chessboard[i][j] == '.'
        )


print(Solution().flipChess(chessboard = ["....X.","....X.","XOOO..","......","......"]))
print(Solution().flipChess(chessboard = [".X.",".O.","XO."]))
print(Solution().flipChess(chessboard = [".......",".......",".......","X......",".O.....","..O....","....OOX"]))