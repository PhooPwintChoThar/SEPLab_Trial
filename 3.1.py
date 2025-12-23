class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name       # Name of the disk
        self.dxpos = xpos       # X position of the disk
        self.dypos = ypos       # Y position of the disk
        self.dheight = height   # Height of the disk
        self.dwidth = width     # Width of the disk

    def showdisk(self, painter):
        """Draw the disk at its current position."""
        #painter.setBrush(Qt.blue)  # Set brush color to blue
        painter.drawEllipse(self.dxpos, self.dypos, self.dwidth, self.dheight)  # Draw the disk as an ellipse
        # painter.setPen(Qt.black)  # Set outline color to black
        # painter.drawText(self.dxpos + 5, self.dypos + self.dheight / 2, self.dname)  # Draw the name of the disk near its center

    def newpos(self, xpos, ypos):
        """Move the disk to a new position."""
        self.dxpos = xpos
        # self.dypos = ypos

    def cleardisk(self, painter):
        """Clear the disk from its current position."""
        painter.setBrush(Qt.white)  # Set brush to white (background color)
        # painter.drawEllipse(self.dxpos, self.dypos, self.dwidth, self.dheight)  # Redraw the disk as a white circle to "clear" it

