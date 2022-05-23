# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timemachine.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from datetime import date
from billboard_list import Billboard
from spotify import SpotifyProcess
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon

import os


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(909, 473)
        self.bilboard = Billboard()
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 881, 451))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gpbox_hotlist = QtWidgets.QGroupBox(self.tab)
        self.gpbox_hotlist.setGeometry(QtCore.QRect(370, 20, 391, 401))
        self.gpbox_hotlist.setObjectName("gpbox_hotlist")
        self.listWidget = QtWidgets.QListWidget(self.gpbox_hotlist)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 371, 371))
        self.listWidget.setObjectName("listWidget")
        # self.listlabel=QtWidgets.QLabel(self.tab)
        # self.listlabel.setGeometry(QtCore.QRect(770,390,50,20))
        # self.listlabel.move(770,390)
        # self.myfont=QtGui.QFont("Arial", 12)
        # self.myfont.setBold(True)
        # self.listlabel.setFont(self.myfont)

        # self.listlabel.setObjectName("listlabel")
        # self.listlabel.setText("merhaba")
        self.gpbox_hldate = QtWidgets.QGroupBox(self.tab)
        self.gpbox_hldate.setGeometry(QtCore.QRect(0, 20, 321, 261))
        self.gpbox_hldate.setObjectName("gpbox_hldate")
        self.label_5 = QtWidgets.QLabel(self.gpbox_hldate)
        self.label_5.setGeometry(QtCore.QRect(16, 34, 81, 16))
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(self.gpbox_hldate)
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setGeometry(QtCore.QRect(110, 30, 161, 21))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.btn_hlistdate = QtWidgets.QPushButton(self.gpbox_hldate)
        self.btn_hlistdate.setGeometry(QtCore.QRect(110, 90, 131, 28))
        self.btn_hlistdate.setObjectName("btn_hlistdate")
        self.btn_gethotlist = QtWidgets.QPushButton(self.gpbox_hldate)
        self.btn_gethotlist.setGeometry(QtCore.QRect(110, 150, 131, 28))
        self.btn_gethotlist.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_gethotlist.setObjectName("btn_gethotlist")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gbox_info = QtWidgets.QGroupBox(self.tab_2)
        self.gbox_info.setGeometry(QtCore.QRect(20, 20, 301, 261))
        self.gbox_info.setObjectName("gbox_info")
        self.label = QtWidgets.QLabel(self.gbox_info)
        self.label.setGeometry(QtCore.QRect(10, 30, 55, 16))
        self.label.setObjectName("label")
        self.cl_idtext = QtWidgets.QLineEdit(self.gbox_info)
        self.cl_idtext.setGeometry(QtCore.QRect(104, 25, 161, 22))
        self.cl_idtext.setObjectName("cl_idtext")
        self.label_2 = QtWidgets.QLabel(self.gbox_info)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_2.setObjectName("label_2")
        self.cl_sectext = QtWidgets.QLineEdit(self.gbox_info)
        self.cl_sectext.setGeometry(QtCore.QRect(104, 57, 161, 22))
        self.cl_sectext.setObjectName("cl_sectext")
        self.txt_playlist = QtWidgets.QLineEdit(self.gbox_info)
        self.txt_playlist.setGeometry(QtCore.QRect(104, 91, 161, 22))
        self.txt_playlist.setObjectName("txt_playlist")
        self.label_3 = QtWidgets.QLabel(self.gbox_info)
        self.label_3.setGeometry(QtCore.QRect(11, 93, 61, 16))
        self.label_3.setObjectName("label_3")
        self.rd_get = QtWidgets.QRadioButton(self.gbox_info)
        self.rd_get.setGeometry(QtCore.QRect(30, 140, 95, 20))
        self.rd_get.setObjectName("rd_get")
        self.rd_enter = QtWidgets.QRadioButton(self.gbox_info)
        self.rd_enter.setGeometry(QtCore.QRect(170, 140, 95, 20))
        self.rd_enter.setObjectName("rd_enter")
        self.btn_id = QtWidgets.QPushButton(self.gbox_info)
        self.btn_id.setGeometry(QtCore.QRect(80, 190, 93, 28))
        self.btn_id.setObjectName("btn_id")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 300, 301, 81))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(82, 30, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(340, 18, 421, 361))
        self.groupBox_3.setObjectName("groupBox_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 20, 401, 331))
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(770, 40, 101, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_2, "")


        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Time Machine"))
        Form.setWindowIcon(QIcon("images/computer.png"))




        Form.setStyleSheet(
            "background-color: #B4ECE3;")
        gboxstyle = """QGroupBox{ border: 1px solid red;
            background: #5EE6EB}"""
        self.label.setStyleSheet("background-color: #5EE6EB;")
        self.label_5.setStyleSheet("background-color: #5EE6EB;")
        self.label_3.setStyleSheet("background-color: #5EE6EB;")
        self.label_2.setStyleSheet("background-color: #5EE6EB;")
        self.gbox_info.setStyleSheet(gboxstyle)
        self.gpbox_hotlist.setStyleSheet(gboxstyle)

        self.gpbox_hotlist.setTitle(_translate("Form", "Bilboard Hot List"))
        self.gpbox_hldate.setTitle(_translate("Form", "Set Hot List Date"))
        self.label_5.setText(_translate("Form", "Hot List Date"))
        self.dateEdit.setDisplayFormat(_translate("Form", "yyyy.MM.dd"))
        self.dateEdit.setStyleSheet("background:yellow")
        self.btn_hlistdate.setText(_translate("Form", "Set Hot List Date"))
        self.btn_hlistdate.clicked.connect(self.get_date)
        self.btn_id.setStyleSheet("background:#EFFFFD")
        self.btn_hlistdate.setStyleSheet("background:#EFFFFD")
        self.btn_gethotlist.setText(_translate("Form", "Get Hot List"))
        self.btn_gethotlist.setStyleSheet("background:#EFFFFD")
        self.btn_gethotlist.clicked.connect(self.get_hotlist)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Bilboard List"))
        self.gbox_info.setTitle(_translate("Form", "Settings"))
        self.gbox_info.setStyleSheet("background-color: #5EE6EB;")
        self.label.setText(_translate("Form", "Client ID"))
        self.label_2.setText(_translate("Form", "Client Sec"))
        self.label_3.setText(_translate("Form", "Play List ID"))
        self.rd_get.setText(_translate("Form", "Get Value"))
        self.rd_enter.setText(_translate("Form", "Enter Value"))
        self.btn_id.setText(_translate("Form", "Set"))
        self.btn_id.clicked.connect(self.setparams)
        self.groupBox.setTitle(_translate("Form", "Get Uri"))
        self.groupBox.setStyleSheet(gboxstyle)
        self.pushButton.setText(_translate("Form", "Get Uri"))
        self.pushButton.setStyleSheet("background:#EFFFFD")
        self.pushButton.clicked.connect(self.show_uris)
        self.groupBox_3.setTitle(_translate("Form", "Song Uri\'s"))
        self.groupBox_3.setStyleSheet(gboxstyle)
        self.gpbox_hldate.setStyleSheet(gboxstyle)
        self.pushButton_2.setText(_translate("Form", "Create Play List"))
        self.pushButton_2.setStyleSheet(_translate("Form", "background:#EFFFFD"))
        self.pushButton_2.clicked.connect(self.bilboard.add_tracks)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Spotify"))

    def show_uris(self):
        self.bilboard.get_song_uri()
        for item in self.bilboard.song_uris:
            for song in self.bilboard.songs_found.items() :
                self.listWidget_2.addItem(f"{item}->{song[0]}:{song[1]}")
                self.bilboard.songs_found.pop(song[0])
                break

    def setparams(self):
        if self.rd_get.isChecked():
            self.bilboard.client_id = os.getenv("SPFY-CLI-ID")
            self.cl_idtext.setText(self.bilboard.client_id)
            self.bilboard.client_sec=os.getenv("SPFY-CLI-SEC")
            self.cl_sectext.setText(self.bilboard.client_sec)
            self.txt_playlist.setText(self.bilboard.playlist_id)
    def get_date(self):
        if self.dateEdit.date().getDate()[1] < 10:
            month = f"0{self.dateEdit.date().getDate()[1]}"
        else:
            month = self.dateEdit.date().getDate()[1]
        date = f"{self.dateEdit.date().getDate()[0]}-{month}-{self.dateEdit.date().getDate()[2]}"
        self.bilboard.list_date = date

    def get_hotlist(self):
        hotlist = self.bilboard.search_hotlist()
        self.gpbox_hotlist.setTitle(f"There are {len(hotlist)} songs")
        for key, value in hotlist.items():
            print(key)
            print(value)
            self.listWidget.addItem(f"{str(key)} : {str(value)}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
