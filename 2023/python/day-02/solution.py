import sys
from collections import defaultdict

with open("input.txt", encoding="utf-8") as f:
    # read_data = f.read()
    p1 = 0
    p2 = 0
    for line in f.read().splitlines():
        ok = True
        id_, line = line.split(":")
        V = defaultdict(int)
        for event in line.split(";"):
            for balls in event.split(","):
                n, colour = balls.split()
                n = int(n)
                V[colour] = max(V[colour], n)
                if int(n) > {"red": 12, "green": 13, "blue": 14}.get(colour, 0):
                    ok = False
        score = 1
        for v in V.values():
            score *= v
        p2 += score
        if ok:
            p1 += int(id_.split()[-1])
print(p1)
print(p2)


# def solve_part1(input):
#     # solution
#     pass


# def solve_part2(input):
#     # solution
#     pass


# if __name__ == "__main__":
#     with open("input.txt", "r") as file:
#         input = file.read().strip()
#         print(solve_part1(input))
#         print(solve_part2(input))
