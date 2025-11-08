print("WELCOME TO LIBRARY SECTION")
while True:
    print("1.ADD A NEW BOOK")
    print("2.CHANGE A BOOK")
    print("3.VIEW ALL BOOK")
    print("4.SEARCH BOOK")
    print("5.DELETE BOOK")
    print("6.EXIT")
    chioce=int((input))

    match(choice):
        case 1:
            section=input("ENTER THE SECTION OF BOOK-")
            branch=input("ENTER THE BRANCH OF BOOK-")
            name=input("ENTER THE NAME OF BOOK-")
            title=int(input("ENTER THE TITLE OF BOOK-"))
            o.addSection(section,branch,name,title)
        case 2:
            sectionname=input("ENTER SECTION_NAME-")
            
            