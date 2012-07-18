#!/usr/bin/env python

import sys, os.path, inspect

class SqueezyPiMonitor():
    def __init__(self, status_deque, monitor_config):
        self.status_deque = status_deque
        self.plugin_name = monitor_config.plugin_name

        self.load_plugin(monitor_config.plugin_data[self.plugin_name])

    def load_plugin(self, plugin_config):
        """Load the monitor plugin"""
        # Expects the class to be called "MonitorPlugin" and 
        # take as arguments the deque and a configuration dictionary
        sys.path.append(os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]) + "/monitor"))
        from lms import MonitorPlugin
        self.monitor_plugin = MonitorPlugin(self.status_deque, plugin_config)

    def start_monitoring(self):
        self.monitor_plugin.start()
