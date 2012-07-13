#!/usr/bin/env python

import sys
from datetime import timedelta
sys.path.append("/home/htpc/development/python/PyLMS")
from pylms.server import Server
from pylms.player import Player

def connect_server():
    server = Server(hostname="henryhtpc.homeip.net", port=9090, username="", password="")
    server.connect()
    
    #print("Logged in:", server.logged_in)
    #print("Version:", server.get_version())

    return server

def main():
    server = connect_server()

    player = server.get_player("STARK")
    elapsed = int(player.get_time_elapsed())
    hours, remainder = divmod(elapsed, 60*60)
    minutes, seconds = divmod(remainder, 60)
    elapsed_string = "{}:{}:{}".format(hours, minutes, seconds) 

    print("Name: %s | Mode: %s | Time: %s | Connected: %s | WiFi: %s" % (player.get_name(), player.get_mode(), elapsed_string, player.is_connected, player.get_wifi_signal_strength()))

    print(player.get_track_title())
    print(timedelta(seconds=player.get_time_remaining()))

if __name__ == "__main__":
    main()
