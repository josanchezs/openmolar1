# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openmolar/openmolar/qt-designer/apptOpenDay.ui'
#
# Created: Sun Jun 21 21:00:14 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 377)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(141, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.dateEdit = QtGui.QDateEdit(Dialog)
        self.dateEdit.setMinimumSize(QtCore.QSize(140, 0))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 1, 2, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 2)
        self.memo_lineEdit = QtGui.QLineEdit(Dialog)
        self.memo_lineEdit.setMaxLength(30)
        self.memo_lineEdit.setObjectName("memo_lineEdit")
        self.gridLayout_2.addWidget(self.memo_lineEdit, 2, 2, 1, 2)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(522, 0))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtGui.QLabel(self.frame)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 1)
        self.dayStart_timeEdit = QtGui.QTimeEdit(self.frame)
        self.dayStart_timeEdit.setObjectName("dayStart_timeEdit")
        self.gridLayout.addWidget(self.dayStart_timeEdit, 0, 2, 1, 1)
        self.es1_checkBox = QtGui.QCheckBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.es1_checkBox.sizePolicy().hasHeightForWidth())
        self.es1_checkBox.setSizePolicy(sizePolicy)
        self.es1_checkBox.setObjectName("es1_checkBox")
        self.gridLayout.addWidget(self.es1_checkBox, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.es1Start_timeEdit = QtGui.QTimeEdit(self.frame)
        self.es1Start_timeEdit.setObjectName("es1Start_timeEdit")
        self.gridLayout.addWidget(self.es1Start_timeEdit, 1, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1)
        self.es1Finish_timeEdit = QtGui.QTimeEdit(self.frame)
        self.es1Finish_timeEdit.setObjectName("es1Finish_timeEdit")
        self.gridLayout.addWidget(self.es1Finish_timeEdit, 1, 4, 1, 1)
        self.lunch_checkBox = QtGui.QCheckBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lunch_checkBox.sizePolicy().hasHeightForWidth())
        self.lunch_checkBox.setSizePolicy(sizePolicy)
        self.lunch_checkBox.setObjectName("lunch_checkBox")
        self.gridLayout.addWidget(self.lunch_checkBox, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.lunchStart_timeEdit = QtGui.QTimeEdit(self.frame)
        self.lunchStart_timeEdit.setObjectName("lunchStart_timeEdit")
        self.gridLayout.addWidget(self.lunchStart_timeEdit, 2, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 3, 1, 1)
        self.lunchFinish_timeEdit = QtGui.QTimeEdit(self.frame)
        self.lunchFinish_timeEdit.setObjectName("lunchFinish_timeEdit")
        self.gridLayout.addWidget(self.lunchFinish_timeEdit, 2, 4, 1, 1)
        self.es2_checkBox = QtGui.QCheckBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.es2_checkBox.sizePolicy().hasHeightForWidth())
        self.es2_checkBox.setSizePolicy(sizePolicy)
        self.es2_checkBox.setObjectName("es2_checkBox")
        self.gridLayout.addWidget(self.es2_checkBox, 3, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)
        self.es2Start_timeEdit = QtGui.QTimeEdit(self.frame)
        self.es2Start_timeEdit.setObjectName("es2Start_timeEdit")
        self.gridLayout.addWidget(self.es2Start_timeEdit, 3, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 3, 1, 1)
        self.es2Finish_timeEdit = QtGui.QTimeEdit(self.frame)
        self.es2Finish_timeEdit.setObjectName("es2Finish_timeEdit")
        self.gridLayout.addWidget(self.es2Finish_timeEdit, 3, 4, 1, 1)
        self.label_11 = QtGui.QLabel(self.frame)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 3, 1, 1)
        self.dayFinish_timeEdit = QtGui.QTimeEdit(self.frame)
        self.dayFinish_timeEdit.setObjectName("dayFinish_timeEdit")
        self.gridLayout.addWidget(self.dayFinish_timeEdit, 4, 4, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 3, 0, 1, 4)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 5, 0, 1, 4)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Open a Day", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Clinician", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Date to Open", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Day Memo - optional", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Day Start", None, QtGui.QApplication.UnicodeUTF8))
        self.es1_checkBox.setText(QtGui.QApplication.translate("Dialog", "Morning Emergency Slot", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Finish", None, QtGui.QApplication.UnicodeUTF8))
        self.lunch_checkBox.setText(QtGui.QApplication.translate("Dialog", "Lunch", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Finish", None, QtGui.QApplication.UnicodeUTF8))
        self.es2_checkBox.setText(QtGui.QApplication.translate("Dialog", "Afternoon Emergency Slot ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Finish", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "Day Finish", None, QtGui.QApplication.UnicodeUTF8))
