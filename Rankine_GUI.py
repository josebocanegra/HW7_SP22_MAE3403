# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Rankine_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(919, 569)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gb_Input = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gb_Input.setFont(font)
        self.gb_Input.setObjectName("gb_Input")
        self.gridLayout = QtWidgets.QGridLayout(self.gb_Input)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_PHigh = QtWidgets.QLabel(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_PHigh.sizePolicy().hasHeightForWidth())
        self.lbl_PHigh.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_PHigh.setFont(font)
        self.lbl_PHigh.setObjectName("lbl_PHigh")
        self.gridLayout.addWidget(self.lbl_PHigh, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.btn_Calculate = QtWidgets.QPushButton(self.gb_Input)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Calculate.setFont(font)
        self.btn_Calculate.setObjectName("btn_Calculate")
        self.gridLayout.addWidget(self.btn_Calculate, 0, 2, 2, 2)
        self.lbl_PLow = QtWidgets.QLabel(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_PLow.sizePolicy().hasHeightForWidth())
        self.lbl_PLow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_PLow.setFont(font)
        self.lbl_PLow.setObjectName("lbl_PLow")
        self.gridLayout.addWidget(self.lbl_PLow, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.le_PLow = QtWidgets.QLineEdit(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_PLow.sizePolicy().hasHeightForWidth())
        self.le_PLow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_PLow.setFont(font)
        self.le_PLow.setClearButtonEnabled(True)
        self.le_PLow.setObjectName("le_PLow")
        self.gridLayout.addWidget(self.le_PLow, 1, 1, 1, 1)
        self.le_PHigh = QtWidgets.QLineEdit(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_PHigh.sizePolicy().hasHeightForWidth())
        self.le_PHigh.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_PHigh.setFont(font)
        self.le_PHigh.setClearButtonEnabled(True)
        self.le_PHigh.setObjectName("le_PHigh")
        self.gridLayout.addWidget(self.le_PHigh, 0, 1, 1, 1)
        self.le_TurbineInletCondition = QtWidgets.QLineEdit(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_TurbineInletCondition.sizePolicy().hasHeightForWidth())
        self.le_TurbineInletCondition.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_TurbineInletCondition.setFont(font)
        self.le_TurbineInletCondition.setClearButtonEnabled(True)
        self.le_TurbineInletCondition.setObjectName("le_TurbineInletCondition")
        self.gridLayout.addWidget(self.le_TurbineInletCondition, 2, 1, 1, 1)
        self.lbl_TurbineInletCondition = QtWidgets.QLabel(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_TurbineInletCondition.sizePolicy().hasHeightForWidth())
        self.lbl_TurbineInletCondition.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_TurbineInletCondition.setFont(font)
        self.lbl_TurbineInletCondition.setObjectName("lbl_TurbineInletCondition")
        self.gridLayout.addWidget(self.lbl_TurbineInletCondition, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.rdo_Quality = QtWidgets.QRadioButton(self.gb_Input)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdo_Quality.setFont(font)
        self.rdo_Quality.setChecked(True)
        self.rdo_Quality.setObjectName("rdo_Quality")
        self.gridLayout.addWidget(self.rdo_Quality, 2, 2, 1, 1)
        self.rdo_THigh = QtWidgets.QRadioButton(self.gb_Input)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdo_THigh.setFont(font)
        self.rdo_THigh.setObjectName("rdo_THigh")
        self.gridLayout.addWidget(self.rdo_THigh, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gb_Input)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbl_SatPropHigh = QtWidgets.QLabel(self.gb_Input)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_SatPropHigh.setFont(font)
        self.lbl_SatPropHigh.setObjectName("lbl_SatPropHigh")
        self.gridLayout.addWidget(self.lbl_SatPropHigh, 4, 1, 1, 1)
        self.lbl_SatPropLow = QtWidgets.QLabel(self.gb_Input)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_SatPropLow.setFont(font)
        self.lbl_SatPropLow.setObjectName("lbl_SatPropLow")
        self.gridLayout.addWidget(self.lbl_SatPropLow, 4, 2, 1, 2)
        self.le_TurbineEff = QtWidgets.QLineEdit(self.gb_Input)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_TurbineEff.setFont(font)
        self.le_TurbineEff.setClearButtonEnabled(True)
        self.le_TurbineEff.setObjectName("le_TurbineEff")
        self.gridLayout.addWidget(self.le_TurbineEff, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.gb_Input)
        self.gb_Output = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_Output.sizePolicy().hasHeightForWidth())
        self.gb_Output.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gb_Output.setFont(font)
        self.gb_Output.setObjectName("gb_Output")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gb_Output)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gb_Output)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gb_Output)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gb_Output)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 2, 1, 1)
        self.le_H2 = QtWidgets.QLineEdit(self.gb_Output)
        self.le_H2.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_H2.setFont(font)
        self.le_H2.setObjectName("le_H2")
        self.gridLayout_2.addWidget(self.le_H2, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gb_Output)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.le_H4 = QtWidgets.QLineEdit(self.gb_Output)
        self.le_H4.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_H4.setFont(font)
        self.le_H4.setObjectName("le_H4")
        self.gridLayout_2.addWidget(self.le_H4, 3, 1, 1, 1)
        self.le_H3 = QtWidgets.QLineEdit(self.gb_Output)
        self.le_H3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_H3.setFont(font)
        self.le_H3.setObjectName("le_H3")
        self.gridLayout_2.addWidget(self.le_H3, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gb_Output)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.le_H1 = QtWidgets.QLineEdit(self.gb_Output)
        self.le_H1.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_H1.setFont(font)
        self.le_H1.setObjectName("le_H1")
        self.gridLayout_2.addWidget(self.le_H1, 0, 1, 1, 1)
        self.le_TurbineWork = QtWidgets.QLineEdit(self.gb_Output)
        self.le_TurbineWork.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_TurbineWork.setFont(font)
        self.le_TurbineWork.setObjectName("le_TurbineWork")
        self.gridLayout_2.addWidget(self.le_TurbineWork, 0, 4, 1, 1)
        self.le_HeatAdded = QtWidgets.QLineEdit(self.gb_Output)
        self.le_HeatAdded.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_HeatAdded.setFont(font)
        self.le_HeatAdded.setObjectName("le_HeatAdded")
        self.gridLayout_2.addWidget(self.le_HeatAdded, 2, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gb_Output)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 1, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gb_Output)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gb_Output)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 2, 5, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gb_Output)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 5, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gb_Output)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 3, 1, 1)
        self.le_PumpWork = QtWidgets.QLineEdit(self.gb_Output)
        self.le_PumpWork.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_PumpWork.setFont(font)
        self.le_PumpWork.setObjectName("le_PumpWork")
        self.gridLayout_2.addWidget(self.le_PumpWork, 1, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gb_Output)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 3, 1, 1, QtCore.Qt.AlignRight)
        self.le_Efficiency = QtWidgets.QLineEdit(self.gb_Output)
        self.le_Efficiency.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_Efficiency.setFont(font)
        self.le_Efficiency.setObjectName("le_Efficiency")
        self.gridLayout_2.addWidget(self.le_Efficiency, 3, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gb_Output)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gb_Output)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gb_Output)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gb_Output)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 1, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gb_Output)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.gb_Output)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.gb_Input.setTitle(_translate("Form", "Input"))
        self.lbl_PHigh.setText(_translate("Form", "P High (bar)"))
        self.btn_Calculate.setText(_translate("Form", "Calculate"))
        self.lbl_PLow.setText(_translate("Form", "P Low (bar)"))
        self.le_PLow.setText(_translate("Form", "0.08"))
        self.le_PLow.setPlaceholderText(_translate("Form", "enter a value for the low pressure isobar"))
        self.le_PHigh.setText(_translate("Form", "80"))
        self.le_PHigh.setPlaceholderText(_translate("Form", "enter a value for the high pressure isobar"))
        self.le_TurbineInletCondition.setText(_translate("Form", "1.0"))
        self.lbl_TurbineInletCondition.setText(_translate("Form", "Turbine Inlet: x ="))
        self.rdo_Quality.setText(_translate("Form", "Quality"))
        self.rdo_THigh.setText(_translate("Form", "T High"))
        self.label.setText(_translate("Form", "Turbine Eff."))
        self.lbl_SatPropHigh.setText(_translate("Form", "Saturated Properties"))
        self.lbl_SatPropLow.setText(_translate("Form", "Saturated Properties"))
        self.le_TurbineEff.setText(_translate("Form", "0.95"))
        self.le_TurbineEff.setPlaceholderText(_translate("Form", "turbine isentropic efficiency 0.0<eta<=1.0"))
        self.gb_Output.setTitle(_translate("Form", "Output"))
        self.label_4.setText(_translate("Form", "kJ/kg"))
        self.label_5.setText(_translate("Form", "h2"))
        self.label_8.setText(_translate("Form", "kJ/kg"))
        self.label_7.setText(_translate("Form", "h4"))
        self.label_9.setText(_translate("Form", "h3"))
        self.label_15.setText(_translate("Form", "Pump Work"))
        self.label_11.setText(_translate("Form", "Heat Added"))
        self.label_16.setText(_translate("Form", "kJ/kg"))
        self.label_17.setText(_translate("Form", "kJ/kg"))
        self.label_14.setText(_translate("Form", "Turbine Work"))
        self.label_10.setText(_translate("Form", "Thermal Efficiency"))
        self.label_3.setText(_translate("Form", "kJ/kg"))
        self.label_12.setText(_translate("Form", "%"))
        self.label_6.setText(_translate("Form", "kJ/kg"))
        self.label_13.setText(_translate("Form", "kJ/kg"))
        self.label_2.setText(_translate("Form", "h1"))

