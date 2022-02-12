import sys , random
from functions import split , listToString

NumberOfWrites = 0

def Main():

    argv1 = str(sys.argv[1])

    if argv1 == None:
        print("Error - No argument Email Provided")

    Email = split(argv1)

    numOfElementInList = len(Email)

    RandomNumberGenerator = random.randint(1, (numOfElementInList-1))

    Email.insert(RandomNumberGenerator,".") 

    Email = listToString(list=Email)

    with open ("output.env", "r") as fileRead:
        data=fileRead.read()

    with open ("output.env", 'a') as fileWrite:

        if Email in data:
            print("End")

        else:
            fileWrite.write(Email)
            fileWrite.write("@gmail.com")
            fileWrite.write("\n")    

    Main()

Main()

    


    

