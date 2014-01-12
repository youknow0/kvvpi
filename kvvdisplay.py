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
	time = d.time
	if d.time == "sofort":
		time = "0"
	elif "min" in d.time:
		time = time.replace(" min", "")
	str_departure = ("%s %s %s" % (d.route.ljust(2), time, d.destination))

	menu.add_item(MenuItem(str_departure.encode('ascii', errors='replace'), 0))

menu.get_action()()
