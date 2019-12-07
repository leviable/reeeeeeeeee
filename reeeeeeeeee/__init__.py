import curses
import time


def reeeeeeeeee():
    s = curses.initscr()
    # Do colors later
    # curses.start_color()
    # curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.noecho()
    curses.curs_set(0)
    s.nodelay(True)
    s.leaveok(True)
    s.scrollok(False)

    for x in range(curses.COLS-12):
        # s.addstr(15, x, "reeeeeeeeeee", curses.color_pair(1))
        s.addstr(15, x, "reeeeeeeeeee")

        s.refresh()
        time.sleep(0.04)

    curses.endwin()
