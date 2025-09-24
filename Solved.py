# N_ROWS is 6 and N_COLS is 5
from WordleGraphics import *

# FIVES and SIXES are all 5-letter and 6-letter English words
from english import FIVES, SIXES


def row_word(n):
    return "".join([gw.get_square_letter(n,i) for i in range(N_COLS)])

def col_word(n):
    return "".join([gw.get_square_letter(i,n) for i in range(gw.get_current_row() + 1)])

def row_color(n, c):
    [gw.set_square_color(n, i, c) for i in range(N_COLS)]

def col_color(n, c):
    [gw.set_square_color(i, n, c) for i in range(N_ROWS)]

def valid_prefix(prefix):
    size = len(prefix)
    return prefix in [word[:size] for word in SIXES]

def enter_action():
    row = gw.get_current_row()
    word = row_word(row) 
    if not word in FIVES:
        row_color(row, MISSING_COLOR)
        return gw.show_message("Not a word")
    if row == (N_ROWS - 1):
        win = True
        for col in range(N_COLS):
           if not col_word(col) in SIXES:
               col_color(col, MISSING_COLOR)
               win = False
        gw.show_message("You win!") if win else gw.show_message("You lose!")
    else:
        bad = False
        for col in range(N_COLS):
            if not valid_prefix(col_word(col)):
               col_color(col, PRESENT_COLOR)
               bad = True
        if bad:
            gw.show_message("No solutions include this word.")
        else:
            [row_color(i, CORRECT_COLOR if i <= row else UNKNOWN_COLOR) for i in range(N_ROWS)]
            gw.set_current_row(row + 1)

gw = WordleGWindow()
gw.add_enter_listener(enter_action)