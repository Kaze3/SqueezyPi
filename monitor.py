#!/usr/bin/env python

import os.path
import sys
from pylms.server import Server
from pylms.player import Player

class SqueezeslaveMonitor:
    def __init__(self, squeezy_pi_config):
        if squeezy_pi_config.use_local_pylms:
            basepath = os.path.dirname(__file__)
            filepath = os.path.abspath(os.path.join(basepath, "..", "PyLMS"))
            sys.path.append(filepath)       
    
    def connect_server(self, server_config):
        """Connect to a Logitech Media server."""
        self.server = Server(hostname=server_config.hostname, port=server_config.port, username=server_config.username, password=server_config.password)
        self.server.connect()

    def connect_player(self, player_config):
        """Connect to the Squeezeslave player (must be connected to a server)."""
        self.player = self.server.get_player(player_config.name)

    #def begin_monitoring(self):
