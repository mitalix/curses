
curses
=
Python curses - simple 3 panel display

Most recent version using element_selector.py

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


![alt text](https://github.com/mitalix/curses/blob/main/Screenshot_2024-02-17_00-45-06.png?raw=true)
