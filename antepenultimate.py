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
curses.curs_set(0)
# stdscr.erase()
# stdscr.refresh()

continue_machine = True
##################################################
## ## ## This is where we gather the information 
## ## ## This is where we do all the stuff
## ## ## like mathematical incantations
##################################################
stuff = 2 # The headings
border = stuff # same category as stuff, but the pipe and dash symbol
border_and_stuff = border + stuff # by chance the border features are normalized and equal each other

##################################################
class Window:
    def __init__(self, name, box, element_pointer, buffer_pointer):  
        self.name = name
        self.box = box
        self.element_pointer = element_pointer ## ## formerly box1 (or boxn) pointer
        self.buffer_pointer = buffer_pointer ## ## formerly box buffer pointer
        self.content = [f'{name.title()}-{chr(65 + a)}-Element-{b}' for b in range(20)] 
        h,w = self.box.getmaxyx()
        self.height = h - border_and_stuff
        self.width  = w - border
        # self.height = 5
    def playtime(self):
        h,w = self.box.getmaxyx()
        self.height = h - stuff - 1
        self.width  = w - border
    def bark(self):
        bow_wow = "bark bark! "
        print(bow_wow)
        # self.box.addstr(5,5,bow_wow)
        stdscr.addstr(bow_wow)
    def doginfo(self):
        stdscr.addstr(f"element_pointer is {str(self.element_pointer)} :: ")
##################################################
## ## ## This is where we incantate the boxes, the entities, the things
##################################################
# n is the number, the number we have chosen randomly, out of the hat, out of the blue, on a blue moon.
#this_range=10
#stdscr.addstr(f'{n}')
# number_of_boxes = n
## ## ################################### ## ## ##
## ## ################################### ## ## ##

n = 3
pane = { 'height': curses.LINES * n  // (n + 1) - border_and_stuff , 'width' : curses.COLS  // (n + 1) - border_and_stuff  }
nlines       = curses.LINES    * n  // (n + 1)
ncols        = curses.COLS         // (n + 1)
begin_y      = curses.LINES       // (n + 1) // (n + 1) ## ## or // (n + 1) // ((n + 1) ** 2)
begin_x      = curses.COLS       // (n + 1)
space = curses.COLS             // ((n + 1) ** 2)
#begin_y      = curses.LINES   // (n + 1) // 2 # Can't decide if it's better or worse, keep this line around
increment = space ## ## We increment the increment, but keep space safe

dictionary_of_content  = {} ## ## ########### ## ## ##
box                    = []
win                    = []
focus                  = []

pointer_indicator      = 0
## ## ################################### ## ## ##
## ## Create n windows
## ## ################################### ## ## ##

for a in range(n):
    win.append(Window(f'box{a}', curses.newwin( nlines, ncols, begin_y + 1, increment + 1), 0, 0))
    increment += space + ncols
    focus.append(win[a].name)

## ## ################################### ## ## ##
## ## Now we are ready to enter the meat grinder
## ## ################################### ## ## ##
while continue_machine:
    ## ## ################################### ## ## ##
    ## ## Print out those boxes to the screen
    ## ## ################################### ## ## ##

    # win[a].box.addstr(win[a].element_pointer + 3,2,f'{win[a].content[0]:^{pane["width"]}}', curses.A_NORMAL)
    if pointer_indicator != 0:
        win[box_index].element_pointer = (win[box_index].element_pointer + pointer_indicator) % win[box_index].height
        pointer_indicator = 0
    for a in range(n):
        win[a].box.clear()
        win[a].box.box()
        win[a].box.addstr(1,2,f'{win[a].name:^{pane["width"]}}')
        win[a].box.addstr(2,0,f'├{"─":─^{pane["width"]+2}}┤')
        for line, element in enumerate(win[a].content[:pane['height']]):
            win[a].box.addstr(line + 3, border, element[:pane['width']])
        ## Highlight the column pointer when not selected as DIM
        this_y = win[a].element_pointer
        win[a].box.addstr(win[a].element_pointer + 3,2,f'{win[a].content[this_y]:^{pane["width"]}}', curses.A_REVERSE | curses.A_DIM)
        # win[a].box.addstr(win[a].element_pointer + 3,2,f'{win[a].content[0]:^{pane["width"]}}', curses.A_REVERSE | curses.A_DIM)
    ## Highlight the focus, i.e., focus[0], the heading or title
    box_index = int(focus[0][3:])
    win[box_index].box.addstr(1,2,f'{win[box_index].name:^{pane["width"]}}', curses.A_REVERSE)
    ## Highlight the focus, i.e., focus[0], the heading or title
    win[box_index].box.addstr(win[box_index].element_pointer + 3,2,f'{win[box_index].content[win[box_index].element_pointer]:^{pane["width"]}}', curses.A_REVERSE | curses.A_ITALIC)




    # this_index = win[box_index].element_pointer
    # win[box_index].box.addstr(win[box_index].element_pointer + 3,2,f'{win[box_index].content[  win[box_index].element_pointer  this_index]:^{pane["width"]}}', curses.A_REVERSE | curses.A_ITALIC)
        # this_y = win[box_index].height
        # stdscr.addstr(str(this_y))
        # win[box_index].doginfo()
        # win[box_index].element_pointer += pointer_indicator % this_y
        # win[0].bark()
        # this_y = win[box_index].playtime.height
    ## ## refresh them all ... now!!! ## ## 
    ## ## refresh them all ... now!!! ## ## 
    ## ## refresh them all ... now!!! ##                                    ## 
    ## ## Refresh them all ... Now!!! ## ## 
    [win[a].box.refresh() for a in range(n)]

    ## ## ################################### ## ## ##
    the_user_presses_the_key_et_voila = stdscr.getkey()
    ## ## ################################### ## ## ##
    match the_user_presses_the_key_et_voila:
        case 'q': 
            continue_machine = False
        case '\t' | "KEY_RIGHT":
            focus.append(focus.pop(0)) # Cycle through the modules
        case "KEY_BTAB" | "KEY_LEFT":
            focus.insert(0,focus.pop()) # Cycle backwards through the modules
        case "KEY_DOWN":
            pointer_indicator = +1
        case "KEY_UP":
            pointer_indicator = -1


##################################################
## ## ################################### ## ## ##
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
## ## ################################### ## ## ##
##################################################

# dictionary_of_windows = {} ## ## ########### ## ## ##