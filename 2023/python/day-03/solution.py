# test_input = """
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664......
# """

# import re

# matrix = [re.split(r"\D", line) for line in test_input.splitlines() if line]

# symbols = ["*" "#", "+", "$"]
# total = 0

# for i, row in enumerate(matrix):
#     for j, cell in enumerate(row):
#         if cell != "":
#             num = int(cell)
#             for di in [-1, 0, 1]:
#                 for dj in [-1, 0, 1]:
#                     if di == 0 and dj == 0:
#                         continue
#                     ni, nj = i + di, j + dj
#                     if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
#                         if matrix[ni][nj] != "" and matrix[ni][nj] in symbols:
#                             total += num
#                             break
#                 else:
#                     continue
#                 break

# # print(f"The sum of the numbers to a symbol is {total}")
# import itertools

# # matrix = [list(line) for line in test_input.splitlines() if line]

# with open("input.txt", "r") as file:
#     matrix = [list(line.strip()) for line in file]

# symbols = ["*", "#", "+", "$"]
# total = 0

# for i, row in enumerate(matrix):
#     for j, cell in enumerate(row):
#         if cell.isdigit() and (j == 0 or not row[j - 1].isdigit()):
#             num = int("".join(itertools.takewhile(str.isdigit, row[j:])))
#             for di in [-1, 0, 1]:
#                 for dj in [-1, 0, 1]:
#                     if di == 0 and dj == 0:
#                         continue
#                     ni, nj = i + di, j + dj
#                     if 0 <= ni < len(matrix) and 0 <= nj < len(row):
#                         if matrix[ni][nj] in symbols:
#                             total += num
#                             break
#                 else:
#                     continue
#                 break

# print(f"The sum of the numbers to a symbol is {total}")


import sys
import re
from collections import defaultdict

D = open("input.txt").read().strip()
lines = D.split("\n")
G = [[c for c in line] for line in lines]
R = len(G)
C = len(G[0])

p1 = 0
nums = defaultdict(list)
for r in range(len(G)):
    gears = set()  # positions of '*' characters next to the current number
    n = 0
    has_part = False
    for c in range(len(G[r]) + 1):
        if c < C and G[r][c].isdigit():
            n = n * 10 + int(G[r][c])
            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if 0 <= r + rr < R and 0 <= c + cc < C:
                        ch = G[r + rr][c + cc]
                        if not ch.isdigit() and ch != ".":
                            has_part = True
                        if ch == "*":
                            gears.add((r + rr, c + cc))
        elif n > 0:
            for gear in gears:
                nums[gear].append(n)
            if has_part:
                p1 += n
            n = 0
            has_part = False
            gears = set()

print(p1)
p2 = 0
for k, v in nums.items():
    if len(v) == 2:
        p2 += v[0] * v[1]
print(p2)
