# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def myFunction(arg1, arg2, *, supressException=False):
    pass


def main():
    # try to call the function without the keyword
    myFunction(1, 2, supressException=True)
    #every param defined after an asterisk must be specified

if __name__ == "__main__":
    main()
