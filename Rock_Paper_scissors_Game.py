# Rock paper scissor GAME
import random
def check(comp,user):
    if(comp == user):
        return 0
    if(comp ==4 and user ==3 ):
        return -1
    if(comp ==3 and user == 5):
        return -1
    if(comp ==5 and user == 4):
        return -1
    return 1

comp = random.randint(3,5)
user = int(input("3  for ROCK, 4 for PAPER, 5 for SCISSORS:\n"))

SCORE = check(comp,user)

print("YOU:", user)
print("COMPUTER:", comp)

if(SCORE ==0):
    print("its draw")
elif(SCORE == -1):
    print("you lose")
else:
    print("you won")
