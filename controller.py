from PyQt5.QtWidgets import *
from view import *
import shape as sm


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        #Navigate stacked widget
        self.button_square.clicked.connect(lambda: self.square())
        self.button_rectangle.clicked.connect(lambda: self.rectangle())
        self.button_triangle.clicked.connect(lambda: self.triangle())
        self.button_circle.clicked.connect(lambda: self.circle())

        #Shape math button press
        self.button_squarePer.clicked.connect(lambda: self.onPressed(option='p_sq'))
        self.button_squareArea.clicked.connect(lambda: self.onPressed(option='a_sq'))
        self.button_squareVol.clicked.connect(lambda: self.onPressed(option='v_sq'))

        self.button_rectanglePer.clicked.connect(lambda: self.onPressed(option='p_rec'))
        self.button_rectangleArea.clicked.connect(lambda: self.onPressed(option='a_rec'))
        self.button_rectangleVol.clicked.connect(lambda: self.onPressed(option='v_rec'))

        self.button_trianglePer.clicked.connect(lambda: self.onPressed(option='p_tri'))
        self.button_triangleArea.clicked.connect(lambda: self.onPressed(option='a_tri'))
        self.button_triangleVol.clicked.connect(lambda: self.onPressed(option='v_tri'))

        self.button_circlePer.clicked.connect(lambda: self.onPressed(option='p_cir'))
        self.button_circleArea.clicked.connect(lambda: self.onPressed(option='a_cir'))
        self.button_circleVol.clicked.connect(lambda: self.onPressed(option='v_cir'))

    def square(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def rectangle(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def triangle(self):
        self.stackedWidget.setCurrentIndex(2)

    def circle(self):
        self.stackedWidget.setCurrentIndex(3)
    
    def onPressed(self, option):
        if option == 'p_sq':
            try:
                per = sm.p_square(float(self.line_squareSide.text().strip()))    
                self.label_squareOutput.setText(f'Perimeter of Square is: {per:.3f}')
            except ValueError:
                self.label_squareOutput.setText('Input must be a positive number')
            except TypeError:
                self.label_squareOutput.setText('Input can not be a negative number')
        elif option == 'a_sq':
            try:
                area = sm.a_square(float(self.line_squareSide.text().strip()))
                self.label_squareOutput.setText(f'Area of Square is: {area:.3f}')
            except ValueError:
                self.label_squareOutput.setText('Input must be a positive number')
            except TypeError:
                self.label_squareOutput.setText('Input can not be a negative number')
        elif option == 'v_sq':
            try:
                vol = sm.v_square(float(self.line_squareSide.text().strip()))
                self.label_squareOutput.setText(f'Volume of Square is: {vol:.3f}')
            except ValueError:
                self.label_squareOutput.setText('Input must be a positive number')
            except TypeError:
                self.label_squareOutput.setText('Input can not be a negative number')
        elif option == 'p_rec':
            try:
                length = float(self.line_rectangleLength.text().strip())
                width = float(self.line_rectangleWidth.text().strip())
                per = sm.p_rectangle(length,width)
                self.label_rectangleOutput.setText(f'Perimeter of Rectangle is: {per:.3f}')
            except ValueError:
                self.label_squareOutput.setText('Input must be a positive number')
            except TypeError:
                self.label_squareOutput.setText('Input can not be a negative number')
        elif option == 'a_rec':
            try:
                length = float(self.line_rectangleLength.text().strip())
                width = float(self.line_rectangleWidth.text().strip())
                area = sm.a_rectangle(length,width)
                self.label_rectangleOutput.setText(f'Area of Rectangle is: {area:.3f}')
            except ValueError:
                self.label_squareOutput.setText('Input must be a positive number')
            except TypeError:
                self.label_squareOutput.setText('Input can not be a negative number')
        elif option == 'v_rec':
            try:
                length = float(self.line_rectangleLength.text().strip())
                width = float(self.line_rectangleWidth.text().strip())
                height = float(self.line_rectangleHeight.text().strip())
                vol = sm.v_rectangle(length,width,height)
                self.label_rectangleOutput.setText(f'Volume of Rectangle is: {vol:.3f}')
            except ValueError:
                self.label_squareOutput.setText('Input must be a positive number')
            except TypeError:
                self.label_squareOutput.setText('Input can not be a negative number')
        elif option == 'p_tri':
            try:
                side1 = float(self.line_triangleSide_1.text().strip())
                side2 = float(self.line_triangleSide_2.text().strip())
                side3 = float(self.line_triangleSide_3.text().strip())
                per = sm.p_triangle(side1,side2,side3)
                self.label_triangleOutput.setText(f'Perimeter of Triangle is: {per:.3f}')
            except ValueError:
                self.label_squareOutput.setText('Input must be a positive number')
            except TypeError:
                self.label_squareOutput.setText('Input can not be a negative number')
        elif option == 'a_tri':
            try:
                base = float(self.line_triangleSide_1.text().strip())
                height = float(self.line_triangleSide_2.text().strip())
                area = sm.a_triangle(base,height)
                self.label_triangleOutput.setText(f'Area of Triangle is: {area:.3f}')
            except ValueError:
                self.label_squareOutput.setText('Input must be a positive number')
            except TypeError:
                self.label_squareOutput.setText('Input can not be a negative number')
        elif option == 'v_tri':
            try:
                side1 = float(self.line_triangleSide_1.text().strip())
                side2 = float(self.line_triangleSide_2.text().strip())
                side3 = float(self.line_triangleSide_3.text().strip())
                vol = sm.v_triangle(side1,side2,side3)
                self.label_triangleOutput.setText(f'Volume of Triangle is: {vol:.3f}')
            except ValueError:
                self.label_squareOutput.setText('Input must be a positive number')
            except TypeError:
                self.label_squareOutput.setText('Input can not be a negative number')
        elif option == 'p_cir':
            try:
                per = sm.p_circle(float(self.line_circleRadius.text().strip()))
                self.label_circleOutput.setText(f'Perimeter of Circle is: {per:.3f}')
            except ValueError:
                self.label_squareOutput.setText('Input must be a positive number')
            except TypeError:
                self.label_squareOutput.setText('Input can not be a negative number')
        elif option == 'a_cir':
            try:
                area = sm.a_circle(float(self.line_circleRadius.text().strip()))
                self.label_circleOutput.setText(f'Area of Circle is: {area:.3f}')
            except ValueError:
                self.label_squareOutput.setText('Input must be a positive number')
            except TypeError:
                self.label_squareOutput.setText('Input can not be a negative number')
        elif option == 'v_cir':
            try:
                vol = sm.v_circle(float(self.line_circleRadius.text().strip()))
                self.label_circleOutput.setText(f'Volume of Circle is: {vol:.3f}')
            except ValueError:
                self.label_squareOutput.setText('Input must be a positive number')
            except TypeError:
                self.label_squareOutput.setText('Input can not be a negative number')