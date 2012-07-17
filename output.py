#!/usr/bin/env python

from collections import deque
from time import sleep
import threading, monitor

class SqueezyPiOutput(threading.Thread):
    def __init__(self, status_deque):
        threading.Thread.__init__(self)
        self.status_deque = status_deque

    def run(self):
        while True:
            try:
                status = self.status_deque.pop()
                print(status.track_artist, " - ", status.track_title, "(", format(status.hours, "02d"), ":", format(status.minutes, "02d"), ":", format(status.seconds, "02d"), ")")
            except IndexError:
                pass
            sleep(0.1)
