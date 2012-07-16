#!/usr/bin/env python

import queue, monitor, output, config

def main():
    squeezypi_config = config.ConfigLoader()

    status_queue = queue.Queue()
    lms_monitor = monitor.SqueezyPiMonitor(status_queue)
    lms_output = output.SqueezyPiOutput(status_queue)

    lms_monitor.connect_server(squeezypi_config.server)
    lms_monitor.connect_player(squeezypi_config.player)

    lms_monitor.start()
    lms_output.start()
    lms_monitor.join()
    lms_output.join()

    print("Output threads started and joined")

if __name__ == '__main__':
    main()
