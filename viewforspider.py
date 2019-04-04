# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewforspider.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_spider_view(object):
    def setupUi(self, spider_view):
        spider_view.setObjectName("spider_view")
        spider_view.resize(279, 500)
        spider_view.setMinimumSize(QtCore.QSize(279, 500))
        spider_view.setMaximumSize(QtCore.QSize(279, 500))
        self.sortclass = QtWidgets.QComboBox(spider_view)
        self.sortclass.setGeometry(QtCore.QRect(170, 20, 101, 22))
        self.sortclass.setObjectName("sortclass")
        self.sortclass.addItem("")
        self.sortclass.addItem("")
        self.sortclass.addItem("")
        self.sortclass.addItem("")
        self.moviesclass = QtWidgets.QComboBox(spider_view)
        self.moviesclass.setGeometry(QtCore.QRect(20, 20, 81, 22))
        self.moviesclass.setObjectName("moviesclass")
        self.moviesclass.addItem("")
        self.moviesclass.addItem("")
        self.moviesclass.addItem("")
        self.moviesclass.addItem("")
        self.moviesclass.addItem("")
        self.moviesclass.addItem("")
        self.moviesclass.addItem("")
        self.moviesclass.addItem("")
        self.makefile = QtWidgets.QPushButton(spider_view)
        self.makefile.setGeometry(QtCore.QRect(20, 90, 81, 23))
        self.makefile.setObjectName("makefile")
        self.openfile = QtWidgets.QPushButton(spider_view)
        self.openfile.setGeometry(QtCore.QRect(170, 90, 101, 23))
        self.openfile.setObjectName("openfile")
        self.textBrowser = QtWidgets.QTextBrowser(spider_view)
        self.textBrowser.setGeometry(QtCore.QRect(20, 130, 241, 351))
        self.textBrowser.setObjectName("textBrowser")
        self.guessyoulike = QtWidgets.QPushButton(spider_view)
        self.guessyoulike.setGeometry(QtCore.QRect(100, 50, 75, 23))
        self.guessyoulike.setObjectName("guessyoulike")

        self.retranslateUi(spider_view)
        self.makefile.clicked.connect(spider_view.execute)
        self.openfile.clicked.connect(spider_view.open_file)
        self.guessyoulike.clicked.connect(spider_view.findyoulike)
        QtCore.QMetaObject.connectSlotsByName(spider_view)

    def retranslateUi(self, spider_view):
        _translate = QtCore.QCoreApplication.translate
        spider_view.setWindowTitle(_translate("spider_view", "猫眼电影抓取"))
        self.sortclass.setItemText(0, _translate("spider_view", "排序类别"))
        self.sortclass.setItemText(1, _translate("spider_view", "按照热门排序"))
        self.sortclass.setItemText(2, _translate("spider_view", "按照时间排序"))
        self.sortclass.setItemText(3, _translate("spider_view", "按照评价排序"))
        self.moviesclass.setItemText(0, _translate("spider_view", "电影类别"))
        self.moviesclass.setItemText(1, _translate("spider_view", "科幻"))
        self.moviesclass.setItemText(2, _translate("spider_view", "动作"))
        self.moviesclass.setItemText(3, _translate("spider_view", "悬疑"))
        self.moviesclass.setItemText(4, _translate("spider_view", "冒险"))
        self.moviesclass.setItemText(5, _translate("spider_view", "战争"))
        self.moviesclass.setItemText(6, _translate("spider_view", "奇幻"))
        self.moviesclass.setItemText(7, _translate("spider_view", "喜剧"))
        self.makefile.setText(_translate("spider_view", "开始抓取"))
        self.openfile.setText(_translate("spider_view", "提取排序"))
        self.guessyoulike.setText(_translate("spider_view", "猜你喜欢"))

