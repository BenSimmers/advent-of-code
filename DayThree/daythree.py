def part1(path):
    diz = dict(zip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 53)))
    with open(path, mode='r') as fr:
        lines = fr.readlines()
    letters = []
    for line in lines:
        sx, dx = line[:len(line)//2], line[len(line)//2:-1]
        common = ''.join((set([letter for letter in sx if letter in dx])))
        letters.append(common)
    return sum(diz[letter] for letter in letters)


def part2(path):
    diz = dict(zip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 53)))
    with open(path, mode='r') as fr:
        lines = [line.strip() for line in fr.readlines()]
    letters = []
    for i in range(0, len(lines), 3):
        line = lines[i:i+3]
        sx, mid, dx = line[0], line[1], line[2]
        common = ''.join((set([letter for letter in sx if letter in mid and letter in dx])))
        letters.append(common)
    return sum(diz[letter] for letter in letters)

if __name__ == '__main__':
    print(part1('input.txt'))
    print(part2('input.txt'))