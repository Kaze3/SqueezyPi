#!/usr/bin/env python

import queue, threading, monitor

class SqueezyPiOutput(threading.Thread):
    def __init__(self, status_queue):
        threading.Thread.__init__(self)
        self.status_queue = status_queue

    def run(self):
        while True:
            status = self.status_queue.get()
            print(status.track_artist, " - ", status.track_title, "(", format(status.hours, "02d"), ":", format(status.minutes, "02d"), ":", format(status.seconds, "02d"), ")")            
