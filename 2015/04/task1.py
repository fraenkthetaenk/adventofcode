import hashlib 
secretKey = "bgvyzdsv"
number = 0

solutionNotFound = True

while solutionNotFound:
    number += 1
    resHash = hashlib.md5(str(secretKey + str(number)).encode()).hexdigest()
    if (len(resHash)>=5):
        if(resHash[0:5] == "00000"):
            solutionNotFound = False


print(number)



import hashlib 
secretKey = "bgvyzdsv"
number = 0

solutionNotFound = True

while solutionNotFound:
    number += 1
    resHash = hashlib.md5(str(secretKey + str(number)).encode()).hexdigest()
    if (len(resHash)>=6):
        if(resHash[0:6] == "000000"):
            solutionNotFound = False


print(number)
