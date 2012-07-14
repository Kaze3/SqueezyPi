#!/usr/bin/env python

from json import JSONDecoder

class ConfigLoader:
    """Class for handling the SqueezyPi JSON configuration file."""
    server_hostname = ""
    server_port = 9090
    server_username = ""
    server_password = ""
    
    player_name = ""

    squeezypi_use_local_pylms = 0

    def load_config(self, config_path='Config.json'):
        """Load the configuration file."""
        decoder = JSONDecoder()
        f = open(config_path, "r")
        data = f.read()
        f.close()

        server_hostname = decoder.decode(data)['Server']['hostname']
        server_port = decoder.decode(data)['Server']['port']
        server_username = decoder.decode(data)['Server']['username']
        server_password = decoder.decode(data)['Server']['password']
        
        player_name = decoder.decode(data)['Player']['name']
        
        squeezypi_use_local_pylms = decoder.decode(data)['SqueezyPi']['use_local_pylms']
