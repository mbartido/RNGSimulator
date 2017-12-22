Hearthstone Random Damage Simulator
===================


### What is this? ###
This is a command line simulator of random damage done in Hearthstone. You input both heroes' health and each minion and their health, as well as random damage done, and you get the output of the chances of each character dying.
## Example Run ##

    Welcome to heartstone chance calculator.
    Initializing teams.
    Enter hero one's health: 6
    Enter amount of hero one's minions: 3
    Enter hero two's health: 7
    Enter amount of hero two's minions: 4
    
    
    ----------Summary----------
    Team One-------------------
    Hero 1: 6 health
    Minion 1: (Name: one1, Health: 1)
    Minion 2: (Name: one2, Health: 1)
    Minion 3: (Name: one3, Health: 1)
    Team Two-------------------
    Hero 2: 7 health
    Minion 1: (Name: two1, Health: 1)
    Minion 2: (Name: two2, Health: 1)
    Minion 3: (Name: two3, Health: 1)
    Minion 4: (Name: two4, Health: 1)
    
    
    Do you want to edit minion health? (y/n): y
    Which team do you want to edit? (1/2): 1
    Editing team 1.
    Enter minion 1's health: 1
    Enter minion 2's health: 2
    Enter minion 3's health: 3
    Do you want to edit again? (y/n): y
    Which team do you want to edit? (1/2): 2
    Editing team 2.
    Enter minion 1's health: 4
    Enter minion 2's health: 5
    Enter minion 3's health: 6
    Enter minion 4's health: 7
    
    
    How much random damage do you want to do?: 32
    Proceeding to chance query.
    
    
    Results--------------------
    Hero 1 dies 32.717% of the time with 32 random damage.
    Hero 1 Minions-------------
    Minion 1 dies 97.595% of the time.
    Minion 2 dies 90.55499999999999% of the time.
    Minion 3 dies 78.044% of the time.
    ---------------------------
    Hero 2 dies 16.411% of the time with 32 random damage.
    Hero 2 Minions-------------
    Minion 1 dies 61.514% of the time.
    Minion 2 dies 44.172% of the time.
    Minion 3 dies 28.176000000000002% of the time.
    Minion 4 dies 15.729000000000001% of the time.


### Setup and Installation ###
Note: You will need python 3.6.2 to run this program.
1. Download repository.
2.  Navigate to the main repository using the command line.
3. Type `python main.py`.
4. Program will run.



### Contributors ###
Author: Michael Bartido
Email: michaelvbartido@gmail.com