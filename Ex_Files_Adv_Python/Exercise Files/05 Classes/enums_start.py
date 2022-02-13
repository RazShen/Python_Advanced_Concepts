# define enumerations using the Enum base class
from enum import Enum,auto

class Grades(Enum):
    A=1
    B=2
    C=3
    D=4
    E = auto()

def main():

    # TODO: enums have human-readable values and types
    print(Grades.A)
    print(type(Grades.A))
    print(repr(Grades.A))

    # TODO: enums have name and value properties
    print(Grades.A.name, Grades.A.value)
    # TODO: print the auto-generated value
    print(Grades.E.name, Grades.E.value)

    # TODO: enums are hashable - can be used as keys
    myGrades = {}
    myGrades[Grades.B] = "nice"
    print(myGrades[Grades.B])

if __name__ == "__main__":
    main()
