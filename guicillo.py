import curses
import time

def other_cac():
    a = 3 + 2

def sequencer_to_str(index):
    sequencer = "|"
    for i in range(0,15):
        if(i == index):
            sequencer += "X|"
        else:
            sequencer += " |"
    return sequencer

def main(stdscr):
    curses.curs_set(0)
    for i in range(15):
        stdscr.addstr(6,20,"Freq: 400")
        stdscr.addstr(7,20,"BPM:  121")
        stdscr.addstr(8,30,"SEQUENCER")
        stdscr.addstr(9,30,sequencer_to_str(i))
        stdscr.refresh()
        time.sleep(0.1)

for i in range(10):
    curses.wrapper(main)
