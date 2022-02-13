# Demonstrate the usage of namdtuple objects

import collections


def main():
    # TODO: create a Point namedtuple

    Point = collections.namedtuple("Point", "x y")
    p1 = Point(1,2)
    p2 = Point(3,4)
    print(p1.x,p2)
    # TODO: use _replace to create a new instance
    p1 = p1._replace(x=6)
    print(p1)


if __name__ == "__main__":
    main()
