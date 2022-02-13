import itertools
# advanced iteration functions in the itertools package


def testFunction(x):
    return x< 40


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    itercycle1 = itertools.cycle(seq1)
    print(next(itercycle1))
    print(next(itercycle1))
    print(next(itercycle1))
    print(next(itercycle1))
    print(next(itercycle1))
    print(next(itercycle1))


    # TODO: use count to create a simple counter
    itercount = itertools.count(100, 10)
    print(next(itercount))
    print(next(itercount))
    print(next(itercount))
    print(next(itercount))



    # TODO: accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30]


    iteraccum = itertools.accumulate(vals)
    print(next(iteraccum))
    print(next(iteraccum))
    print(next(iteraccum))

    iteracaccumMax = itertools.accumulate(vals,max)
    print(list(iteracaccumMax))

    # TODO: use chain to connect sequences together

    iterchain = itertools.chain("ABCD","1234")
    print(list(iterchain))
    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    iterdrop = itertools.dropwhile(testFunction, vals)
    print(list(iterdrop))
    itertake = itertools.takewhile(testFunction, vals)
    print(list(itertake))
if __name__ == "__main__":
    main()
    