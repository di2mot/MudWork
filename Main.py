#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QLabel, QLineEdit, QTextEdit, QGridLayout,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)
# Это отвечает за иконку
        self.setGeometry(600, 300, 600, 320)
        self.setWindowTitle('MudWork')
        self.setWindowIcon(QIcon('icon.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
