#!/usr/bin/env python3

import random, sys 

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uick')
        playermove = input()
        if playermove == 'q':
            print('GG my friend, see you next time')
            sys.exit() #Quick the program
        if playermove == 'r' or playermove == 'p' or playermove == 's':
            break # Break out of the player input loop.
            print('Type one of r, p, s, or q.')


    #Display what the player choose:
    if playermove == 'r':
        print('ROCK versus...')
    elif playermove == 's':
        print('Scissors versus...')
    elif playermove == 'p':
        print('Paper versus...')

    #Display what the computer choose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK!')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER!')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS!')
    
    #Display and record win/loss/tie:

    if playermove == computerMove:
        print('It is a  tie!')
        ties = ties + 1
    elif playermove == 'r' and computerMove == 's':
        print('You win this round!')
        wins = wins + 1
    elif playermove == 's' and computerMove == 'r':
        print('You lose this round!')
        losses = losses + 1 
    elif playermove == 'p' and computerMove == 'r':
        print('You win this round!')
        wins = wins + 1
    elif playermove == 'r' and computerMove == 'p':
        print('You lose this round!')
        losses = losses + 1
    elif playermove == 's' and computerMove == 'p':
        print('You win this round!')
        wins = wins + 1
    elif playermove == 'p' and computerMove == 's':
        print('You lose this round!')
        losses = losses + 1