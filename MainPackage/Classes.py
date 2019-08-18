# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:08:24 2019

Creatig the Classes for the BlackJack Game

@author: paras
"""

import random


suits=('Hearts', 'Diamonds', 'Spades','Clubs')
ranks=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}



class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    

class Deck():
    def __init__(self):
        self.deck=[] # starting with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp+='\n'+ card.__str__()
        return 'The deck has: '+ deck_comp
    
    def __len__(self):
        return len(self.deck)
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card=self.deck.pop()
        return single_card
    


class Hand:
    
    def __init__(self):
        self.cards=[] # start with an empty list as we did in the deck class
        self.value=0  # start with zero value
        self.aces=0   # add an attribute  to keep track of aces
    
    def add_card(self,card):
        #card pass in from the Deck.deal() --> single card object(suit,rank)
        self.cards.append(card)
        self.value+=values[card.rank]
        
        #tracking Aces
        if card.rank=="Ace":
            self.aces+=1
                    
    def adjust_for_ace(self):
        #If total value > 1 and I still have an Ace then change my ace value
        #to be 1 instead of 11
        while self.value>21 and self.aces: # if zero treated as FALSE other number not zero are treated as TRUE
            self.value -= 10
            self.aces -= 1
     
        
class Chips:
    
    def __init__(self,chips=100):
        self.total=chips
        self.bet=0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
    
