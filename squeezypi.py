#!/usr/bin/env python

import sys
from datetime import timedelta
from pylms.server import Server
from pylms.player import Player
from json import JSONDecoder

def connect_server():
    decoder = JSONDecoder()
    f = open("Config.json", "r")
    data = f.read()
    f.close()

    server_hostname = decoder.decode(data)['Server']['hostname']
    server_port = decoder.decode(data)['Server']['port']
    server_username = decoder.decode(data)['Server']['username']
    server_password = decoder.decode(data)['Server']['password']
    
    server = Server(hostname=server_hostname, port=server_port, username=server_username, password=server_password)
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
