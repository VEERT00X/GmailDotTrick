import random

def listToString(list): 
    
    str1 = "" 
    
    for ele in list: 
        str1 += ele  
    
    return str1 


def split(word):
    return [char for char in word]


def GenerateEmail(email):
    GeneratedEmail = email
    Adress = split(word=GeneratedEmail)

    numOfElementInList = len(Adress)
    RandomNumberGenerator = random.randint(1, (numOfElementInList-1))
    Adress.insert(RandomNumberGenerator,".")
    Adress = listToString(list=Adress)
    return Adress

def Main(email):
    EmailString = (GenerateEmail(email=email))

    with open ("output.env", "r") as fileRead:
        data=fileRead.read()
    
    if EmailString in data:
        print("Email already generated.")
    else:
        with open ("output.env", 'a') as fileWrite:
            fileWrite.write(EmailString)
            fileWrite.write("@gmail.com")
            fileWrite.write("\n")
    Main(email=EmailString)