
curses
=
Python curses - simple 3 panel display

> [!CAUTION]
> Under development


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

|Are|
|:-:|
|centered|

|Are|
|:-:|
|centered|


|centered|
|:-:|




|Flinstones, meet the Flintstones, a modern stone age family|
|:--------------------------------------------------------------------:|

<p align="center">
<b>Flinstones, meet the Flintstones, a modern stone age family</b>
</p>
<br>

      ┌───────────────────────┐      ┌───────────────────────┐      ┌───────────────────────┐
      │         box1          │      │         box2          │      │         box3          │
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

