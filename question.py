# Answer to programming question for:
# Programming Bootcamp Volunteer Tutor Expression of Interest - Semester 1, 2020

# ====================================================

# Read a list of integers from user input.

def readInt():
    aListOfIntegers = list()
    quit = False
    while not quit:
        integer = input("Please enter an integer (enter q for quit): ")
        if integer == "q":
            break
        aListOfIntegers.append(int(integer))

    print()

    return aListOfIntegers

# ====================================================

# Find all pairs of numbers in the list whose
# product is even and whose sum is odd.

def findPairs(aListOfInt):
    aListOfPairs = []
    length = len(aListOfInt)
    for i in range(0, length):
        for j in range(0, length):
            if j != i:
                if ((aListOfInt[j] * aListOfInt[i]) % 2 == 0) and ((aListOfInt[j] + aListOfInt[i]) % 2 == 1):
                    if aListOfInt[j] > aListOfInt[i]:
                        high = aListOfInt[j]
                        low = aListOfInt[i]
                    else:
                        high = aListOfInt[i]
                        low = aListOfInt[j]
                    if [low, high] not in aListOfPairs:
                        aListOfPairs.append([low, high])

    return aListOfPairs

# ====================================================

# Print out a formatted list of the pairs.

def prettyString(aListOfPairs):
    print("The following are pairs whose product is even and sum is odd:")
    for pair in aListOfPairs:
        print("- " + str(pair[0]) + " and " + str(pair[1]))

# ====================================================

if __name__ == "__main__":
    prettyString(findPairs(readInt()))
    # print(readInt())










