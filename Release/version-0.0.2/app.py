import random # Using random we will generate random number to add "." in random place in [email] .

email = 'e-x-a-m-p-l-e' # Insert your email here example: ('v-e-e-r-t-0-0-x') (Works only with gmail).


        
def Generate():
    x = email.split("-")
    numOfElementInList = len(x)
    Rnum = random.randint(2, (numOfElementInList-1))
    x.insert(Rnum,".")
    
    listToStr = ''.join(map(str, x))
  
    

    with open ("output.env", "r") as fileRead:
        data=fileRead.read()


    if listToStr in data:
        fileRead.close()
        return
    else:  
        fileWrite = open("output.env", "a")

        fileWrite.write(listToStr)
        fileWrite.write("@gmail.com")
        fileWrite.write("\n")
        fileWrite.close()


while True:
    Generate()





