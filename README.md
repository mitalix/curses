# curses
Python curses - simple 3 panel display


Under development
The objective is write the program an simultaneously utilize gitub for source control


Navigate between three seperate windows

TAB - move horizontally
ENTER - select a command
UP/DOWN - navigate elements in panel

Objective: 
  box1 - Select (future) commands
  box2 - Manage and poll dnsmasq service
  box3 - Launch scrolling >journalctl -fex
  
The background color is `#ffffff` for light mode and `#000000` for dark mode.

                     `rgb(9, 105, 218)`Flinstones, meet the Flintstones, a modern stone age family.

      ┌───────────────────────┐      ┌───────────────────────┐      ┌───────────────────────┐
      │        box1`#000000`         │      │         box2          │      │         box3          │
      ├───────────────────────┤      ├───────────────────────┤      ├───────────────────────┤
      │ Element-0             │      │ Element-0             │      │ Element-0             │
      │ Element-1             │      │ Element-1             │      │ Element-1             │
      │ Element-2             │      │ Element-2             │      │ Element-2             │
      │ Element-3             │      │ Element-3is box1      │      │ Element-3             │
      │ Element-4             │      │ Element-4Dinosaur False      │ Element-4             │
      │ Element-5             │      │ Element-5             │      │ Element-5             │
      │ Element-6             │      │ Element-6             │      │ Element-6             │
      │ box1_pointer is 10    │      │ box2_pointer is 4     │      │ box3_pointer is 11    │
      │ Element-8             │      │ Element-8             │      │ Element-8             │
      │ Element-9             │      │ Element-9             │      │ Element-9             │
      │ BINGOnt-10inosaur     │      │ Element-10            │      │ Element-10            │
      │ Element-11            │      │ Element-11            │      │ Element-11inosaur     │
      │ Element-12            │      │ Element-12            │      │ Element-12            │
      │ Element-13            │      │ Element-13            │      │ Element-13            │
      │ Element-14            │      │ Element-14            │      │ Element-14            │
      └───────────────────────┘      └───────────────────────┘      └───────────────────────┘



