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
