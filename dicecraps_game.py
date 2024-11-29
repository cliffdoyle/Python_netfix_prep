"""Simulating the dice game Craps"""
"""
You roll two six-sided dice, each with faces containing one, two, three, four, five
and six spots, respectively. When the dice come to rest, the sum of the spots on the
two upward faces is calculated. If the sum is 7 or 11 on the first roll, you win. If the sum is 2, 3 or 12 on the first roll (called “craps”), you lose (i.e., the “house”
wins). If the sum is 4, 5, 6, 8, 9 or 10 on the first roll, that sum becomes your
“point.” To win, you must continue rolling the dice until you “make your point”
(i.e., roll that same point value). You lose by rolling a 7 before making your point.
    """
import random
    
def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1=random.randrange(1,7)
    die2=random.randrange(1,7)
    return (die1,die2) #pack die face values into a tuple

def display_dice(dice):
    """Display one roll of the two dice"""
    die1,die2 = dice #unpack the tuple into variables die1 and die2
    print(f'Player rolled {die1}+{die2}={sum(dice)}')

die_values=roll_dice() #first roll
display_dice(die_values)

#determine game status and point, based on first roll
sum_of_dice=sum(die_values)

if sum_of_dice in (7,11): #win
    game_status='Won'
elif sum_of_dice in (2,3,12): #lose
    game_status='Lost'
else: 
    game_status='Continue'
    my_point=sum_of_dice
    print('Point is',my_point)

#Continue rolling until player wins or loses
while game_status=='Continue':
    die_values=roll_dice()
    display_dice(die_values)
    sum_of_dice=sum(die_values)
    
    if sum_of_dice==my_point: #win by making point
        game_status='Won'
    elif sum_of_dice==7:
        game_status='Lost'
        
#display "wins" or "loses" message
if game_status=='Won':
    print('Player Wins')
else:
    print('Player loses')