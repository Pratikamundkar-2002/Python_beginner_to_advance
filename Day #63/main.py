
# EXERCISE -
# Stone-Papper-Scissor Game :-

import random   # to generate the random numbers

def check(comp, user):
    if comp==user: # draw then return 0
        return 0
# then print all the loosing conditions for user
    if (comp==0 and user==1):
        return -1

    if (comp==1 and user==2):
        return -1
    
    if (comp==2 and user==0):
        return -1
    
    return 1
    
comp= (random.randint(0,2)) # random integer will be generated from 0 to 2
user = int(input("0 for Stone, 1 for Paper, 2 for Scissors:\n"))
print("You", user)
print("computer", comp)

score= check(comp, user)
if (score==0):
    print("Its a draw")
elif (score==-1):
    print("You Lose")
else:
    print("You Won")