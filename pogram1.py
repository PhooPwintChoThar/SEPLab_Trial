import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# ---- Simple_drawing_window (for rectangles, circles, and polygons) ----
class Simple_drawing_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Drawing")
        self.resize(500, 500)

    def paintEvent(self, e):
        p = QPainter(self)

        # ---- Blue Rectangle ----
        p.setPen(QPen(QColor(0, 0, 150), 3))
        p.setBrush(QColor(100, 150, 255))
        p.drawRect(50, 50, 150, 100)

        # ---- Red Circle ----
        p.setPen(QPen(QColor(150, 0, 0), 3))
        p.setBrush(QColor(255, 100, 100))
        p.drawEllipse(250, 50, 120, 120)

        # ---- Yellow Star (Polygon) ----
        p.setPen(QPen(QColor(255, 165, 0), 2))
        p.setBrush(QColor(255, 215, 0))
        star = [
            QPoint(150, 250), QPoint(170, 290),
            QPoint(215, 295), QPoint(180, 325),
            QPoint(195, 370), QPoint(150, 345),
            QPoint(105, 370), QPoint(120, 325),
            QPoint(85, 295), QPoint(130, 290)
        ]
        p.drawPolygon(star)

        # ---- Diagonal Lines Pattern ----
        p.setPen(QPen(QColor(0, 0, 0), 1))
        for i in range(0, 120, 10):
            p.drawLine(300 + i, 250, 250, 370 - i)

        p.end()

# ---- BirdDrawingWidget (for the bird) ----
class BirdDrawingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blue Bird Drawing")
        self.resize(600, 400)

    def paintEvent(self, event):
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

# ---- Second Simple Drawing Window (for the rectangle, circle, star, etc.) ----
class Simple_drawing_window2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple GitHub Drawing - Window 2")
        self.resize(500, 500)

    def paintEvent(self, e):
        p = QPainter(self)

        # ---- Blue Rectangle ----
        p.setPen(QPen(QColor(0, 0, 150), 3))
        p.setBrush(QColor(100, 150, 255))
        p.drawRect(50, 50, 150, 100)

        # ---- Red Circle ----
        p.setPen(QPen(QColor(150, 0, 0), 3))
        p.setBrush(QColor(255, 100, 100))
        p.drawEllipse(250, 50, 120, 120)

        # ---- Yellow Star (Polygon) ----
        p.setPen(QPen(QColor(255, 165, 0), 2))
        p.setBrush(QColor(255, 215, 0))
        star = [
            QPoint(150, 250), QPoint(170, 290),
            QPoint(215, 295), QPoint(180, 325),
            QPoint(195, 370), QPoint(150, 345),
            QPoint(105, 370), QPoint(120, 325),
            QPoint(85, 295), QPoint(130, 290)
        ]
        p.drawPolygon(star)

        # ---- Diagonal Lines Pattern ----
        p.setPen(QPen(QColor(0, 0, 0), 1))
        for i in range(0, 120, 10):
            p.drawLine(300 + i, 250, 250, 370 - i)

        p.end()

# ---- New Third Drawing Window (with a triangle and rectangle) ----
class Simple_drawing_window3(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Drawing - Window 3")
        self.resize(500, 500)

    def paintEvent(self, e):
        p = QPainter(self)

        # ---- Green Triangle ----
        p.setPen(QPen(QColor(0, 150, 0), 3))
        p.setBrush(QColor(0, 255, 0))
        triangle = [QPoint(100, 100), QPoint(200, 100), QPoint(150, 200)]
        p.drawPolygon(triangle)

        # ---- Purple Rectangle ----
        p.setPen(QPen(QColor(150, 0, 150), 3))
        p.setBrush(QColor(180, 105, 255))
        p.drawRect(250, 50, 150, 100)

        # ---- Diagonal Line ----
        p.setPen(QPen(QColor(255, 0, 0), 2))
        p.drawLine(100, 300, 400, 400)

        p.end()

# ---- Main Window that holds all widgets ----
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drawing Program")
        self.setGeometry(100, 100, 1000, 800)
        self.setStyleSheet("background-color: white;")

        # Initialize all the drawing widgets
        self.canvas1 = Simple_drawing_window()
        self.canvas1.setParent(self)
        self.canvas1.setGeometry(0, 0, 500, 500)  # Set position and size

        self.canvas2 = BirdDrawingWidget()
        self.canvas2.setParent(self)
        self.canvas2.setGeometry(510, 0, 600, 400)  # Set position and size

        self.canvas3 = Simple_drawing_window2()
        self.canvas3.setParent(self)
        self.canvas3.setGeometry(0, 510, 500, 500)  # Set position and size

        self.canvas4 = Simple_drawing_window3()
        self.canvas4.setParent(self)
        self.canvas4.setGeometry(510, 410, 500, 500)  # Set position and size

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
