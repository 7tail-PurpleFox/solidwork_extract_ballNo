from constant import *
import tool
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem
from ui_main import Ui_MainWindow
import time
from xlsxwriter.exceptions import FileCreateError
import math


class MainWindow(QMainWindow):
    # 所有同class共用的資料
    error_signal = Signal(str, int) # error, error_type
    set_table_signal = Signal(int)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # initialize
        self.table_list = []
        self.table_combobox_items = []
        self.sw_app = None
        self.model = None
        self.info_model = None
        tool.add_items(self.ui.description_comboBox, DESCRIPTION_COMBOBOX_ITEMS)
        tool.add_items(self.ui.measurement_comboBox, MEASUREMENT_COMBOBOX_ITEMS)
        tool.add_items(self.ui.replaceValue_comboBox, REPLACE_VALUE_COMBOBOX_ITEMS)
        tool.add_items(self.ui.extraBall_comboBox, EXTRABALL_COMBOBOX_ITEMS)
        tool.add_items(self.ui.infoDescription_comboBox, DESCRIPTION_COMBOBOX_ITEMS)
        tool.add_items(self.ui.infoMeasurement_comboBox, MEASUREMENT_COMBOBOX_ITEMS)
        self.ui.description_comboBox.setCurrentIndex(0)
        self.ui.measurement_comboBox.setCurrentIndex(0)
        self.ui.replaceValue_comboBox.setCurrentIndex(0)
        self.ui.extraBall_comboBox.setCurrentIndex(0)
        self.ui.infoDescription_comboBox.setCurrentIndex(0)
        self.ui.infoMeasurement_comboBox.setCurrentIndex(0)

        self.set_info_table()



        # connect
        self.error_signal.connect(self.handle_error)
        self.set_table_signal.connect(self.set_table)
        self.ui.fileChoose_pushButton.clicked.connect(self.open_file)
        self.ui.fileDrag_plainTextEdit.fileDropped.connect(self.on_files_dropped)
        self.ui.deletePresentTable_pushButton.clicked.connect(self.delete_present_table)
        self.ui.deleteAllTable_pushButton.clicked.connect(self.delete_all_table)
        self.ui.tableListChoose_comboBox.activated.connect(self.set_table_lable)
        self.ui.tableListChoose_comboBox.activated.connect(lambda: self.set_table())
        self.ui.description_comboBox.activated.connect(lambda: self.set_table())
        self.ui.measurement_comboBox.activated.connect(lambda: self.set_table())
        self.ui.replaceValue_comboBox.activated.connect(lambda: self.set_table())
        self.ui.extraBall_comboBox.activated.connect(lambda: self.set_table())
        self.ui.CNC_checkBox.clicked.connect(lambda: self.set_table())
        self.ui.CNC_checkBox.clicked.connect(lambda: self.check_buttonGroup(self.ui.CNC_checkBox.isChecked(), self.ui.CNC_buttonGroup))
        self.ui.characteristic_checkBox.clicked.connect(lambda: self.set_table())
        self.ui.characteristic_checkBox.clicked.connect(lambda: self.check_buttonGroup(self.ui.characteristic_checkBox.isChecked(), self.ui.characteristic_buttonGroup))
        self.ui.tolerance_checkBox.clicked.connect(lambda: self.set_table())
        self.ui.tolerance_checkBox.clicked.connect(lambda: self.check_buttonGroup(self.ui.tolerance_checkBox.isChecked(), self.ui.toleranceType_buttonGroup))
        self.ui.unit_checkBox.clicked.connect(lambda: self.set_table())
        self.ui.Phi_checkBox.clicked.connect(lambda: self.set_table())
        self.ui.characteristic_buttonGroup.buttonClicked.connect(lambda: self.set_table())
        self.ui.CNC_buttonGroup.buttonClicked.connect(lambda: self.set_table())
        self.ui.toleranceType_buttonGroup.buttonClicked.connect(lambda: self.set_table())
        self.ui.lastTable_pushButton.clicked.connect(lambda: self.gotoTable(self.ui.tableListChoose_comboBox.currentIndex() - 1))
        self.ui.nextTable_pushButton.clicked.connect(lambda: self.gotoTable(self.ui.tableListChoose_comboBox.currentIndex() + 1))
        self.ui.replaceValue_comboBox.activated.connect(self.check_extraBall_comboBox)
        self.ui.extraBall_comboBox.activated.connect(self.check_replaceValue_comboBox)
        self.ui.exportPresentTable_pushButton.clicked.connect(self.export_table)
        self.ui.exportAllTable_pushButton.clicked.connect(self.export_mutiple_tables)       


        self.ui.infoCharacteristic_checkBox.clicked.connect(lambda: self.check_buttonGroup(self.ui.infoCharacteristic_checkBox.isChecked(), self.ui.infoCharacteristic_buttonGroup))
        self.ui.infoCNC_checkBox.clicked.connect(lambda: self.check_buttonGroup(self.ui.infoCNC_checkBox.isChecked(), self.ui.infoCNC_buttonGroup))
        self.ui.infoInput_plainTextEdit.textChanged.connect(self.set_info_table)
        self.ui.infoSeperate_lineEdit.textChanged.connect(self.set_info_table)
        self.ui.infoDescription_comboBox.activated.connect(self.set_info_table)
        self.ui.infoMeasurement_comboBox.activated.connect(self.set_info_table)
        self.ui.infoCharacteristic_checkBox.clicked.connect(self.set_info_table)
        self.ui.infoCNC_checkBox.clicked.connect(self.set_info_table)
        self.ui.infoCharacteristic_buttonGroup.buttonClicked.connect(self.set_info_table)
        self.ui.infoCNC_buttonGroup.buttonClicked.connect(self.set_info_table)
        self.ui.infoShowExtratBall_checkBox.clicked.connect(self.set_info_table)
        self.ui.infoExport_pushButton.clicked.connect(self.export_info_table)
        
        

    def open_file(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "選擇檔案",
            "",
            "SOLIDWORKS Drawing Document (*.SLDDRW);;All Files (*)"
        )
        self.process_file(file_paths)

    def on_files_dropped(self, file_paths):
        self.process_file(file_paths)

    def process_file(self, file_paths):
        if file_paths:
            if self.ui.fileChooseMode_buttonGroup.checkedButton()==self.ui.fileChooseModeRefresh_radioButton:
                self.clear_table()

            try:
                tool.run_with_waiting(self.extract_BallNo, file_paths, parent=self)
                if self.check_table_enable():
                    tool.add_items(self.ui.tableListChoose_comboBox, self.table_combobox_items)
                    self.set_table_lable()
                    self.set_table()
            except Exception as e:
                self.handle_error(repr(e))


    def extract_BallNo(self,file_paths):
        try: 
            progids = tool.get_all_solidworks_version()
            if len(progids) == 0:
                raise RuntimeError(NO_SLDWORKS_ERROR)
            sw = None
            num_id = None
            progid = None
            for id, pid in progids:
                try:
                    sw = tool.open_Sldworks(pid)
                    num_id = id
                    progid = pid
                    break
                except:
                    self.error_signal.emit(SLDWORKS_OPEN_ERROR_WITH_VERSION.format(str(int(num_id)+SLDWORKS_PROGID_TO_CE_DIFFERENC)), DEFAULT_WARNING_TYPE)
                    pass
            if sw is None:
                raise RuntimeError(ALL_SLDWORKS_FAIL_ERROR)
            if num_id < SLDWORKS_2025_PROGID:
                self.error_signal.emit(SLDWORKS_VERSION_LOWER_THAN_2025_WARNING.format(str(int(num_id)+SLDWORKS_PROGID_TO_CE_DIFFERENC)), DEFAULT_WARNING_TYPE)
            self.sw_app = sw
            self.sw_app.Visible = False       #是否可視化
            for file in file_paths:
                if file.lower().endswith(".slddrw"):
                    file = os.path.abspath(file)
                    if not os.path.exists(file):
                        self.error_signal.emit(FILE_NOT_FOUND_ERROR.format(file), DEFAULT_ERROR_TYPE)
                        continue
                    data = tool.get_BallNo(self.sw_app, file, self.error_signal)
                    if data is None:
                        self.sw_app = tool.reopen_Sldworks(self.sw_app, progid)
                        continue

                    if len(data.extraBallNo_list) > 0:
                        self.error_signal.emit(EXTRA_BALLNO_WARNING.format(file, ', '.join(sorted(data.extraBallNo_list, key=tool.split_value))), EXTRA_BALLNO_WARNING_TYPE)

                    self.add_table(data)

                    time.sleep(0.7)
        except:
            raise
        finally:
            tool.close_Sldworks(self.sw_app)
            self.sw_app = None

    def delete_present_table(self):
        if tool.show_double_check_box(self):
            self.pop_table()
            self.set_table_lable()
            self.set_table()
            self.check_table_enable()

    def delete_all_table(self):
        if tool.show_double_check_box(self):
            self.clear_table()
            self.check_table_enable()
    
    def check_buttonGroup(self, enable: bool, buttonGroup):
        for but in buttonGroup.buttons():
            but.setEnabled(enable)

    def check_extraBall_comboBox(self):
        if (self.ui.replaceValue_comboBox.currentData() == REPLACE_VALUE_ONLY_USE) or (self.ui.replaceValue_comboBox.currentData() == REPLACE_VALUE_ONLY_UNUSE):
            self.ui.extraBall_comboBox.setEnabled(False)
        else:
            self.ui.extraBall_comboBox.setEnabled(True)

    def check_replaceValue_comboBox(self):
        if self.ui.extraBall_comboBox.currentData() == EXTRA_BALL_ONLY:
            self.ui.replaceValue_comboBox.setEnabled(False)
        else:
            self.ui.replaceValue_comboBox.setEnabled(True)

    def gotoTable(self, tableIndex: int):
        if (tableIndex >= 0) and (tableIndex < len(self.table_list)):
            self.ui.tableListChoose_comboBox.setCurrentIndex(tableIndex)
            self.set_table_lable()
            self.set_table()
        

    def handle_error(self, message, *args):
        # 處理錯誤並顯示錯誤框
        if args:
            if args[0] == DEFAULT_ERROR_TYPE:
                tool.show_error_box(self, message=message)
            elif args[0] == DEFAULT_WARNING_TYPE:
                tool.show_error_box(self, title=WARNING_TITLE, message=message)
            elif args[0] == REPLACE_VALUE_WARNING_TYPE:
                if self.ui.replaceValueWarning_checkBox.isChecked():
                     tool.show_error_box(self, title=WARNING_TITLE, message=message)
            elif args[0] == EXTRA_BALLNO_WARNING_TYPE:
                if self.ui.exrtraBallNoWarning_checkBox.isChecked():
                     tool.show_error_box(self, title=WARNING_TITLE, message=message)
        else:
            tool.show_error_box(self, message=message)


    def check_table_enable(self):
        if len(self.table_list) == 0:
            self.ui.tableListChoose_comboBox.setEnabled(False)
            self.ui.deletePresentTable_pushButton.setEnabled(False)
            self.ui.deleteAllTable_pushButton.setEnabled(False)
            self.ui.lastTable_pushButton.setEnabled(False)
            self.ui.nextTable_pushButton.setEnabled(False)
            self.ui.exportPresentTable_pushButton.setEnabled(False)
            self.ui.exportAllTable_pushButton.setEnabled(False)

            self.ui.tableListChoose_comboBox.clear()
            self.ui.tableList_label.setText("請先選擇檔案")
            if self.model is not None:
                self.model.clear()
                self.model = None
            return False
        else:
            self.ui.tableListChoose_comboBox.setEnabled(True)
            self.ui.deletePresentTable_pushButton.setEnabled(True)
            self.ui.deleteAllTable_pushButton.setEnabled(True)
            self.ui.lastTable_pushButton.setEnabled(True)
            self.ui.nextTable_pushButton.setEnabled(True)
            self.ui.exportPresentTable_pushButton.setEnabled(True)
            self.ui.exportAllTable_pushButton.setEnabled(True)

            return True
        
    def set_table_lable(self):
        if self.ui.tableListChoose_comboBox.currentIndex() == -1:
            self.ui.tableListChoose_comboBox.setCurrentIndex(0)         
        self.ui.tableList_label.setText(self.ui.tableListChoose_comboBox.currentText())

    def add_table(self, table: tool.Table_Object):
        self.table_list.append(table)
        self.table_combobox_items.append((table.file_path, None))
        self.ui.fileDrag_plainTextEdit.appendPlainText(table.file_path)
    
    def clear_table(self):
        self.table_list.clear()
        self.table_combobox_items.clear()
        self.ui.fileDrag_plainTextEdit.clear()
        self.ui.tableListChoose_comboBox.clear()

    def pop_table(self):
        index = self.ui.tableListChoose_comboBox.currentIndex()
        self.table_list.pop(index)
        tool.pop_line(self.ui.fileDrag_plainTextEdit, index)
        self.table_combobox_items.pop(index)
        self.ui.tableListChoose_comboBox.removeItem(index)
    
    def export_table(self):
        file_name = self.ui.tableListChoose_comboBox.currentText()
        file_name = os.path.basename(file_name)
        file_name = os.path.splitext(file_name)[0]
        file_name += ".xlsx"
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "儲存檔案",
            file_name,
            "Excel Files (*.xlsx);;All Files (*)"
        )
        
        if file_path:
            try:
                rows = self.model.rowCount()
                cols = self.model.columnCount()
                data = []
                header = []

                for c in range(cols):
                    header.append(self.model.headerData(c, Qt.Horizontal))

                for r in range(rows):
                    row_data = []
                    for c in range(cols):
                        index = self.model.index(r, c)
                        row_data.append(index.data())
                    data.append(row_data)
                data = sorted(data, key=lambda row: tool.split_value(row[0]))
                data.insert(0, header)
                tool.save_to_excel(data, file_path)
            except PermissionError:
                self.handle_error(FILE_PERMISSION_ERROR.format(file_path))
            except FileCreateError:
                self.handle_error(FILE_PERMISSION_ERROR.format(file_path))
            except:
                self.handle_error(FILE_SAVE_ERROR)

    def export_mutiple_tables(self):
        file_name = "球號工作表.xlsx"
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "儲存檔案",
            file_name,
            "Excel Files (*.xlsx);;All Files (*)"
        )

        
        if file_path:
            try:
                sheet_data = [] # (sheet, data)
                for i in range(len(self.table_list)):
                    self.set_table_signal.emit(i)
                    rows = self.model.rowCount()
                    cols = self.model.columnCount()
                    data = []
                    header = []

                    for c in range(cols):
                        header.append(self.model.headerData(c, Qt.Horizontal))

                    for r in range(rows):
                        row_data = []
                        for c in range(cols):
                            index = self.model.index(r, c)
                            row_data.append(index.data())
                        data.append(row_data)
                    data = sorted(data, key=lambda row: tool.split_value(row[0]))
                    data.insert(0, header)

                    f = self.table_list[i].file_path
                    f = os.path.basename(f)
                    f = os.path.splitext(f)[0]
                    sheet_data.append((f, data))

                tool.save_to_multiple_sheet_excel(sheet_data, file_path)
            except PermissionError:
                self.handle_error(FILE_PERMISSION_ERROR.format(file_path))
            except FileCreateError:
                self.handle_error(FILE_PERMISSION_ERROR.format(file_path))
            except:
                self.handle_error(FILE_SAVE_ERROR)
            finally:
                self.set_table()
                
    def export_info_table(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "儲存檔案",
            "球號對照表.xlsx",
            "Excel Files (*.xlsx);;All Files (*)"
        )
        
        if file_path:
            try:
                rows = self.info_model.rowCount()
                cols = self.info_model.columnCount()
                data = []
                header = []

                for c in range(cols):
                    header.append(self.info_model.headerData(c, Qt.Horizontal))

                for r in range(rows):
                    row_data = []
                    for c in range(cols):
                        index = self.info_model.index(r, c)
                        row_data.append(index.data())
                    data.append(row_data)
                data = sorted(data, key=lambda row: tool.split_value(row[0]))
                data.insert(0, header)
                tool.save_to_excel(data, file_path)
            except PermissionError:
                self.handle_error(FILE_PERMISSION_ERROR.format(file_path))
            except FileCreateError:
                self.handle_error(FILE_PERMISSION_ERROR.format(file_path))
            except Exception as e:
                self.handle_error(FILE_SAVE_ERROR)

    def get_tableKeys(self):
        table_keys = []
        for i in TABLE_KEYS:
            if i == TABLE_DESCRIPTION:
                desc_type = self.ui.description_comboBox.currentData()
                if desc_type is None:
                    continue
            elif i == TABLE_MEASUREMENT:
                meas_type = self.ui.measurement_comboBox.currentData()
                if meas_type is None:
                    continue
            elif i == TABLE_TOLERANCE:
                if not self.ui.tolerance_checkBox.isChecked():
                    continue
            elif i == TABLE_CHARACTERISTIC:
                if not self.ui.characteristic_checkBox.isChecked():
                    continue
            elif i == TABLE_CNC:
                if not self.ui.CNC_checkBox.isChecked():
                    continue

            table_keys.append(i)

        return table_keys
    
    def get_ballNoList(self, current):
        ballNos_orgin = [] # (index, ballNo, isExtra)
        for i, n in enumerate(current.ballNo_list):
            ballNos_orgin.append((i, n, False))
        for i, n in enumerate(current.extraBallNo_list):
            ballNos_orgin.append((i, n, True))
    
        remove_check = []
        for index, ballNo, isExtra in ballNos_orgin:
            if self.ui.extraBall_comboBox.currentData() == EXTRA_BALL_UNUSE:
                if isExtra:
                    remove_check.append(True)
                    continue
            elif self.ui.extraBall_comboBox.currentData() == EXTRA_BALL_ONLY:
                if not isExtra:
                    remove_check.append(True)
                    continue
            
            if self.ui.characteristic_checkBox.isChecked():
                spec = ""
                if isExtra:
                    spec = current.extra_characteristic_list[index]
                else:
                    spec = current.characteristic_list[index]
                if self.ui.characteristic_buttonGroup.checkedButton() == self.ui.characteristicSC_radioButton:
                    if spec != CHARACTERISTIC_SC:
                        remove_check.append(True)
                        continue
                elif self.ui.characteristic_buttonGroup.checkedButton() == self.ui.characteristicCC_radioButton:
                    if spec != CHARACTERISTIC_CC:
                        remove_check.append(True)
                        continue
                elif self.ui.characteristic_buttonGroup.checkedButton() == self.ui.characteristicOther_radioButton:
                    if (spec == CHARACTERISTIC_SC) or (spec == CHARACTERISTIC_CC):
                        remove_check.append(True)
                        continue

            if self.ui.CNC_checkBox.isChecked():
                cnc = ""
                if isExtra:
                    cnc = current.extra_cnc_list[index]
                else:
                    cnc = current.cnc_list[index]
                if self.ui.CNC_buttonGroup.checkedButton() == self.ui.CNC_Turning_radioButton:
                    if cnc != CNC_TURNING:
                        remove_check.append(True)
                        continue
                elif self.ui.CNC_buttonGroup.checkedButton() == self.ui.CNC_Milling_radioButton:
                    if cnc != CNC_MILLING:
                        remove_check.append(True)
                        continue

            if self.ui.replaceValue_comboBox.currentData() == REPLACE_VALUE_DONT_SHOW:
                if not isExtra:
                    temp_check = False
                    for j in current.replaceValueCheck_list:
                        if j[0] == index:
                            temp_check = True
                            continue
                    if temp_check:
                        remove_check.append(True)
                        continue
            elif (self.ui.replaceValue_comboBox.currentData() == REPLACE_VALUE_ONLY_USE) or (self.ui.replaceValue_comboBox.currentData() == REPLACE_VALUE_ONLY_UNUSE):
                if not isExtra:
                    temp_check = True
                    for j in current.replaceValueCheck_list:
                        if j[0] == index:
                            temp_check = False
                    if temp_check:
                        remove_check.append(True)
                        continue
                else:
                    remove_check.append(True)
                    continue

            remove_check.append(False)
            
        ballNos = []
        for i, r in enumerate(remove_check):
            if not r:
                ballNos.append(ballNos_orgin[i])
        return ballNos

    def set_table(self, index=None):
        if len(self.table_list) == 0:
            return
        try:
            self.model = QStandardItemModel()
            table_keys = self.get_tableKeys()
            self.model.setHorizontalHeaderLabels(table_keys)
            if index is None:
                index = self.ui.tableListChoose_comboBox.currentIndex()
            current = self.table_list[index]
            ballNos = self.get_ballNoList(current) # (index, ballNo, isExtra)

            for row, ball_item in enumerate(ballNos):
                index = ball_item[0]
                isExtra = ball_item[2]
                ballNo = ball_item[1]
                for col, key in enumerate(table_keys):
                    if key == TABLE_BALLNO:
                        self.model.setItem(row, col, QStandardItem(str(ballNo)))
                    elif key == TABLE_DESCRIPTION:
                        desc_type = self.ui.description_comboBox.currentData()
                        descList_dict = None
                        if isExtra:
                            descList_dict = current.extra_desciptionList_dict.get(desc_type)
                        else:
                            descList_dict = current.desciptionList_dict.get(desc_type)
                        if descList_dict is not None:
                            self.model.setItem(row, col, QStandardItem(str(descList_dict[index])))
                    elif key == TABLE_MEASUREMENT:
                        meas_type = self.ui.measurement_comboBox.currentData()
                        measList_dict = None
                        if isExtra:
                            measList_dict = current.extra_measurementList_dict.get(meas_type)
                        else:
                            measList_dict = current.measurementList_dict.get(meas_type)
                        if measList_dict is not None:
                            self.model.setItem(row, col, QStandardItem(str(measList_dict[index])))
                    elif key == TABLE_STANDARDVALUE:
                        if isExtra:
                            self.model.setItem(row, col, QStandardItem(""))
                        else:
                            val = current.standardValue_list[index]
                            if (self.ui.replaceValue_comboBox.currentData() == REPLACE_VALUE_USE) or (self.ui.replaceValue_comboBox.currentData() == REPLACE_VALUE_ONLY_USE):
                                for i in current.replaceValueCheck_list:
                                    if i[0] == index:
                                        val = i[1]
                            val = tool.cm_to_mm(val)
                            if current.hasPhi_list[index] and self.ui.Phi_checkBox.isChecked():
                                val = PHI + val
                            if self.ui.unit_checkBox.isChecked():
                                val += UNIT_MM
                            self.model.setItem(row, col, QStandardItem(str(val)))
                    elif key == TABLE_LOWERBOUND:
                        if isExtra:
                            self.model.setItem(row, col, QStandardItem(""))
                        else:
                            val = current.standardValue_list[index]
                            if (self.ui.replaceValue_comboBox.currentData() == REPLACE_VALUE_USE) or (self.ui.replaceValue_comboBox.currentData() == REPLACE_VALUE_ONLY_USE):
                                for i in current.replaceValueCheck_list:
                                    if i[0] == index:
                                        val = i[1]
                            lower = current.toleranceValueTuple_list[index][0] + val
                            lower = tool.cm_to_mm(lower)
                            if current.hasPhi_list[index] and self.ui.Phi_checkBox.isChecked():
                                lower = PHI + lower
                            if self.ui.unit_checkBox.isChecked():
                                lower += UNIT_MM
                            self.model.setItem(row, col, QStandardItem(str(lower)))
                    elif key == TABLE_UPPERBOUND:
                        if isExtra:
                            self.model.setItem(row, col, QStandardItem(""))
                        else:
                            val = current.standardValue_list[index]
                            if (self.ui.replaceValue_comboBox.currentData() == REPLACE_VALUE_USE) or (self.ui.replaceValue_comboBox.currentData() == REPLACE_VALUE_ONLY_USE):
                                for i in current.replaceValueCheck_list:
                                    if i[0] == index:
                                        val = i[1]
                            upper = current.toleranceValueTuple_list[index][1] + val
                            upper = tool.cm_to_mm(upper)
                            if current.hasPhi_list[index] and self.ui.Phi_checkBox.isChecked():
                                upper = PHI + upper
                            if self.ui.unit_checkBox.isChecked():
                                upper += UNIT_MM
                            self.model.setItem(row, col, QStandardItem(str(upper)))
                    elif key == TABLE_TOLERANCE:
                        if isExtra:
                            self.model.setItem(row, col, QStandardItem(""))
                        else:
                            tol_type = current.toleranceType_list[index]
                            up = current.toleranceValueTuple_list[index][1]
                            low = current.toleranceValueTuple_list[index][0]
                            v = current.standardValue_list[index]
                            if (self.ui.replaceValue_comboBox.currentData() == REPLACE_VALUE_USE) or (self.ui.replaceValue_comboBox.currentData() == REPLACE_VALUE_ONLY_USE):
                                for i in current.replaceValueCheck_list:
                                    if i[0] == index:
                                        v = i[1]
        
                            tol = ""
                            if self.ui.toleranceType_buttonGroup.checkedButton()==self.ui.toleranceTypeSymmetric_radioButton:
                                if tol_type == SWTOLSYMMETRIC:
                                    up = tool.cm_to_mm(up)
                                    low = tool.cm_to_mm(low)
                                    v = tool.cm_to_mm(v)
                                    if current.hasPhi_list[index] and self.ui.Phi_checkBox.isChecked():
                                        v = PHI + v
                                    if float(up) < 0:
                                        up = str(float(up)*-1)
                                    tol = TOLERANCE_SYMMETRIC_STRING.format(v, up)
                                else:
                                    up = up - low
                                    up /= 2
                                    v = v + low
                                    v += up
                                    up = tool.cm_to_mm(up)
                                    low = tool.cm_to_mm(low)
                                    v = tool.cm_to_mm(v)
                                    if current.hasPhi_list[index] and self.ui.Phi_checkBox.isChecked():
                                        v = PHI + v
                                    if float(up) < 0:
                                        up = str(float(up)*-1)
                                    tol = TOLERANCE_SYMMETRIC_STRING.format(v, up)

                            elif self.ui.toleranceType_buttonGroup.checkedButton()==self.ui.toleranceTypeBi_radioButton:
                                up = tool.cm_to_mm(up)
                                low = tool.cm_to_mm(low)
                                v = tool.cm_to_mm(v)
                                if current.hasPhi_list[index] and self.ui.Phi_checkBox.isChecked():
                                    v = PHI + v
                                if float(up) >= 0:
                                    up = "+" + up
                                if float(low) == 0:
                                    if math.copysign(1, float(low))==1:
                                        low = "-" + low
                                elif float(low) > 0:
                                    low = "+" + low
                                tol = TOLERANCE_BILAT_STRING.format(v, up, low)
                            else:
                                up = tool.cm_to_mm(up)
                                low = tool.cm_to_mm(low)
                                v = tool.cm_to_mm(v)
                                if current.hasPhi_list[index] and self.ui.Phi_checkBox.isChecked():
                                    v = PHI + v
                                if tol_type == SWTOLSYMMETRIC:
                                    if float(up) < 0:
                                        up = str(float(up)*-1)
                                    tol = TOLERANCE_SYMMETRIC_STRING.format(v, up)
                                elif tol_type == SWTOLBILAT:
                                    if float(up) >= 0:
                                        up = "+" + up
                                    if float(low) == 0:
                                        if math.copysign(1, float(low))==1:
                                            low = "-" + low
                                    elif float(low) > 0:
                                        low = "+" + low
                                    tol = TOLERANCE_BILAT_STRING.format(v, up, low)
                                else:
                                    tol = v
                            if self.ui.unit_checkBox.isChecked():
                                tol += UNIT_MM
                            self.model.setItem(row, col, QStandardItem(str(tol)))
                    elif key == TABLE_CHARACTERISTIC:
                        spec = ""
                        if isExtra:
                            spec = current.extra_characteristic_list[index]
                        else:
                            spec = current.characteristic_list[index]
                        self.model.setItem(row, col, QStandardItem(str(spec)))
                    elif key == TABLE_CNC:
                        cnc = ""
                        if isExtra:
                            cnc = current.extra_cnc_list[index]
                        else:
                            cnc = current.cnc_list[index]
                        self.model.setItem(row, col, QStandardItem(str(cnc)))


            proxy =  tool.MySortProxy(sortable_columns=[0])
            proxy.setSourceModel(self.model)
            self.ui.ballNoTable_tableView.setModel(proxy)
            self.ui.ballNoTable_tableView.sortByColumn(0, Qt.AscendingOrder)
            self.ui.ballNoTable_tableView.resize_all()

        except Exception as e:
            self.handle_error(repr(e))

    def get_infoKeys(self):
        info_keys = []
        for i in INFO_KEYS:
            if i == TABLE_DESCRIPTION:
                desc_type = self.ui.infoDescription_comboBox.currentData()
                if desc_type is None:
                    continue
            elif i == TABLE_MEASUREMENT:
                meas_type = self.ui.infoMeasurement_comboBox.currentData()
                if meas_type is None:
                    continue
            elif i == TABLE_CHARACTERISTIC:
                if not self.ui.infoCharacteristic_checkBox.isChecked():
                    continue
            elif i == TABLE_CNC:
                if not self.ui.infoCNC_checkBox.isChecked():
                    continue
            info_keys.append(i)
        return info_keys
    
    def get_info_list(self):
        info_list = self.ui.infoInput_plainTextEdit.toPlainText()
        if self.ui.infoSeperate_lineEdit.text() == "":
            info_list = info_list.split()
        else:
            info_list = info_list.split(self.ui.infoSeperate_lineEdit.text())
        
        if len(info_list) == 0:
            info_list = list(BALLNO_TABLE.keys())
    
        remove_check = []
        for info in info_list:
            item = BALLNO_TABLE.get(info, None)
            if item is None:
                if self.ui.infoShowExtratBall_checkBox.isChecked():
                    remove_check.append(False)
                else:
                    remove_check.append(True)
                continue
            if self.ui.infoCharacteristic_checkBox.isChecked():
                spec = item.get(CHARACTERISTIC_KEY, "")
                if self.ui.infoCharacteristic_buttonGroup.checkedButton() == self.ui.infoCharacteristicSC_radioButton:
                    if spec != CHARACTERISTIC_SC:
                        remove_check.append(True)
                        continue
                elif self.ui.infoCharacteristic_buttonGroup.checkedButton() == self.ui.infoCharacteristicCC_radioButton:
                    if spec != CHARACTERISTIC_CC:
                        remove_check.append(True)
                        continue
                elif self.ui.infoCharacteristic_buttonGroup.checkedButton() == self.ui.infoCharacteristicOther_radioButton:
                    if (spec == CHARACTERISTIC_SC) or (spec == CHARACTERISTIC_CC):
                        remove_check.append(True)
                        continue

            if self.ui.infoCNC_checkBox.isChecked():
                cnc = item.get(CNC_KEY, "")
                if self.ui.infoCNC_buttonGroup.checkedButton() == self.ui.infoCNC_Turning_radioButton:
                    if cnc != CNC_TURNING:
                        remove_check.append(True)
                        continue
                elif self.ui.infoCNC_buttonGroup.checkedButton() == self.ui.infoCNC_Milling_radioButton:
                    if cnc != CNC_MILLING:
                        remove_check.append(True)
                        continue

            remove_check.append(False)
            
        infos = []
        for i, r in enumerate(remove_check):
            if not r:
                infos.append(info_list[i])
        return infos
    
    def set_info_table(self):
        try:
            self.info_model = QStandardItemModel()
            info_keys = self.get_infoKeys()
            self.info_model.setHorizontalHeaderLabels(info_keys)
            info_list = self.get_info_list() # ballno

            for row, info in enumerate(info_list):
                item = BALLNO_TABLE.get(info, None)
                for col, key in enumerate(info_keys):
                    if key == TABLE_BALLNO:
                        self.info_model.setItem(row, col, QStandardItem(str(info)))
                    elif key == TABLE_DESCRIPTION:
                        desc = ""
                        if item is not None:
                            desc_type = self.ui.infoDescription_comboBox.currentData()
                            desc = item.get(desc_type, "")
                        self.info_model.setItem(row, col, QStandardItem(str(desc)))
                    elif key == TABLE_MEASUREMENT:
                        meas = ""
                        if item is not None:
                            meas_type = self.ui.infoMeasurement_comboBox.currentData()
                            meas = item.get(meas_type, "")
                        self.info_model.setItem(row, col, QStandardItem(str(meas)))
                    elif key == TABLE_CHARACTERISTIC:
                        spec = ""
                        if item is not None:
                            spec = item.get(CHARACTERISTIC_KEY, "")
                        self.info_model.setItem(row, col, QStandardItem(str(spec)))
                    elif key == TABLE_CNC:
                        cnc = ""
                        if item is not None:
                            cnc = item.get(CNC_KEY, "")
                        self.info_model.setItem(row, col, QStandardItem(str(cnc)))


            proxy =  tool.MySortProxy(sortable_columns=[0])
            proxy.setSourceModel(self.info_model)
            self.ui.info_tableView.setModel(proxy)
            self.ui.info_tableView.sortByColumn(0, Qt.AscendingOrder)
            self.ui.info_tableView.resize_all()
        except Exception as e:
            self.handle_error(repr(e))

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.setWindowIcon(QIcon(ICON_PATH))
    window.show()
    # initial_check
    if tool.check_solidworks_is_running():
        window.handle_error(SLDWORKS_OPENING_WARNING, DEFAULT_WARNING_TYPE)
    app.exec()
    