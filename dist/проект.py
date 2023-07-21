import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel, QColorDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 700, 600)
        self.setWindowTitle('Проект')
        # Подключение к базе данных
        self.con = sqlite3.connect("project.db")
        self.cur = self.con.cursor()
        # январь кнопки
        self.button_January1 = QPushButton('1', self)
        self.button_January1.resize(20, 20)
        self.button_January1.move(105, 120)
        self.button_January1.clicked.connect(self.January1)

        self.button_January2 = QPushButton('2', self)
        self.button_January2.resize(20, 20)
        self.button_January2.move(125, 120)
        self.button_January2.clicked.connect(self.January2)

        self.button_January3 = QPushButton('3', self)
        self.button_January3.resize(20, 20)
        self.button_January3.move(145, 120)
        self.button_January3.clicked.connect(self.January3)

        self.button_January4 = QPushButton('4', self)
        self.button_January4.resize(20, 20)
        self.button_January4.move(25, 140)
        self.button_January4.clicked.connect(self.January4)

        self.button_January5 = QPushButton('5', self)
        self.button_January5.resize(20, 20)
        self.button_January5.move(45, 140)
        self.button_January5.clicked.connect(self.January5)

        self.button_January6 = QPushButton('6', self)
        self.button_January6.resize(20, 20)
        self.button_January6.move(65, 140)
        self.button_January6.clicked.connect(self.January6)

        self.button_January7 = QPushButton('7', self)
        self.button_January7.resize(20, 20)
        self.button_January7.move(85, 140)
        self.button_January7.clicked.connect(self.January7)

        self.button_January8 = QPushButton('8', self)
        self.button_January8.resize(20, 20)
        self.button_January8.move(105, 140)
        self.button_January8.clicked.connect(self.January8)

        self.button_January9 = QPushButton('9', self)
        self.button_January9.resize(20, 20)
        self.button_January9.move(125, 140)
        self.button_January9.clicked.connect(self.January9)

        self.button_January10 = QPushButton('10', self)
        self.button_January10.resize(20, 20)
        self.button_January10.move(145, 140)
        self.button_January10.clicked.connect(self.January10)

        self.button_January11 = QPushButton('11', self)
        self.button_January11.resize(20, 20)
        self.button_January11.move(25, 160)
        self.button_January11.clicked.connect(self.January11)

        self.button_January12 = QPushButton('12', self)
        self.button_January12.resize(20, 20)
        self.button_January12.move(45, 160)
        self.button_January12.clicked.connect(self.January12)

        self.button_January13 = QPushButton('13', self)
        self.button_January13.resize(20, 20)
        self.button_January13.move(65, 160)
        self.button_January13.clicked.connect(self.January13)

        self.button_January14 = QPushButton('14', self)
        self.button_January14.resize(20, 20)
        self.button_January14.move(85, 160)
        self.button_January14.clicked.connect(self.January14)

        self.button_January15 = QPushButton('15', self)
        self.button_January15.resize(20, 20)
        self.button_January15.move(105, 160)
        self.button_January15.clicked.connect(self.January15)

        self.button_January16 = QPushButton('16', self)
        self.button_January16.resize(20, 20)
        self.button_January16.move(125, 160)
        self.button_January16.clicked.connect(self.January16)

        self.button_January17 = QPushButton('17', self)
        self.button_January17.resize(20, 20)
        self.button_January17.move(145, 160)
        self.button_January17.clicked.connect(self.January17)

        self.button_January18 = QPushButton('18', self)
        self.button_January18.resize(20, 20)
        self.button_January18.move(25, 180)
        self.button_January18.clicked.connect(self.January18)

        self.button_January19 = QPushButton('19', self)
        self.button_January19.resize(20, 20)
        self.button_January19.move(45, 180)
        self.button_January19.clicked.connect(self.January19)

        self.button_January20 = QPushButton('20', self)
        self.button_January20.resize(20, 20)
        self.button_January20.move(65, 180)
        self.button_January20.clicked.connect(self.January20)

        self.button_January21 = QPushButton('21', self)
        self.button_January21.resize(20, 20)
        self.button_January21.move(85, 180)
        self.button_January21.clicked.connect(self.January21)

        self.button_January22 = QPushButton('22', self)
        self.button_January22.resize(20, 20)
        self.button_January22.move(105, 180)
        self.button_January22.clicked.connect(self.January22)

        self.button_January23 = QPushButton('23', self)
        self.button_January23.resize(20, 20)
        self.button_January23.move(125, 180)
        self.button_January23.clicked.connect(self.January23)

        self.button_January24 = QPushButton('24', self)
        self.button_January24.resize(20, 20)
        self.button_January24.move(145, 180)
        self.button_January24.clicked.connect(self.January24)

        self.button_January25 = QPushButton('25', self)
        self.button_January25.resize(20, 20)
        self.button_January25.move(25, 200)
        self.button_January25.clicked.connect(self.January25)

        self.button_January26 = QPushButton('26', self)
        self.button_January26.resize(20, 20)
        self.button_January26.move(45, 200)
        self.button_January26.clicked.connect(self.January26)

        self.button_January27 = QPushButton('27', self)
        self.button_January27.resize(20, 20)
        self.button_January27.move(65, 200)
        self.button_January27.clicked.connect(self.January27)

        self.button_January28 = QPushButton('28', self)
        self.button_January28.resize(20, 20)
        self.button_January28.move(85, 200)
        self.button_January28.clicked.connect(self.January28)

        self.button_January29 = QPushButton('29', self)
        self.button_January29.resize(20, 20)
        self.button_January29.move(105, 200)
        self.button_January29.clicked.connect(self.January29)

        self.button_January30 = QPushButton('30', self)
        self.button_January30.resize(20, 20)
        self.button_January30.move(125, 200)
        self.button_January30.clicked.connect(self.January30)

        self.button_January31 = QPushButton('31', self)
        self.button_January31.resize(20, 20)
        self.button_January31.move(145, 200)
        self.button_January31.clicked.connect(self.January31)

        # Февраль кнопки

        self.button_February1 = QPushButton('1', self)
        self.button_February1.resize(20, 20)
        self.button_February1.move(195, 120)
        self.button_February1.clicked.connect(self.February1)

        self.button_February2 = QPushButton('2', self)
        self.button_February2.resize(20, 20)
        self.button_February2.move(215, 120)
        self.button_February2.clicked.connect(self.February2)

        self.button_February3 = QPushButton('3', self)
        self.button_February3.resize(20, 20)
        self.button_February3.move(235, 120)
        self.button_February3.clicked.connect(self.February3)

        self.button_February4 = QPushButton('4', self)
        self.button_February4.resize(20, 20)
        self.button_February4.move(255, 120)
        self.button_February4.clicked.connect(self.February4)

        self.button_February5 = QPushButton('5', self)
        self.button_February5.resize(20, 20)
        self.button_February5.move(275, 120)
        self.button_February5.clicked.connect(self.February5)

        self.button_February6 = QPushButton('6', self)
        self.button_February6.resize(20, 20)
        self.button_February6.move(295, 120)
        self.button_February6.clicked.connect(self.February6)

        self.button_February7 = QPushButton('7', self)
        self.button_February7.resize(20, 20)
        self.button_February7.move(315, 120)
        self.button_February7.clicked.connect(self.February7)

        self.button_February8 = QPushButton('8', self)
        self.button_February8.resize(20, 20)
        self.button_February8.move(195, 140)
        self.button_February8.clicked.connect(self.February8)

        self.button_February9 = QPushButton('9', self)
        self.button_February9.resize(20, 20)
        self.button_February9.move(215, 140)
        self.button_February9.clicked.connect(self.February9)

        self.button_February10 = QPushButton('10', self)
        self.button_February10.resize(20, 20)
        self.button_February10.move(235, 140)
        self.button_February10.clicked.connect(self.February10)

        self.button_February11 = QPushButton('11', self)
        self.button_February11.resize(20, 20)
        self.button_February11.move(255, 140)
        self.button_February11.clicked.connect(self.February11)

        self.button_February12 = QPushButton('12', self)
        self.button_February12.resize(20, 20)
        self.button_February12.move(275, 140)
        self.button_February12.clicked.connect(self.February12)

        self.button_February13 = QPushButton('13', self)
        self.button_February13.resize(20, 20)
        self.button_February13.move(295, 140)
        self.button_February13.clicked.connect(self.February13)

        self.button_February14 = QPushButton('14', self)
        self.button_February14.resize(20, 20)
        self.button_February14.move(315, 140)
        self.button_February14.clicked.connect(self.February14)

        self.button_February15 = QPushButton('15', self)
        self.button_February15.resize(20, 20)
        self.button_February15.move(195, 160)
        self.button_February15.clicked.connect(self.February15)

        self.button_February16 = QPushButton('16', self)
        self.button_February16.resize(20, 20)
        self.button_February16.move(215, 160)
        self.button_February16.clicked.connect(self.February16)

        self.button_February17 = QPushButton('17', self)
        self.button_February17.resize(20, 20)
        self.button_February17.move(235, 160)
        self.button_February17.clicked.connect(self.February17)

        self.button_February18 = QPushButton('18', self)
        self.button_February18.resize(20, 20)
        self.button_February18.move(255, 160)
        self.button_February18.clicked.connect(self.February18)

        self.button_February19 = QPushButton('19', self)
        self.button_February19.resize(20, 20)
        self.button_February19.move(275, 160)
        self.button_February19.clicked.connect(self.February19)

        self.button_February20 = QPushButton('20', self)
        self.button_February20.resize(20, 20)
        self.button_February20.move(295, 160)
        self.button_February20.clicked.connect(self.February20)

        self.button_February21 = QPushButton('21', self)
        self.button_February21.resize(20, 20)
        self.button_February21.move(315, 160)
        self.button_February21.clicked.connect(self.February21)

        self.button_February22 = QPushButton('22', self)
        self.button_February22.resize(20, 20)
        self.button_February22.move(195, 180)
        self.button_February22.clicked.connect(self.February22)

        self.button_February23 = QPushButton('23', self)
        self.button_February23.resize(20, 20)
        self.button_February23.move(215, 180)
        self.button_February23.clicked.connect(self.February23)

        self.button_February24 = QPushButton('24', self)
        self.button_February24.resize(20, 20)
        self.button_February24.move(235, 180)
        self.button_February24.clicked.connect(self.February24)

        self.button_February25 = QPushButton('25', self)
        self.button_February25.resize(20, 20)
        self.button_February25.move(255, 180)
        self.button_February25.clicked.connect(self.February25)

        self.button_February26 = QPushButton('26', self)
        self.button_February26.resize(20, 20)
        self.button_February26.move(275, 180)
        self.button_February26.clicked.connect(self.February26)

        self.button_February27 = QPushButton('27', self)
        self.button_February27.resize(20, 20)
        self.button_February27.move(295, 180)
        self.button_February27.clicked.connect(self.February27)

        self.button_February28 = QPushButton('28', self)
        self.button_February28.resize(20, 20)
        self.button_February28.move(315, 180)
        self.button_February28.clicked.connect(self.February28)

        # Кнопки март

        self.button_March1 = QPushButton('1', self)
        self.button_March1.resize(20, 20)
        self.button_March1.move(365, 120)
        self.button_March1.clicked.connect(self.March1)

        self.button_March2 = QPushButton('2', self)
        self.button_March2.resize(20, 20)
        self.button_March2.move(385, 120)
        self.button_March2.clicked.connect(self.March2)

        self.button_March3 = QPushButton('3', self)
        self.button_March3.resize(20, 20)
        self.button_March3.move(405, 120)
        self.button_March3.clicked.connect(self.March3)

        self.button_March4 = QPushButton('4', self)
        self.button_March4.resize(20, 20)
        self.button_March4.move(425, 120)
        self.button_March4.clicked.connect(self.March4)

        self.button_March5 = QPushButton('5', self)
        self.button_March5.resize(20, 20)
        self.button_March5.move(445, 120)
        self.button_March5.clicked.connect(self.March5)

        self.button_March6 = QPushButton('6', self)
        self.button_March6.resize(20, 20)
        self.button_March6.move(465, 120)
        self.button_March6.clicked.connect(self.March6)

        self.button_March7 = QPushButton('7', self)
        self.button_March7.resize(20, 20)
        self.button_March7.move(485, 120)
        self.button_March7.clicked.connect(self.March7)

        self.button_March8 = QPushButton('8', self)
        self.button_March8.resize(20, 20)
        self.button_March8.move(365, 140)
        self.button_March8.clicked.connect(self.March8)

        self.button_March9 = QPushButton('9', self)
        self.button_March9.resize(20, 20)
        self.button_March9.move(385, 140)
        self.button_March9.clicked.connect(self.March9)

        self.button_March10 = QPushButton('10', self)
        self.button_March10.resize(20, 20)
        self.button_March10.move(405, 140)
        self.button_March10.clicked.connect(self.March10)

        self.button_March11 = QPushButton('11', self)
        self.button_March11.resize(20, 20)
        self.button_March11.move(425, 140)
        self.button_March11.clicked.connect(self.March11)

        self.button_March12 = QPushButton('12', self)
        self.button_March12.resize(20, 20)
        self.button_March12.move(445, 140)
        self.button_March12.clicked.connect(self.March12)

        self.button_March13 = QPushButton('13', self)
        self.button_March13.resize(20, 20)
        self.button_March13.move(465, 140)
        self.button_March13.clicked.connect(self.March13)

        self.button_March14 = QPushButton('14', self)
        self.button_March14.resize(20, 20)
        self.button_March14.move(485, 140)
        self.button_March14.clicked.connect(self.March14)

        self.button_March15 = QPushButton('15', self)
        self.button_March15.resize(20, 20)
        self.button_March15.move(365, 160)
        self.button_March15.clicked.connect(self.March15)

        self.button_March16 = QPushButton('16', self)
        self.button_March16.resize(20, 20)
        self.button_March16.move(385, 160)
        self.button_March16.clicked.connect(self.March16)

        self.button_March17 = QPushButton('17', self)
        self.button_March17.resize(20, 20)
        self.button_March17.move(405, 160)
        self.button_March17.clicked.connect(self.March17)

        self.button_March18 = QPushButton('18', self)
        self.button_March18.resize(20, 20)
        self.button_March18.move(425, 160)
        self.button_March18.clicked.connect(self.March18)

        self.button_March19 = QPushButton('19', self)
        self.button_March19.resize(20, 20)
        self.button_March19.move(445, 160)
        self.button_March19.clicked.connect(self.March19)

        self.button_March20 = QPushButton('20', self)
        self.button_March20.resize(20, 20)
        self.button_March20.move(465, 160)
        self.button_March20.clicked.connect(self.March20)

        self.button_March21 = QPushButton('21', self)
        self.button_March21.resize(20, 20)
        self.button_March21.move(485, 160)
        self.button_March21.clicked.connect(self.March21)

        self.button_March22 = QPushButton('22', self)
        self.button_March22.resize(20, 20)
        self.button_March22.move(365, 180)
        self.button_March22.clicked.connect(self.March22)

        self.button_March23 = QPushButton('23', self)
        self.button_March23.resize(20, 20)
        self.button_March23.move(385, 180)
        self.button_March23.clicked.connect(self.March23)

        self.button_March24 = QPushButton('24', self)
        self.button_March24.resize(20, 20)
        self.button_March24.move(405, 180)
        self.button_March24.clicked.connect(self.March24)

        self.button_March25 = QPushButton('25', self)
        self.button_March25.resize(20, 20)
        self.button_March25.move(425, 180)
        self.button_March25.clicked.connect(self.March25)

        self.button_March26 = QPushButton('26', self)
        self.button_March26.resize(20, 20)
        self.button_March26.move(445, 180)
        self.button_March26.clicked.connect(self.March26)

        self.button_March27 = QPushButton('27', self)
        self.button_March27.resize(20, 20)
        self.button_March27.move(465, 180)
        self.button_March27.clicked.connect(self.March27)

        self.button_March28 = QPushButton('28', self)
        self.button_March28.resize(20, 20)
        self.button_March28.move(485, 180)
        self.button_March28.clicked.connect(self.March28)

        self.button_March29 = QPushButton('29', self)
        self.button_March29.resize(20, 20)
        self.button_March29.move(365, 200)
        self.button_March29.clicked.connect(self.March29)

        self.button_March30 = QPushButton('30', self)
        self.button_March30.resize(20, 20)
        self.button_March30.move(385, 200)
        self.button_March30.clicked.connect(self.March30)

        self.button_March31 = QPushButton('31', self)
        self.button_March31.resize(20, 20)
        self.button_March31.move(405, 200)
        self.button_March31.clicked.connect(self.March31)

        # апрель кнопки

        self.button_April1 = QPushButton('1', self)
        self.button_April1.resize(20, 20)
        self.button_April1.move(595, 120)
        self.button_April1.clicked.connect(self.April1)

        self.button_April2 = QPushButton('2', self)
        self.button_April2.resize(20, 20)
        self.button_April2.move(615, 120)
        self.button_April2.clicked.connect(self.April2)

        self.button_April3 = QPushButton('3', self)
        self.button_April3.resize(20, 20)
        self.button_April3.move(635, 120)
        self.button_April3.clicked.connect(self.April3)

        self.button_April4 = QPushButton('4', self)
        self.button_April4.resize(20, 20)
        self.button_April4.move(655, 120)
        self.button_April4.clicked.connect(self.April4)

        self.button_April5 = QPushButton('5', self)
        self.button_April5.resize(20, 20)
        self.button_April5.move(535, 140)
        self.button_April5.clicked.connect(self.April5)

        self.button_April6 = QPushButton('6', self)
        self.button_April6.resize(20, 20)
        self.button_April6.move(555, 140)
        self.button_April6.clicked.connect(self.April6)

        self.button_April7 = QPushButton('7', self)
        self.button_April7.resize(20, 20)
        self.button_April7.move(575, 140)
        self.button_April7.clicked.connect(self.April7)

        self.button_April8 = QPushButton('8', self)
        self.button_April8.resize(20, 20)
        self.button_April8.move(595, 140)
        self.button_April8.clicked.connect(self.April8)

        self.button_April9 = QPushButton('9', self)
        self.button_April9.resize(20, 20)
        self.button_April9.move(615, 140)
        self.button_April9.clicked.connect(self.April9)

        self.button_April10 = QPushButton('10', self)
        self.button_April10.resize(20, 20)
        self.button_April10.move(635, 140)
        self.button_April10.clicked.connect(self.April10)

        self.button_April11 = QPushButton('11', self)
        self.button_April11.resize(20, 20)
        self.button_April11.move(655, 140)
        self.button_April11.clicked.connect(self.April11)

        self.button_April12 = QPushButton('12', self)
        self.button_April12.resize(20, 20)
        self.button_April12.move(535, 160)
        self.button_April12.clicked.connect(self.April12)

        self.button_April13 = QPushButton('13', self)
        self.button_April13.resize(20, 20)
        self.button_April13.move(555, 160)
        self.button_April13.clicked.connect(self.April13)

        self.button_April14 = QPushButton('14', self)
        self.button_April14.resize(20, 20)
        self.button_April14.move(575, 160)
        self.button_April14.clicked.connect(self.April14)

        self.button_April15 = QPushButton('15', self)
        self.button_April15.resize(20, 20)
        self.button_April15.move(595, 160)
        self.button_April15.clicked.connect(self.April15)

        self.button_April16 = QPushButton('16', self)
        self.button_April16.resize(20, 20)
        self.button_April16.move(615, 160)
        self.button_April16.clicked.connect(self.April16)

        self.button_April17 = QPushButton('17', self)
        self.button_April17.resize(20, 20)
        self.button_April17.move(635, 160)
        self.button_April17.clicked.connect(self.April17)

        self.button_April18 = QPushButton('18', self)
        self.button_April18.resize(20, 20)
        self.button_April18.move(655, 160)
        self.button_April18.clicked.connect(self.April18)

        self.button_April19 = QPushButton('19', self)
        self.button_April19.resize(20, 20)
        self.button_April19.move(535, 180)
        self.button_April19.clicked.connect(self.April19)

        self.button_April20 = QPushButton('20', self)
        self.button_April20.resize(20, 20)
        self.button_April20.move(555, 180)
        self.button_April20.clicked.connect(self.April20)

        self.button_April21 = QPushButton('21', self)
        self.button_April21.resize(20, 20)
        self.button_April21.move(575, 180)
        self.button_April21.clicked.connect(self.April21)

        self.button_April22 = QPushButton('22', self)
        self.button_April22.resize(20, 20)
        self.button_April22.move(595, 180)
        self.button_April22.clicked.connect(self.April22)

        self.button_April23 = QPushButton('23', self)
        self.button_April23.resize(20, 20)
        self.button_April23.move(615, 180)
        self.button_April23.clicked.connect(self.April23)

        self.button_April24 = QPushButton('24', self)
        self.button_April24.resize(20, 20)
        self.button_April24.move(635, 180)
        self.button_April24.clicked.connect(self.April24)

        self.button_April25 = QPushButton('25', self)
        self.button_April25.resize(20, 20)
        self.button_April25.move(655, 180)
        self.button_April25.clicked.connect(self.April25)

        self.button_April26 = QPushButton('26', self)
        self.button_April26.resize(20, 20)
        self.button_April26.move(535, 200)
        self.button_April26.clicked.connect(self.April26)

        self.button_April27 = QPushButton('27', self)
        self.button_April27.resize(20, 20)
        self.button_April27.move(555, 200)
        self.button_April27.clicked.connect(self.April27)

        self.button_April28 = QPushButton('28', self)
        self.button_April28.resize(20, 20)
        self.button_April28.move(575, 200)
        self.button_April28.clicked.connect(self.April28)

        self.button_April29 = QPushButton('29', self)
        self.button_April29.resize(20, 20)
        self.button_April29.move(595, 200)
        self.button_April29.clicked.connect(self.April29)

        self.button_April30 = QPushButton('30', self)
        self.button_April30.resize(20, 20)
        self.button_April30.move(615, 200)
        self.button_April30.clicked.connect(self.April30)

        # Кнопки май

        self.button_May1 = QPushButton('1', self)
        self.button_May1.resize(20, 20)
        self.button_May1.move(125, 260)
        self.button_May1.clicked.connect(self.May1)

        self.button_May2 = QPushButton('2', self)
        self.button_May2.resize(20, 20)
        self.button_May2.move(145, 260)
        self.button_May2.clicked.connect(self.May2)

        self.button_May3 = QPushButton('3', self)
        self.button_May3.resize(20, 20)
        self.button_May3.move(25, 280)
        self.button_May3.clicked.connect(self.May3)

        self.button_May4 = QPushButton('4', self)
        self.button_May4.resize(20, 20)
        self.button_May4.move(45, 280)
        self.button_May4.clicked.connect(self.May4)

        self.button_May5 = QPushButton('5', self)
        self.button_May5.resize(20, 20)
        self.button_May5.move(65, 280)
        self.button_May5.clicked.connect(self.May5)

        self.button_May6 = QPushButton('6', self)
        self.button_May6.resize(20, 20)
        self.button_May6.move(85, 280)
        self.button_May6.clicked.connect(self.May6)

        self.button_May7 = QPushButton('7', self)
        self.button_May7.resize(20, 20)
        self.button_May7.move(105, 280)
        self.button_May7.clicked.connect(self.May7)

        self.button_May8 = QPushButton('8', self)
        self.button_May8.resize(20, 20)
        self.button_May8.move(125, 280)
        self.button_May8.clicked.connect(self.May8)

        self.button_May9 = QPushButton('9', self)
        self.button_May9.resize(20, 20)
        self.button_May9.move(145, 280)
        self.button_May9.clicked.connect(self.May9)

        self.button_May10 = QPushButton('10', self)
        self.button_May10.resize(20, 20)
        self.button_May10.move(25, 300)
        self.button_May10.clicked.connect(self.May10)

        self.button_May11 = QPushButton('11', self)
        self.button_May11.resize(20, 20)
        self.button_May11.move(45, 300)
        self.button_May11.clicked.connect(self.May11)

        self.button_May12 = QPushButton('12', self)
        self.button_May12.resize(20, 20)
        self.button_May12.move(65, 300)
        self.button_May12.clicked.connect(self.May12)

        self.button_May13 = QPushButton('13', self)
        self.button_May13.resize(20, 20)
        self.button_May13.move(85, 300)
        self.button_May13.clicked.connect(self.May13)

        self.button_May14 = QPushButton('14', self)
        self.button_May14.resize(20, 20)
        self.button_May14.move(105, 300)
        self.button_May14.clicked.connect(self.May14)

        self.button_May15 = QPushButton('15', self)
        self.button_May15.resize(20, 20)
        self.button_May15.move(125, 300)
        self.button_May15.clicked.connect(self.May15)

        self.button_May16 = QPushButton('16', self)
        self.button_May16.resize(20, 20)
        self.button_May16.move(145, 300)
        self.button_May16.clicked.connect(self.May16)

        self.button_May17 = QPushButton('17', self)
        self.button_May17.resize(20, 20)
        self.button_May17.move(25, 320)
        self.button_May17.clicked.connect(self.May17)

        self.button_May18 = QPushButton('18', self)
        self.button_May18.resize(20, 20)
        self.button_May18.move(45, 320)
        self.button_May18.clicked.connect(self.May18)

        self.button_May19 = QPushButton('19', self)
        self.button_May19.resize(20, 20)
        self.button_May19.move(65, 320)
        self.button_May19.clicked.connect(self.May19)

        self.button_May20 = QPushButton('20', self)
        self.button_May20.resize(20, 20)
        self.button_May20.move(85, 320)
        self.button_May20.clicked.connect(self.May20)

        self.button_May21 = QPushButton('21', self)
        self.button_May21.resize(20, 20)
        self.button_May21.move(105, 320)
        self.button_May21.clicked.connect(self.May21)

        self.button_May22 = QPushButton('22', self)
        self.button_May22.resize(20, 20)
        self.button_May22.move(125, 320)
        self.button_May22.clicked.connect(self.May22)

        self.button_May23 = QPushButton('23', self)
        self.button_May23.resize(20, 20)
        self.button_May23.move(145, 320)
        self.button_May23.clicked.connect(self.May23)

        self.button_May24 = QPushButton('24', self)
        self.button_May24.resize(20, 20)
        self.button_May24.move(25, 340)
        self.button_May24.clicked.connect(self.May24)

        self.button_May25 = QPushButton('25', self)
        self.button_May25.resize(20, 20)
        self.button_May25.move(45, 340)
        self.button_May25.clicked.connect(self.May25)

        self.button_May26 = QPushButton('26', self)
        self.button_May26.resize(20, 20)
        self.button_May26.move(65, 340)
        self.button_May26.clicked.connect(self.May26)

        self.button_May27 = QPushButton('27', self)
        self.button_May27.resize(20, 20)
        self.button_May27.move(85, 340)
        self.button_May27.clicked.connect(self.May27)

        self.button_May28 = QPushButton('28', self)
        self.button_May28.resize(20, 20)
        self.button_May28.move(105, 340)
        self.button_May28.clicked.connect(self.May28)

        self.button_May29 = QPushButton('29', self)
        self.button_May29.resize(20, 20)
        self.button_May29.move(125, 340)
        self.button_May29.clicked.connect(self.May29)

        self.button_May30 = QPushButton('30', self)
        self.button_May30.resize(20, 20)
        self.button_May30.move(145, 340)
        self.button_May30.clicked.connect(self.May30)

        self.button_May31 = QPushButton('31', self)
        self.button_May31.resize(20, 20)
        self.button_May31.move(25, 360)
        self.button_May31.clicked.connect(self.May31)

        # Июнь

        self.button_June1 = QPushButton('1', self)
        self.button_June1.resize(20, 20)
        self.button_June1.move(215, 260)
        self.button_June1.clicked.connect(self.June1)

        self.button_June2 = QPushButton('2', self)
        self.button_June2.resize(20, 20)
        self.button_June2.move(235, 260)
        self.button_June2.clicked.connect(self.June2)

        self.button_June3 = QPushButton('3', self)
        self.button_June3.resize(20, 20)
        self.button_June3.move(255, 260)
        self.button_June3.clicked.connect(self.June3)

        self.button_June4 = QPushButton('4', self)
        self.button_June4.resize(20, 20)
        self.button_June4.move(275, 260)
        self.button_June4.clicked.connect(self.June4)

        self.button_June5 = QPushButton('5', self)
        self.button_June5.resize(20, 20)
        self.button_June5.move(295, 260)
        self.button_June5.clicked.connect(self.June5)

        self.button_June6 = QPushButton('6', self)
        self.button_June6.resize(20, 20)
        self.button_June6.move(315, 260)
        self.button_June6.clicked.connect(self.June6)

        self.button_June7 = QPushButton('7', self)
        self.button_June7.resize(20, 20)
        self.button_June7.move(195, 280)
        self.button_June7.clicked.connect(self.June7)

        self.button_June8 = QPushButton('8', self)
        self.button_June8.resize(20, 20)
        self.button_June8.move(215, 280)
        self.button_June8.clicked.connect(self.June8)

        self.button_June9 = QPushButton('9', self)
        self.button_June9.resize(20, 20)
        self.button_June9.move(235, 280)
        self.button_June9.clicked.connect(self.June9)

        self.button_June10 = QPushButton('10', self)
        self.button_June10.resize(20, 20)
        self.button_June10.move(255, 280)
        self.button_June10.clicked.connect(self.June10)

        self.button_June11 = QPushButton('11', self)
        self.button_June11.resize(20, 20)
        self.button_June11.move(275, 280)
        self.button_June11.clicked.connect(self.June11)

        self.button_June12 = QPushButton('12', self)
        self.button_June12.resize(20, 20)
        self.button_June12.move(295, 280)
        self.button_June12.clicked.connect(self.June12)

        self.button_June13 = QPushButton('13', self)
        self.button_June13.resize(20, 20)
        self.button_June13.move(315, 280)
        self.button_June13.clicked.connect(self.June13)

        self.button_June14 = QPushButton('14', self)
        self.button_June14.resize(20, 20)
        self.button_June14.move(195, 300)
        self.button_June14.clicked.connect(self.June14)

        self.button_June15 = QPushButton('15', self)
        self.button_June15.resize(20, 20)
        self.button_June15.move(215, 300)
        self.button_June15.clicked.connect(self.June15)

        self.button_June16 = QPushButton('16', self)
        self.button_June16.resize(20, 20)
        self.button_June16.move(235, 300)
        self.button_June16.clicked.connect(self.June16)

        self.button_June17 = QPushButton('17', self)
        self.button_June17.resize(20, 20)
        self.button_June17.move(255, 300)
        self.button_June17.clicked.connect(self.June17)

        self.button_June18 = QPushButton('18', self)
        self.button_June18.resize(20, 20)
        self.button_June18.move(275, 300)
        self.button_June18.clicked.connect(self.June18)

        self.button_June19 = QPushButton('19', self)
        self.button_June19.resize(20, 20)
        self.button_June19.move(295, 300)
        self.button_June19.clicked.connect(self.June19)

        self.button_June20 = QPushButton('20', self)
        self.button_June20.resize(20, 20)
        self.button_June20.move(315, 300)
        self.button_June20.clicked.connect(self.June20)

        self.button_June21 = QPushButton('21', self)
        self.button_June21.resize(20, 20)
        self.button_June21.move(195, 320)
        self.button_June21.clicked.connect(self.June21)

        self.button_June22 = QPushButton('22', self)
        self.button_June22.resize(20, 20)
        self.button_June22.move(215, 320)
        self.button_June22.clicked.connect(self.June22)

        self.button_June23 = QPushButton('23', self)
        self.button_June23.resize(20, 20)
        self.button_June23.move(235, 320)
        self.button_June23.clicked.connect(self.June23)

        self.button_June24 = QPushButton('24', self)
        self.button_June24.resize(20, 20)
        self.button_June24.move(255, 320)
        self.button_June24.clicked.connect(self.June24)

        self.button_June25 = QPushButton('25', self)
        self.button_June25.resize(20, 20)
        self.button_June25.move(275, 320)
        self.button_June25.clicked.connect(self.June25)

        self.button_June26 = QPushButton('26', self)
        self.button_June26.resize(20, 20)
        self.button_June26.move(295, 320)
        self.button_June26.clicked.connect(self.June26)

        self.button_June27 = QPushButton('27', self)
        self.button_June27.resize(20, 20)
        self.button_June27.move(315, 320)
        self.button_June27.clicked.connect(self.June27)

        self.button_June28 = QPushButton('28', self)
        self.button_June28.resize(20, 20)
        self.button_June28.move(195, 340)
        self.button_June28.clicked.connect(self.June28)

        self.button_June29 = QPushButton('29', self)
        self.button_June29.resize(20, 20)
        self.button_June29.move(215, 340)
        self.button_June29.clicked.connect(self.June29)

        self.button_June30 = QPushButton('30', self)
        self.button_June30.resize(20, 20)
        self.button_June30.move(235, 340)
        self.button_June30.clicked.connect(self.June30)

        # Июль кнопки

        self.button_July1 = QPushButton('1', self)
        self.button_July1.resize(20, 20)
        self.button_July1.move(425, 260)
        self.button_July1.clicked.connect(self.July1)

        self.button_July2 = QPushButton('2', self)
        self.button_July2.resize(20, 20)
        self.button_July2.move(445, 260)
        self.button_July2.clicked.connect(self.July2)

        self.button_July3 = QPushButton('3', self)
        self.button_July3.resize(20, 20)
        self.button_July3.move(465, 260)
        self.button_July3.clicked.connect(self.July3)

        self.button_July4 = QPushButton('4', self)
        self.button_July4.resize(20, 20)
        self.button_July4.move(485, 260)
        self.button_July4.clicked.connect(self.July4)

        self.button_July5 = QPushButton('5', self)
        self.button_July5.resize(20, 20)
        self.button_July5.move(365, 280)
        self.button_July5.clicked.connect(self.July5)

        self.button_July6 = QPushButton('6', self)
        self.button_July6.resize(20, 20)
        self.button_July6.move(385, 280)
        self.button_July6.clicked.connect(self.July6)

        self.button_July7 = QPushButton('7', self)
        self.button_July7.resize(20, 20)
        self.button_July7.move(405, 280)
        self.button_July7.clicked.connect(self.July7)

        self.button_July8 = QPushButton('8', self)
        self.button_July8.resize(20, 20)
        self.button_July8.move(425, 280)
        self.button_July8.clicked.connect(self.July8)

        self.button_July9 = QPushButton('9', self)
        self.button_July9.resize(20, 20)
        self.button_July9.move(445, 280)
        self.button_July9.clicked.connect(self.July9)

        self.button_July10 = QPushButton('10', self)
        self.button_July10.resize(20, 20)
        self.button_July10.move(465, 280)
        self.button_July10.clicked.connect(self.July10)

        self.button_July11 = QPushButton('11', self)
        self.button_July11.resize(20, 20)
        self.button_July11.move(485, 280)
        self.button_July11.clicked.connect(self.July11)

        self.button_July12 = QPushButton('12', self)
        self.button_July12.resize(20, 20)
        self.button_July12.move(365, 300)
        self.button_July12.clicked.connect(self.July12)

        self.button_July13 = QPushButton('13', self)
        self.button_July13.resize(20, 20)
        self.button_July13.move(385, 300)
        self.button_July13.clicked.connect(self.July13)

        self.button_July14 = QPushButton('14', self)
        self.button_July14.resize(20, 20)
        self.button_July14.move(405, 300)
        self.button_July14.clicked.connect(self.July14)

        self.button_July15 = QPushButton('15', self)
        self.button_July15.resize(20, 20)
        self.button_July15.move(425, 300)
        self.button_July15.clicked.connect(self.July15)

        self.button_July16 = QPushButton('16', self)
        self.button_July16.resize(20, 20)
        self.button_July16.move(445, 300)
        self.button_July16.clicked.connect(self.July16)

        self.button_July17 = QPushButton('17', self)
        self.button_July17.resize(20, 20)
        self.button_July17.move(465, 300)
        self.button_July17.clicked.connect(self.July17)

        self.button_July18 = QPushButton('18', self)
        self.button_July18.resize(20, 20)
        self.button_July18.move(485, 300)
        self.button_July18.clicked.connect(self.July18)

        self.button_July19 = QPushButton('19', self)
        self.button_July19.resize(20, 20)
        self.button_July19.move(365, 320)
        self.button_July19.clicked.connect(self.July19)

        self.button_July20 = QPushButton('20', self)
        self.button_July20.resize(20, 20)
        self.button_July20.move(385, 320)
        self.button_July20.clicked.connect(self.July20)

        self.button_July21 = QPushButton('21', self)
        self.button_July21.resize(20, 20)
        self.button_July21.move(405, 320)
        self.button_July21.clicked.connect(self.July21)

        self.button_July22 = QPushButton('22', self)
        self.button_July22.resize(20, 20)
        self.button_July22.move(425, 320)
        self.button_July22.clicked.connect(self.July22)

        self.button_July23 = QPushButton('23', self)
        self.button_July23.resize(20, 20)
        self.button_July23.move(445, 320)
        self.button_July23.clicked.connect(self.July23)

        self.button_July24 = QPushButton('24', self)
        self.button_July24.resize(20, 20)
        self.button_July24.move(465, 320)
        self.button_July24.clicked.connect(self.July24)

        self.button_July25 = QPushButton('25', self)
        self.button_July25.resize(20, 20)
        self.button_July25.move(485, 320)
        self.button_July25.clicked.connect(self.July25)

        self.button_July26 = QPushButton('26', self)
        self.button_July26.resize(20, 20)
        self.button_July26.move(365, 340)
        self.button_July26.clicked.connect(self.July26)

        self.button_July27 = QPushButton('27', self)
        self.button_July27.resize(20, 20)
        self.button_July27.move(385, 340)
        self.button_July27.clicked.connect(self.July27)

        self.button_July28 = QPushButton('28', self)
        self.button_July28.resize(20, 20)
        self.button_July28.move(405, 340)
        self.button_July28.clicked.connect(self.July28)

        self.button_July29 = QPushButton('29', self)
        self.button_July29.resize(20, 20)
        self.button_July29.move(425, 340)
        self.button_July29.clicked.connect(self.July29)

        self.button_July30 = QPushButton('30', self)
        self.button_July30.resize(20, 20)
        self.button_July30.move(445, 340)
        self.button_July30.clicked.connect(self.July30)

        self.button_July31 = QPushButton('31', self)
        self.button_July31.resize(20, 20)
        self.button_July31.move(465, 340)
        self.button_July31.clicked.connect(self.July31)

        # Август кнопки

        self.button_August1 = QPushButton('1', self)
        self.button_August1.resize(20, 20)
        self.button_August1.move(655, 260)
        self.button_August1.clicked.connect(self.August1)

        self.button_August2 = QPushButton('2', self)
        self.button_August2.resize(20, 20)
        self.button_August2.move(535, 280)
        self.button_August2.clicked.connect(self.August2)

        self.button_August3 = QPushButton('3', self)
        self.button_August3.resize(20, 20)
        self.button_August3.move(555, 280)
        self.button_August3.clicked.connect(self.August3)

        self.button_August4 = QPushButton('4', self)
        self.button_August4.resize(20, 20)
        self.button_August4.move(575, 280)
        self.button_August4.clicked.connect(self.August4)

        self.button_August5 = QPushButton('5', self)
        self.button_August5.resize(20, 20)
        self.button_August5.move(595, 280)
        self.button_August5.clicked.connect(self.August5)

        self.button_August6 = QPushButton('6', self)
        self.button_August6.resize(20, 20)
        self.button_August6.move(615, 280)
        self.button_August6.clicked.connect(self.August6)

        self.button_August7 = QPushButton('7', self)
        self.button_August7.resize(20, 20)
        self.button_August7.move(635, 280)
        self.button_August7.clicked.connect(self.August7)

        self.button_August8 = QPushButton('8', self)
        self.button_August8.resize(20, 20)
        self.button_August8.move(655, 280)
        self.button_August8.clicked.connect(self.August8)

        self.button_August9 = QPushButton('9', self)
        self.button_August9.resize(20, 20)
        self.button_August9.move(535, 300)
        self.button_August9.clicked.connect(self.August9)

        self.button_August10 = QPushButton('10', self)
        self.button_August10.resize(20, 20)
        self.button_August10.move(555, 300)
        self.button_August10.clicked.connect(self.August10)

        self.button_August11 = QPushButton('11', self)
        self.button_August11.resize(20, 20)
        self.button_August11.move(575, 300)
        self.button_August11.clicked.connect(self.August11)

        self.button_August12 = QPushButton('12', self)
        self.button_August12.resize(20, 20)
        self.button_August12.move(595, 300)
        self.button_August12.clicked.connect(self.August12)

        self.button_August13 = QPushButton('13', self)
        self.button_August13.resize(20, 20)
        self.button_August13.move(615, 300)
        self.button_August13.clicked.connect(self.August13)

        self.button_August14 = QPushButton('14', self)
        self.button_August14.resize(20, 20)
        self.button_August14.move(635, 300)
        self.button_August14.clicked.connect(self.August14)

        self.button_August15 = QPushButton('15', self)
        self.button_August15.resize(20, 20)
        self.button_August15.move(655, 300)
        self.button_August15.clicked.connect(self.August15)

        self.button_August16 = QPushButton('16', self)
        self.button_August16.resize(20, 20)
        self.button_August16.move(535, 320)
        self.button_August16.clicked.connect(self.August16)

        self.button_August17 = QPushButton('17', self)
        self.button_August17.resize(20, 20)
        self.button_August17.move(555, 320)
        self.button_August17.clicked.connect(self.August17)

        self.button_August18 = QPushButton('18', self)
        self.button_August18.resize(20, 20)
        self.button_August18.move(575, 320)
        self.button_August18.clicked.connect(self.August18)

        self.button_August19 = QPushButton('19', self)
        self.button_August19.resize(20, 20)
        self.button_August19.move(595, 320)
        self.button_August19.clicked.connect(self.August19)

        self.button_August20 = QPushButton('20', self)
        self.button_August20.resize(20, 20)
        self.button_August20.move(615, 320)
        self.button_August20.clicked.connect(self.August20)

        self.button_August21 = QPushButton('21', self)
        self.button_August21.resize(20, 20)
        self.button_August21.move(635, 320)
        self.button_August21.clicked.connect(self.August21)

        self.button_August22 = QPushButton('22', self)
        self.button_August22.resize(20, 20)
        self.button_August22.move(655, 320)
        self.button_August22.clicked.connect(self.August22)

        self.button_August23 = QPushButton('23', self)
        self.button_August23.resize(20, 20)
        self.button_August23.move(535, 340)
        self.button_August23.clicked.connect(self.August23)

        self.button_August24 = QPushButton('24', self)
        self.button_August24.resize(20, 20)
        self.button_August24.move(555, 340)
        self.button_August24.clicked.connect(self.August24)

        self.button_August25 = QPushButton('25', self)
        self.button_August25.resize(20, 20)
        self.button_August25.move(575, 340)
        self.button_August25.clicked.connect(self.August25)

        self.button_August26 = QPushButton('26', self)
        self.button_August26.resize(20, 20)
        self.button_August26.move(595, 340)
        self.button_August26.clicked.connect(self.August26)

        self.button_August27 = QPushButton('27', self)
        self.button_August27.resize(20, 20)
        self.button_August27.move(615, 340)
        self.button_August27.clicked.connect(self.August27)

        self.button_August28 = QPushButton('28', self)
        self.button_August28.resize(20, 20)
        self.button_August28.move(635, 340)
        self.button_August28.clicked.connect(self.August28)

        self.button_August29 = QPushButton('29', self)
        self.button_August29.resize(20, 20)
        self.button_August29.move(655, 340)
        self.button_August29.clicked.connect(self.August29)

        self.button_August30 = QPushButton('30', self)
        self.button_August30.resize(20, 20)
        self.button_August30.move(535, 360)
        self.button_August30.clicked.connect(self.August30)

        self.button_August31 = QPushButton('31', self)
        self.button_August31.resize(20, 20)
        self.button_August31.move(555, 360)
        self.button_August31.clicked.connect(self.August31)

        # Сентябрь кнопки
        self.button_September1 = QPushButton('1', self)
        self.button_September1.resize(20, 20)
        self.button_September1.move(65, 425)
        self.button_September1.clicked.connect(self.September1)

        self.button_September2 = QPushButton('2', self)
        self.button_September2.resize(20, 20)
        self.button_September2.move(85, 425)
        self.button_September2.clicked.connect(self.September2)

        self.button_September3 = QPushButton('3', self)
        self.button_September3.resize(20, 20)
        self.button_September3.move(105, 425)
        self.button_September3.clicked.connect(self.September3)

        self.button_September4 = QPushButton('4', self)
        self.button_September4.resize(20, 20)
        self.button_September4.move(125, 425)
        self.button_September4.clicked.connect(self.September4)

        self.button_September5 = QPushButton('5', self)
        self.button_September5.resize(20, 20)
        self.button_September5.move(145, 425)
        self.button_September5.clicked.connect(self.September5)

        self.button_September6 = QPushButton('6', self)
        self.button_September6.resize(20, 20)
        self.button_September6.move(25, 445)
        self.button_September6.clicked.connect(self.September6)

        self.button_September7 = QPushButton('7', self)
        self.button_September7.resize(20, 20)
        self.button_September7.move(45, 445)
        self.button_September7.clicked.connect(self.September7)

        self.button_September8 = QPushButton('8', self)
        self.button_September8.resize(20, 20)
        self.button_September8.move(65, 445)
        self.button_September8.clicked.connect(self.September8)

        self.button_September9 = QPushButton('9', self)
        self.button_September9.resize(20, 20)
        self.button_September9.move(85, 445)
        self.button_September9.clicked.connect(self.September9)

        self.button_September10 = QPushButton('10', self)
        self.button_September10.resize(20, 20)
        self.button_September10.move(105, 445)
        self.button_September10.clicked.connect(self.September10)

        self.button_September11 = QPushButton('11', self)
        self.button_September11.resize(20, 20)
        self.button_September11.move(125, 445)
        self.button_September11.clicked.connect(self.September11)

        self.button_September12 = QPushButton('12', self)
        self.button_September12.resize(20, 20)
        self.button_September12.move(145, 445)
        self.button_September12.clicked.connect(self.September12)

        self.button_September13 = QPushButton('13', self)
        self.button_September13.resize(20, 20)
        self.button_September13.move(25, 465)
        self.button_September13.clicked.connect(self.September13)

        self.button_September14 = QPushButton('14', self)
        self.button_September14.resize(20, 20)
        self.button_September14.move(45, 465)
        self.button_September14.clicked.connect(self.September14)

        self.button_September15 = QPushButton('15', self)
        self.button_September15.resize(20, 20)
        self.button_September15.move(65, 465)
        self.button_September15.clicked.connect(self.September15)

        self.button_September16 = QPushButton('16', self)
        self.button_September16.resize(20, 20)
        self.button_September16.move(85, 465)
        self.button_September16.clicked.connect(self.September16)

        self.button_September17 = QPushButton('17', self)
        self.button_September17.resize(20, 20)
        self.button_September17.move(105, 465)
        self.button_September17.clicked.connect(self.September17)

        self.button_September18 = QPushButton('18', self)
        self.button_September18.resize(20, 20)
        self.button_September18.move(125, 465)
        self.button_September18.clicked.connect(self.September18)

        self.button_September19 = QPushButton('19', self)
        self.button_September19.resize(20, 20)
        self.button_September19.move(145, 465)
        self.button_September19.clicked.connect(self.September19)

        self.button_September20 = QPushButton('20', self)
        self.button_September20.resize(20, 20)
        self.button_September20.move(25, 485)
        self.button_September20.clicked.connect(self.September20)

        self.button_September21 = QPushButton('21', self)
        self.button_September21.resize(20, 20)
        self.button_September21.move(45, 485)
        self.button_September21.clicked.connect(self.September21)

        self.button_September22 = QPushButton('22', self)
        self.button_September22.resize(20, 20)
        self.button_September22.move(65, 485)
        self.button_September22.clicked.connect(self.September22)

        self.button_September23 = QPushButton('23', self)
        self.button_September23.resize(20, 20)
        self.button_September23.move(85, 485)
        self.button_September23.clicked.connect(self.September23)

        self.button_September24 = QPushButton('24', self)
        self.button_September24.resize(20, 20)
        self.button_September24.move(105, 485)
        self.button_September24.clicked.connect(self.September24)

        self.button_September25 = QPushButton('25', self)
        self.button_September25.resize(20, 20)
        self.button_September25.move(125, 485)
        self.button_September25.clicked.connect(self.September25)

        self.button_September26 = QPushButton('26', self)
        self.button_September26.resize(20, 20)
        self.button_September26.move(145, 485)
        self.button_September26.clicked.connect(self.September26)

        self.button_September27 = QPushButton('27', self)
        self.button_September27.resize(20, 20)
        self.button_September27.move(25, 505)
        self.button_September27.clicked.connect(self.September27)

        self.button_September28 = QPushButton('28', self)
        self.button_September28.resize(20, 20)
        self.button_September28.move(45, 505)
        self.button_September28.clicked.connect(self.September28)

        self.button_September29 = QPushButton('29', self)
        self.button_September29.resize(20, 20)
        self.button_September29.move(65, 505)
        self.button_September29.clicked.connect(self.September29)

        self.button_September30 = QPushButton('30', self)
        self.button_September30.resize(20, 20)
        self.button_September30.move(85, 505)
        self.button_September30.clicked.connect(self.September30)

        # Кнопки Октябрь

        self.button_October1 = QPushButton('1', self)
        self.button_October1.resize(20, 20)
        self.button_October1.move(275, 425)
        self.button_October1.clicked.connect(self.October1)

        self.button_October2 = QPushButton('2', self)
        self.button_October2.resize(20, 20)
        self.button_October2.move(295, 425)
        self.button_October2.clicked.connect(self.October2)

        self.button_October3 = QPushButton('3', self)
        self.button_October3.resize(20, 20)
        self.button_October3.move(315, 425)
        self.button_October3.clicked.connect(self.October3)

        self.button_October4 = QPushButton('4', self)
        self.button_October4.resize(20, 20)
        self.button_October4.move(195, 445)
        self.button_October4.clicked.connect(self.October4)

        self.button_October5 = QPushButton('5', self)
        self.button_October5.resize(20, 20)
        self.button_October5.move(215, 445)
        self.button_October5.clicked.connect(self.October5)

        self.button_October6 = QPushButton('6', self)
        self.button_October6.resize(20, 20)
        self.button_October6.move(235, 445)
        self.button_October6.clicked.connect(self.October6)

        self.button_October7 = QPushButton('7', self)
        self.button_October7.resize(20, 20)
        self.button_October7.move(255, 445)
        self.button_October7.clicked.connect(self.October7)

        self.button_October8 = QPushButton('8', self)
        self.button_October8.resize(20, 20)
        self.button_October8.move(275, 445)
        self.button_October8.clicked.connect(self.October8)

        self.button_October9 = QPushButton('9', self)
        self.button_October9.resize(20, 20)
        self.button_October9.move(295, 445)
        self.button_October9.clicked.connect(self.October9)

        self.button_October10 = QPushButton('10', self)
        self.button_October10.resize(20, 20)
        self.button_October10.move(315, 445)
        self.button_October10.clicked.connect(self.October10)

        self.button_October11 = QPushButton('11', self)
        self.button_October11.resize(20, 20)
        self.button_October11.move(195, 465)
        self.button_October11.clicked.connect(self.October11)

        self.button_October12 = QPushButton('12', self)
        self.button_October12.resize(20, 20)
        self.button_October12.move(215, 465)
        self.button_October12.clicked.connect(self.October12)

        self.button_October13 = QPushButton('13', self)
        self.button_October13.resize(20, 20)
        self.button_October13.move(235, 465)
        self.button_October13.clicked.connect(self.October13)

        self.button_October14 = QPushButton('14', self)
        self.button_October14.resize(20, 20)
        self.button_October14.move(255, 465)
        self.button_October14.clicked.connect(self.October14)

        self.button_October15 = QPushButton('15', self)
        self.button_October15.resize(20, 20)
        self.button_October15.move(275, 465)
        self.button_October15.clicked.connect(self.October15)

        self.button_October16 = QPushButton('16', self)
        self.button_October16.resize(20, 20)
        self.button_October16.move(295, 465)
        self.button_October16.clicked.connect(self.October16)

        self.button_October17 = QPushButton('17', self)
        self.button_October17.resize(20, 20)
        self.button_October17.move(315, 465)
        self.button_October17.clicked.connect(self.October17)

        self.button_October18 = QPushButton('18', self)
        self.button_October18.resize(20, 20)
        self.button_October18.move(195, 485)
        self.button_October18.clicked.connect(self.October18)

        self.button_October19 = QPushButton('19', self)
        self.button_October19.resize(20, 20)
        self.button_October19.move(215, 485)
        self.button_October19.clicked.connect(self.October19)

        self.button_October20 = QPushButton('20', self)
        self.button_October20.resize(20, 20)
        self.button_October20.move(235, 485)
        self.button_October20.clicked.connect(self.October20)

        self.button_October21 = QPushButton('21', self)
        self.button_October21.resize(20, 20)
        self.button_October21.move(255, 485)
        self.button_October21.clicked.connect(self.October21)

        self.button_October22 = QPushButton('22', self)
        self.button_October22.resize(20, 20)
        self.button_October22.move(275, 485)
        self.button_October22.clicked.connect(self.October22)

        self.button_October23 = QPushButton('23', self)
        self.button_October23.resize(20, 20)
        self.button_October23.move(295, 485)
        self.button_October23.clicked.connect(self.October23)

        self.button_October24 = QPushButton('24', self)
        self.button_October24.resize(20, 20)
        self.button_October24.move(315, 485)
        self.button_October24.clicked.connect(self.October24)

        self.button_October25 = QPushButton('25', self)
        self.button_October25.resize(20, 20)
        self.button_October25.move(195, 505)
        self.button_October25.clicked.connect(self.October25)

        self.button_October26 = QPushButton('26', self)
        self.button_October26.resize(20, 20)
        self.button_October26.move(215, 505)
        self.button_October26.clicked.connect(self.October26)

        self.button_October27 = QPushButton('27', self)
        self.button_October27.resize(20, 20)
        self.button_October27.move(235, 505)
        self.button_October27.clicked.connect(self.October27)

        self.button_October28 = QPushButton('28', self)
        self.button_October28.resize(20, 20)
        self.button_October28.move(255, 505)
        self.button_October28.clicked.connect(self.October28)

        self.button_October29 = QPushButton('29', self)
        self.button_October29.resize(20, 20)
        self.button_October29.move(275, 505)
        self.button_October29.clicked.connect(self.October29)

        self.button_October30 = QPushButton('30', self)
        self.button_October30.resize(20, 20)
        self.button_October30.move(295, 505)
        self.button_October30.clicked.connect(self.October30)

        self.button_October31 = QPushButton('31', self)
        self.button_October31.resize(20, 20)
        self.button_October31.move(315, 505)
        self.button_October31.clicked.connect(self.October31)

        # Ноябрь кнопки

        self.button_November1 = QPushButton('1', self)
        self.button_November1.resize(20, 20)
        self.button_November1.move(365, 425)
        self.button_November1.clicked.connect(self.November1)

        self.button_November2 = QPushButton('2', self)
        self.button_November2.resize(20, 20)
        self.button_November2.move(385, 425)
        self.button_November2.clicked.connect(self.November2)

        self.button_November3 = QPushButton('3', self)
        self.button_November3.resize(20, 20)
        self.button_November3.move(405, 425)
        self.button_November3.clicked.connect(self.November3)

        self.button_November4 = QPushButton('4', self)
        self.button_November4.resize(20, 20)
        self.button_November4.move(425, 425)
        self.button_November4.clicked.connect(self.November4)

        self.button_November5 = QPushButton('5', self)
        self.button_November5.resize(20, 20)
        self.button_November5.move(445, 425)
        self.button_November5.clicked.connect(self.November5)

        self.button_November6 = QPushButton('6', self)
        self.button_November6.resize(20, 20)
        self.button_November6.move(465, 425)
        self.button_November6.clicked.connect(self.November6)

        self.button_November7 = QPushButton('7', self)
        self.button_November7.resize(20, 20)
        self.button_November7.move(485, 425)
        self.button_November7.clicked.connect(self.November7)

        self.button_November8 = QPushButton('8', self)
        self.button_November8.resize(20, 20)
        self.button_November8.move(365, 445)
        self.button_November8.clicked.connect(self.November8)

        self.button_November9 = QPushButton('9', self)
        self.button_November9.resize(20, 20)
        self.button_November9.move(385, 445)
        self.button_November9.clicked.connect(self.November9)

        self.button_November10 = QPushButton('10', self)
        self.button_November10.resize(20, 20)
        self.button_November10.move(405, 445)
        self.button_November10.clicked.connect(self.November10)

        self.button_November11 = QPushButton('11', self)
        self.button_November11.resize(20, 20)
        self.button_November11.move(425, 445)
        self.button_November11.clicked.connect(self.November11)

        self.button_November12 = QPushButton('12', self)
        self.button_November12.resize(20, 20)
        self.button_November12.move(445, 445)
        self.button_November12.clicked.connect(self.November12)

        self.button_November13 = QPushButton('13', self)
        self.button_November13.resize(20, 20)
        self.button_November13.move(465, 445)
        self.button_November13.clicked.connect(self.November13)

        self.button_November14 = QPushButton('14', self)
        self.button_November14.resize(20, 20)
        self.button_November14.move(485, 445)
        self.button_November14.clicked.connect(self.November14)

        self.button_November15 = QPushButton('15', self)
        self.button_November15.resize(20, 20)
        self.button_November15.move(365, 465)
        self.button_November15.clicked.connect(self.November15)

        self.button_November16 = QPushButton('16', self)
        self.button_November16.resize(20, 20)
        self.button_November16.move(385, 465)
        self.button_November16.clicked.connect(self.November16)

        self.button_November17 = QPushButton('17', self)
        self.button_November17.resize(20, 20)
        self.button_November17.move(405, 465)
        self.button_November17.clicked.connect(self.November17)

        self.button_November18 = QPushButton('18', self)
        self.button_November18.resize(20, 20)
        self.button_November18.move(425, 465)
        self.button_November18.clicked.connect(self.November18)

        self.button_November19 = QPushButton('19', self)
        self.button_November19.resize(20, 20)
        self.button_November19.move(445, 465)
        self.button_November19.clicked.connect(self.November19)

        self.button_November20 = QPushButton('20', self)
        self.button_November20.resize(20, 20)
        self.button_November20.move(465, 465)
        self.button_November20.clicked.connect(self.November20)

        self.button_November21 = QPushButton('21', self)
        self.button_November21.resize(20, 20)
        self.button_November21.move(485, 465)
        self.button_November21.clicked.connect(self.November21)

        self.button_November22 = QPushButton('22', self)
        self.button_November22.resize(20, 20)
        self.button_November22.move(365, 485)
        self.button_November22.clicked.connect(self.November22)

        self.button_November23 = QPushButton('23', self)
        self.button_November23.resize(20, 20)
        self.button_November23.move(385, 485)
        self.button_November23.clicked.connect(self.November23)

        self.button_November24 = QPushButton('24', self)
        self.button_November24.resize(20, 20)
        self.button_November24.move(405, 485)
        self.button_November24.clicked.connect(self.November24)

        self.button_November25 = QPushButton('25', self)
        self.button_November25.resize(20, 20)
        self.button_November25.move(425, 485)
        self.button_November25.clicked.connect(self.November25)

        self.button_November26 = QPushButton('26', self)
        self.button_November26.resize(20, 20)
        self.button_November26.move(445, 485)
        self.button_November26.clicked.connect(self.November26)

        self.button_November27 = QPushButton('27', self)
        self.button_November27.resize(20, 20)
        self.button_November27.move(465, 485)
        self.button_November27.clicked.connect(self.November27)

        self.button_November28 = QPushButton('28', self)
        self.button_November28.resize(20, 20)
        self.button_November28.move(485, 485)
        self.button_November28.clicked.connect(self.November28)

        self.button_November29 = QPushButton('29', self)
        self.button_November29.resize(20, 20)
        self.button_November29.move(365, 505)
        self.button_November29.clicked.connect(self.November29)

        self.button_November30 = QPushButton('30', self)
        self.button_November30.resize(20, 20)
        self.button_November30.move(385, 505)
        self.button_November30.clicked.connect(self.November30)

        # Декабрь кнопки

        self.button_December1 = QPushButton('1', self)
        self.button_December1.resize(20, 20)
        self.button_December1.move(575, 425)
        self.button_December1.clicked.connect(self.December1)

        self.button_December2 = QPushButton('2', self)
        self.button_December2.resize(20, 20)
        self.button_December2.move(595, 425)
        self.button_December2.clicked.connect(self.December2)

        self.button_December3 = QPushButton('3', self)
        self.button_December3.resize(20, 20)
        self.button_December3.move(615, 425)
        self.button_December3.clicked.connect(self.December3)

        self.button_December4 = QPushButton('4', self)
        self.button_December4.resize(20, 20)
        self.button_December4.move(635, 425)
        self.button_December4.clicked.connect(self.December4)

        self.button_December5 = QPushButton('5', self)
        self.button_December5.resize(20, 20)
        self.button_December5.move(655, 425)
        self.button_December5.clicked.connect(self.December5)

        self.button_December6 = QPushButton('6', self)
        self.button_December6.resize(20, 20)
        self.button_December6.move(535, 445)
        self.button_December6.clicked.connect(self.December6)

        self.button_December7 = QPushButton('7', self)
        self.button_December7.resize(20, 20)
        self.button_December7.move(555, 445)
        self.button_December7.clicked.connect(self.December7)

        self.button_December8 = QPushButton('8', self)
        self.button_December8.resize(20, 20)
        self.button_December8.move(575, 445)
        self.button_December8.clicked.connect(self.December8)

        self.button_December9 = QPushButton('9', self)
        self.button_December9.resize(20, 20)
        self.button_December9.move(595, 445)
        self.button_December9.clicked.connect(self.December9)

        self.button_December10 = QPushButton('10', self)
        self.button_December10.resize(20, 20)
        self.button_December10.move(615, 445)
        self.button_December10.clicked.connect(self.December10)

        self.button_December11 = QPushButton('11', self)
        self.button_December11.resize(20, 20)
        self.button_December11.move(635, 445)
        self.button_December11.clicked.connect(self.December11)

        self.button_December12 = QPushButton('12', self)
        self.button_December12.resize(20, 20)
        self.button_December12.move(655, 445)
        self.button_December12.clicked.connect(self.December12)

        self.button_December13 = QPushButton('13', self)
        self.button_December13.resize(20, 20)
        self.button_December13.move(535, 465)
        self.button_December13.clicked.connect(self.December13)

        self.button_December14 = QPushButton('14', self)
        self.button_December14.resize(20, 20)
        self.button_December14.move(555, 465)
        self.button_December14.clicked.connect(self.December14)

        self.button_December15 = QPushButton('15', self)
        self.button_December15.resize(20, 20)
        self.button_December15.move(575, 465)
        self.button_December15.clicked.connect(self.December15)

        self.button_December16 = QPushButton('16', self)
        self.button_December16.resize(20, 20)
        self.button_December16.move(595, 465)
        self.button_December16.clicked.connect(self.December16)

        self.button_December17 = QPushButton('17', self)
        self.button_December17.resize(20, 20)
        self.button_December17.move(615, 465)
        self.button_December17.clicked.connect(self.December17)

        self.button_December18 = QPushButton('18', self)
        self.button_December18.resize(20, 20)
        self.button_December18.move(635, 465)
        self.button_December18.clicked.connect(self.December18)

        self.button_December19 = QPushButton('19', self)
        self.button_December19.resize(20, 20)
        self.button_December19.move(655, 465)
        self.button_December19.clicked.connect(self.December19)

        self.button_December20 = QPushButton('20', self)
        self.button_December20.resize(20, 20)
        self.button_December20.move(535, 485)
        self.button_December20.clicked.connect(self.December20)

        self.button_December21 = QPushButton('21', self)
        self.button_December21.resize(20, 20)
        self.button_December21.move(555, 485)
        self.button_December21.clicked.connect(self.December21)

        self.button_December22 = QPushButton('22', self)
        self.button_December22.resize(20, 20)
        self.button_December22.move(575, 485)
        self.button_December22.clicked.connect(self.December22)

        self.button_December23 = QPushButton('23', self)
        self.button_December23.resize(20, 20)
        self.button_December23.move(595, 485)
        self.button_December23.clicked.connect(self.December23)

        self.button_December24 = QPushButton('24', self)
        self.button_December24.resize(20, 20)
        self.button_December24.move(615, 485)
        self.button_December24.clicked.connect(self.December24)

        self.button_December25 = QPushButton('25', self)
        self.button_December25.resize(20, 20)
        self.button_December25.move(635, 485)
        self.button_December25.clicked.connect(self.December25)

        self.button_December26 = QPushButton('26', self)
        self.button_December26.resize(20, 20)
        self.button_December26.move(655, 485)
        self.button_December26.clicked.connect(self.December26)

        self.button_December27 = QPushButton('27', self)
        self.button_December27.resize(20, 20)
        self.button_December27.move(535, 505)
        self.button_December27.clicked.connect(self.December27)

        self.button_December28 = QPushButton('28', self)
        self.button_December28.resize(20, 20)
        self.button_December28.move(555, 505)
        self.button_December28.clicked.connect(self.December28)

        self.button_December29 = QPushButton('29', self)
        self.button_December29.resize(20, 20)
        self.button_December29.move(575, 505)
        self.button_December29.clicked.connect(self.December29)

        self.button_December30 = QPushButton('30', self)
        self.button_December30.resize(20, 20)
        self.button_December30.move(595, 505)
        self.button_December30.clicked.connect(self.December30)

        self.button_December31 = QPushButton('31', self)
        self.button_December31.resize(20, 20)
        self.button_December31.move(615, 505)
        self.button_December31.clicked.connect(self.December31)

        # январь текс
        self.label = QLabel(self)
        self.label.setText("Январь")
        self.label.move(75, 75)

        self.label = QLabel(self)
        self.label.setText("Пн")
        self.label.move(30, 100)

        self.label = QLabel(self)
        self.label.setText("Вт")
        self.label.move(50, 100)

        self.label = QLabel(self)
        self.label.setText("Ср")
        self.label.move(70, 100)

        self.label = QLabel(self)
        self.label.setText("Чт")
        self.label.move(90, 100)

        self.label = QLabel(self)
        self.label.setText("Пт")
        self.label.move(110, 100)

        self.label = QLabel(self)
        self.label.setText("Сб")
        self.label.move(130, 100)

        self.label = QLabel(self)
        self.label.setText("Вс")
        self.label.move(150, 100)

        # февраль текс

        self.label = QLabel(self)
        self.label.setText("Февраль")
        self.label.move(250, 75)

        self.label = QLabel(self)
        self.label.setText("Пн")
        self.label.move(200, 100)

        self.label = QLabel(self)
        self.label.setText("Вт")
        self.label.move(220, 100)

        self.label = QLabel(self)
        self.label.setText("Ср")
        self.label.move(240, 100)

        self.label = QLabel(self)
        self.label.setText("Чт")
        self.label.move(260, 100)

        self.label = QLabel(self)
        self.label.setText("Пт")
        self.label.move(280, 100)

        self.label = QLabel(self)
        self.label.setText("Сб")
        self.label.move(300, 100)

        self.label = QLabel(self)
        self.label.setText("Вс")
        self.label.move(320, 100)

        # Март текст

        self.label = QLabel(self)
        self.label.setText("Март")
        self.label.move(425, 75)

        self.label = QLabel(self)
        self.label.setText("Пн")
        self.label.move(370, 100)

        self.label = QLabel(self)
        self.label.setText("Вт")
        self.label.move(390, 100)

        self.label = QLabel(self)
        self.label.setText("Ср")
        self.label.move(410, 100)

        self.label = QLabel(self)
        self.label.setText("Чт")
        self.label.move(430, 100)

        self.label = QLabel(self)
        self.label.setText("Пт")
        self.label.move(450, 100)

        self.label = QLabel(self)
        self.label.setText("Сб")
        self.label.move(470, 100)

        self.label = QLabel(self)
        self.label.setText("Вс")
        self.label.move(490, 100)

        # Апрель текст

        self.label = QLabel(self)
        self.label.setText("Апрель")
        self.label.move(595, 75)

        self.label = QLabel(self)
        self.label.setText("Пн")
        self.label.move(540, 100)

        self.label = QLabel(self)
        self.label.setText("Вт")
        self.label.move(560, 100)

        self.label = QLabel(self)
        self.label.setText("Ср")
        self.label.move(580, 100)

        self.label = QLabel(self)
        self.label.setText("Чт")
        self.label.move(600, 100)

        self.label = QLabel(self)
        self.label.setText("Пт")
        self.label.move(620, 100)

        self.label = QLabel(self)
        self.label.setText("Сб")
        self.label.move(640, 100)

        self.label = QLabel(self)
        self.label.setText("Вс")
        self.label.move(660, 100)

        # Май текст

        self.label = QLabel(self)
        self.label.setText("Май")
        self.label.move(75, 220)

        self.label = QLabel(self)
        self.label.setText("Пн")
        self.label.move(30, 245)

        self.label = QLabel(self)
        self.label.setText("Вт")
        self.label.move(50, 245)

        self.label = QLabel(self)
        self.label.setText("Ср")
        self.label.move(70, 245)

        self.label = QLabel(self)
        self.label.setText("Чт")
        self.label.move(90, 245)

        self.label = QLabel(self)
        self.label.setText("Пт")
        self.label.move(110, 245)

        self.label = QLabel(self)
        self.label.setText("Сб")
        self.label.move(130, 245)

        self.label = QLabel(self)
        self.label.setText("Вс")
        self.label.move(150, 245)

        # Июнь текст

        self.label = QLabel(self)
        self.label.setText("Июнь")
        self.label.move(250, 220)

        self.label = QLabel(self)
        self.label.setText("Пн")
        self.label.move(200, 245)

        self.label = QLabel(self)
        self.label.setText("Вт")
        self.label.move(220, 245)

        self.label = QLabel(self)
        self.label.setText("Ср")
        self.label.move(240, 245)

        self.label = QLabel(self)
        self.label.setText("Чт")
        self.label.move(260, 245)

        self.label = QLabel(self)
        self.label.setText("Пт")
        self.label.move(280, 245)

        self.label = QLabel(self)
        self.label.setText("Сб")
        self.label.move(300, 245)

        self.label = QLabel(self)
        self.label.setText("Вс")
        self.label.move(320, 245)

        # Июль текст

        self.label = QLabel(self)
        self.label.setText("Июль")
        self.label.move(425, 220)

        self.label = QLabel(self)
        self.label.setText("Пн")
        self.label.move(370, 245)

        self.label = QLabel(self)
        self.label.setText("Вт")
        self.label.move(390, 245)

        self.label = QLabel(self)
        self.label.setText("Ср")
        self.label.move(410, 245)

        self.label = QLabel(self)
        self.label.setText("Чт")
        self.label.move(430, 245)

        self.label = QLabel(self)
        self.label.setText("Пт")
        self.label.move(450, 245)

        self.label = QLabel(self)
        self.label.setText("Сб")
        self.label.move(470, 245)

        self.label = QLabel(self)
        self.label.setText("Вс")
        self.label.move(490, 245)

        # Август текс
        self.label = QLabel(self)
        self.label.setText("Август")
        self.label.move(595, 220)

        self.label = QLabel(self)
        self.label.setText("Пн")
        self.label.move(540, 245)

        self.label = QLabel(self)
        self.label.setText("Вт")
        self.label.move(560, 245)

        self.label = QLabel(self)
        self.label.setText("Ср")
        self.label.move(580, 245)

        self.label = QLabel(self)
        self.label.setText("Чт")
        self.label.move(600, 245)

        self.label = QLabel(self)
        self.label.setText("Пт")
        self.label.move(620, 245)

        self.label = QLabel(self)
        self.label.setText("Сб")
        self.label.move(640, 245)

        self.label = QLabel(self)
        self.label.setText("Вс")
        self.label.move(660, 245)

        # Сентябрь текс
        self.label = QLabel(self)
        self.label.setText("Сентябрь")
        self.label.move(75, 385)

        self.label = QLabel(self)
        self.label.setText("Пн")
        self.label.move(30, 410)

        self.label = QLabel(self)
        self.label.setText("Вт")
        self.label.move(50, 410)

        self.label = QLabel(self)
        self.label.setText("Ср")
        self.label.move(70, 410)

        self.label = QLabel(self)
        self.label.setText("Чт")
        self.label.move(90, 410)

        self.label = QLabel(self)
        self.label.setText("Пт")
        self.label.move(110, 410)

        self.label = QLabel(self)
        self.label.setText("Сб")
        self.label.move(130, 410)

        self.label = QLabel(self)
        self.label.setText("Вс")
        self.label.move(150, 410)

        # Октябрь текс
        self.label = QLabel(self)
        self.label.setText("Октябрь")
        self.label.move(250, 385)

        self.label = QLabel(self)
        self.label.setText("Пн")
        self.label.move(200, 410)

        self.label = QLabel(self)
        self.label.setText("Вт")
        self.label.move(220, 410)

        self.label = QLabel(self)
        self.label.setText("Ср")
        self.label.move(240, 410)

        self.label = QLabel(self)
        self.label.setText("Чт")
        self.label.move(260, 410)

        self.label = QLabel(self)
        self.label.setText("Пт")
        self.label.move(280, 410)

        self.label = QLabel(self)
        self.label.setText("Сб")
        self.label.move(300, 410)

        self.label = QLabel(self)
        self.label.setText("Вс")
        self.label.move(320, 410)

        # Ноябрь текс
        self.label = QLabel(self)
        self.label.setText("Ноябрь")
        self.label.move(425, 385)

        self.label = QLabel(self)
        self.label.setText("Пн")
        self.label.move(370, 410)

        self.label = QLabel(self)
        self.label.setText("Вт")
        self.label.move(390, 410)

        self.label = QLabel(self)
        self.label.setText("Ср")
        self.label.move(410, 410)

        self.label = QLabel(self)
        self.label.setText("Чт")
        self.label.move(430, 410)

        self.label = QLabel(self)
        self.label.setText("Пт")
        self.label.move(450, 410)

        self.label = QLabel(self)
        self.label.setText("Сб")
        self.label.move(470, 410)

        self.label = QLabel(self)
        self.label.setText("Вс")
        self.label.move(490, 410)

        # Январь текс
        self.label = QLabel(self)
        self.label.setText("Январь")
        self.label.move(595, 385)

        self.label = QLabel(self)
        self.label.setText("Пн")
        self.label.move(540, 410)

        self.label = QLabel(self)
        self.label.setText("Вт")
        self.label.move(560, 410)

        self.label = QLabel(self)
        self.label.setText("Ср")
        self.label.move(580, 410)

        self.label = QLabel(self)
        self.label.setText("Чт")
        self.label.move(600, 410)

        self.label = QLabel(self)
        self.label.setText("Пт")
        self.label.move(620, 410)

        self.label = QLabel(self)
        self.label.setText("Сб")
        self.label.move(640, 410)

        self.label = QLabel(self)
        self.label.setText("Вс")
        self.label.move(660, 410)

        # Мини иструкция

        self.label = QLabel(self)
        self.label.setText("Ввод заметок")
        self.label.move(10, 0)

        self.label = QLabel(self)
        self.label.setText("Вывод заметок")
        self.label.move(450, 0)

        # Ввод заметок

        self.name_1 = QLineEdit(self)
        self.name_1.resize(300, 25)
        self.name_1.move(0, 25)

        # Вывод звметок

        self.name_2 = QLineEdit(self)
        self.name_2.resize(300, 25)
        self.name_2.move(350, 25)

    # Связка конпок Январь

    def January1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January1.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January1'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January1'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January2(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January2.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January2'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January2'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January3(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January3.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January3'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January3'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January4(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January4.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January4'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January4'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January5(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January5.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January5'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January5'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January6(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January6.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January6'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January6'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January7(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January7.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January7'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January7'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January8(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January8.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January8'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January8'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January9(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January9.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January9'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January9'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January10(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January10.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January10'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January10'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January11(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January11.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January11'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January11'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January12(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January12.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January12'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January12'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January13(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January13.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January13'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January13'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January14(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January14.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January14'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January14'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January15(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January15.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January15'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January15'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January16(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January16.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January16'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January16'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January17(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January17.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January17'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January17'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January18(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January18.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January18'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January18'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January19(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January19.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January19'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January19'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January20(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January20.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January20'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January20'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January21(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January21.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January21'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January21'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January22(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January22.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January22'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January22'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January23(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January23.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January23'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January23'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January24(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January24.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January24'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January24'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January25(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January25.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January25'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January25'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January26(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January26.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January26'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January26'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January27(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January27.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January27'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January27'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January28(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January28.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January28'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January28'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January29(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January29.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January29'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January29'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")


    def January30(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January30.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January30'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January30'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def January31(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_January31.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'January31'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'January31'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

        #Связка кнопок январь

    def February1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February1.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February1'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February1'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February2(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February2.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February2'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February2'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February3(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February3.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February3'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February3'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February4(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February4.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February4'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February4'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February5(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February5.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February5'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February5'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February6(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February6.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February6'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February6'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February7(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February7.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February7'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February7'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February8(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February8.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February8'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February8'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February9(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February9.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February9'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February9'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February10(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February10.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February10'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February10'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February11(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February11.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February11'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February11'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February12(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February12.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February12'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February12'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February13(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February13.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February13'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February13'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February14(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February14.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February14'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February14'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February15(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February15.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February15'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February15'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February16(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February16.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February16'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February16'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February17(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February17.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February17'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February17'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February18(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February18.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February18'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February18'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February19(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February19.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February19'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February19'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February20(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February20.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February20'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February20'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February21(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February21.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February21'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February21'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February22(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February22.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February22'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February22'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February23(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February23.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February23'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February23'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February24(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February24.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February24'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February24'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February25(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February25.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February25'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February25'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February26(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February26.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February26'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February26'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February27(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February27.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February27'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February27'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def February28(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_February28.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'February28'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'February28'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    # Связка кнопок март
    def March1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March1.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March1'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March1'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March2(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March2.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March2'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March2'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March3(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March3.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March3'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March3'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March4(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March4.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March4'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March4'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March5(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March5.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March5'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March5'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March6(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March6.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March6'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March6'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March7(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March7.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March7'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March7'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March8(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March8.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March8'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March8'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March9(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March9.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March9'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March9'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March10(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March10.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March10'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March10'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March11(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March11.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March11'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March11'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March12(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March12.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March12'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March12'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March13(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March13.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March13'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March13'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March14(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March14.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March14'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March14'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March15(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March15.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March15'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March15'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March16(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March16.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March16'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March16'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March17(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March17.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March17'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March17'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March18(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March18.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March18'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March18'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March19(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March19.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March19'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March19'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March20(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March20.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March20'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March20'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March21(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March21.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March21'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March21'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March22(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March22.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March22'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March22'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March23(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March23.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March23'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March23'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March24(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March24.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March24'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March24'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March25(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March25.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March25'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March25'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March26(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March26.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March26'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March26'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March27(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March27.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March27'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March27'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March28(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March28.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March28'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March28'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March29(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March29.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March29'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March29'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March30(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March30.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March30'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March30'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def March31(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_March31.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'March31'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'March31'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

        # Связка кнопок апрель

    def April1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April1.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April1'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April1'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April2(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April2.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April2'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April2'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April3(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April3.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April3'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April3'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April4(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April4.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April4'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April4'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April5(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April5.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April5'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April5'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April6(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April6.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April6'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April6'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April7(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April7.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April7'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April7'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April8(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April8.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April8'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April8'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April9(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April9.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April9'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April9'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April10(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April10.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April10'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April10'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April11(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April11.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April11'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April11'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April12(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April12.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April12'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April12'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April13(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April13.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April13'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April13'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April14(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April14.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April14'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April14'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April15(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April15.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April15'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April15'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April16(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April16.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April16'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April16'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April17(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April17.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April17'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April17'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April18(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April18.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April18'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April18'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April19(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April19.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April19'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April19'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April20(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April20.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April20'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April20'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April21(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April21.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April21'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April21'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April22(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April22.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April22'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April22'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April23(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April23.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April23'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April23'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April24(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April24.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April24'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April24'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April25(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April25.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April25'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April25'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April26(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April26.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April26'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April26'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April27(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April27.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April27'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April27'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April28(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April28.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April28'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April28'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April29(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April29.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April29'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April29'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def April30(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_April30.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'April30'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'April30'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    # Связка кнопок май

    def May1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May1.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May1'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May1'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May2(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May2.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May2'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May2'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May3(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May3.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May3'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May3'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May4(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May4.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May4'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May4'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May5(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May5.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May5'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May5'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May6(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May6.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May6'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May6'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May7(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May7.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May7'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May7'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May8(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May8.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May8'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May8'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May9(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May9.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May9'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May9'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May10(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May10.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May10'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May10'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May11(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May11.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May11'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May11'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May12(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May12.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May12'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May12'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May13(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May13.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May13'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May13'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May14(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May14.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May14'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May14'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May15(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May15.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May15'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May15'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May16(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May16.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May16'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May16'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May17(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May17.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May17'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May17'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May18(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May18.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May18'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May18'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May19(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May19.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May19'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May19'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May20(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May20.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May20'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May20'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May21(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May21.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May21'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May21'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May22(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May22.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May22'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May22'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May23(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May23.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May23'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May23'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May24(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May24.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May24'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May24'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May25(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May25.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May25'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May25'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May26(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May26.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May26'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May26'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May27(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May27.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May27'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May27'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May28(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May28.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May28'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May28'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May29(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May29.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May29'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May29'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May30(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May30.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May30'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May30'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def May31(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_May31.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'May31'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'May31'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    # Связка конпок Июнь

    def June1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June1.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June1'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June1'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June2(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June2.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June2'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June2'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June3(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June3.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June3'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June3'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June4(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June4.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June4'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June4'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June5(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June5.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June5'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June5'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June6(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June6.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June6'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June6'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June7(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June7.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June7'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June7'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June8(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June8.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June8'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June8'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June9(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June9.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June9'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June9'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June10(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June10.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June10'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June10'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June11(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June11.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June11'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June11'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June12(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June12.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June12'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June12'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June13(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June13.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June13'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June13'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June14(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June14.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June14'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June14'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June15(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June15.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June15'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June15'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June16(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June16.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June16'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June16'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June17(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June17.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June17'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June17'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June18(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June18.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June18'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June18'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June19(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June19.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June19'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June19'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June20(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June20.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June20'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June20'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June21(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June21.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June21'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June21'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June22(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June22.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June22'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June22'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June23(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June23.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June23'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June23'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June24(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June24.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June24'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June24'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June25(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June25.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June25'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June25'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June26(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June26.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June26'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June26'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June27(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June27.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June27'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June27'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June28(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June28.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June28'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June28'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June29(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June29.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June29'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June29'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def June30(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_June30.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'June30'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'June30'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    # Связка кнопок Июль

    def July1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July1.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July1'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July1'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July2(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July2.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July2'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July2'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July3(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July3.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July3'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July3'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July4(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July4.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July4'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July4'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July5(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July5.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July5'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July5'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July6(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July6.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July6'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July6'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July7(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July7.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July7'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July7'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July8(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July8.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July8'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July8'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July9(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July9.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July9'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July9'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July10(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July10.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July10'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July10'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July11(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July11.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July11'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July11'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July12(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July12.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July12'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July12'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July13(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July13.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July13'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July13'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July14(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July14.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July14'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July14'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July15(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July15.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July15'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July15'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July16(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July16.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July16'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July16'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July17(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July17.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July17'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July17'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July18(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July18.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July18'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July18'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July19(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July19.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July19'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July19'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July20(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July20.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July20'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July20'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July21(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July21.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July21'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July21'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July22(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July22.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July22'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July22'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July23(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July23.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July23'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July23'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July24(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July24.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July24'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July24'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July25(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July25.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July25'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July25'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July26(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July26.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July26'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July26'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July27(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July27.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July27'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July27'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July28(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July28.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July28'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July28'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July29(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July29.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July29'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July29'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July30(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July30.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July30'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July30'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def July31(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_July31.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'July31'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'July31'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    # Связка конпок Август

    def August1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August1.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August1'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August1'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August2(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August2.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August2'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August2'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August3(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August3.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August3'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August3'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August4(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August4.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August4'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August4'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August5(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August5.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August5'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August5'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August6(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August6.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August6'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August6'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August7(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August7.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August7'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August7'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August8(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August8.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August8'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August8'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August9(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August9.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August9'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August9'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August10(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August10.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August10'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August10'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August11(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August11.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August11'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August11'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August12(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August12.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August12'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August12'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August13(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August13.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August13'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August13'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August14(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August14.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August14'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August14'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August15(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August15.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August15'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August15'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August16(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August16.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August16'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August16'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August17(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August17.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August17'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August17'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August18(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August18.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August18'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August18'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August19(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August19.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August19'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August19'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August20(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August20.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August20'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August20'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August21(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August21.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August21'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August21'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August22(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August22.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August22'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August22'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August22(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August22.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August22'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August22'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August23(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August23.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August23'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August23'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August24(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August24.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August24'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August24'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August25(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August25.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August25'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August25'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August26(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August26.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August26'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August26'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August27(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August27.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August27'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August27'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August28(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August28.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August28'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August28'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August29(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August29.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August29'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August29'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August30(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August30.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August30'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August30'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def August31(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_August31.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'August31'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'August31'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    # Связка кнопок Сентябрь

    def September1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September1.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September1'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September1'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September2(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September2.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September2'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September2'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September3(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September3.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September3'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September3'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September4(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September4.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September4'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September4'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September5(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September5.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September5'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September5'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September6(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September6.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September6'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September6'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September7(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September7.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September7'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September7'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September8(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September8.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September8'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September8'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September9(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September9.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'Septembe9'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September9'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September10(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September10.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September10'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September10'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September11(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September11.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September11'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September11'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September12(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September12.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September12'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September12'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September13(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September13.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September13'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September13'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September14(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September14.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September14'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September14'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September15(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September15.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September15'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September15'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September16(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September16.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September16'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September16'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September17(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September17.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September17'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September17'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September18(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September18.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September18'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September18'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September19(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September19.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September19'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September19'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September20(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September20.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September20'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September20'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September21(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September21.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September21'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September21'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September21(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September21.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September21'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September21'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September22(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September22.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September22'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September22'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September23(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September23.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September23'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September23'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September24(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September24.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September24'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September24'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September25(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September25.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September25'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September25'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September26(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September26.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September26'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September26'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September27(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September27.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September27'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September27'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September28(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September28.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September28'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September28'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September29(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September29.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September29'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September29'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def September30(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_September30.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'September30'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'September30'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    # Связка кнопок Октябрь

    def October1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October1.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October1'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October1'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October2(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October2.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October2'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October2'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October3(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October3.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October3'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October3'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October4(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October4.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October4'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October4'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October5(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October5.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October5'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October5'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October6(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October6.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October6'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October6'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October7(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October7.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October7'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October7'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October8(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October8.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October8'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October8'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October9(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October9.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October9'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October9'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October10(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October10.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October10'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October10'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October11(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October11.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October11'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October11'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October12(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October12.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October12'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October12'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October13(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October13.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October13'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October13'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October14(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October14.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October14'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October14'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October15(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October15.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October15'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October15'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October16(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October16.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October16'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October16'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October17(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October17.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October17'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October17'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October18(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October18.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October18'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October18'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October19(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October19.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October19'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October19'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October20(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October20.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October20'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October20'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October21(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October21.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October21'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October21'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October22(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October22.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October22'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October22'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October23(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October23.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October23'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October23'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October24(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October24.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October24'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October24'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October25(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October25.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October25'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October25'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October26(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October26.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October26'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October26'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October27(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October27.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October27'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October27'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October28(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October28.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October28'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October28'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October29(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October29.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October29'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October29'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October30(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October30.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October30'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October30'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def October31(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_October31.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'October31'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'October31'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    # Связка кнопок Ноябрь

    def November1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November1.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November1'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November1'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November2(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November2.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November2'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November2'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November3(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November3.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November3'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November3'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November4(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November4.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November4'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November4'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November5(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November5.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November5'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November5'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November6(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November6.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November6'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November6'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November7(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November7.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November7'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November7'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November8(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November8.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November8'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November8'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November9(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November9.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November9'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November9'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November10(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November10.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November10'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November10'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November11(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November11.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November11'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November11'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November12(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November12.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November12'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November12'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November13(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November13.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November13'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November13'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November14(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November14.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November14'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November14'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November15(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November15.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November15'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November15'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November16(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November16.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November16'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November16'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November17(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November17.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November17'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November17'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November18(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November18.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November18'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November18'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November19(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November19.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November19'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November19'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November20(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November20.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November20'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November20'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November21(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November21.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November21'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November21'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November22(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November22.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November22'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November22'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November23(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November23.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November23'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November23'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November24(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November24.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November24'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November24'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November25(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November25.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November25'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November25'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November26(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November26.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November26'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November26'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November27(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November27.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November27'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November27'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November28(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November28.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November28'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November28'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November29(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November29.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November29'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November29'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def November30(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_November30.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'November30'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'November30'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    # Связка кнопок Декабрь

    def December1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December1.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December1'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December1'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December2(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December2.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December2'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December2'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December3(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December3.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December3'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December3'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December4(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December4.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December4'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December4'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December5(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December5.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December5'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December5'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December6(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December6.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December6'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December6'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December7(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December7.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December7'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December7'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December8(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December8.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December8'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December8'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December9(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December9.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December9'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December9'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December10(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December10.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December10'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December10'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December11(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December11.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December11'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December11'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December12(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December12.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December12'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December12'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December13(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December13.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December13'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December13'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December14(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December14.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December14'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December14'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December15(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December15.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December15'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December15'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December16(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December16.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December16'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December16'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December17(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December17.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December17'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December17'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December18(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December18.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December18'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December18'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December19(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December19.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December19'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December19'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December20(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December20.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December20'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December20'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December21(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December21.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December21'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December21'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December22(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December22.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December22'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December22'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December23(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December23.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December23'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December23'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December24(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December24.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December24'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December24'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December25(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December25.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December25'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December25'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December26(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December26.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December26'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December26'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December27(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December27.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December27'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December27'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December28(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December28.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December28'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December28'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December29(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December29.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December29'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December29'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December30(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December30.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December30'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December30'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")

    def December31(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_December31.setStyleSheet("background-color: {}".format(color.name()))
        name = self.name_1.text()

        if name != "":
            self.cur.execute(f"""UPDATE project SET Note = "{name}" WHERE Day = 'December31'""")
            self.con.commit()

        a = list(self.cur.execute("""SELECT Note FROM project WHERE Day = 'December31'"""))

        if str(a[0][0]) == "None" or str(a[0][0]) == "":
            self.name_2.setText("Вы ничего не планировали")
        else:
            self.name_2.setText(str(a[0][0]))

        self.name_1.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

