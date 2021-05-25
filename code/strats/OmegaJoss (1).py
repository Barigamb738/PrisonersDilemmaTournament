import random

#THIS IS OMEGA JOSS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def strategy(history, memory):
    #vars
    TotalAgression = 0 #How many times it defected
    TotalNiceness = history.shape[1]+1-TotalAgression #How many times it cooped
    choice = 1 #The choice of Omega Joss. duh.
    nextChoice = None #This overwrites the next move of Omega Joss

    #parameters (test for best value)
    chance = 0.8 #initial chance of defecting. TEST DONE
    forgive = 50 #Omega Joss will forgive after "forgive" turnes. TEST DONE
    gracePeriod = 10 #10 - 20 => 4, 30 => 5, 40 => 6 We need no more tests to see that lower values are better. TEST DONE
    #So what is we eliminate it. Not a good idea. 0 => 6 New test found 10 => 6
    #I need more tests.
    #10 proved to be inconsistent.
    #So i am going with 20
    #I just had the idea to leave these comments where i talk to myself so others can see it.
    #Or at the very least Cary. Hi Cary 
    grimThreshold = 40

    if history.shape[1] < 1: #If it's the first round
        return choice, [TotalAgression, nextChoice] #Then Cooperate
    TotalAgression = memory[0] #Reading memory
    nextChoice = memory[1] #Same
    if nextChoice is not None: #Overwriteing any decision if nextChoice is not None
        choice = nextChoice #      ^
        nextChoice = None #        ^
    elif TotalAgression >= grimThreshold:
        choice = 0
    elif TotalAgression == history.shape[1]: #If it always defected then we defect
        choice = 0
    elif random.random() <= (chance - TotalAgression/(history.shape[1]+1) + TotalNiceness/(history.shape[1]+1)) and history[0, -1] != 0 and history.shape[1] >= gracePeriod: 
        #Randomization and makeing sure it is not the grace period and that we avoid defecting twice in a row
        choice = 0  
    elif history[1,-1] == 0 and not iProvoked(history, history.shape[1], history.shape[1], forgive):
        #If he defected and i didn't provoke that defection then i defect.
        #The check for who provoked cancels most of the echo effect explained in this video
        #https://www.youtube.com/watch?v=BOvAbjfJ0x0
        choice = 0  
        TotalAgression += 1
    elif iProvoked(history, history.shape[1], history.shape[1], forgive):
        #if i provoked i wanna make up for it by cooperating not just on this turn but also the next
        nextChoice = 1
    return choice, [TotalAgression, nextChoice] #Return the function. duh


#2 interconnected recursive functions to fiugure out who provoked or who started the chain.
#I can't be bothered to explain this.
#Maybe later
def iProvoked(history, n, nOriginal, forgive):
    if nOriginal - n >= forgive:
        return True
    if(history.shape[0] <= n+1 or n-history.shape[0]-1 <= history.shape[0]):
        return False
    if history[0, n-history.shape[0]-1] == 0:
        return not heProvoked(history, n-1, nOriginal, forgive)
    else:
        return False

def heProvoked(history, n, nOriginal, forgive):
    if nOriginal - n >= forgive:
        return False
    if(history.shape[1] <= n+1 or n-history.shape[1]-1 <= history.shape[1]):
        return False
    if history[1, n-history.shape[1]-1] == 0:
        return not iProvoked(history, n-1, nOriginal, forgive)
    else:
        return False