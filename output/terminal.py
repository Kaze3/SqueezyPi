import curses, threading
from collections import deque
from time import sleep, time

class TerminalOutput(threading.Thread):
    def __init__(self, status_deque):
        threading.Thread.__init__(self)
        self.status_deque = status_deque

    def reset_check_time(self):
        self.check_time = time() + 0.1

    def reset_refresh_time(self):
        self.refresh_time = time() + 0.5

    def initialize_timers(self):
        self.reset_refresh_time()
        self.reset_check_time()

    def set_size(self, lines, width):
        self.lines = lines
        self.width = width
        self.new_status = [""]*lines
        self.status = [""]*lines
        self.start_index = [0]*lines
        
    def run(self):
        try:
            curses.wrapper(self.main)
        except KeyboardInterrupt:
            pass

    def main(self, screen):
        self.initialize_timers()
        win = curses.newwin(self.lines, self.width, 0, 0)

        while True:
            now = time()
            if now > self.check_time:
                try:
                    self.new_status = self.status_deque.pop()
                except IndexError:
                    pass
                self.reset_check_time()

            if now > self.refresh_time:       
                for i in range(self.lines):
                    if self.status[i] != self.new_status[i]:
                        self.start_index[i] = 0
                        self.status = self.new_status
                    
                    str_length = len(self.status[i])    

                    if str_length > self.width:
                        long_line = self.status[i] + " -=- "
                        str_length += 5

                        if self.start_index[i] >= str_length:
                            self.start_index[i] = 0                 
                        
                        index = self.start_index[i]       

                        if index + self.width <= str_length:
                            display = long_line[index:index + self.width - 1]
                        else:
                            display = long_line[index:] + long_line[0:index + self.width - str_length - 1]
                        
                        self.start_index[i] += 1
                    else:
                        display = self.status[i]

                    win.addstr(i, 0, display)
                win.refresh()
                self.reset_refresh_time()

    def clean_up(self):
        time.sleep(5)
        curses.endwin()

def main():
    lines = 3
    width = 12
    
    status_deque = deque()
    update = ["This is a long line", "This is also a long line", "Short"]
    status_deque.append(update)
    output = TerminalOutput(status_deque)
    output.set_size(lines, width)
    output.start()
    #output.clean_up()
    
if __name__ == '__main__':
    main()
