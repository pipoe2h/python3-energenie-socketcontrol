#!/usr/bin/python3

import argparse
from gpiozero import Energenie

parser = argparse.ArgumentParser()
parser.add_argument("socket", help="socket number to control (1-4)")
parser.add_argument("status", help="turn on/off the socket (on/off)")
args = parser.parse_args()

socket = Energenie(int(args.socket))
if args.status == "on":
   print("Turning on socket:", args.socket)
   socket.on()
if args.status == "off":
   print("Turning off socket:", args.socket)
   socket.off()
