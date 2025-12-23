import sys
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QApplication, QWidget

class BirdDrawingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blue Bird Drawing")
        self.setGeometry(100, 100, 600, 400)

    def paintEvent(self, event):
        # Create a QPainter object to handle drawing
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Enable smooth drawing
        painter.setBrush(QColor(0, 0, 255))  # Set brush color to blue
        painter.setPen(Qt.NoPen)  # No outline

        # Draw the bird (a simple version)
        # Body (ellipse)
        painter.drawEllipse(200, 150, 200, 120)  # Body

        # Wing (ellipse)
        painter.setBrush(QColor(0, 0, 200))  # Darker blue for the wing
        painter.drawEllipse(250, 180, 120, 70)  # Wing

        # Head (circle)
        painter.setBrush(QColor(0, 0, 255))  # Blue head
        painter.drawEllipse(320, 100, 60, 60)  # Head

        # Beak (triangle)
        painter.setBrush(QColor(255, 165, 0))  # Orange beak
        painter.setPen(Qt.NoPen)  # No outline for the beak
        points = [QPoint(350, 120), QPoint(370, 140), QPoint(350, 140)]
        painter.drawPolygon(*points)  # Beak

        # Eyes (black circles)
        painter.setBrush(QColor(0, 0, 0))  # Black eyes
        painter.drawEllipse(335, 120, 10, 10)  # Left eye
        painter.drawEllipse(355, 120, 10, 10)  # Right eye

        painter.end()  # End painting

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drawing Program")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: white;")

        # Add a BirdDrawingWidget to this window
        self.canvas = BirdDrawingWidget()
        self.canvas.setParent(self)
        self.canvas.setGeometry(0, 0, 600, 400)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
