#!/usr/bin/env python

from collections import deque
import monitor, output, config

def main():
    squeezypi_config = config.ConfigLoader()

    status_deque = deque()
    squeezypi_monitor = monitor.SqueezyPiMonitor(status_deque, squeezypi_config.monitor)
    squeezypi_output = output.SqueezyPiOutput(status_deque)

    squeezypi_monitor.start_monitoring()

    squeezypi_output.start()
#    squeezypi_monitor.join()
#    squeezypi_output.join()

if __name__ == '__main__':
    main()
