#!/bin/python


import curses



def shoe_horn(stdscr):
    stdscr.refresh()
    text             = 'Flinstones, meet the Flintstones, a modern stone age family.'
    stdscr.addstr(1, curses.COLS // 2 - len(text) // 2, text)
    this_y, this_x   = stdscr.getmaxyx()
    three_boxes      = ["box1", "box2", "box3"]
    focus            = ["box1", "box2", "box3"]
    box1_list        = [f'Element-{a}' for a in range(20)]
    box2_list        = [f'Element-{a}' for a in range(20)]
    box3_list        = [f'Element-{a}' for a in range(20)]

    height           = this_y * 3 // 4
    width            = this_x    // 4
    y                = this_y   // 8
    x_box1           = (this_x - (3 * width)) // (len(three_boxes) + 1)
    x_box2           = x_box1 + width + x_box1
    x_box3           = x_box2 + width + x_box1
    box1             = curses.newwin(height, width, y, x_box1)
    box2             = curses.newwin(height, width, y, x_box2)
    box3             = curses.newwin(height, width, y, x_box3)
    Enter            = False
    continue_machine = True
    pointer          = 0
    heading_offset   = 4
    box1_pointer     = 0
    box2_pointer     = 0
    box3_pointer     = 0
    box1_index     = 0
    box2_index     = 0
    box3_index     = 0
    
    ## ## ############################################
    ## ## ############################################
    while continue_machine:
    ## ## ############################################
    ## ## Clear the menus
    ## ## ############################################
        box1.erase()
        box2.erase()
        box3.erase()
    ## ## ############################################
    ## ## Create new boxes
    ## ## ############################################
        this_y, this_x = box1.getmaxyx()
    ## ## ############################################
        heading = three_boxes[0]
        box1.box()
        box1.addstr(1,1,f'{heading:^{this_x - 2}}')
        box1.addstr(2,0,f'├{"─":─^{this_x - 2}}┤')
    ## ## ############################################
        heading = three_boxes[1]
        box2.box()
        box2.addstr(1,1,f'{heading:^{this_x - 2}}')
        box2.addstr(2,0,f'├{"─":─^{this_x - 2}}┤')
    ## ## ############################################
        heading = three_boxes[2]
        box3.box()
        box3.addstr(1,1,f'{heading:^{this_x - 2}}')
        box3.addstr(2,0,f'├{"─":─^{this_x - 2}}┤')


    ## ## ############################################
    ## ## Status messages
    ## ## ############################################
        # box1.addstr(4,2, f"Going in ... ")
        # box2.addstr(4,2, f"Going in ... ")
        # box3.addstr(4,2, f"Going in ... ")
        # box1.addstr(5,2, f"box1_pointer is {box1_pointer}")
        # box2.addstr(5,2, f"box2_pointer is {box2_pointer}")
        # box3.addstr(5,2, f"box3_pointer is {box3_pointer}")
        # box1.addstr(6,2, f"pointer is {pointer}")
        box2.addstr(6,2, f"focus[0] is {focus[0]}")
        box2.addstr(7,2, f'Enter or Space is {Enter}')
        Enter = False
        
    ## ## ############################################
    ## ## Initialize the selected menu items
    ## ## ############################################
        box1.addstr(box1_pointer + heading_offset - 1,2,"DINO the Dinosaur", curses.A_REVERSE | curses.A_DIM)
        box2.addstr(box2_pointer + heading_offset - 1,2,"DINO the Dinosaur", curses.A_REVERSE | curses.A_DIM)
        box3.addstr(box3_pointer + heading_offset - 1,2,"DINO the Dinosaur", curses.A_REVERSE | curses.A_DIM)
    ## ## ############################################
    ## ## List elements in pane
    ## ## ############################################
        box1_buffer = box1_list[box1_index:height-heading_offset]
        for line, element in enumerate(box1_buffer):
            box1.addstr(line + 3,2, element[:10])
        box2_buffer = box2_list[box2_index:height-heading_offset]
        for line, element in enumerate(box2_buffer):
            box2.addstr(line + 3,2, element[:10])
        box3_buffer = box3_list[box3_index:height-heading_offset]
        for line, element in enumerate(box3_buffer):
            box3.addstr(line + 3,2, element[:10])
    ## ## ############################################
    ## ## Customize the layout - Highlight the pointer
    ## ## ############################################
        if focus[0] == "box1":
            prev = box1_pointer
            box1.addstr(1,1,f'{focus[0]:^{this_x - 2}}', curses.A_REVERSE)
            # box1.addstr(box1_pointer + heading_offset - 1,2,"BINGO", curses.A_NORMAL)
            box1_pointer = (box1_pointer + pointer) % (height - heading_offset)# if pointer else False
            # box1.addstr(prev + heading_offset - 1,2,f'{" ": ^{this_x - 3}}', curses.A_NORMAL)
            box1.addstr(box1_pointer + heading_offset - 1,2,"BINGO", curses.A_REVERSE | curses.A_ITALIC | curses.A_UNDERLINE | curses.A_BOLD)
    ## ## ############################################
        elif focus[0] == "box2":
            prev = box2_pointer
            box2.addstr(1,1,f'{focus[0]:^{this_x - 2}}', curses.A_REVERSE)
            box2_pointer = (box2_pointer + pointer) % (height - heading_offset) #if pointer else False
            box2.addstr(prev + heading_offset - 1,2,f'{" ": ^{this_x - 3}}', curses.A_NORMAL)
            box2.addstr(box2_pointer + heading_offset - 1,2,"BINGO", curses.A_REVERSE | curses.A_ITALIC | curses.A_UNDERLINE | curses.A_BOLD)
    ## ## ############################################
        elif focus[0] == "box3":
            prev = box3_pointer
            box3.addstr(1,1,f'{focus[0]:^{this_x - 2}}', curses.A_REVERSE)
            box3_pointer = (box3_pointer + pointer) % (height - heading_offset) #if pointer else False
            box3.addstr(prev + heading_offset - 1,2,f'{" ": ^{this_x - 3}}', curses.A_NORMAL)
            box3.addstr(box3_pointer + heading_offset - 1,2,"BINGO", curses.A_REVERSE | curses.A_ITALIC | curses.A_UNDERLINE | curses.A_BOLD)
        pointer = 0
    ## ## ############################################
    ## ## ############################################
    ## ## ############################################
    ## ## Status messages
    ## ## ############################################
        # box1.addstr(9,2, f" . . . Coming out ")
        # box2.addstr(9,2, f" . . . Coming out ")
        # box3.addstr(9,2, f" . . . Coming out ")
        # box2.addstr(8,2, f'Enter or Space is {Enter}')
        box1.addstr(10,2, f"box1_pointer is {box1_pointer}")
        box2.addstr(10,2, f"box2_pointer is {box2_pointer}")
        box3.addstr(10,2, f"box3_pointer is {box3_pointer}")
        # box1.addstr(11,2, f"pointer is {pointer}")
        # box2.addstr(12,2, f"focus[0] is {focus[0]}")
        
    ## ## ############################################
    ## ## Initialize the selected menu items
    ## ## ############################################
        box1.refresh()
        box2.refresh()
        box3.refresh()

        k = stdscr.getkey()

    ## ## ############################################
        match k:
            case 'q':
                continue_machine = False
                # break
            case '\t' | "KEY_RIGHT":
                focus.append(focus.pop(0)) # Cycle through the modules
            case "KEY_BTAB" | "KEY_LEFT":
                focus.insert(0,focus.pop()) # Cycle backwards through the modules
            case "KEY_DOWN":
                # stdscr.addstr(k)
                pointer = 1
            case "KEY_UP":
                # stdscr.addstr(k)
                pointer = -1
            case "\n" | " ":
                stdscr.addstr(k)
                Enter = True
    ## ## ############################################

curses.wrapper(shoe_horn)






    #              if direction == "up":
    #     pointer = (pointer - 1) % (h - 4)
    # else:
    #     pointer = (pointer + 1) % (h - 4)
    # this.chgat(pointer+3,0,curses.A_REVERSE)



            #     focus.append(focus.pop(0)) # Cycle through the modules
            # case "KEY_BTAB":
            #     focus.insert(0,focus.pop()) # Cycle backwards through the modules


            # '├{"─":─^{this_x - 2}}┤
        # box2.addstr(7,2, f"height is {height}")
        # box2.addstr(8,2, f"heading_offset is {heading_offset}")
        # box2.addstr(9,2, f"(box1_pointer + 1) % (height - heading_offset) is {(box1_pointer + 1) % (height - heading_offset)}")
        # box2.addstr(4,2, f"pointer is {pointer}")




