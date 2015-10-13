#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

gameplan = range(1, 10, 1)

def print_gameplan():
    global gameplan
    count = 0
    for i in gameplan:
        print i, " ", 
        count += 1
        if count == 3:
            print "\n"
            count = 0

def check_win():
    global gameplan
    win_cond = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
        (2, 5, 8), (0, 4, 8), (2, 4, 6))
    players = ["X", "O"]
    for p in players:
        for i in win_cond:
            count = 0
            for j in i:
                if gameplan[j] == p:
                    count += 1
                    if count == 3:
                        print p, "wins!!!"
                        sys.exit(0)

def main():
    global gameplan
    print_gameplan()

    turn = 1
    round_check = 0
    while True:
        if turn == 1:
            player = "X"
            turn += 1
        elif turn == 2:
            player = "O"
            turn -= 1
        print "Now it's " + player + " turn"
        while True:
            move = input("Make your move: ")
            move -= 1
            if move <= 8 and move >= 0:
                if isinstance(gameplan[move], int):
                    gameplan[move] = player
                    break
        print_gameplan()
        check_win()
        round_check += 1
        if round_check == 9:
            print "It's a draw!"
            sys.exit(0)

if __name__=='__main__':
    main()
