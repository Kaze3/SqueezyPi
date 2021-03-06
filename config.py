#!/usr/bin/env python

from json import JSONDecoder

class ConfigLoader:
    """Class for handling the SqueezyPi JSON configuration file."""

    def __init__(self, config_path='config.json'):
        """Load the configuration file."""
        f = open(config_path, "r")
        data = f.read()
        f.close()

        self.server = self.ServerConfig(data)
        self.player = self.PlayerConfig(data)

    class ServerConfig:
        """Load and store server configuration variables"""
        def __init__(self, data):
            decoder = JSONDecoder()
            self.hostname = decoder.decode(data)['Server']['hostname']
            self.port = decoder.decode(data)['Server']['port']
            self.username = decoder.decode(data)['Server']['username']
            self.password = decoder.decode(data)['Server']['password']

    class PlayerConfig:
        """Load and store player configuration variables"""
        def __init__(self, data):
            decoder = JSONDecoder()
            self.name = decoder.decode(data)['Player']['name']
