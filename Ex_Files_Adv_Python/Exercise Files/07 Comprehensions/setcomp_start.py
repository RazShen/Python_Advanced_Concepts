# Demonstrate how to use set comprehensions


def main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # TODO: build a set of unique Fahrenheit temperatures
    uniqueFahr = {x*9/5 +32 for x in ctemps}
    print(uniqueFahr)
    # TODO: build a set from an input source
    inputChars = "what a nice day to be alive, so many emptions"
    upperSet = {c.upper() for c in inputChars if not c.isspace() and not c ==","}
    print(upperSet)
if __name__ == "__main__":
    main()
