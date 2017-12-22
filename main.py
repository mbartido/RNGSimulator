# Main program for whole thing

from hero import hero
from minion import minion
import random

def main():
    print("Welcome to heartstone chance calculator.")
    print("Initializing teams.")
    
    # Class initialization
    hero1 = hero()
    hero2 = hero()
    # We will keep these as numbers right now    
    hero1Minions = 0            
    hero2Minions = 0
    # These will be the lists of minions of each hero
    hero1List = []
    hero2List = []
    damageCount = 0           # Amount of random damage we want to do
    
    # Initializing hero's info
    # Hero1 health part
    hero1H = heroInput("one")
    hero1.health = hero1H
    # Hero1 minion part
    hero1Minions = minionInput("one")
    minionInitializer("one", hero1Minions, hero1List)
    
    # Hero2 health part
    hero2H = heroInput("two")
    hero2.health = hero2H
    # Hero2 minion part
    hero2Minions = minionInput("two")
    minionInitializer("two", hero2Minions, hero2List)

    # Prints summary of data entered for both heroes' board states
    summary(hero1, hero2, hero1List, hero2List)
    # For editing minion health
    edit(hero1List, hero2List)
    damageCount = dmg()
    heroPercentage(hero1, hero2, hero1List, hero2List, hero1, damageCount)
    
# Takes in team name and returns the input, 
# an int for the hero's health
def heroInput(team):
    health = 0
    try:
        health = int(input("Enter hero " + team + "'s health: "))
    except ValueError:
        print("Sorry not an integer.")
        health = heroInput(team)
    return health

# Takes in team name and returns the input,
# an int for the amount of minion's for that hero 
def minionInput(team):
    minions = 0
    try:
        minions = int(input("Enter amount of hero " + team + "'s minions: "))
    except ValueError:
        print("Sorry not an integer.")
        minions = minionInput(team)
    return minions
    
# Takes in team and number of minions, and 
# initializes those number of minions for that team
def minionInitializer(team, number, minionList):
    if team is "one":        
        for x in range(1, number + 1):
            teamMinion = team + str(x)
            minionList.append(minion(1, teamMinion))
            
    if team is "two":
        for x in range(1, number + 1):
            teamMinion = team + str(x)
            minionList.append(minion(1, teamMinion))
            
# Takes in 2 heros, and 2 sets of minions in lists
# and displays a summary of entered
def summary(hero1, hero2, minionList1, minionList2):
    print("\n")
    print("----------Summary----------")
    print("Team One-------------------")
    print("Hero 1: " + str(hero1.health) + " health")
    for x in minionList1:
        print("Minion " + str(minionList1.index(x) + 1) + ": " + str(x))
    print("Team Two-------------------")
    print("Hero 2: " + str(hero2.health) + " health")
    for x in minionList2:
        print("Minion " + str(minionList2.index(x) + 1) + ": " + str(x))
        
# Asks if person wants to edit minion health's 
# Answer is y/n 
def edit(minionList1, minionList2):
    # this is for going through the list and editing the specific minion healths
    def listIterate(minionList):
        for x in minionList:
            try:
                minionChoice = int(input(
                        "Enter minion " + str(minionList.index(x) + 1) + "'s health: "))
            except ValueError:
                print("Sorry not an integer.")
                minionChoice = int(input(
                        "Enter minion " + str(minionList.index(x) + 1) + "'s health: "))  
            x.health = minionChoice
    
    # this is for choosing the team to edit
    def team():
        teamChoice = input("Which team do you want to edit? (1/2): ")
        if teamChoice == "1":
            print("Editing team 1.")
            listIterate(minionList1)
        elif teamChoice == "2":
            print("Editing team 2.")
            listIterate(minionList2)
        else:
            print("Please enter 1 or 2.")
            team()
            
    # for choosing whether or not you want to edit again
    def again():
        doAgain = input("Do you want to edit again? (y/n): ")
        if doAgain == "y":
            team()
        elif doAgain == "n":
            print("n chose.")
        else:
            print("Please enter y or n.")
            again()
            
    # Main portion of the edit
    print("\n")
    answer = input("Do you want to edit minion health? (y/n): ")
    if answer == "y":
        team()
        again()
    elif answer == "n":
        print("Proceeding to chance query.")
    else:
        print("Please enter y or n.")
        edit(minionList1, minionList2)
    
# Takes in two heroes, two lists, chosen hero, and random damage, and outputs
# percentage time hero is killed and percentage each time each minion is killed
# over n amount of trials (in this case 100000)
def heroPercentage(hero1, hero2, minionList1, minionList2, chosenHero, damage):
    # We will put the potential targets in a dictionary
    # With this set we will run n amount of trials to figure out
    # the percentage of times a chosen hero is killed
           
    # The original dictionary where everything is added
    # Keys will be the minion name and values will be the minion's health
    ourDict = {} 
    k = 0               # Amount of times the chosen hero is killed
    d = 0               # Amount of times the other hero is killed
    n = 100000          # Amound of trials we will perform
    # These 2 lists will hold counters for each time a minion has died     
    list1 = []          # For hero 1
    list2 = []          # For hero 2
    # Initialize minion death counters to zero for each list
    for x in minionList1:
        list1.append(0)
    for x in minionList2:
        list2.append(0)
    
    # Add everything to set
    ourDict[hero1] = hero1.health
    ourDict[hero2] = hero2.health
    for x in minionList1:
        ourDict[x.name] = x.health
    for x in minionList2:
        ourDict[x.name] = x.health
    trialDict = ourDict   # The set we will be performing trials on
    
    # Actual trials
    for x in range(n):
        trialDict = ourDict.copy()
        # Do damage to random targets
        for y in range(1, damage + 1):
            # Get a random minion in dictionary
            randomTarget = random.choice(list(trialDict))
            
            # Subtract one from the target's health
            trialDict[randomTarget] = trialDict[randomTarget] - 1
            
            # Check if chosen hero is dead. If they are break and add one to k
            if trialDict[chosenHero] == 0:
                k = k + 1
                break
                    
            # Break if other hero is dead
            if trialDict[hero1] == 0 or trialDict[hero2] == 0:
                d = d + 1
                break
            
            # If target is dead remove from the dict
            if trialDict[randomTarget] == 0:                
                # If target is minion from list1
                if "one" in randomTarget:
                    # Get number at the end of the minion name
                    number = int(randomTarget[3:len(randomTarget)+1])
                    # Add one to its counter
                    list1[number-1] = list1[number-1] + 1
                    trialDict.pop(randomTarget, None)

                # If target is minion from list2
                else:
                    # Get number at end of minion name
                    number = int(randomTarget[3:len(randomTarget)+1])
                    # Add one to its counter
                    list2[number-1] = list2[number-1] + 1
                    trialDict.pop(randomTarget, None)
        
    # Return the percentage of k/n
    print("\n")
    print("Results--------------------")
    print("Hero 1 dies " + str((k/n) * 100) + "% of the time with " +
          str(damage) + " random damage.")
    print("Hero 1 Minions-------------")
    for x in range(0, len(list1)):
        print("Minion " + str(x + 1) + " dies " + 
              str((list1[x]/n) * 100) + "% of the time.")
    print("---------------------------")
    
    print("Hero 2 dies " + str((d/n) * 100) + "% of the time with " +
          str(damage) + " random damage.")
    print("Hero 2 Minions-------------")
    for x in range(0, len(list2)):  
        print("Minion " + str(x + 1) + " dies " +
              str((list2[x]/n) * 100) + "% of the time.")
        
# Asks how much damage and returns that number
def dmg():
    count = 0
    try:   
        print("\n")
        count = int(input("How much random damage do you want to do?: "))
        print("Proceeding to chance query.")
    except ValueError:
        print("Sorry not an integer.")
        count = dmg()
    return count
             
if __name__ == "__main__":
    main()
