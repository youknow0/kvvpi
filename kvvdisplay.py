#!/usr/bin/env python

from kvvliveapi.kvvliveapi import get_departures
from lcdmenu.LCDMenu import *
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

STOP_ID = "de:8212:31"

lcd = Adafruit_CharLCDPlate()
lcd.begin(16, 2)

menu = Menu(lcd, "Main Menu")

departures = (get_departures(STOP_ID))

for d in departures:
	str_departure = ("%s %s %s" % (d.time, d.route, d.destination))

	menu.add_item(MenuItem(str_departure.encode('ascii', errors='replace'), 0))

menu.get_action()()
