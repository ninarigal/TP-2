#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from es_ES.py import words

import random

def menu():
    print("1. Play")
    print("2. See words list")
    print("3. Quit")
    num = int(input("Select at most one option: "))
    while num != 1 or num != 2 or num != 3:
        num = int(input("Select at most one option: "))
    if num == 1:
        play()
    elif num == 2:
        pass#words_list
    else:
        pass#quit

def play():
    print("1 . Human hangman")
    print("2. Computer hangman")
    print("3. Go back")
    mode = int(input("Select at most one option: "))
    while mode != 1 or mode != 2 or mode != 3:
        mode = int(input("Select at most one option: "))
    if mode == 1:
        human_hangman()
    elif mode == 2:
        #computer_hangman()
        pass
    else:
        menu()

def human_hangman():
    chances = 5
    word = random.choice(words)
    leters_entered = (" ")
    for i in word:
        print("_", end=" ")
    while chances > 0:
        print (str(chances), "tries remaining" )
        character = input("Choose a character: ")
        chances -= 1
        for i in word:
            if character == i:
                leters_entered.append(character)
                print(i, end= " (" + leters_entered + ")")
            else:
                leters_entered.append(character)
                print("_", end= " (" + leters_entered + ")")


