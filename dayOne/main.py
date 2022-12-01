def CountingCalories():
    with open("input.txt") as file:
        elves = []
        elf = 0
        for c in [line.rstrip() for line in filecl.readlines()]:
            if c:
                elf += int(c)
            else:
                elves.append(elf)
                elf = 0
        print(max(elves))
        print(sum(sorted(elves, reverse=True)[0:3]))


    # 1. Read the input file
    # 2. Create a list of elves
    # 3. Add the calories of each elf
    # 4. Print the max calories
    # 5. Print the sum of the top 3 elves
# Path: main.py

if __name__ == "__main__":
    CountingCalories()

