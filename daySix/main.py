def aocday6(distinct_char):
    # Read input file
    sequence = distinct_char
    with open("input.txt", "r") as f:
        # Read each line
        l = f.readlines()[0]
        for i in range(sequence, len(l)): #what is the sequence?
            # Check if the character is already in the string
            # if the character is not in the string
            # add it to the string and increment the sequence
            #if l[i] not in l[:sequence]:
            if len(set(l[i-sequence:i])) == sequence:
                # print the character/string
                print(i)
                break
        
# Main function
if __name__ == "__main__":
    aocday6(4)
    aocday6(14)