import random

def backgammon_roll():
    '''backgammon_roll() -> int
    returns the total of a backgammon roll'''
    # roll two 6-sided dice
    die1=0
    die2=0
    move=0
    while move <= 100:
        die1 = random.randrange(1,7)
        die2 = random.randrange(1,7)
        total = die1 + die2
        if die1 == die2:  # check for doubles
            move += 2*total
        else:
            move += total
    return move
print(backgammon_roll(),"-",backgammon_roll() )