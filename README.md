
curses
=
Python curses - simple 3 panel display

> [!WARNING]
> Under development, unstructured, not even using functions, repeating a lot of useless code

Twofold solution to write the program and simultaneously utilize gitub for source control

### Navigate between three seperate windows
* **TAB** - move horizontally
* **ENTER** - select a command
* **UP/DOWN**- navigate elements in panel

### Objective
#### box1 - Select (future) commands
* To launch or manage dnsmasq
* Launch PXE environment, i.e., dhcp, tftp and nfs
* Launch a QEMU image to PXE boot
* Prepare environment for metal server to PXE boot

#### box2 - Monitor and poll dnsmasq service
#### box3 - Launch continuous scrolling "journalctl -fex" using subprocess
* Capability to scroll up into history
* Hot key to scroll to bottom

##### (The background color isn't showing up correctly for box headings)


<p align="center">
<b>Flinstones, meet the Flintstones, a modern stone age family</b>
</p>

     ┌───────────────────┐     ┌───────────────────┐     ┌───────────────────┐
     │       box1        │     │       box2        │     │       box3        │
     ├───────────────────┤     ├───────────────────┤     ├───────────────────┤
     │ Element-0         │     │ Element-0         │     │ Element-0         │
     │ Element-1         │     │ Element-1         │     │ Element-1         │
     │ Element-2         │     │ Element-2         │     │ Element-2         │
     │ Element-3         │     │ Element-3         │     │ Element-3         │
     │ Element-4         │     │ Element-4         │     │ Element-4         │
     │ Element-5         │     │ Element-5         │     │ Element-5         │
     │ Element-6         │     │ Element-6         │     │ Element-6         │
     │ Element-7         │     │ Element-7         │     │ Element-7         │
     │ Element-8         │     │ Element-8         │     │ Element-8         │
     │ Element-9         │     │ Element-9         │     │ Element-9         │
     │ Element-10        │     │ Element-10        │     │ Element-10        │
     └───────────────────┘     └───────────────────┘     └───────────────────┘


![alt text](https://github.com/mitalix/curses/blob/main/Screenshot_2024-02-17_00-45-06.png?raw=true)
