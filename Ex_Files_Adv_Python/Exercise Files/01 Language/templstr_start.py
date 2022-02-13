from string import Template
# demonstrate template string functions


def main():
    # Usual string formatting with format()
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)
    
    # TODO: create a template with placeholders
    templ = Template("Watching ${title} by ${author}")



    # TODO: use the substitute method with keyword arguments
    str2 = templ.substitute(title="Jackie Chan", author="You")
    print(str2)


    # TODO: use the substitute method with a dictionary
    data = {
        "author": "You",
        "title":  "Jackie Chan"
    }
    str3 = templ.substitute(data)
    print(str3)
    
if __name__ == "__main__":
    main()
    