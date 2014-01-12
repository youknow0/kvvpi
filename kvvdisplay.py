#!/usr/bin/env python

from kvvliveapi.kvvliveapi import get_departures
from lcdmenu.LCDMenu import *
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from time import sleep

STOP_ID = "de:8212:31"


def load_data():
	global menu
	tries = 1
	had_error = True
	departures = None

	while had_error:
		lcd.clear()
		lcd.message("Loading...\ntry %d" % tries)
		
		try:
			departures = (get_departures(STOP_ID))
		except:
			had_error = True
			sleep(0.25)
		else:
			had_error = False

		tries+=1
	
	menu.clear_all_items()

	for d in departures:
		time = d.time
		if d.time == "sofort":
			time = "0"
		elif "min" in d.time:
			time = time.replace(" min", "")

		route = d.route.ljust(2)

		destination = d.destination

		line_length_wo_dest = len(route) + len(time) + 2
		line_length = line_length_wo_dest + len(destination)

		destination_avail = line_width - line_length_wo_dest
		if line_length > line_width:
			destination_avail = line_width - line_length_wo_dest
			if destination_avail > 0:
				destination = destination[0:destination_avail]
			else:
				destination = ""
		else:
			destination = destination.ljust(destination_avail)

		str_departure = ("%s %s %s" % (route, destination, time))

		menu.add_item(MenuItem(str_departure.encode('ascii', errors='replace'), load_data))


line_width = 16
lcd = Adafruit_CharLCDPlate()
lcd.begin(line_width, 2)

menu = Menu(lcd, "Main Menu")
menu.set_item_prefix("")

load_data()
menu.get_action()()

