'''
Rock Paper Scissors
-------------------------------------------------------------
'''

import random
import re 
import os


def play_status():
    valid_responses = ['yes', 'no']
    while True:
        try:
            response = input("Would you like to play ? '(Yes or No)' ")
            if response.lower() not in valid_responses:
                raise ValueError(" Yes or No ")
            if response.lower() == 'yes':
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Thanks for playing! ")
                exit()
        except ValueError as err:
            print(err)

def play_rps():
    pass