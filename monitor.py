#!/usr/bin/env python

import os.path
import sys

class SqueezeslaveMonitor:
    def __init__(self, use_local_pylms=False):
        if use_local_pylms:
            basepath = os.path.dirname(__file__)
            filepath = os.path.abspath(os.path.join(basepath, "..", "PyLMS"))
            sys.path.append(filepath) 
        
        from pylms.server import Server
        from pylms.player import Player
    
    def connect_server(self, server_hostname, server_port, server_username, server_password):
        """Connect to a Logitech Media server."""
        self.server = Server(hostname=server_hostname, port=server_port, username=server_username, password=server_password)
        self.server.connect()

    def connect_player(self, player_name):
        """Connect to the Squeezeslave player (must be connected to a server)."""
        self.player = self.server.get_player(player_name)

    #def begin_monitoring(self):
