from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(383, 350)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_P_Units = QtWidgets.QLabel(self.groupBox)
        self.lbl_P_Units.setObjectName("lbl_P_Units")
        self.gridLayout.addWidget(self.lbl_P_Units, 1, 3, 1, 1)
        self.chk_Temp = QtWidgets.QCheckBox(self.groupBox)
        self.chk_Temp.setText("")
        self.chk_Temp.setObjectName("chk_Temp")
        self.gridLayout.addWidget(self.chk_Temp, 2, 2, 1, 1)
        self.le_P = QtWidgets.QLineEdit(self.groupBox)
        self.le_P.setObjectName("le_P")
        self.gridLayout.addWidget(self.le_P, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.lbl_T_Units = QtWidgets.QLabel(self.groupBox)
        self.lbl_T_Units.setObjectName("lbl_T_Units")
        self.gridLayout.addWidget(self.lbl_T_Units, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 6, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.le_Q = QtWidgets.QLineEdit(self.groupBox)
        self.le_Q.setText("")
        self.le_Q.setObjectName("le_Q")
        self.gridLayout.addWidget(self.le_Q, 4, 1, 1, 1)
        self.chk_Press = QtWidgets.QCheckBox(self.groupBox)
        self.chk_Press.setText("")
        self.chk_Press.setObjectName("chk_Press")
        self.gridLayout.addWidget(self.chk_Press, 1, 2, 1, 1)
        self.le_T = QtWidgets.QLineEdit(self.groupBox)
        self.le_T.setObjectName("le_T")
        self.gridLayout.addWidget(self.le_T, 2, 1, 1, 1)
        self.chk_Quality = QtWidgets.QCheckBox(self.groupBox)
        self.chk_Quality.setText("")
        self.chk_Quality.setObjectName("chk_Quality")
        self.gridLayout.addWidget(self.chk_Quality, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.lbl_H_Units = QtWidgets.QLabel(self.groupBox)
        self.lbl_H_Units.setObjectName("lbl_H_Units")
        self.gridLayout.addWidget(self.lbl_H_Units, 5, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.le_H = QtWidgets.QLineEdit(self.groupBox)
        self.le_H.setText("")
        self.le_H.setObjectName("le_H")
        self.gridLayout.addWidget(self.le_H, 5, 1, 1, 1)
        self.chk_Enthalpy = QtWidgets.QCheckBox(self.groupBox)
        self.chk_Enthalpy.setText("")
        self.chk_Enthalpy.setObjectName("chk_Enthalpy")
        self.gridLayout.addWidget(self.chk_Enthalpy, 5, 2, 1, 1)
        self.le_S = QtWidgets.QLineEdit(self.groupBox)
        self.le_S.setText("")
        self.le_S.setObjectName("le_S")
        self.gridLayout.addWidget(self.le_S, 6, 1, 1, 1)
        self.le_SpV = QtWidgets.QLineEdit(self.groupBox)
        self.le_SpV.setText("")
        self.le_SpV.setObjectName("le_SpV")
        self.gridLayout.addWidget(self.le_SpV, 7, 1, 1, 1)
        self.chk_SpV = QtWidgets.QCheckBox(self.groupBox)
        self.chk_SpV.setText("")
        self.chk_SpV.setObjectName("chk_SpV")
        self.gridLayout.addWidget(self.chk_SpV, 7, 2, 1, 1)
        self.lbl_SpV_Units = QtWidgets.QLabel(self.groupBox)
        self.lbl_SpV_Units.setObjectName("lbl_SpV_Units")
        self.gridLayout.addWidget(self.lbl_SpV_Units, 7, 3, 1, 1)
        self.lbl_S_Units = QtWidgets.QLabel(self.groupBox)
        self.lbl_S_Units.setObjectName("lbl_S_Units")
        self.gridLayout.addWidget(self.lbl_S_Units, 6, 3, 1, 1)
        self.lbl_Properties = QtWidgets.QLabel(self.groupBox)
        self.lbl_Properties.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_Properties.setObjectName("lbl_Properties")
        self.gridLayout.addWidget(self.lbl_Properties, 8, 0, 1, 6)
        self.chk_Entropy = QtWidgets.QCheckBox(self.groupBox)
        self.chk_Entropy.setText("")
        self.chk_Entropy.setObjectName("chk_Entropy")
        self.gridLayout.addWidget(self.chk_Entropy, 6, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Calculate = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Calculate.setObjectName("pushButton_Calculate")
        self.horizontalLayout.addWidget(self.pushButton_Calculate)
        self.pushButton_Exit = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.horizontalLayout.addWidget(self.pushButton_Exit)
        self.gridLayout.addLayout(self.horizontalLayout, 9, 0, 1, 5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 11, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Steam Property Calculator"))
        self.lbl_P_Units.setText(_translate("Form", "kPa"))
        self.le_P.setText(_translate("Form", "8000"))
        self.label_6.setText(_translate("Form", "Temperature"))
        self.lbl_T_Units.setText(_translate("Form", "C"))
        self.label_5.setText(_translate("Form", "Quality"))
        self.le_T.setText(_translate("Form", "550"))
        self.label_3.setText(_translate("Form", "Enthalpy"))
        self.label_7.setText(_translate("Form", "Pressure"))
        self.lbl_H_Units.setText(_translate("Form", "kJ/kg"))
        self.label_4.setText(_translate("Form", "Entropy"))
        self.lbl_SpV_Units.setText(_translate("Form", "kg/m^3"))
        self.lbl_S_Units.setText(_translate("Form", "kJ/(kg*K)"))
        self.lbl_Properties.setText(_translate("Form", "Region"))
        self.label_8.setText(_translate("Form", "Specific Volume"))
        self.pushButton_Calculate.setText(_translate("Form", "Calculate"))
        self.pushButton_Exit.setText(_translate("Form", "Exit"))