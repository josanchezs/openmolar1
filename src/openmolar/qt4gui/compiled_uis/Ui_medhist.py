# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medhist.ui'
#
# Created: Tue Oct  6 21:47:29 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(790, 559)
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.doctor_lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.doctor_lineEdit.setMaxLength(60)
        self.doctor_lineEdit.setObjectName("doctor_lineEdit")
        self.gridLayout_3.addWidget(self.doctor_lineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.doctorAddy_lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.doctorAddy_lineEdit.setMaxLength(60)
        self.doctorAddy_lineEdit.setObjectName("doctorAddy_lineEdit")
        self.gridLayout_3.addWidget(self.doctorAddy_lineEdit, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 7)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.curMeds_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.curMeds_lineEdit.setMaxLength(60)
        self.curMeds_lineEdit.setObjectName("curMeds_lineEdit")
        self.gridLayout.addWidget(self.curMeds_lineEdit, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.pastMeds_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.pastMeds_lineEdit.setMaxLength(60)
        self.pastMeds_lineEdit.setObjectName("pastMeds_lineEdit")
        self.gridLayout.addWidget(self.pastMeds_lineEdit, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.allergies_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.allergies_lineEdit.setMaxLength(60)
        self.allergies_lineEdit.setObjectName("allergies_lineEdit")
        self.gridLayout.addWidget(self.allergies_lineEdit, 2, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)
        self.heart_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.heart_lineEdit.setMaxLength(60)
        self.heart_lineEdit.setObjectName("heart_lineEdit")
        self.gridLayout.addWidget(self.heart_lineEdit, 3, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 2)
        self.lungs_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lungs_lineEdit.setMaxLength(60)
        self.lungs_lineEdit.setObjectName("lungs_lineEdit")
        self.gridLayout.addWidget(self.lungs_lineEdit, 4, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 1, 1, 1)
        self.liver_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.liver_lineEdit.setMaxLength(60)
        self.liver_lineEdit.setObjectName("liver_lineEdit")
        self.gridLayout.addWidget(self.liver_lineEdit, 5, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 2)
        self.bleeding_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.bleeding_lineEdit.setMaxLength(60)
        self.bleeding_lineEdit.setObjectName("bleeding_lineEdit")
        self.gridLayout.addWidget(self.bleeding_lineEdit, 6, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 2)
        self.kidneys_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.kidneys_lineEdit.setMaxLength(60)
        self.kidneys_lineEdit.setObjectName("kidneys_lineEdit")
        self.gridLayout.addWidget(self.kidneys_lineEdit, 7, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 2)
        self.anaesthetic_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.anaesthetic_lineEdit.setMaxLength(60)
        self.anaesthetic_lineEdit.setObjectName("anaesthetic_lineEdit")
        self.gridLayout.addWidget(self.anaesthetic_lineEdit, 8, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 2)
        self.other_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.other_lineEdit.setMaxLength(60)
        self.other_lineEdit.setObjectName("other_lineEdit")
        self.gridLayout.addWidget(self.other_lineEdit, 9, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 7)
        self.checked_pushButton = QtGui.QPushButton(Dialog)
        self.checked_pushButton.setObjectName("checked_pushButton")
        self.gridLayout_2.addWidget(self.checked_pushButton, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.date_label = QtGui.QLabel(Dialog)
        self.date_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.date_label.setObjectName("date_label")
        self.gridLayout_2.addWidget(self.date_label, 2, 2, 1, 1)
        self.dateEdit = QtGui.QDateEdit(Dialog)
        self.dateEdit.setReadOnly(True)
        self.dateEdit.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1900, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 2, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 4, 1, 1)
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 2, 5, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 2, 6, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_( u"Medical Notes"))
        self.groupBox_2.setTitle(_( u"Doctor\'s details"))
        self.label.setText(_( u"Doctor\'s Name"))
        self.label_2.setText(_( u"Address / Tel No"))
        self.groupBox.setTitle(_( u"Known Conditions"))
        self.label_3.setText(_( u"Current Medication"))
        self.label_4.setText(_( u"Past Medication"))
        self.label_5.setText(_( u"Allergies"))
        self.label_6.setText(_( u"Heart"))
        self.label_7.setText(_( u"Lungs"))
        self.label_8.setText(_( u"Liver"))
        self.label_11.setText(_( u"Bleeding"))
        self.label_9.setText(_( u"Kidneys"))
        self.label_10.setText(_( u"Anaesthetic / operations"))
        self.label_12.setText(_( u"Other"))
        self.checked_pushButton.setText(_( u"Mark as Checked  Today"))
        self.date_label.setText(_( u"Checked"))
        self.checkBox.setText(_( u"Mark Patient as Med Alert"))

