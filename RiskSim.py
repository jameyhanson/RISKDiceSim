'''
Created on Jan 5, 2017

@author: Jamey Hanson
Desc: Simulate rolling dice in Risk game attacks to 
      find the probability of each outcome
Usage: RiskSim.py [number_trials]
'''
__author__ = 'Jamey Hanson (jamey@cloudera.com)'
__version__ = '1.0'

from random import randrange
from sys import argv

class Die:  # 6-side die
    def __init__(self):
        self.value = 1
        
    def get_value(self):
        return self.value
    
    def roll(self):
        self.value = randrange(1, 7)

def sim_rolls(num_rolls, attack_dice, defend_dice):
    a_dice = {}
    d_dice = {}
    
    both_lose_1 = 0
    a_lose_1 = 0
    a_lose_2 = 0
    d_lose_1 = 0
    d_lose_2 = 0
    
    for attack in range(attack_dice):
        a_dice[attack] = Die()
        
    for defend in range(defend_dice):
        d_dice[defend] = Die()
        
    for roll in range(num_rolls):
        attack_loss = 0
        defend_loss = 0
        
        # roll attack dice
        a_rolls = []
        for a in range(attack_dice):
            a_dice[a].roll()
            a_rolls.append(a_dice[a].get_value())
        a_rolls.sort(reverse = True)
        
        # roll defend dice
        d_rolls = []
        for d in range(defend_dice):
            d_dice[d].roll()
            d_rolls.append(d_dice[d].get_value())
        d_rolls.sort(reverse = True)
        
        # see who won the round
        for check in range(min(attack_dice, defend_dice)):
            if a_rolls[check] > d_rolls[check]:
                defend_loss += 1
            else:
                attack_loss += 1
                
        # increment counters
        if (attack_dice == 3 or attack_dice == 2) and defend_dice == 2:
            if attack_loss == 0:
                d_lose_2 += 1
            elif attack_loss == 1:
                both_lose_1 += 1
            else:
                a_lose_2 += 1
        elif attack_dice == 1 and defend_dice == 2:
            if attack_loss == 0:
                d_lose_1 += 1
            else:
                a_lose_1 += 1
        else:
            if attack_loss == 1:
                a_lose_1 += 1
            else:
                d_lose_1 += 1
        
    output = '{0:0d}\t{1:0d}\t{2:.1%}\t\t{3:.1%}\t\t{4:.1%}\t\t{5:.1%}\t\t{6:.1%}' \
            .format(attack_dice, defend_dice, a_lose_2/num_rolls, both_lose_1/num_rolls, \
            d_lose_2/num_rolls, a_lose_1/num_rolls, d_lose_1/num_rolls)
    return output.replace('0.0%', '  -')

def main():
    try:
        num_rolls = int(argv[1])
    except IndexError:
        num_rolls = 1000

    print('\naDice\tdDice\ta_lose_2\tboth_lose_1\td_lose_2\ta_lose_1\td_lose_1')
    print('=' * 88)
    
    for defend_dice in range(2, 0, -1):
        for attack_dice in range(3, 0, -1):
            print(sim_rolls(num_rolls, attack_dice, defend_dice))
            
if __name__ == '__main__':
    main()
        
