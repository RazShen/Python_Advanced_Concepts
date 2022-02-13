# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*args):
    """ summing of args

    :param args: list of args
    :return: the sum of the args
    """
    res = 0
    for arg in args:
        res += arg
    print(args)
    print("placeholder #1 {} #2 {} #3 {}".format(*args))
    return sum(args)




def main():
    # TODO: pass different arguments
    print(addition(2,4,6))
    print(addition(*[2,4,6]))
    print([2,4,6])
    print(*[2,4,6])
    print((2,4,6))
    print(*(2,4,6))
    # TODO: pass an existing list


if __name__ == "__main__":
    main()
