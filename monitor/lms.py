#!/usr/bin/env python

from pylms.server import Server
from pylms.player import Player
import re, time, sys, threading

class MonitorPlugin(threading.Thread):
    """Monitor plugin for the Logitech Media Server program"""
    def __init__(self, status_deque, configuration):
        threading.Thread.__init__(self)
        self.status_deque = status_deque

        self.connect_server(configuration['Server'])
        self.connect_player(configuration['Player'])
        self._generate_output_format(configuration['output_format'])

    def _generate_output_format(self, config_string):
        """Generate the output string format according to the passed string"""
        options = {'%a' : self.player_status.update_track_title,\
                   '%h' : self.player_status.update_track_hours_elapsed,
                   '%m' : self.player_status.update_track_minutes_elapsed,
                   '%s' : self.player_status.update_track_seconds_elapsed,
		   '%t' : self.player_status.update_track_artist}

        option_match = re.compile(r'(?<!%)(%\w{1}(?!\w))')
        self.output_string = config_string
        self.output_functions = []

        try:
            for match in option_match.finditer(config_string):
                self.output_string = self.output_string[:match.start()] + '{}' + self.output_string[match.end():]
                self.output_functions.append(options[match.group()])
        except:
            sys.exit('LMSMonitor: chosen output option does not exist') 

    def connect_server(self, server_config):
        """Connect to a Logitech Media server."""
        self.server = Server(hostname=server_config['hostname'], port=server_config['port'], username=server_config['username'], password=server_config['password'])
        self.server.connect()

    def connect_player(self, player_config):
        """Connect to the Squeezeslave player (must be connected to a server)."""
        self.player = self.server.get_player(player_config['name'])
        self.player_status = PlayerStatus(self.player)

    def run(self):
        while True:
            status_string = self.output_string
            for i in range(0, self.output_functions.__len__()):
                status_split = status_string.split('{}', 1)
                status_string = status_split[0] + self.output_functions[i]() + status_split[1]

            self.status_deque.append(status_string)
            time.sleep(1)

class PlayerStatus:
    def __init__(self, player):
        self.player = player

    def update_track_hours_elapsed(self):
        elapsed = int(self.player.get_time_elapsed())
        return format(divmod(elapsed, 3600)[0], "02d")

    def update_track_minutes_elapsed(self):
        elapsed = int(self.player.get_time_elapsed())
        _remainder = divmod(elapsed, 3600)[1]
        return format(divmod(_remainder, 60)[0], "02d")

    def update_track_seconds_elapsed(self):
        elapsed = int(self.player.get_time_elapsed())
        _remainder = divmod(elapsed, 3600)[1]
        return format(divmod(_remainder, 60)[1], "02d")

    def update_track_artist(self):
        return self.player.get_track_artist()

    def update_track_title(self):
        return self.player.get_track_title()
