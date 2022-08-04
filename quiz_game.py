print("Welcome to my computer quiz")
playing = input(" Do you want tp play ?  ")

if playing != "yes":
    quit()
print(" okay let's play :)")
score = 0
answer = input("what does CPU means? ")
if answer == "Central processing unit":
    print('correct !')
    score += 1
else:
    print("incorrect!")


answer = input("what does GCP means? ")
if answer == "Google cloud platform":
    print('correct !')
    score += 1
else:
    print("incorrect!")


answer = input("what does API means? ")
if answer == "Application  programming interface":
    print('correct !')
    score += 1
else:
    print("incorrect!")



answer = input ("what does VM means? ")
if answer == "Virtual machine":
    print('correct !')
    score += 1
else:
    print("incorrect!")



answer = input("what does VPC means? ")
if answer == "Virtual private cloud":
    print('correct !')
    score += 1
else:
    print("incorrect!")

print(" You got" + str(score) + " questions correct! ")
print(" You got" + str((score / 5) * 100) + "%.")



