#!/usr/bin/env python

from collections import deque
from pylms.server import Server
from pylms.player import Player
from sys import exit
from time import sleep
import re
import threading

class LMSMonitor(threading.Thread):
    def __init__(self, status_deque):
        threading.Thread.__init__(self)
        self.status_deque = status_deque
        self.player = PlayerStatus()

    def _generate_output_format(config_string):
        """Generate the output string format according to the passed string"""
        options = {'%a' : self.player.update_track_title,\
		   '%t' : self.player.update_track_artist}

        option_match = re.compile(r'(?<!%)(%\w{1}(?!\w))')
        self.output_string = config_string
        self.output_functions = []
        try:
            for match in option_match.finditer(config_string):
                self.output_string = self.output_string[:match.start()] + '{}' + self.output_string[match.end():]
                self.output_functions.extend(options[match.group()])
        except:
            sys.exit('LMSMonitor: chosen output option does not exist')
            

    def connect_server(self, server_config):
        """Connect to a Logitech Media server."""
        self.server = Server(hostname=server_config.hostname, port=server_config.port, username=server_config.username, password=server_config.password)
        self.server.connect()

    def connect_player(self, player_config):
        """Connect to the Squeezeslave player (must be connected to a server)."""
        self.player = self.server.get_player(player_config.name)

    def run(self):
        while True:
	    status_string = self.output_string
            for i in range(0, self.output_functions.__len__()):
                status_split = status_string.split('{}', 1)
                status_string = status_split[0] + self.output_functions[i]() + status_split[1]

            self.status_deque.append(status_string)
            time.sleep(1)

class PlayerStatus:
    def update_time_elapsed(self, time_elapsed):
        time_elapsed = int(time_elapsed)
        self.hours, _remainder = divmod(time_elapsed, 3600)
        self.minutes, self.seconds = divmod(_remainder, 60)

    def update_track_artist(self, track_artist):
        self.track_artist = track_artist

    def update_track_title(self, track_title):
        self.track_title = track_title
