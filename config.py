#!/usr/bin/env python

from json import JSONDecoder

class ConfigLoader:
    """Class for handling the SqueezyPi JSON configuration file."""

    def load_config(self, config_path='Config.json'):
        """Load the configuration file."""
        decoder = JSONDecoder()
        f = open(config_path, "r")
        data = f.read()
        f.close()

        self.server_hostname = decoder.decode(data)['Server']['hostname']
        self.server_port = decoder.decode(data)['Server']['port']
        self.server_username = decoder.decode(data)['Server']['username']
        self.server_password = decoder.decode(data)['Server']['password']
        
        self.player_name = decoder.decode(data)['Player']['name']
        
        self.squeezypi_use_local_pylms = decoder.decode(data)['SqueezyPi']['use_local_pylms']
