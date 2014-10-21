# Cultural Dictionary
# Cathy
# 2014.10.21

import sqlite3 as s
from graphics import *

ScreenWidth = 640
ScreenHeight = 360

def __main__():

    # Connect to sqlite
    cx = s.connect("dict.db")
    cu = cx.cursor()
    select_sql = "select desc from dict where word = ?"

    # Prepare win
    win = GraphWin("Cultural Dictionary", ScreenWidth, ScreenHeight);
    win.setBackground('white')
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    # Draw the interface
    Text(Point(0.7,3.5), "What word do you want to know:").draw(win)
    wordRect = Entry(Point(1.7,3.5), 20)
    wordRect.setText("Einstein")
    wordRect.setFill('white')
    wordRect.draw(win)
    Rectangle(Point(2.2, 3.65), Point(2.8, 3.35)).draw(win)
    Text(Point(2.5, 3.5), "Search").draw(win)

    #Prepare output
    output = Text(Point(1.5, 2.0),"")
    output.setSize(14)
    output.draw(win)
    Rectangle(Point(0.25, 0.5), Point(2.75, 3)).draw(win)

    while (True):
        # wait for a mouse click
        # Check if it's in search rect
        p = win.getMouse()
        while (not(2.2<p.getX()<2.8 and 3.35<p.getY()<3.65)): p = win.getMouse()
        word = wordRect.getText()

        # Get description
        cu.execute(select_sql, [word])
        description = cu.fetchone()
        if description:
            description = description[0]
        else:
            description = "No record for this word"

        # Format description
        formated_description = ""
        n = len(description)/50
        for i in range(n):
            formated_description = formated_description + description[50*i:50*(i+1)] + "\n"
        formated_description = formated_description + description[50*n:]
        output.setText(formated_description)

    win.getMouse()
    win.close()

__main__()
