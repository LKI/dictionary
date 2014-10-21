# Cultural Dictionary
# Cathy
# 2014.10.21

from graphics import *

ScreenWidth = 640
ScreenHeight = 360

def __main__():

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

    output = Text(Point(1.5, 2.0),"")
    output.setSize(14)
    output.draw(win)
    Rectangle(Point(0.25, 0.5), Point(2.75, 3)).draw(win)

    while (True):
        # wait for a mouse click
        # Check if it's in search rect
        p = win.getMouse()
        while (not(2.2<p.getX()<2.8 and 3.35<p.getY()<3.65)): p = win.getMouse()
        print "x=", p.getX(), " y=", p.getY()
        word = wordRect.getText()
        print "word=", word

        # Get description
        description = "Albert Einstein was born to a middle-class German Jewish family. His parents were concerned that he scarcely talked until the age of three, but he was not stupid as a quiet child. He would build tall houses of cards and hated playing soldier. At the age of twelve he was fascinated by a geometry book."
        # Format description
        formated_description = ""
        for i in range(len(description)/50):
            formated_description = formated_description + description[50*i:50*(i+1)] + "\n"
        output.setText(formated_description)

    win.getMouse()
    win.close()

__main__()
