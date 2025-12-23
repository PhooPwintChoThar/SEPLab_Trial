import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon(
            QPoint(70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150)
        )
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)
        p.drawPolygon(
            QPoint(50, 200), QPoint(150, 200),
            QPoint(100, 400)
        )
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()
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

class Simple_drawing_window4(Simple_drawing_window):
    def __init__(self):
        super().__init__()

    def paintEvent(self, e):
        # return super().paintEvent(e)
        p = QPainter(self)
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawRect(50,50,200,150)
        p.end



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