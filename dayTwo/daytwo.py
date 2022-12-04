
totalScoreMap = {"X": 1, "A": 1, "Y": 2, "B": 2, "Z": 3, "C": 3}
map = {
    ("A", "X"): 3,
    ("A", "Y"): 6,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("B", "Y"): 3,
    ("B", "Z"): 6,
    ("C", "X"): 6,
    ("C", "Y"): 0,
    ("C", "Z"): 3,
}
battle = {(k[0], v): k[1] for k, v in map.items()}
strategy = {"X": 0, "Y": 3, "Z": 6}

with open("./input.txt") as f:
    part1 = 0
    part2 = 0
    for line in f:
        i, mh = line.strip().split(" ")
        part1 += totalScoreMap[mh] + map[(i, mh)]
        part2 += totalScoreMap[battle[(i, strategy[mh])]] + strategy[mh]
    print(part1 + ' ' + part2)