# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 15:31:21 2019

Creating A simple black jack game using OOP in Python

@author: paras
"""

from MainPackage import Classes

def take_bet():
    while True:
        try:
            betvalue=int(input('Enter your bet value: '))
        except:
            print('Whoops! That is not a bet value.\nPlease Reenter')
            continue
        else:
            if(betvalue>Classes.Chips.total):
                print('Sorry!! You do not have enough Chips.\nPlease Reenter different bet amount')
                continue
            else:
                break

def hit(deck,hand):
    deck.deal()

playing=True




'''
d1=Classes.Deck()
d1.shuffle()


test_player= Classes.Hand()
pull_card=  d1.deal()
print(pull_card)
test_player.add_card(pull_card)
print(test_player.value)
'''