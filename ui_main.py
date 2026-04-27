# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QCheckBox,
    QComboBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTextBrowser, QVBoxLayout, QWidget)

from tool import (CopyableTableView, FileDropPlainTextEdit)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.fileDrag_plainTextEdit = FileDropPlainTextEdit(self.tab)
        self.fileDrag_plainTextEdit.setObjectName(u"fileDrag_plainTextEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fileDrag_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.fileDrag_plainTextEdit.setSizePolicy(sizePolicy1)
        self.fileDrag_plainTextEdit.setMinimumSize(QSize(376, 0))
        self.fileDrag_plainTextEdit.setMaximumSize(QSize(16777215, 125))

        self.gridLayout_4.addWidget(self.fileDrag_plainTextEdit, 0, 0, 4, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.description_comboBox = QComboBox(self.tab)
        self.description_comboBox.setObjectName(u"description_comboBox")

        self.gridLayout.addWidget(self.description_comboBox, 1, 1, 1, 1)

        self.measurement_comboBox = QComboBox(self.tab)
        self.measurement_comboBox.setObjectName(u"measurement_comboBox")

        self.gridLayout.addWidget(self.measurement_comboBox, 1, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.characteristic_checkBox = QCheckBox(self.tab)
        self.characteristic_checkBox.setObjectName(u"characteristic_checkBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.characteristic_checkBox.sizePolicy().hasHeightForWidth())
        self.characteristic_checkBox.setSizePolicy(sizePolicy2)
        self.characteristic_checkBox.setChecked(True)

        self.horizontalLayout_4.addWidget(self.characteristic_checkBox)

        self.characteristicAll_radioButton = QRadioButton(self.tab)
        self.characteristic_buttonGroup = QButtonGroup(MainWindow)
        self.characteristic_buttonGroup.setObjectName(u"characteristic_buttonGroup")
        self.characteristic_buttonGroup.addButton(self.characteristicAll_radioButton)
        self.characteristicAll_radioButton.setObjectName(u"characteristicAll_radioButton")
        self.characteristicAll_radioButton.setEnabled(True)
        self.characteristicAll_radioButton.setCheckable(True)
        self.characteristicAll_radioButton.setChecked(True)

        self.horizontalLayout_4.addWidget(self.characteristicAll_radioButton)

        self.characteristicSC_radioButton = QRadioButton(self.tab)
        self.characteristic_buttonGroup.addButton(self.characteristicSC_radioButton)
        self.characteristicSC_radioButton.setObjectName(u"characteristicSC_radioButton")
        self.characteristicSC_radioButton.setEnabled(True)
        self.characteristicSC_radioButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.characteristicSC_radioButton)

        self.characteristicCC_radioButton = QRadioButton(self.tab)
        self.characteristic_buttonGroup.addButton(self.characteristicCC_radioButton)
        self.characteristicCC_radioButton.setObjectName(u"characteristicCC_radioButton")
        self.characteristicCC_radioButton.setEnabled(True)
        self.characteristicCC_radioButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.characteristicCC_radioButton)

        self.characteristicOther_radioButton = QRadioButton(self.tab)
        self.characteristic_buttonGroup.addButton(self.characteristicOther_radioButton)
        self.characteristicOther_radioButton.setObjectName(u"characteristicOther_radioButton")
        self.characteristicOther_radioButton.setEnabled(True)
        self.characteristicOther_radioButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.characteristicOther_radioButton)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CNC_checkBox = QCheckBox(self.tab)
        self.CNC_checkBox.setObjectName(u"CNC_checkBox")
        sizePolicy2.setHeightForWidth(self.CNC_checkBox.sizePolicy().hasHeightForWidth())
        self.CNC_checkBox.setSizePolicy(sizePolicy2)
        self.CNC_checkBox.setMinimumSize(QSize(0, 0))
        self.CNC_checkBox.setMaximumSize(QSize(16777215, 16777215))
        self.CNC_checkBox.setCheckable(True)
        self.CNC_checkBox.setChecked(True)
        self.CNC_checkBox.setTristate(False)

        self.horizontalLayout.addWidget(self.CNC_checkBox)

        self.CNC_All_radioButton = QRadioButton(self.tab)
        self.CNC_buttonGroup = QButtonGroup(MainWindow)
        self.CNC_buttonGroup.setObjectName(u"CNC_buttonGroup")
        self.CNC_buttonGroup.addButton(self.CNC_All_radioButton)
        self.CNC_All_radioButton.setObjectName(u"CNC_All_radioButton")
        self.CNC_All_radioButton.setEnabled(True)
        self.CNC_All_radioButton.setCheckable(True)
        self.CNC_All_radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.CNC_All_radioButton)

        self.CNC_Turning_radioButton = QRadioButton(self.tab)
        self.CNC_buttonGroup.addButton(self.CNC_Turning_radioButton)
        self.CNC_Turning_radioButton.setObjectName(u"CNC_Turning_radioButton")
        self.CNC_Turning_radioButton.setEnabled(True)
        self.CNC_Turning_radioButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.CNC_Turning_radioButton)

        self.CNC_Milling_radioButton = QRadioButton(self.tab)
        self.CNC_buttonGroup.addButton(self.CNC_Milling_radioButton)
        self.CNC_Milling_radioButton.setObjectName(u"CNC_Milling_radioButton")
        self.CNC_Milling_radioButton.setEnabled(True)
        self.CNC_Milling_radioButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.CNC_Milling_radioButton)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)


        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tolerance_checkBox = QCheckBox(self.tab)
        self.tolerance_checkBox.setObjectName(u"tolerance_checkBox")
        sizePolicy2.setHeightForWidth(self.tolerance_checkBox.sizePolicy().hasHeightForWidth())
        self.tolerance_checkBox.setSizePolicy(sizePolicy2)
        self.tolerance_checkBox.setMaximumSize(QSize(16777215, 16777215))
        self.tolerance_checkBox.setChecked(True)

        self.horizontalLayout_9.addWidget(self.tolerance_checkBox)

        self.toleranceTypeDefault_radioButton = QRadioButton(self.tab)
        self.toleranceType_buttonGroup = QButtonGroup(MainWindow)
        self.toleranceType_buttonGroup.setObjectName(u"toleranceType_buttonGroup")
        self.toleranceType_buttonGroup.addButton(self.toleranceTypeDefault_radioButton)
        self.toleranceTypeDefault_radioButton.setObjectName(u"toleranceTypeDefault_radioButton")
        self.toleranceTypeDefault_radioButton.setChecked(True)

        self.horizontalLayout_9.addWidget(self.toleranceTypeDefault_radioButton)

        self.toleranceTypeSymmetric_radioButton = QRadioButton(self.tab)
        self.toleranceType_buttonGroup.addButton(self.toleranceTypeSymmetric_radioButton)
        self.toleranceTypeSymmetric_radioButton.setObjectName(u"toleranceTypeSymmetric_radioButton")

        self.horizontalLayout_9.addWidget(self.toleranceTypeSymmetric_radioButton)

        self.toleranceTypeBi_radioButton = QRadioButton(self.tab)
        self.toleranceType_buttonGroup.addButton(self.toleranceTypeBi_radioButton)
        self.toleranceTypeBi_radioButton.setObjectName(u"toleranceTypeBi_radioButton")

        self.horizontalLayout_9.addWidget(self.toleranceTypeBi_radioButton)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)


        self.gridLayout_4.addLayout(self.horizontalLayout_9, 3, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fileChoose_pushButton = QPushButton(self.tab)
        self.fileChoose_pushButton.setObjectName(u"fileChoose_pushButton")

        self.verticalLayout.addWidget(self.fileChoose_pushButton)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.fileChooseModeRefresh_radioButton = QRadioButton(self.tab)
        self.fileChooseMode_buttonGroup = QButtonGroup(MainWindow)
        self.fileChooseMode_buttonGroup.setObjectName(u"fileChooseMode_buttonGroup")
        self.fileChooseMode_buttonGroup.addButton(self.fileChooseModeRefresh_radioButton)
        self.fileChooseModeRefresh_radioButton.setObjectName(u"fileChooseModeRefresh_radioButton")
        self.fileChooseModeRefresh_radioButton.setChecked(True)

        self.horizontalLayout_7.addWidget(self.fileChooseModeRefresh_radioButton)

        self.fileChooseModeAppend_radioButton = QRadioButton(self.tab)
        self.fileChooseMode_buttonGroup.addButton(self.fileChooseModeAppend_radioButton)
        self.fileChooseModeAppend_radioButton.setObjectName(u"fileChooseModeAppend_radioButton")

        self.horizontalLayout_7.addWidget(self.fileChooseModeAppend_radioButton)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)

        self.exportPresentTable_pushButton = QPushButton(self.tab)
        self.exportPresentTable_pushButton.setObjectName(u"exportPresentTable_pushButton")
        self.exportPresentTable_pushButton.setEnabled(False)

        self.horizontalLayout_6.addWidget(self.exportPresentTable_pushButton)

        self.exportAllTable_pushButton = QPushButton(self.tab)
        self.exportAllTable_pushButton.setObjectName(u"exportAllTable_pushButton")
        self.exportAllTable_pushButton.setEnabled(False)

        self.horizontalLayout_6.addWidget(self.exportAllTable_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.gridLayout_4.addLayout(self.verticalLayout, 4, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.unit_checkBox = QCheckBox(self.tab)
        self.unit_checkBox.setObjectName(u"unit_checkBox")
        sizePolicy2.setHeightForWidth(self.unit_checkBox.sizePolicy().hasHeightForWidth())
        self.unit_checkBox.setSizePolicy(sizePolicy2)
        self.unit_checkBox.setChecked(True)

        self.horizontalLayout_5.addWidget(self.unit_checkBox)

        self.exrtraBallNoWarning_checkBox = QCheckBox(self.tab)
        self.exrtraBallNoWarning_checkBox.setObjectName(u"exrtraBallNoWarning_checkBox")
        sizePolicy2.setHeightForWidth(self.exrtraBallNoWarning_checkBox.sizePolicy().hasHeightForWidth())
        self.exrtraBallNoWarning_checkBox.setSizePolicy(sizePolicy2)
        self.exrtraBallNoWarning_checkBox.setChecked(True)

        self.horizontalLayout_5.addWidget(self.exrtraBallNoWarning_checkBox)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Phi_checkBox = QCheckBox(self.tab)
        self.Phi_checkBox.setObjectName(u"Phi_checkBox")
        sizePolicy2.setHeightForWidth(self.Phi_checkBox.sizePolicy().hasHeightForWidth())
        self.Phi_checkBox.setSizePolicy(sizePolicy2)
        self.Phi_checkBox.setMinimumSize(QSize(0, 0))
        self.Phi_checkBox.setChecked(True)

        self.horizontalLayout_8.addWidget(self.Phi_checkBox)

        self.replaceValueWarning_checkBox = QCheckBox(self.tab)
        self.replaceValueWarning_checkBox.setObjectName(u"replaceValueWarning_checkBox")
        sizePolicy2.setHeightForWidth(self.replaceValueWarning_checkBox.sizePolicy().hasHeightForWidth())
        self.replaceValueWarning_checkBox.setSizePolicy(sizePolicy2)
        self.replaceValueWarning_checkBox.setMinimumSize(QSize(107, 0))
        self.replaceValueWarning_checkBox.setChecked(True)

        self.horizontalLayout_8.addWidget(self.replaceValueWarning_checkBox)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.extraBall_comboBox = QComboBox(self.tab)
        self.extraBall_comboBox.setObjectName(u"extraBall_comboBox")

        self.gridLayout_2.addWidget(self.extraBall_comboBox, 0, 1, 1, 1)

        self.replaceValue_comboBox = QComboBox(self.tab)
        self.replaceValue_comboBox.setObjectName(u"replaceValue_comboBox")

        self.gridLayout_2.addWidget(self.replaceValue_comboBox, 1, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 4, 1, 1, 1)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line, 5, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 6, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 6, 1, 1, 1)

        self.tableList_label = QLabel(self.tab)
        self.tableList_label.setObjectName(u"tableList_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableList_label.sizePolicy().hasHeightForWidth())
        self.tableList_label.setSizePolicy(sizePolicy3)
        self.tableList_label.setWordWrap(True)

        self.gridLayout_4.addWidget(self.tableList_label, 7, 0, 1, 1)

        self.tableListChoose_comboBox = QComboBox(self.tab)
        self.tableListChoose_comboBox.setObjectName(u"tableListChoose_comboBox")
        self.tableListChoose_comboBox.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableListChoose_comboBox.sizePolicy().hasHeightForWidth())
        self.tableListChoose_comboBox.setSizePolicy(sizePolicy4)
        self.tableListChoose_comboBox.setMinimumSize(QSize(376, 0))
        self.tableListChoose_comboBox.setEditable(False)

        self.gridLayout_4.addWidget(self.tableListChoose_comboBox, 7, 1, 1, 1)

        self.ballNoTable_tableView = CopyableTableView(self.tab)
        self.ballNoTable_tableView.setObjectName(u"ballNoTable_tableView")
        self.ballNoTable_tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.gridLayout_4.addWidget(self.ballNoTable_tableView, 8, 0, 1, 2)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.deletePresentTable_pushButton = QPushButton(self.tab)
        self.deletePresentTable_pushButton.setObjectName(u"deletePresentTable_pushButton")
        self.deletePresentTable_pushButton.setEnabled(False)

        self.horizontalLayout_12.addWidget(self.deletePresentTable_pushButton)

        self.deleteAllTable_pushButton = QPushButton(self.tab)
        self.deleteAllTable_pushButton.setObjectName(u"deleteAllTable_pushButton")
        self.deleteAllTable_pushButton.setEnabled(False)

        self.horizontalLayout_12.addWidget(self.deleteAllTable_pushButton)

        self.lastTable_pushButton = QPushButton(self.tab)
        self.lastTable_pushButton.setObjectName(u"lastTable_pushButton")
        self.lastTable_pushButton.setEnabled(False)
        self.lastTable_pushButton.setCheckable(False)

        self.horizontalLayout_12.addWidget(self.lastTable_pushButton)

        self.nextTable_pushButton = QPushButton(self.tab)
        self.nextTable_pushButton.setObjectName(u"nextTable_pushButton")
        self.nextTable_pushButton.setEnabled(False)

        self.horizontalLayout_12.addWidget(self.nextTable_pushButton)


        self.gridLayout_4.addLayout(self.horizontalLayout_12, 9, 0, 1, 2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_7 = QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.infoInput_plainTextEdit = QPlainTextEdit(self.tab_2)
        self.infoInput_plainTextEdit.setObjectName(u"infoInput_plainTextEdit")
        sizePolicy1.setHeightForWidth(self.infoInput_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.infoInput_plainTextEdit.setSizePolicy(sizePolicy1)
        self.infoInput_plainTextEdit.setMaximumSize(QSize(16777215, 100))
        self.infoInput_plainTextEdit.setReadOnly(False)

        self.gridLayout_7.addWidget(self.infoInput_plainTextEdit, 0, 0, 4, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 2, 1, 1)

        self.infoDescription_comboBox = QComboBox(self.tab_2)
        self.infoDescription_comboBox.setObjectName(u"infoDescription_comboBox")

        self.gridLayout_3.addWidget(self.infoDescription_comboBox, 1, 1, 1, 1)

        self.infoMeasurement_comboBox = QComboBox(self.tab_2)
        self.infoMeasurement_comboBox.setObjectName(u"infoMeasurement_comboBox")

        self.gridLayout_3.addWidget(self.infoMeasurement_comboBox, 1, 2, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_3, 0, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.infoCharacteristic_checkBox = QCheckBox(self.tab_2)
        self.infoCharacteristic_checkBox.setObjectName(u"infoCharacteristic_checkBox")
        sizePolicy2.setHeightForWidth(self.infoCharacteristic_checkBox.sizePolicy().hasHeightForWidth())
        self.infoCharacteristic_checkBox.setSizePolicy(sizePolicy2)
        self.infoCharacteristic_checkBox.setChecked(True)

        self.horizontalLayout_10.addWidget(self.infoCharacteristic_checkBox)

        self.infoCharacteristicAll_radioButton = QRadioButton(self.tab_2)
        self.infoCharacteristic_buttonGroup = QButtonGroup(MainWindow)
        self.infoCharacteristic_buttonGroup.setObjectName(u"infoCharacteristic_buttonGroup")
        self.infoCharacteristic_buttonGroup.addButton(self.infoCharacteristicAll_radioButton)
        self.infoCharacteristicAll_radioButton.setObjectName(u"infoCharacteristicAll_radioButton")
        self.infoCharacteristicAll_radioButton.setEnabled(True)
        self.infoCharacteristicAll_radioButton.setCheckable(True)
        self.infoCharacteristicAll_radioButton.setChecked(True)

        self.horizontalLayout_10.addWidget(self.infoCharacteristicAll_radioButton)

        self.infoCharacteristicSC_radioButton = QRadioButton(self.tab_2)
        self.infoCharacteristic_buttonGroup.addButton(self.infoCharacteristicSC_radioButton)
        self.infoCharacteristicSC_radioButton.setObjectName(u"infoCharacteristicSC_radioButton")
        self.infoCharacteristicSC_radioButton.setEnabled(True)
        self.infoCharacteristicSC_radioButton.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.infoCharacteristicSC_radioButton)

        self.infoCharacteristicCC_radioButton = QRadioButton(self.tab_2)
        self.infoCharacteristic_buttonGroup.addButton(self.infoCharacteristicCC_radioButton)
        self.infoCharacteristicCC_radioButton.setObjectName(u"infoCharacteristicCC_radioButton")
        self.infoCharacteristicCC_radioButton.setEnabled(True)
        self.infoCharacteristicCC_radioButton.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.infoCharacteristicCC_radioButton)

        self.infoCharacteristicOther_radioButton = QRadioButton(self.tab_2)
        self.infoCharacteristic_buttonGroup.addButton(self.infoCharacteristicOther_radioButton)
        self.infoCharacteristicOther_radioButton.setObjectName(u"infoCharacteristicOther_radioButton")
        self.infoCharacteristicOther_radioButton.setEnabled(True)
        self.infoCharacteristicOther_radioButton.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.infoCharacteristicOther_radioButton)


        self.gridLayout_7.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.infoCNC_checkBox = QCheckBox(self.tab_2)
        self.infoCNC_checkBox.setObjectName(u"infoCNC_checkBox")
        sizePolicy2.setHeightForWidth(self.infoCNC_checkBox.sizePolicy().hasHeightForWidth())
        self.infoCNC_checkBox.setSizePolicy(sizePolicy2)
        self.infoCNC_checkBox.setMinimumSize(QSize(0, 0))
        self.infoCNC_checkBox.setMaximumSize(QSize(16777215, 16777215))
        self.infoCNC_checkBox.setCheckable(True)
        self.infoCNC_checkBox.setChecked(True)
        self.infoCNC_checkBox.setTristate(False)

        self.horizontalLayout_11.addWidget(self.infoCNC_checkBox)

        self.infoCNC_All_radioButton = QRadioButton(self.tab_2)
        self.infoCNC_buttonGroup = QButtonGroup(MainWindow)
        self.infoCNC_buttonGroup.setObjectName(u"infoCNC_buttonGroup")
        self.infoCNC_buttonGroup.addButton(self.infoCNC_All_radioButton)
        self.infoCNC_All_radioButton.setObjectName(u"infoCNC_All_radioButton")
        self.infoCNC_All_radioButton.setEnabled(True)
        self.infoCNC_All_radioButton.setCheckable(True)
        self.infoCNC_All_radioButton.setChecked(True)

        self.horizontalLayout_11.addWidget(self.infoCNC_All_radioButton)

        self.infoCNC_Turning_radioButton = QRadioButton(self.tab_2)
        self.infoCNC_buttonGroup.addButton(self.infoCNC_Turning_radioButton)
        self.infoCNC_Turning_radioButton.setObjectName(u"infoCNC_Turning_radioButton")
        self.infoCNC_Turning_radioButton.setEnabled(True)
        self.infoCNC_Turning_radioButton.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.infoCNC_Turning_radioButton)

        self.infoCNC_Milling_radioButton = QRadioButton(self.tab_2)
        self.infoCNC_buttonGroup.addButton(self.infoCNC_Milling_radioButton)
        self.infoCNC_Milling_radioButton.setObjectName(u"infoCNC_Milling_radioButton")
        self.infoCNC_Milling_radioButton.setEnabled(True)
        self.infoCNC_Milling_radioButton.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.infoCNC_Milling_radioButton)

        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)


        self.gridLayout_7.addLayout(self.horizontalLayout_11, 2, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.infoShowExtratBall_checkBox = QCheckBox(self.tab_2)
        self.infoShowExtratBall_checkBox.setObjectName(u"infoShowExtratBall_checkBox")
        self.infoShowExtratBall_checkBox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.infoShowExtratBall_checkBox)

        self.infoExport_pushButton = QPushButton(self.tab_2)
        self.infoExport_pushButton.setObjectName(u"infoExport_pushButton")

        self.horizontalLayout_2.addWidget(self.infoExport_pushButton)


        self.gridLayout_7.addLayout(self.horizontalLayout_2, 3, 1, 2, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.infoSeperate_lineEdit = QLineEdit(self.tab_2)
        self.infoSeperate_lineEdit.setObjectName(u"infoSeperate_lineEdit")
        sizePolicy1.setHeightForWidth(self.infoSeperate_lineEdit.sizePolicy().hasHeightForWidth())
        self.infoSeperate_lineEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.infoSeperate_lineEdit)


        self.gridLayout_7.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.line_2 = QFrame(self.tab_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_2, 5, 0, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(373, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_4, 6, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(373, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 6, 1, 1, 1)

        self.info_tableView = CopyableTableView(self.tab_2)
        self.info_tableView.setObjectName(u"info_tableView")

        self.gridLayout_7.addWidget(self.info_tableView, 7, 0, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_6 = QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.help_textBrowser = QTextBrowser(self.tab_3)
        self.help_textBrowser.setObjectName(u"help_textBrowser")
        self.help_textBrowser.setOpenExternalLinks(True)

        self.gridLayout_6.addWidget(self.help_textBrowser, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_5.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.measurement_comboBox.setCurrentIndex(-1)
        self.tableListChoose_comboBox.setCurrentIndex(-1)
        self.infoMeasurement_comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5716\u9762\u8b80\u7403\u865f", None))
        self.fileDrag_plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u53ef\u62d6\u62c9\u6a94\u6848\u81f3\u6b64", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u63cf\u8ff0\u9078\u9805", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6aa2\u6e2c\u9078\u9805", None))
        self.characteristic_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u7ba1\u5236\u7279\u6027", None))
        self.characteristicAll_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8", None))
        self.characteristicSC_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u50c5SC", None))
        self.characteristicCC_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u50c5CC", None))
        self.characteristicOther_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6", None))
        self.CNC_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u8eca\u9291\u5e8a", None))
        self.CNC_All_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8", None))
        self.CNC_Turning_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u50c5\u8eca\u5e8a", None))
        self.CNC_Milling_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u50c5\u9291\u5e8a", None))
        self.label_7.setText("")
        self.tolerance_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u516c\u5dee", None))
        self.toleranceTypeDefault_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u9810\u8a2d", None))
        self.toleranceTypeSymmetric_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u5c0d\u7a31\u516c\u5dee", None))
        self.toleranceTypeBi_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u96d9\u5411\u516c\u5dee", None))
        self.label_8.setText("")
        self.fileChoose_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u9078\u64c7\u6a94\u6848", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u9078\u64c7\u6a94\u6848\u6a21\u5f0f", None))
        self.fileChooseModeRefresh_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.fileChooseModeAppend_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e", None))
        self.exportPresentTable_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u55ae\u7b46\u532f\u51fa", None))
        self.exportAllTable_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u591a\u7b46\u532f\u51fa", None))
        self.unit_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u986f\u793a\u55ae\u4f4d", None))
        self.exrtraBallNoWarning_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u7121\u5c3a\u5bf8\u7403\u865f\u8b66\u544a", None))
        self.Phi_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u986f\u793a\u00d8", None))
        self.replaceValueWarning_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u4ee3\u503c\u8b66\u544a", None))
        self.tableList_label.setText(QCoreApplication.translate("MainWindow", u"\u8acb\u5148\u9078\u64c7\u6a94\u6848", None))
        self.deletePresentTable_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u522a\u9664\u7576\u524d\u9801\u9762", None))
        self.deleteAllTable_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u522a\u9664\u6240\u6709\u9801\u9762", None))
        self.lastTable_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u9801", None))
        self.nextTable_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u9801", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u5716\u9762\u8f49\u7403\u865f", None))
#if QT_CONFIG(tooltip)
        self.infoInput_plainTextEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.infoInput_plainTextEdit.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.infoInput_plainTextEdit.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.infoInput_plainTextEdit.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.infoInput_plainTextEdit.setDocumentTitle("")
        self.infoInput_plainTextEdit.setPlainText("")
        self.infoInput_plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f38\u5165\u7403\u865f\u641c\u5c0b\uff0c\u53ef\u591a\u7b46\u8f38\u5165 ex: 1 2 3 4", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u63cf\u8ff0\u9078\u9805", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6aa2\u6e2c\u9078\u9805", None))
        self.infoCharacteristic_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u7ba1\u5236\u7279\u6027", None))
        self.infoCharacteristicAll_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8", None))
        self.infoCharacteristicSC_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u50c5SC", None))
        self.infoCharacteristicCC_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u50c5CC", None))
        self.infoCharacteristicOther_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6", None))
        self.infoCNC_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u8eca\u9291\u5e8a", None))
        self.infoCNC_All_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8", None))
        self.infoCNC_Turning_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u50c5\u8eca\u5e8a", None))
        self.infoCNC_Milling_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u50c5\u9291\u5e8a", None))
        self.label_9.setText("")
        self.infoShowExtratBall_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u986f\u793a\u641c\u5c0b\u6642\u7121\u5c0d\u61c9\u8cc7\u8a0a\u7684\u7403\u865f", None))
        self.infoExport_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u532f\u51fa", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u641c\u5c0b\u5206\u9694\u7b26\u865f(\u9810\u8a2d\u662f\u7a7a\u683c\u548c\u63db\u884c)", None))
        self.infoSeperate_lineEdit.setInputMask("")
        self.infoSeperate_lineEdit.setText("")
        self.infoSeperate_lineEdit.setPlaceholderText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u7403\u865f\u8cc7\u8a0a", None))
        self.help_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft JhengHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u91cd\u8981!!!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u6b64\u7a0b\u5f0f\u53ea\u80fd\u5224\u65b7\u5c3a\u5bf8\u985e\u578b\uff0c\u4e0d\u80fd\u5224\u65b7\u5e7e\u4f55\u516c\u5dee\u3001\u8a3b\u89e3\u548c\u96f6\u4ef6\u7403\u865f\u3002"
                        "</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u5c3a\u5bf8\u985e\u578b\u5167\u5efa\u7403\u865f\u6700\u591a\u53ea\u523099\uff0c\u4e14\u53ea\u80fd\u5305\u542b\u6578\u5b57\uff0c100\u4ee5\u4e0a\u6216\u5305\u542b\u5b57\u6bcd\u7684\u7403\u865f\u662f\u984d\u5916\u8a3b\u8a18\u7684\uff0c\u6293\u4e0d\u5230\u5c3a\u5bf8\uff0c\u9700\u81ea\u884c\u67e5\u770b\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u4ee5\u4e0b\u662f\u5c3a\u5bf8"
                        "\u985e\u578b\uff0c\u53ef\u6293\u5230\u5c3a\u5bf8\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/resource/example_1.PNG\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u4ee5\u4e0b\u662f\u6293\u4e0d\u5230\u5c3a\u5bf8\u7684\u985e\u578b\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/resource/example_2.PNG\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/resource/example_3.PNG\" "
                        "/></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/resource/example_4.PNG\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inde"
                        "nt:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-rig"
                        "ht:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u5716\u9762\u8f49\u7403\u865f\u9801\u9762\u64cd\u4f5c\u65b9\u5f0f</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p "
                        "style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/resource/example_5.PNG\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u5728\u5716\u9762\u8f49\u7403\u865f\u9801\u9762\uff0c\u6309\u4e0b\u9078\u64c7\u6a94\u6848\u6309\u9215\u6216\u5c07\u6a94\u6848\u62d6\u5165\u5de6\u4e0a\u89d2\u6846\uff0c\u53ef\u4ee5\u532f\u5165\u5716\u9762\uff0c\u4e26\u6703\u5728\u4e0b\u65b9\u8868\u683c\u986f\u793a\u8cc7\u8a0a(\u50c5SLDDRW\u6a94\u6703\u57f7\u884c)\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u53ef\u9078\u53d6\u6574\u500b\u8cc7\u6599\u593e\u7684\u6a94\u6848\u62d6\u5165\u5de6\u4e0a\u89d2\u6846\u532f\u5165\uff0c\u6548\u7387\u8f03\u9ad8\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:"
                        "0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/resource/example_6.PNG\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u6bcf\u7b46\u6a94\u6848\u532f\u5165\u5f8c\u6703\u6709\u4e00\u500b\u5c6c\u65bc\u5b83\u7684\u9801\u9762\uff0c\u8868\u683c\u53f3\u4e0a\u65b9\u53ef\u4ee5\u9078\u64c7\u9801\u9762\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragra"
                        "ph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/resource/example_9.PNG\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u6a94\u6848\u6a21\u5f0f\u9078\u64c7\u65b0\u589e\u53ef\u4ee5\u907f\u514d\u4e4b\u524d\u532f\u5165\u7684\u9801\u9762\u88ab\u5237\u65b0\u6389\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; marg"
                        "in-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/resource/example_10.PNG\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u53f3\u4e0a\u89d2\u53ef\u7be9\u9078\u8868\u683c\u7684\u8cc7\u8a0a\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/resource/example_11.PNG\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        "><span style=\" font-size:16pt;\">\u8868\u683c\u5167\u8cc7\u8a0a\u53efctrl + c\u6216\u53f3\u9375\u6309\u8907\u88fd\u5230\u526a\u8cbc\u7c3f\uff0c\u53ef\u8cbc\u5230excel\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u6309\u7403\u865f\u8868\u982d\u80fd\u6539\u8b8a\u6392\u5217\u9806\u5e8f\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/resource/example_7.PNG\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                        "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u7121\u5c3a\u5bf8\u7403\u865f\u8b66\u544a\u662f\u6307\u8b80\u5230\u8a3b\u89e3\u3001\u96f6\u4ef6\u7403\u865f\u3001\u5e7e\u4f55\u516c\u5dee\u985e\u578b\u7684\u7403\u865f\u6642\u6703\u8df3\u51fa\u8b66\u544a\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u53d6\u4ee3\u503c\u8b66\u544a\u662f\u6307\u8b80\u5230\u6709\u4f7f\u7528\u53d6\u4ee3\u503c\u8986\u84cb\u539f\u5c3a\u5bf8\u6642\u6703\u8df3\u51fa\u8b66\u544a\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:"
                        "0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/resource/example_8.PNG\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u55ae\u7b46\u532f\u51fa\u662f\u628a\u76ee\u524d\u9801\u9762\u5b58\u5230\u4e00\u500bexcel\u5de5\u4f5c\u8868\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u591a\u7b46\u532f\u51fa\u662f\u628a\u6240\u6709\u9801\u9762\u5b58\u5230\u4e00\u500bexcel\u5de5\u4f5c\u8868\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">excel\u5de5\u4f5c\u8868\u683c\u5f0f\u4e2d\u6587\u662f\u6a19\u6977\u9ad4\uff0c\u82f1\u6587\u662fTimes New Roman\u3002</span></p>\n"
"<p style=\"-qt-paragraph-t"
                        "ype:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br "
                        "/></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u7403\u865f\u8cc7\u8a0a\u9801\u9762\u64cd\u4f5c\u65b9\u5f0f</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; marg"
                        "in-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/resource/example_12.PNG\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u5728\u7403\u865f\u8cc7\u8a0a\u9801\u9762\uff0c\u5de6\u4e0a\u89d2\u641c\u5c0b\u6b04\uff0c\u53ef\u641c\u5c0b\u9700\u8981\u7684\u7403\u865f\u8cc7\u8a0a\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u641c\u5c0b\u5206\u9694\u7b26\u865f\u662f\u641c\u5c0b\u6b04\u591a\u7b46\u8f38\u5165\u6642\u7528"
                        "\u4f86\u5206\u9694\u6bcf\u7b46\u8f38\u5165\u7684\u7b26\u865f\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">ex: \u641c\u5c0b\u6b041 2 3 4\u6216 1\uff0c\u641c\u5c0b\u5206\u9694\u7b26\u865f\u662f\u7a7a\u503c\uff0c\u80fd\u641c\u52301\u30012\u30013\u30014\u7684\u7403\u865f\u8cc7\u8a0a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">		     2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">		     3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">		     4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; ma"
                        "rgin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">ex: \u641c\u5c0b\u6b041,2,3,4\uff0c\u641c\u5c0b\u5206\u9694\u7b26\u865f\u662f  ,  \uff0c\u80fd\u641c\u52301\u30012\u30013\u30014\u7684\u7403\u865f\u8cc7\u8a0a</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/resource/example_13.PNG\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u53f3\u4e0a\u89d2\u53ef\u7be9\u9078\u8868\u683c\u7684\u8cc7\u8a0a\u3002</span></p>\n"
""
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/resource/example_14.PNG\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u8868\u683c\u5167\u8cc7\u8a0a\u53efctrl + c\u6216\u53f3\u9375\u6309\u8907\u88fd\u5230\u526a\u8cbc\u7c3f\uff0c\u53ef\u8cbc\u5230excel\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u6309\u7403\u865f\u8868\u982d\u80fd\u6539"
                        "\u8b8a\u6392\u5217\u9806\u5e8f\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u641c\u5c0b\u6b04\u70ba\u7a7a\u503c\u6642\uff0c\u6703\u5217\u51fa\u6240\u6709\u7403\u865f\u8cc7\u8a0a\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/resource/example_15.PNG\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u532f\u51fa\u662f"
                        "\u628a\u76ee\u524d\u7403\u865f\u8cc7\u8a0a\u5b58\u5230\u4e00\u500bexcel\u5de5\u4f5c\u8868\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">excel\u5de5\u4f5c\u8868\u683c\u5f0f\u4e2d\u6587\u662f\u6a19\u6977\u9ad4\uff0c\u82f1\u6587\u662fTimes New Roman\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-"
                        "bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragrap"
                        "h-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><"
                        "br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                        " text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.7tailpurplefox.com\"><img src=\":/resource/icon.png\" /></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u5e6b\u52a9", None))
    # retranslateUi

