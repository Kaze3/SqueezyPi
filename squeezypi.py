#!/usr/bin/env python

from collections import deque
import monitor, output, config

def main():
    squeezypi_config = config.ConfigLoader()

    status_deque = deque()
    lms_monitor = monitor.SqueezyPiMonitor(status_deque)
    lms_output = output.SqueezyPiOutput(status_deque)

    lms_monitor.connect_server(squeezypi_config.server)
    lms_monitor.connect_player(squeezypi_config.player)

    lms_monitor.start()
    lms_output.start()
    lms_monitor.join()
    lms_output.join()

    print("Output threads started and joined")

if __name__ == '__main__':
    main()
