#!/usr/bin/env python

from json import JSONDecoder

class ConfigLoader:
    """Class for handling the SqueezyPi JSON configuration file."""

    def __init__(self, config_path='config.json'):
        """Load the configuration file."""
        f = open(config_path, "r")
        data = f.read()
        f.close()

        decoder = JSONDecoder()
        decoded_configuration = decoder.decode(data)
   
        self.monitor = self.MonitorConfig(decoded_configuration['Monitor'])

    class MonitorConfig:
        """Load and store monitor plugin configuration"""
        def __init__(self, data):
            self.plugin_name = data['plugin_name']

            # now remove monitor-specific configuration
            # and leave only plugin-specific configuration
            data.pop('plugin_name')
            self.plugin_data = data
