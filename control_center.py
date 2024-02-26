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
    def __init__(self, name, box, element_pointer, buffer_pointer, something_unique):  
        self.name            = name
        self.box             = box
        self.element_pointer = element_pointer ## ## Highlights the currently selected element
        self.buffer_pointer  = buffer_pointer  ## ## Is the top position of the window pane
        self.content         = [f'{name.title()}-{chr(65 + something_unique)}-Element-{b}' for b in range(20)]  ## content is another word for buffer
        h,w                  = self.box.getmaxyx()
        self.height          = h - border_and_stuff
        self.width           = w - border
        elements_we_need     = self.content[self.buffer_pointer:self.height]
        self.scoop           = [y[:self.width] for y in elements_we_need]
    def recalculate_dimensions(self):
        h,w                  = self.box.getmaxyx()
        self.height          = h - border_and_stuff
        self.width           = w - border
        elements_we_need     = self.content[self.buffer_pointer:self.height + self.buffer_pointer]
        self.scoop           = elements_we_need
        # stdscr.addstr(str(self.content))
        # self.doginfo()

    def bark(self):
        bow_wow = "bark bark! "
        stdscr.addstr(bow_wow)
    def doginfo(self):
        stdscr.addstr(f"element_pointer is {str(self.element_pointer)} :: ")
        stdscr.addstr(f"buffer_pointer is {str(self.buffer_pointer)} :: ")
        stdscr.addstr(f"height is {str(self.height)} :: \n")
##################################################
## ## ## This is where we incantate the boxes, the entities, the things
##################################################
# number_of_boxes = n
n = 5
pane = { 'height': curses.LINES * n  // (n + 1) - border_and_stuff,
         'width' : curses.COLS      // (n + 1)  - border_and_stuff }
nlines       = curses.LINES   * n  // (n + 1)
ncols        = curses.COLS        // (n + 1)
begin_y      = curses.LINES      // (n + 1) // (n + 1) ## ## or // ((n + 1) ** 2)
begin_x      = curses.COLS      // (n + 1)
space        = curses.COLS     // ((n + 1) ** 2)
#begin_y     = curses.LINES   // (n + 1) // 2 # Can't decide if it's better or worse, keep this line around
increment    = space ## ## We increment the increment, but keep space safe

dictionary_of_content  = {} ## ## ########### ## ## ##
win                    = []
focus                  = []
pointer_indicator      = 0
## ## ################################### ## ## ##
## ## Create n windows
## ## ################################### ## ## ##
for a in range(n):
    win.append(Window(f'box{a}', curses.newwin(nlines, ncols, begin_y + 1, increment + 1), 0, 0, something_unique=a))  ## I'll probably get rid of something_unique, later
    increment += ncols + space 
    focus.append(win[a].name)  ## ## create the list of names to focus on 
## ## ################################### ## ## ##
## ## Now we are ready to enter the meat grinder
## ## ################################### ## ## ##
while continue_machine:
    box_index = int(focus[0][3:])
    # win[box_index].doginfo()
#    stdscr.addstr(f'win[box_index].element_pointer is {win[box_index].element_pointer} :: ')
    ## ## ################################### ## ## ##
    ## ## Print out those boxes to the screen
    ## ## ################################### ## ## ##
    if pointer_indicator:   ## If the user presses up or down, synchronize with the element pointer
        if pointer_indicator < 0 and win[box_index].element_pointer < 1:
            win[box_index].element_pointer = win[box_index].height - 2
            win[box_index].buffer_pointer  = win[box_index].content.index(win[box_index].content[-1]) - win[box_index].height + 2
            win[box_index].recalculate_dimensions()
            pointer_indicator = 0
        elif pointer_indicator < 0 and win[box_index].buffer_pointer > 0:
            pass
            # win[box_index].buffer_pointer -= 1
            win[box_index].recalculate_dimensions()
            # pointer_indicator = 0
        elif win[box_index].element_pointer ==  win[box_index].height - 2:  ## pointer_indicator, must, by elimination be positive and not zero
            # stdscr.addstr(f'pointer_indicator is {pointer_indicator} :: ')
            win[box_index].buffer_pointer += 1
            win[box_index].recalculate_dimensions()
            # stdscr.addstr(f'buffer_pointer is {win[box_index].buffer_pointer} :: ')
            if (win[box_index].element_pointer + win[box_index].buffer_pointer) > win[box_index].content.index(win[box_index].content[-1]):
                stdscr.addstr(f'pointer_indicator is {pointer_indicator} :: ')
            # if (win[box_index].element_pointer + win[box_index].buffer_pointer) > win[box_index].height:
                win[box_index].element_pointer = 0
                win[box_index].buffer_pointer  = 0
                win[box_index].recalculate_dimensions()
            pointer_indicator = 0
        win[box_index].element_pointer = (win[box_index].element_pointer + pointer_indicator) % win[box_index].height
        pointer_indicator              = 0
    for a in range(n): ## Display the default state of the screen
        win[a].box.clear()
        win[a].box.box()
        win[a].box.addstr(1,2,f'{win[a].name:^{pane["width"]}}')
        win[a].box.addstr(2,0,f'├{"─":─^{pane["width"]+2}}┤')
        for line, element in enumerate(win[a].scoop):
            win[a].box.addstr(line + 3, border, element)
        ## Highlight the column pointer when not selected and use DIM attribute
        this_y = win[a].element_pointer
        win[a].box.addstr(win[a].element_pointer + 3,border,f'{win[a].scoop[this_y]:^{pane["width"]}}', curses.A_REVERSE | curses.A_DIM)
        ## Highlight the focus, i.e., focus[0], the heading or title
    win[box_index].box.addstr(1,2,f'{win[box_index].name:^{pane["width"]}}', curses.A_REVERSE)
        ## Element which is Highlighted is also italic
    win[box_index].box.addstr(win[box_index].element_pointer + 3,border,f'{win[box_index].scoop[win[box_index].element_pointer]:^{pane["width"]}}', curses.A_REVERSE | curses.A_ITALIC) ## ## Refresh them all ... Now!!! ## ## 
    [win[a].box.refresh() for a in range(n)] ## ## ################################### ## ## ##
    the_user_presses_the_key_et_voila = stdscr.getkey()
        ## ## ################################### ## ## ##
    match the_user_presses_the_key_et_voila:
        case 'q':                      continue_machine  = False
        case '\t'       | "KEY_RIGHT": focus.append(focus.pop(0)) # Cycle through the modules
        case "KEY_BTAB" | "KEY_LEFT":  focus.insert(0,focus.pop()) # Cycle backwards through the modules
        case "KEY_DOWN":               pointer_indicator = +1
        case "KEY_UP":                 pointer_indicator = -1
##################################################
## ## ################################### ## ## ##
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
## ## ################################### ## ## ##
##################################################
                

            # win[box_index].recalculate_dimensions()
            # win[box_index].element_pointer += 1
            # win[0].bark()
            # win[box_index].doginfo()

            # Ideally we want to go to the bottom of the list and perhaps one up from the bottom by ...
            # win[0].bark()
            # setting element_point to become win[box].height - index(win[box].content[-1]), but let us implement that later
            # win[box_index].doginfo()
            # win[box_index].element_pointer = win[box_index].content.index(win[box_index].content[-1])
            # win[box_index].buffer_pointer  = win[box_index].content.index(win[box_index].content[-1])
            # win[box_index].buffer_pointer  = 19 - win[box_index].height - 1
            # if (win[box_index].element_pointer + win[box_index].buffer_pointer) > win[box_index].content.index(win[box_index].content[-1]):
        # win[a].box.addstr(win[a].element_pointer + 3,border,f'{win[a].content[this_y]:^{pane["width"]}}', curses.A_REVERSE | curses.A_DIM)
    # box_index = int(focus[0][3:])






