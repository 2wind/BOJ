import sys


class Sudoku:
    def __init__(self):
        self.col = [[0 for j in range(9)] for i in range(9)]
        self.row = [[0 for j in range(9)] for i in range(9)]
        self.box = [[0 for j in range(9)] for i in range(9)]
    
    def get(self, i, j):
        return self.col[i][j]

    def get_candidates(self, i, j):
        full = set(range(1, 10))
        near = set()
        near.update(self.col[i])
        near.update(self.row[j])
        near.update(self.box[(i//3)*3 + j // 3])
        if 0 in near:
            near.remove(0)
        return list(full - near)

    def put(self, i, j, n):
        self.col[i][j] = n
        self.row[j][i] = n
        self.box[(i//3)*3 + j // 3][(i%3)*3 + j%3] = n

    def _check_lst(self, lst):
        compared = set()
        for i in lst:
            if i > 0:
                if i in compared:
                    return False
                else:
                    compared.add(i)
        return True

    def _check_horizontal(self, i, j):
        return self._check_lst(self.col[i])
    def _check_vertical(self, i, j):
        return self._check_lst(self.row[j])
    def _check_box(self, i, j):
        return self._check_lst(self.box[(i//3)*3 + j // 3])

    def check_sudoku(self, i, j):
        return self._check_horizontal(i,j) and self._check_vertical(i, j) and self._check_box(i, j)

    def __str__(self):
        str_list = []
        for col in self.col:
            str_list.append("".join(map(str, col)))

        return "\n".join(str_list)

        

sudoku = Sudoku()
    
for i in range(9):
    numbers = [int(x) for x in  list(sys.stdin.readline().strip())]
    for j in range(9):
        sudoku.put(i, j, numbers[j])


def solve(number, sudoku):
    if number == 81:
        print(sudoku)
        return True
    else:
        i, j = number // 9, number % 9
        if sudoku.get(i, j): # 1~9
            return solve(number +1, sudoku)
        else: # 0
            numbers = sudoku.get_candidates(i, j)
            numbers.sort()
            for n in numbers:
                sudoku.put(i, j, n)
                if solve(number +1, sudoku):
                    return True
                sudoku.put(i, j, 0)
            return False

solve(0, sudoku)



