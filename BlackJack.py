# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 15:31:21 2019

Creating A simple black jack game using OOP in Python

@author: paras
"""

from MainPackage import Classes

playing=True
replay=False
def take_bet(chips):
    while True:
        try:
            chips.bet=int(input('How many chips would you like to bet?  '))
        except:
            print('Whoops! That is not a bet value.\nPlease Reenter')
            continue
        else:
            if(chips.bet>chips.total):
                print(f'Sorry you do not have sufficient chips. You have: {chips.total} Chips.')
                continue
            else:
                break

def hit(deck,hand):
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
    
def hit_or_stand(deck,hand):
    global playing
    while True:
         x=input('Hit or Stand? Enter h or s  ')
         
         if x[0].lower()=='h':
             hit(deck,hand)
         elif x[0].lower()=='s':
             print("Player Stands Dealer's Turn")
             playing=False
         else:
             print("\nSorry, I didn't understand that, Please enter h or s only! ")
             continue
         break

def show_some(player,dealer):
    print('\nDEALERS HAND:')
    print('one card hidden!')
    print(dealer.cards[1])
    print('\n')
    print('PLAYERS HAND:')
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    print('DEALERS HAND:')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('PLAYERS HAND:')
    for card in player.cards:
        print(card)


def player_busts(player,dealer,chips):
    print('\nPLAYER BUST!!!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('\nPLAYER WINS!!!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('\nPLAYER WINS!!! DEALER BUSTED!')
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print('\nDEALER WINS!!!')
    chips.lose_bet()
    
def push(player,dealer):
    print('\nDealer and Player Tie! PUSH')
    
             
'''
 Setting up the Game Play for Black Jack
'''    

while True:
    # Print an opening statement
    print('\n\n!!!WELCOME TO BLACK JACK GAME!!!')
    
    # Create & shuffle the deck, deal two cards to each player
    deck= Classes.Deck()
    deck.shuffle()
    
    player_hand = Classes.Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    
    dealer_hand = Classes.Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
        
    # Set up the Player's chips
    if not replay:
        player_chips=Classes.Chips()
    
    # Prompt the Player for their bet
    
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value<=21:
        while dealer_hand.value<player_hand.value:
            hit(deck,dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)
    
        # Run different winning scenarios
        if(dealer_hand.value>21):
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif(dealer_hand.value>player_hand.value):
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif(dealer_hand.value<player_hand.value):
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
        
    
    # Inform Player of their chips total 
    print(f'\nPlayer Total Chips are at : { player_chips.total }')
    # Ask to play again
    new_game =input('Would you like to play another hand? y/n ')
    
    if new_game[0].lower()=='y':
      playing=True
      replay=True
      player_chips=Classes.Chips(player_chips.total)
      continue
    else:
       print('\nThank you for playing!!!')
       break    
    
    

