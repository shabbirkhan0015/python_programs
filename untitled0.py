from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class Ui_MainWindow(QMainWindow):
    class GraphicsScene(QGraphicsScene):
        def __init__(self, parent=None):
            QGraphicsScene.__init__(self, parent)
            self.setSceneRect(-100, -100, 200, 200)
        list = []
        lineList = []
        ellList = []
        flag = 0
        count = 64

        def mousePressEvent(self, event):
            if event.button() == Qt.LeftButton:
                brush = QBrush(Qt.black)
                pen = QPen(brush, 2, Qt.SolidLine, Qt.SquareCap, Qt.BevelJoin)
                global x
                x = event.scenePos().x()
                global y
                y = event.scenePos().y()

                self.count += 1
                self.list.append((x, y, chr(self.count)))

                ell = QGraphicsEllipseItem(x, y, 3, 3)
                ell.setPen(pen)
                self.addItem(ell)

                conEll = QGraphicsEllipseItem(x - 2, y - 2, 6, 6)
                pe = QPen(Qt.transparent)
                conEll.setPen(pe)
                self.addItem(conEll)
                self.ellList.append((conEll, chr(self.count)))

                self.ptno = QGraphicsTextItem("")
                self.ptno.setPos(QPointF(x - 15, y - 20))

                ln2 = 'A'
                flaggy = 0
                for check in range(0, len(self.ellList) - 1):
                    re = self.ellList[check]
                    rell = re[0]
                    if rell.contains(QPointF(x, y)):
                        flaggy = 1
                        self.count -= 1
                        ln2 = re[1]
                        break

                if flaggy != 1:
                    self.ptno.setPlainText(chr(self.count))
                    self.addItem(self.ptno)

                if self.flag == 0:
                    self.flag = 1
                elif self.flag == 1:
                    xy = self.list[-2]
                    x2 = xy[0]
                    y2 = xy[1]

                    self.line = QGraphicsLineItem(QLineF(x2, y2, x, y))
                    self.line.setPen(pen)
                    self.addItem(self.line)

                    z = self.list[-2]
                    ln = z[2]
                    if flaggy == 1:
                        self.lineList.append((self.line, ln2 + chr(self.count)))
                    else:
                        self.lineList.append((self.line, ln + chr(self.count)))
                    print(self.lineList[-1][1])
                    s = str(self.lineList[-1][1])

                # a = self.line.angle()
                # print(self.line.length())
                # print('Angle: ')
                # print(a)

            if event.button() == Qt.RightButton:
                self.flag = 0

        secondFlag = 0

        def mouseMoveEvent(self, event):
            brush = QBrush(Qt.black)
            pen = QPen(brush, 2, Qt.SolidLine, Qt.SquareCap, Qt.BevelJoin)
            x1 = event.scenePos().x()
            y1 = event.scenePos().y()

            '''self.line = QGraphicsLineItem(QLineF(x, y, x1, y1))
            self.line.setPen(pen)

            if self.secondFlag == 0:
                self.addItem(self.line)
                self.secondFlag = 1
                self.linelist.append(self.line)
            else:
                self.linelist.append(self.line)
                self.removeItem(self.linelist[-2])
                self.addItem(self.line)
            '''

        def mouseReleaseEvent(self, event):
            brush = QBrush(Qt.black)
            pen = QPen(brush, 2)
            x3 = event.scenePos().x()
            y3 = event.scenePos().y()

            xy = self.list[0]
            x1 = xy[0]
            y1 = xy[1]

            # line3 = QGraphicsLineItem(x, y, x3, y3)
            # line3.setPen(pen)
            # self.addItem(line3)

            # self.addEllipse(x3, y3, 3, 3, pen, brush)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.scene = self.GraphicsScene()
        self.graphicsView.setScene(self.scene)

        self.graphicsView.setAlignment(Qt.AlignLeft | Qt.AlignTop)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 525)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QRect(190, 0, 501, 471))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(110, 360, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QRect(10, 10, 171, 141))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setGeometry(QRect(20, 20, 61, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QRect(80, 20, 71, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setGeometry(QRect(80, 50, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QLabel(self.groupBox)
        self.label.setGeometry(QRect(20, 55, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setGeometry(QRect(20, 80, 47, 21))
        self.label_2.setObjectName("label_2")
        self.angleBox = QDoubleSpinBox(self.groupBox)
        self.angleBox.setGeometry(QRect(80, 80, 71, 22))
        self.angleBox.setCursor(QCursor(Qt.ArrowCursor))
        self.angleBox.setMaximum(360.0)
        self.angleBox.setObjectName("angleBox")
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QRect(20, 110, 131, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 697, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.clr)
        self.show()

    def clr(self):
        self.scene.removeItem(self.scene.line)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Clear"))
        self.groupBox.setTitle(_translate("MainWindow", "Set Angle"))
        self.label_3.setText(_translate("MainWindow", "Line 1"))
        self.label.setText(_translate("MainWindow", "Line 2"))
        self.label_2.setText(_translate("MainWindow", "Angle"))
        self.pushButton_2.setText(_translate("MainWindow", "Set"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = Ui_MainWindow()
    sys.exit(app.exec_())