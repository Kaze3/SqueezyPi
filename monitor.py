#!/usr/bin/env python

from pylms.server import Server
from pylms.player import Player
import queue, threading, time

class SqueezyPiMonitor(threading.Thread):
    def __init__(self, status_queue):
        threading.Thread.__init__(self)
        self.status_queue = status_queue

    def connect_server(self, server_config):
        """Connect to a Logitech Media server."""
        self.server = Server(hostname=server_config.hostname, port=server_config.port, username=server_config.username, password=server_config.password)
        self.server.connect()

    def connect_player(self, player_config):
        """Connect to the Squeezeslave player (must be connected to a server)."""
        self.player = self.server.get_player(player_config.name)

    def run(self):
        status = PlayerStatus()
        while True:
            status.update_track_artist(self.player.get_track_artist())
            status.update_track_title(self.player.get_track_title())
            status.update_time_elapsed(self.player.get_time_elapsed())
            self.status_queue.put(status)
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
