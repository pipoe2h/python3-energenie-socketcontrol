Energenie SocketControl
=========

This python script allows you to configure and operate the Energenie remote control sockets through a Raspberry Pi with
the Energenie Pi-mote control board.

The python script has been only tested with Raspbian OS.

![alt tag](https://energenie4u.co.uk/res/images/products/large/ENER002-2PI.jpg)

Requirements
------------

An Energenie Pi-mote control board and at least one remote control socket are required.
- ([Pi-mote control board - ENER314](https://energenie4u.co.uk/catalogue/product/ENER314))
- ([Remote controlled socket - ENER002](https://energenie4u.co.uk/catalogue/product/ENER002-2PI))

Python3 and elevated privileges (sudo) are required.

Arguments
---------

The arguments to be passed to this python program are:
- Socket (1-4). Type the desired socket number to control 
- State (on/off). Type the desired action to perform

Dependencies
------------

This python scripts requires of the following Debian packages:
- build-essential
- python3-dev
- python3-gpiozero
- python3-pkg-resources 

Example
-------

To run the python program the socket number and state must be introduced.

- Help
```
# sudo python3 socketcontrol.py -h
usage: socketcontrol.py [-h] socket status

positional arguments:
  socket      socket number to control (1-4)
  status      turn on/off the socket (on/off)

optional arguments:
  -h, --help  show this help message and exit

```

- Configure or Power on socket 1
```
# sudo python3 socketcontrol.py 1 on
Turning on socket: 1

```

- Configure or Power off socket 1
```
# sudo python3 socketcontrol.py 1 off
Turning off socket: 1

```

License
-------

MIT

Author Information
------------------

* [Jose Gomez](https://github.com/pipoe2h) | [www](http://www.joseluisgomez.com) | [twitter](http://twitter.com/pipoe2h)
