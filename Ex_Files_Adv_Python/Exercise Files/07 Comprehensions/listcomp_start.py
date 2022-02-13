# Demonstrate how to use list comprehensions

def even(num):
    return num > 4

def main():
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # TODO: Perform a mapping and filter function on a list
    evenSquared = list(map(lambda t: t**2, filter(lambda e: e > 4 and e < 16, evens)))
    print(evenSquared)

    # TODO: Derive a new list of numbers frm a given list
    evenSquared = [e ** 2 for e in evens if e > 4 and e < 16]
    print(evenSquared)

    # TODO: Limit the items operated on with a predicate condition
    oddsSquared = [e ** 2 for e in odds if e > 3 and e < 17]
    print(oddsSquared)

if __name__ == "__main__":
    main()
