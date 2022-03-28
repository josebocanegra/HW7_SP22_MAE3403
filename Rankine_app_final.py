import sys
from PyQt5.QtWidgets import QWidget, QApplication
from Rankine_GUI import Ui_Form  # from the GUI file your created
from Rankine import rankine
from PyQt5 import QtCore, QtGui, QtWidgets


class main_window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Rankine Cycle Calculator')

        self.rankine = rankine()
        self.label = [self.le_PHigh, self.le_PLow, self.le_TurbineInletCondition, self.le_TurbineEff, self.le_H1,
                      self.le_H2, self.le_H3, self.le_H4, self.le_HeatAdded, self.le_PumpWork, self.le_Efficiency,
                      self.le_TurbineWork]

        self.btn_Calculate.clicked.connect(self.Calculate)
        self.show()


    def Calculate(self):

        self.rankine.p_high = float(self.le_PHigh.text()) * 100
        self.rankine.p_low = float(self.le_PLow.text()) * 100
        self.rankine.eff_turbine = float(self.le_TurbineEff.text())

        self.rankine.quality = float(self.le_TurbineInletCondition.text()) if self.rdo_Quality.isChecked() else None
        self.rankine.t_high = float(self.le_TurbineInletCondition.text()) if self.rdo_THigh.isChecked() else None

        if self.rdo_Quality.isChecked():
            self.lbl_TurbineInletCondition.setText(QtCore.QCoreApplication.translate("Form", "Turbine Inlet: x ="))
        if self.rdo_THigh.isChecked():
            self.lbl_TurbineInletCondition.setText(QtCore.QCoreApplication.translate("Form", "Turbine Inlet: T_high ="))

        self.rankine.calc_efficiency()

        self.le_H1.setText("{:.2f}".format(self.rankine.state1.h))
        self.le_H2.setText("{:.2f}".format(self.rankine.state2.h))
        self.le_H3.setText("{:.2f}".format(self.rankine.state3.h))
        self.le_H4.setText("{:.2f}".format(self.rankine.state4.h))
        self.le_HeatAdded.setText("{:.2f}".format(self.rankine.heat_added))
        self.le_PumpWork.setText("{:.2f}".format(self.rankine.pump_work))
        self.le_Efficiency.setText("{:.2f}".format(self.rankine.efficiency))
        self.le_TurbineWork.setText("{:.2f}".format(self.rankine.turbine_work))

        self.lbl_SatPropHigh.setText(
            "\nPSat = {:.2f} bar, TSat= {:.2f} C\nhf = {:.2f} kJ/kg , hg = {:.2f} kJ/kg\nsf= {:.2f} kJ/kg*K, sg= {:.2f} kJ/kg*K\nvf= {:.4f} m^3/kg, vg= {:.2f} m^3/kg".format(
                self.rankine.p_high / 100, self.rankine.state1.T, self.rankine.state1.hf, self.rankine.state1.hg,
                self.rankine.state1.sf, self.rankine.state1.sg, self.rankine.state1.vf, self.rankine.state1.vg))
        self.lbl_SatPropLow.setText(
            "\nPSat = {:.2f} bar, TSat= {:.2f} C\nhf = {:.2f} kJ/kg , hg = {:.2f} kJ/kg\nsf= {:.2f} kJ/kg*K, sg= {:.2f} kJ/kg*K\nvf= {:.4f} m^3/kg, vg= {:.2f} m^3/kg".format(
                self.rankine.p_low / 100, self.rankine.state2.T, self.rankine.state2.hf, self.rankine.state2.hg,
                self.rankine.state2.sf, self.rankine.state2.sg, self.rankine.state2.vf, self.rankine.state2.vg))

        return

    def ExitApp(self):
        app.exit()


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())
