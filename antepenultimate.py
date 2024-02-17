#!/bin/python

import curses

##################################################
## ## ################################### ## ## ##
##################################################

stdscr = curses.initscr()
stdscr.refresh()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

##################################################
## ## ## This is where we gather the information 
## ## ## This is where we do all the stuff
## ## ## like mathematical incantations
##################################################
stuff = 2 # The headings
border = stuff # same category as stuff, but the pipe and dash symbol
border_and_stuff = border + stuff # by chance the border features are normalized and equal each other

antepenultimate = { 'y': curses.LINES,                        'x': curses.COLS }
penultimate     = { 'y': antepenultimate['y'] * 3 // 4,       'x': antepenultimate['x'] * 1 // 4 }
ultimate        = { 'y': penultimate['y'] - border_and_stuff, 'x': penultimate['x'] - border_and_stuff }

vertical_poll_position = antepenultimate['y'] * 1 // 8 # Arbitrarily nice at the top of the screen
##################################################
## ## ## This is where we incantate the boxes, the entities, the things
##################################################
# n is the number, the number we have chosen randomly, out of the hat, out of the blue, on a blue moon.
n = 7
number_of_boxes = n
list_of_boxes = range(number_of_boxes)

## ## ################################### ## ## ##
dictionary_of_windows = {} ## ## ########### ## ## ##
## ## ################################### ## ## ##
nlines       = penultimate['y']
ncols        = antepenultimate['x']//n
begin_y     = vertical_poll_position
begin_x = (antepenultimate['x']//(n+2))

for a in list_of_boxes:
    dictionary_of_windows.update( {
        f'box{a}':
            curses.newwin(
                nlines,
                ncols,
                begin_y,
                (a + 3) + (a * begin_x))
        } ) 

## ## ################################### ## ## ##
## ## Print them on the screen
## ## ################################### ## ## ##
for pane in dictionary_of_windows:
    dictionary_of_windows[pane].box()
    dictionary_of_windows[pane].addstr(4,border,f"pane = {pane}"[:ultimate['x']])
    dictionary_of_windows[pane].refresh()

## ## ################################### ## ## ##
the_user_presses_the_key_et_voila = stdscr.getkey()
## ## ################################### ## ## ##

##################################################
## ## ################################### ## ## ##
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
## ## ################################### ## ## ##
##################################################





## ## ################################### ## ## ##
## ## Aperture or visible panel
## ## 
## ## ################################### ## ## ##
##################################################
## ## ################################### ## ## ##
