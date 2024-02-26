#!/bin/python

import sys

m  = move = 0
if len(sys.argv) > 1:
    m = sys.argv[1]
    if m not in ["0","-1", "+1"]:
        print('m = move changed to 0, only acceptable values are ', ["0","-1", "+1"])
        m  = move = 0
    
y  = window_size     = 7
bl = buffer_len      = 20
b  = buffer          = [f'Element {a}' for a in range(buffer_len)]
bp = buffer_pointer  = 0
e  = elements        = b[bp:bp+y]
ep = element_pointer = 0
first                = 0
last                 = b.index(b[-1])
pretty_m             = m
repeat               = True
m                    = int(m)
while repeat is True:
    bazingo = str('\u0332    ep     bp    ep + bp    y     y - 1     m    first     last    buffer_len')
    print('{:s}'.format('\u0332'.join(bazingo)))
    print("   ", ep,'    ', bp,'      ', ep + bp, '     ', y ,'     ', y - 1, "    ", pretty_m, "    ", first, "      ", last, "        ", bl)
    if m > 0: ## ## Move Down
        if ep >= y - 1:
            if ep == last:
                ep = 0
                bp = 0
            else:
                bp += 1
                ep += 1
            e = b[bp:bp + y]
        else:
            ep += 1
    elif m < 0: ## ## Move Up
        if ep == 0:
            if bp == first:
                bp = last - y + 1
                ep = last
            else:
                bp -= 1
            e = b[bp:bp + y]
        elif ep == bp:
            bp -= 1
            ep -= 1
            e = b[bp:bp + y]
        else:
            ep -= 1

    wp = window_pointer  = ep - bp 
    bazingo = str('\u0332    ep     bp    ep + bp    y     y - 1     m    first     last    buffer_len')
    print('{:s}'.format('\u0332'.join(bazingo)))
    print("   ", ep,'    ', bp,'      ', ep + bp, '     ', y ,'     ', y - 1, "    ", pretty_m, "    ", first, "      ", last, "        ", bl)
    for x,z in enumerate(e):
        if x is wp:
            print(f'{x}--> {z}')
        else:
            print(f'{x}    {z}')

    my_input = input()
    if my_input == 'q':
        repeat = False
