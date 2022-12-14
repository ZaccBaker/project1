# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import icon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 550)
        MainWindow.setMinimumSize(QtCore.QSize(984, 550))
        MainWindow.setMaximumSize(QtCore.QSize(984, 550))
        MainWindow.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_shapes = QtWidgets.QFrame(self.centralwidget)
        self.frame_shapes.setGeometry(QtCore.QRect(0, 0, 110, 550))
        self.frame_shapes.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_shapes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_shapes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_shapes.setObjectName("frame_shapes")
        self.button_square = QtWidgets.QPushButton(self.frame_shapes)
        self.button_square.setGeometry(QtCore.QRect(10, 54, 90, 70))
        self.button_square.setStyleSheet("image: url(:/Square/icons/new_square.png);")
        self.button_square.setText("")
        self.button_square.setObjectName("button_square")
        self.button_rectangle = QtWidgets.QPushButton(self.frame_shapes)
        self.button_rectangle.setGeometry(QtCore.QRect(10, 178, 90, 70))
        self.button_rectangle.setStyleSheet("image: url(:/Rectangle/icons/new_rec.png);")
        self.button_rectangle.setText("")
        self.button_rectangle.setObjectName("button_rectangle")
        self.button_triangle = QtWidgets.QPushButton(self.frame_shapes)
        self.button_triangle.setGeometry(QtCore.QRect(10, 302, 90, 70))
        self.button_triangle.setStyleSheet("image: url(:/Triangle/icons/new_tri.png);")
        self.button_triangle.setText("")
        self.button_triangle.setObjectName("button_triangle")
        self.button_circle = QtWidgets.QPushButton(self.frame_shapes)
        self.button_circle.setGeometry(QtCore.QRect(10, 426, 90, 70))
        self.button_circle.setStyleSheet("image: url(:/Circle/icons/new_circle.png);")
        self.button_circle.setText("")
        self.button_circle.setObjectName("button_circle")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(110, 0, 874, 550))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_square = QtWidgets.QWidget()
        self.page_square.setObjectName("page_square")
        self.button_squarePer = QtWidgets.QPushButton(self.page_square)
        self.button_squarePer.setGeometry(QtCore.QRect(20, 131, 140, 40))
        self.button_squarePer.setStyleSheet("font: 75 18pt \"Rockwell\";")
        self.button_squarePer.setObjectName("button_squarePer")
        self.button_squareArea = QtWidgets.QPushButton(self.page_square)
        self.button_squareArea.setGeometry(QtCore.QRect(20, 255, 140, 40))
        self.button_squareArea.setStyleSheet("font: 75 18pt \"Rockwell\";")
        self.button_squareArea.setObjectName("button_squareArea")
        self.button_squareVol = QtWidgets.QPushButton(self.page_square)
        self.button_squareVol.setGeometry(QtCore.QRect(20, 397, 140, 40))
        self.button_squareVol.setStyleSheet("font: 75 18pt \"Rockwell\";")
        self.button_squareVol.setObjectName("button_squareVol")
        self.label_square = QtWidgets.QLabel(self.page_square)
        self.label_square.setGeometry(QtCore.QRect(371, 10, 132, 50))
        self.label_square.setStyleSheet("font: 75 30pt \"Rockwell\";")
        self.label_square.setAlignment(QtCore.Qt.AlignCenter)
        self.label_square.setObjectName("label_square")
        self.label_squareOutput = QtWidgets.QLabel(self.page_square)
        self.label_squareOutput.setGeometry(QtCore.QRect(245, 160, 436, 106))
        self.label_squareOutput.setStyleSheet("font: 75 18pt \"Rockwell\";")
        self.label_squareOutput.setText("")
        self.label_squareOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.label_squareOutput.setWordWrap(True)
        self.label_squareOutput.setObjectName("label_squareOutput")
        self.line_squareSide = QtWidgets.QLineEdit(self.page_square)
        self.line_squareSide.setGeometry(QtCore.QRect(285, 110, 113, 20))
        self.line_squareSide.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.line_squareSide.setAlignment(QtCore.Qt.AlignCenter)
        self.line_squareSide.setObjectName("line_squareSide")
        self.label_squareSide = QtWidgets.QLabel(self.page_square)
        self.label_squareSide.setGeometry(QtCore.QRect(200, 90, 71, 61))
        self.label_squareSide.setStyleSheet("font: 75 14pt \"Rockwell\";")
        self.label_squareSide.setAlignment(QtCore.Qt.AlignCenter)
        self.label_squareSide.setWordWrap(True)
        self.label_squareSide.setObjectName("label_squareSide")
        self.stackedWidget.addWidget(self.page_square)
        self.page_rectangle = QtWidgets.QWidget()
        self.page_rectangle.setObjectName("page_rectangle")
        self.label_rectangle = QtWidgets.QLabel(self.page_rectangle)
        self.label_rectangle.setGeometry(QtCore.QRect(342, 10, 190, 50))
        self.label_rectangle.setStyleSheet("font: 75 30pt \"Rockwell\";")
        self.label_rectangle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rectangle.setObjectName("label_rectangle")
        self.button_rectangleArea = QtWidgets.QPushButton(self.page_rectangle)
        self.button_rectangleArea.setGeometry(QtCore.QRect(20, 255, 140, 40))
        self.button_rectangleArea.setStyleSheet("font: 75 18pt \"Rockwell\";")
        self.button_rectangleArea.setObjectName("button_rectangleArea")
        self.button_rectanglePer = QtWidgets.QPushButton(self.page_rectangle)
        self.button_rectanglePer.setGeometry(QtCore.QRect(20, 131, 140, 40))
        self.button_rectanglePer.setStyleSheet("font: 75 18pt \"Rockwell\";")
        self.button_rectanglePer.setObjectName("button_rectanglePer")
        self.button_rectangleVol = QtWidgets.QPushButton(self.page_rectangle)
        self.button_rectangleVol.setGeometry(QtCore.QRect(20, 397, 140, 40))
        self.button_rectangleVol.setStyleSheet("font: 75 18pt \"Rockwell\";")
        self.button_rectangleVol.setObjectName("button_rectangleVol")
        self.line_rectangleLength = QtWidgets.QLineEdit(self.page_rectangle)
        self.line_rectangleLength.setGeometry(QtCore.QRect(285, 110, 113, 20))
        self.line_rectangleLength.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.line_rectangleLength.setAlignment(QtCore.Qt.AlignCenter)
        self.line_rectangleLength.setObjectName("line_rectangleLength")
        self.line_rectangleWidth = QtWidgets.QLineEdit(self.page_rectangle)
        self.line_rectangleWidth.setGeometry(QtCore.QRect(285, 170, 113, 20))
        self.line_rectangleWidth.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.line_rectangleWidth.setAlignment(QtCore.Qt.AlignCenter)
        self.line_rectangleWidth.setObjectName("line_rectangleWidth")
        self.line_rectangleHeight = QtWidgets.QLineEdit(self.page_rectangle)
        self.line_rectangleHeight.setGeometry(QtCore.QRect(285, 230, 113, 20))
        self.line_rectangleHeight.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.line_rectangleHeight.setAlignment(QtCore.Qt.AlignCenter)
        self.line_rectangleHeight.setObjectName("line_rectangleHeight")
        self.label_rectangleOutput = QtWidgets.QLabel(self.page_rectangle)
        self.label_rectangleOutput.setGeometry(QtCore.QRect(245, 255, 436, 106))
        self.label_rectangleOutput.setStyleSheet("font: 75 18pt \"Rockwell\";")
        self.label_rectangleOutput.setText("")
        self.label_rectangleOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rectangleOutput.setWordWrap(True)
        self.label_rectangleOutput.setObjectName("label_rectangleOutput")
        self.label_rectangleLength = QtWidgets.QLabel(self.page_rectangle)
        self.label_rectangleLength.setGeometry(QtCore.QRect(190, 90, 71, 61))
        self.label_rectangleLength.setStyleSheet("font: 75 14pt \"Rockwell\";")
        self.label_rectangleLength.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rectangleLength.setWordWrap(True)
        self.label_rectangleLength.setObjectName("label_rectangleLength")
        self.label_rectangleWidth = QtWidgets.QLabel(self.page_rectangle)
        self.label_rectangleWidth.setGeometry(QtCore.QRect(190, 150, 71, 61))
        self.label_rectangleWidth.setStyleSheet("font: 75 14pt \"Rockwell\";")
        self.label_rectangleWidth.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rectangleWidth.setWordWrap(True)
        self.label_rectangleWidth.setObjectName("label_rectangleWidth")
        self.label_rectangleHeight = QtWidgets.QLabel(self.page_rectangle)
        self.label_rectangleHeight.setGeometry(QtCore.QRect(190, 210, 71, 61))
        self.label_rectangleHeight.setStyleSheet("font: 75 14pt \"Rockwell\";")
        self.label_rectangleHeight.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rectangleHeight.setWordWrap(True)
        self.label_rectangleHeight.setObjectName("label_rectangleHeight")
        self.stackedWidget.addWidget(self.page_rectangle)
        self.page_triangle = QtWidgets.QWidget()
        self.page_triangle.setObjectName("page_triangle")
        self.label_triangle = QtWidgets.QLabel(self.page_triangle)
        self.label_triangle.setGeometry(QtCore.QRect(351, 10, 170, 50))
        self.label_triangle.setStyleSheet("font: 75 30pt \"Rockwell\";")
        self.label_triangle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_triangle.setObjectName("label_triangle")
        self.button_triangleArea = QtWidgets.QPushButton(self.page_triangle)
        self.button_triangleArea.setGeometry(QtCore.QRect(20, 255, 140, 40))
        self.button_triangleArea.setStyleSheet("font: 75 18pt \"Rockwell\";")
        self.button_triangleArea.setObjectName("button_triangleArea")
        self.button_trianglePer = QtWidgets.QPushButton(self.page_triangle)
        self.button_trianglePer.setGeometry(QtCore.QRect(20, 131, 140, 40))
        self.button_trianglePer.setStyleSheet("font: 75 18pt \"Rockwell\";")
        self.button_trianglePer.setObjectName("button_trianglePer")
        self.button_triangleVol = QtWidgets.QPushButton(self.page_triangle)
        self.button_triangleVol.setGeometry(QtCore.QRect(20, 397, 140, 40))
        self.button_triangleVol.setStyleSheet("font: 75 18pt \"Rockwell\";")
        self.button_triangleVol.setObjectName("button_triangleVol")
        self.line_triangleSide_1 = QtWidgets.QLineEdit(self.page_triangle)
        self.line_triangleSide_1.setGeometry(QtCore.QRect(285, 110, 113, 20))
        self.line_triangleSide_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.line_triangleSide_1.setAlignment(QtCore.Qt.AlignCenter)
        self.line_triangleSide_1.setObjectName("line_triangleSide_1")
        self.line_triangleSide_2 = QtWidgets.QLineEdit(self.page_triangle)
        self.line_triangleSide_2.setGeometry(QtCore.QRect(285, 170, 113, 20))
        self.line_triangleSide_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.line_triangleSide_2.setAlignment(QtCore.Qt.AlignCenter)
        self.line_triangleSide_2.setObjectName("line_triangleSide_2")
        self.line_triangleSide_3 = QtWidgets.QLineEdit(self.page_triangle)
        self.line_triangleSide_3.setGeometry(QtCore.QRect(285, 230, 113, 20))
        self.line_triangleSide_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.line_triangleSide_3.setAlignment(QtCore.Qt.AlignCenter)
        self.line_triangleSide_3.setObjectName("line_triangleSide_3")
        self.label_triangleOutput = QtWidgets.QLabel(self.page_triangle)
        self.label_triangleOutput.setGeometry(QtCore.QRect(245, 255, 436, 106))
        self.label_triangleOutput.setStyleSheet("font: 75 18pt \"Rockwell\";")
        self.label_triangleOutput.setText("")
        self.label_triangleOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.label_triangleOutput.setWordWrap(True)
        self.label_triangleOutput.setObjectName("label_triangleOutput")
        self.label_triangleA = QtWidgets.QLabel(self.page_triangle)
        self.label_triangleA.setGeometry(QtCore.QRect(190, 90, 71, 61))
        self.label_triangleA.setStyleSheet("font: 75 14pt \"Rockwell\";")
        self.label_triangleA.setAlignment(QtCore.Qt.AlignCenter)
        self.label_triangleA.setWordWrap(True)
        self.label_triangleA.setObjectName("label_triangleA")
        self.label_triangleB = QtWidgets.QLabel(self.page_triangle)
        self.label_triangleB.setGeometry(QtCore.QRect(190, 150, 71, 61))
        self.label_triangleB.setStyleSheet("font: 75 14pt \"Rockwell\";")
        self.label_triangleB.setAlignment(QtCore.Qt.AlignCenter)
        self.label_triangleB.setWordWrap(True)
        self.label_triangleB.setObjectName("label_triangleB")
        self.label_triangleC = QtWidgets.QLabel(self.page_triangle)
        self.label_triangleC.setGeometry(QtCore.QRect(190, 210, 71, 61))
        self.label_triangleC.setStyleSheet("font: 75 14pt \"Rockwell\";")
        self.label_triangleC.setAlignment(QtCore.Qt.AlignCenter)
        self.label_triangleC.setWordWrap(True)
        self.label_triangleC.setObjectName("label_triangleC")
        self.stackedWidget.addWidget(self.page_triangle)
        self.page_circle = QtWidgets.QWidget()
        self.page_circle.setObjectName("page_circle")
        self.label_circle = QtWidgets.QLabel(self.page_circle)
        self.label_circle.setGeometry(QtCore.QRect(372, 10, 130, 50))
        self.label_circle.setStyleSheet("font: 75 30pt \"Rockwell\";")
        self.label_circle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_circle.setObjectName("label_circle")
        self.button_circleArea = QtWidgets.QPushButton(self.page_circle)
        self.button_circleArea.setGeometry(QtCore.QRect(20, 255, 140, 40))
        self.button_circleArea.setStyleSheet("font: 75 18pt \"Rockwell\";")
        self.button_circleArea.setObjectName("button_circleArea")
        self.button_circlePer = QtWidgets.QPushButton(self.page_circle)
        self.button_circlePer.setGeometry(QtCore.QRect(20, 131, 140, 40))
        self.button_circlePer.setStyleSheet("font: 75 18pt \"Rockwell\";")
        self.button_circlePer.setObjectName("button_circlePer")
        self.button_circleVol = QtWidgets.QPushButton(self.page_circle)
        self.button_circleVol.setGeometry(QtCore.QRect(20, 397, 140, 40))
        self.button_circleVol.setStyleSheet("font: 75 18pt \"Rockwell\";")
        self.button_circleVol.setObjectName("button_circleVol")
        self.line_circleRadius = QtWidgets.QLineEdit(self.page_circle)
        self.line_circleRadius.setGeometry(QtCore.QRect(285, 110, 113, 20))
        self.line_circleRadius.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.line_circleRadius.setAlignment(QtCore.Qt.AlignCenter)
        self.line_circleRadius.setObjectName("line_circleRadius")
        self.label_circleOutput = QtWidgets.QLabel(self.page_circle)
        self.label_circleOutput.setGeometry(QtCore.QRect(245, 160, 436, 106))
        self.label_circleOutput.setStyleSheet("font: 75 18pt \"Rockwell\";")
        self.label_circleOutput.setText("")
        self.label_circleOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.label_circleOutput.setWordWrap(True)
        self.label_circleOutput.setObjectName("label_circleOutput")
        self.label_circleRadius = QtWidgets.QLabel(self.page_circle)
        self.label_circleRadius.setGeometry(QtCore.QRect(190, 90, 71, 61))
        self.label_circleRadius.setStyleSheet("font: 75 14pt \"Rockwell\";")
        self.label_circleRadius.setAlignment(QtCore.Qt.AlignCenter)
        self.label_circleRadius.setWordWrap(True)
        self.label_circleRadius.setObjectName("label_circleRadius")
        self.stackedWidget.addWidget(self.page_circle)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_squarePer.setText(_translate("MainWindow", "Perimeter"))
        self.button_squareArea.setText(_translate("MainWindow", "Area"))
        self.button_squareVol.setText(_translate("MainWindow", "Volume"))
        self.label_square.setText(_translate("MainWindow", "Square"))
        self.label_squareSide.setText(_translate("MainWindow", "Side Length"))
        self.label_rectangle.setText(_translate("MainWindow", "Rectangle"))
        self.button_rectangleArea.setText(_translate("MainWindow", "Area"))
        self.button_rectanglePer.setText(_translate("MainWindow", "Perimeter"))
        self.button_rectangleVol.setText(_translate("MainWindow", "Volume"))
        self.label_rectangleLength.setText(_translate("MainWindow", "Length"))
        self.label_rectangleWidth.setText(_translate("MainWindow", "Width"))
        self.label_rectangleHeight.setText(_translate("MainWindow", "Height"))
        self.label_triangle.setText(_translate("MainWindow", "Triangle"))
        self.button_triangleArea.setText(_translate("MainWindow", "Area"))
        self.button_trianglePer.setText(_translate("MainWindow", "Perimeter"))
        self.button_triangleVol.setText(_translate("MainWindow", "Volume"))
        self.label_triangleA.setText(_translate("MainWindow", "A"))
        self.label_triangleB.setText(_translate("MainWindow", "B"))
        self.label_triangleC.setText(_translate("MainWindow", "C"))
        self.label_circle.setText(_translate("MainWindow", "Circle"))
        self.button_circleArea.setText(_translate("MainWindow", "Area"))
        self.button_circlePer.setText(_translate("MainWindow", "Perimeter"))
        self.button_circleVol.setText(_translate("MainWindow", "Volume"))
        self.label_circleRadius.setText(_translate("MainWindow", "Radius"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
