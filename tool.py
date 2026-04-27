from constant import *
from PySide6.QtWidgets import QPlainTextEdit, QMessageBox, QDialog, QLabel, QVBoxLayout, QApplication, QHeaderView, QTableView, QMenu
from PySide6.QtCore import Signal, Qt, QThread, QObject, QSortFilterProxyModel, QItemSelectionModel, QItemSelection
from PySide6.QtGui import QDropEvent, QDragEnterEvent, QMovie, QTextCursor, QKeySequence, QAction
import win32com.client
import pythoncom
from decimal import Decimal
import xlsxwriter
import winreg
import re



def add_items(combo, items):
    """
    add items into combobox
    """
    combo.clear()
    for text, value in items:
        combo.addItem(text, value)


def pop_line(plainTextEdit, index):
    doc = plainTextEdit.document()
    block = doc.findBlockByNumber(index)

    if not block.isValid():
        return  # index 超出範圍

    cursor = QTextCursor(block)
    cursor.select(QTextCursor.BlockUnderCursor)
    cursor.removeSelectedText()
    cursor.deleteChar()  # 刪掉殘留的換行

class FileDropPlainTextEdit(QPlainTextEdit):
    fileDropped = Signal(list)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.setAcceptDrops(True)


    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            file_paths = [url.toLocalFile() for url in event.mimeData().urls()]
            self.fileDropped.emit(file_paths)

        else:
            event.ignore()
    # 沒這個dropEvent不會觸發
    def dragMoveEvent(self, event):
        event.acceptProposedAction()

class CopyableTableView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSelectionBehavior(QTableView.SelectItems)
        self.setSelectionMode(QTableView.ExtendedSelection)

        # 啟用右鍵選單
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.open_menu)

        self.setSortingEnabled(True)

    def keyPressEvent(self, event):
        # 捕捉 Ctrl+C
        if event.matches(QKeySequence.Copy):
            self.copy_selection()
        else:
            super().keyPressEvent(event)

    def open_menu(self, pos):
        index = self.indexAt(pos)
        if not index.isValid():
            return
        menu = QMenu(self)
        copy_action = QAction("複製", self)
        copy_action.triggered.connect(self.copy_selection)
        menu.addAction(copy_action)
        menu.exec(self.viewport().mapToGlobal(pos))

    def copy_selection(self):
        indexes = self.selectedIndexes()
        if not indexes:
            return

        # 依行排序
        indexes.sort(key=lambda x: (x.row(), x.column()))

        current_row = indexes[0].row()
        rows_text = []
        row_data = []

        for idx in indexes:
            if idx.row() != current_row:
                rows_text.append('\t'.join(row_data))
                row_data = []
                current_row = idx.row()
            row_data.append(str(idx.data()))

        rows_text.append('\t'.join(row_data))  # 加上最後一行

        clipboard_text = '\n'.join(rows_text)
        QApplication.clipboard().setText(clipboard_text)
        # print("已複製到剪貼簿:\n", clipboard_text)
    
    def on_header_clicked(self, logicalIndex):
        modifiers = QApplication.keyboardModifiers()
        selection_model = self.selectionModel()
        if selection_model is None:
            return

        if modifiers & Qt.ControlModifier:
            # Ctrl: 切換選取
            selection_model.select(
                self.model().index(0, logicalIndex),
                QItemSelectionModel.Columns | QItemSelectionModel.Toggle
            )
        elif modifiers & Qt.ShiftModifier:
             # Shift: 延伸選取
            current_index = selection_model.currentIndex()
            start_col = current_index.column() if current_index.isValid() else 0
            end_col = logicalIndex

            # 保證 start <= end
            if start_col > end_col:
                start_col, end_col = end_col, start_col

            # 建立 selection 範圍
            selection = QItemSelection(
                self.model().index(0, start_col),
                self.model().index(self.model().rowCount() - 1, end_col)
            )
            selection_model.select(selection, QItemSelectionModel.Columns | QItemSelectionModel.Select)
        else:
            # 單擊: 單欄選取
            self.selectColumn(logicalIndex)

    def resize_all(self):
        self.resizeRowsToContents() # 高度包住所有文字

        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # 自動調整欄寬
        self.horizontalHeader().sectionClicked.connect(self.on_header_clicked)

        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

class MySortProxy(QSortFilterProxyModel):
    def __init__(self, sortable_columns=None):
        super().__init__()
        if sortable_columns is None:
            sortable_columns = []
        self.sortable_columns = sortable_columns  # 可排序欄位索引

    def lessThan(self, left, right):
        col = left.column()
        if col not in self.sortable_columns:
            return False # 其他欄不能sort
            # return left.row() < right.row() # 其他欄可以sort

        l = self.sourceModel().item(left.row(), left.column()).text()
        r = self.sourceModel().item(right.row(), right.column()).text()

        try:
            l_num, l_suffix = split_value(l)
            r_num, r_suffix = split_value(r)
            if l_num != r_num:
                return l_num < r_num
            return l_suffix < r_suffix
        except (ValueError, TypeError):
            l = str(l)
            r = str(r)
            return l < r
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Vertical and role == Qt.DisplayRole: # 顯示排序後的 row number
            return str(section + 1)
        return super().headerData(section, orientation, role)

# 用正則把字串拆成數字和字母部分
def split_value(val):
    match = re.match(r'(\d+)(.*)', str(val))
    if match:
        num = float(match.group(1))
        suffix = match.group(2)
        return num, suffix
    else:
        return float('inf'), str(val) # 沒有數字的放最後

def show_error_box(parent, title: str="錯誤", message: str="未預期的錯誤"):
    # parent->self
    msg = QMessageBox(parent)
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle(title)
    msg.setTextFormat(Qt.RichText)
    html = message.replace("\n", "<br>")
    html = "<div align='center'>" + html + "</div>"
    msg.setText(html)
    msg.exec()

# ----- 工作者類別，用來執行耗時任務 -----
class Worker(QObject):
    finished = Signal()
    show_error = Signal(str)      # 用來觸發主線程顯示錯誤框
    
    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            # 嘗試執行傳入的函式
            self.func(*self.args, **self.kwargs)
        except Exception as e:
            # 捕獲異常並傳遞回主線程
            self.show_error.emit(repr(e))
        finally:
            # 發送 finished 信號表示工作完成
            self.finished.emit()

# ----- 等待視窗類別 -----
class WaitingDialog(QDialog):
    def __init__(self, text="請稍候...", parent=None):
        super().__init__(parent)
        self.setWindowTitle(text)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)  # 禁用 X 按鈕
        self.setModal(True)
        
        layout = QVBoxLayout()
        self.label = QLabel(text)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # 可選：GIF 動畫
        self.movie = QMovie(LOADING_GIF_PATH)  # 替換成你的 GIF
        if self.movie.isValid():
            self.label.setMovie(self.movie)
            self.movie.start()
        
        self.setLayout(layout)
        self.resize(200, 100)

        # 在 QMovie 結束時手動清理資源
        self.movie.finished.connect(self.on_movie_finished)

    def on_movie_finished(self):
        # 做清理工作，避免資源泄漏
        self.movie.stop()

# ----- 簡單封裝等待視窗函數 -----
def run_with_waiting(func, *args, parent=None, **kwargs):
    # 確保函式傳入正確
    if not callable(func):
        raise ValueError(f"傳入的參數不是有效的函式: {func}")
    
    dialog = WaitingDialog(parent=parent)
    thread = QThread()
    worker = Worker(func, *args, **kwargs)
    worker.moveToThread(thread)

    thread.started.connect(worker.run)
    worker.finished.connect(dialog.accept)
    worker.finished.connect(thread.quit)
    worker.finished.connect(worker.deleteLater)
    thread.finished.connect(thread.deleteLater)

    # 當捕獲到錯誤時，顯示錯誤框
    worker.show_error.connect(parent.handle_error)  # 這裡將錯誤信號連接到主線程的錯誤處理方法

    dialog.finished.connect(lambda: thread.quit())
    dialog.finished.connect(lambda: thread.wait()) # 等待 thread 結束
    dialog.finished.connect(lambda: thread.deleteLater())

    dialog.show()
    thread.start()
    dialog.exec()  # 這裡會阻塞，但 UI 還是能更新



def show_double_check_box(parent=None):
    if parent:
        box = QMessageBox(parent)
    else:
        box = QMessageBox()
    box.setWindowTitle("確認")
    box.setText("是否確定要繼續？")
    box.setIcon(QMessageBox.Question)

    yes_btn = box.addButton("確定", QMessageBox.YesRole)
    no_btn = box.addButton("取消", QMessageBox.NoRole)

    box.setDefaultButton(no_btn)

    box.exec()

    if box.clickedButton() == yes_btn:
        return True
    else:
        return False

def open_Sldworks(progid=None):
    pythoncom.CoInitialize()
    if progid is None:
        progid = "Sldworks.application"
    try:
        sw_app =  win32com.client.DispatchEx(progid)   #開新的sldworks接口(不影響使用中的)
        return sw_app
    except Exception as e:
        raise Exception(SLDWORKS_OPEN_ERROR) from e


def close_Sldworks(sw_app):
    try:
        sw_app.ExitApp()
    except:
        pass
    pythoncom.CoUninitialize()

def is_sw_app_running(sw_app):
    """
    檢查 SolidWorks 是否仍在運行
    """
    try:
        # 嘗試檢查 sw_app 的狀態
        sw_app.Ping()  # 如果 sw_app 沒有關閉，這將會成功
        return True
    except Exception:
        return False

def reopen_Sldworks(sw_app, progid=None):
    try:
        sw_app.ExitApp()  # 確保退出 SolidWorks 應用程序
        while is_sw_app_running(sw_app):
            pass
    except:
        pass
    pythoncom.CoUninitialize()  # 清理 COM 服務
    pythoncom.CoInitialize()
    if progid is None:
        progid = "Sldworks.application"
    try:
        sw_app =  win32com.client.DispatchEx(progid)   #開新的sldworks接口(不影響使用中的)
        return sw_app
    except Exception as e:
        raise Exception(SLDWORKS_OPEN_ERROR) from e

class Table_Object():
    def __init__(self):
        self.file_path = ""
        # unit: cm
        self.ballNo_list = []

        self.standardValue_list = []
        self.toleranceValueTuple_list = []
        self.toleranceType_list = []
        self.replaceValueCheck_list = [] # (index, value)
        self.hasPhi_list = []

        self.characteristic_list = []
        self.cnc_list = []
        

        self.desciptionList_dict = {
            "Description_1": [],
            "Description_2": [],
            "Description_3": [],
            "Description_4": []
        }

        self.measurementList_dict = {
            "Measurement_1": [],
            "Measurement_2": [],
            "Measurement_3": [],
            "Measurement_NO": [],
        }


        self.extraBallNo_list = []
        self.extra_characteristic_list = []
        self.extra_cnc_list = []

        self.extra_desciptionList_dict = {
            "Description_1": [],
            "Description_2": [],
            "Description_3": [],
            "Description_4": []
        }

        self.extra_measurementList_dict = {
            "Measurement_1": [],
            "Measurement_2": [],
            "Measurement_3": [],
            "Measurement_NO": [],
        }

def get_BallNo(sw_app, file: str, error_signal: Signal):
    errors = win32com.client.VARIANT(
        pythoncom.VT_I4 | pythoncom.VT_BYREF, 0
    )
    warnings = win32com.client.VARIANT(
        pythoncom.VT_I4 | pythoncom.VT_BYREF, 0
    )
    try:
        model = sw_app.OpenDoc6(
            file,
            SWDOCDRAWING,
            SWOPENDOCOPTIONS_SILENT|SW_OPEN_READONLY,
            "",
            errors,
            warnings
        )
    except:
        error_signal.emit(DOC_OPEN_ERROR.format(file), DEFAULT_ERROR_TYPE)
        return

    if model is None:
        error_signal.emit(DOC_OPEN_ERROR.format(file), DEFAULT_ERROR_TYPE)
        return
    try:
        drawing = model
        # sheet = model.GetCurrentSheet
        view = drawing.GetFirstView

        Table = Table_Object()
        Table.file_path = file

        while view:
            # print("View name:", view.GetName2)
            dispDim = view.GetFirstDisplayDimension
            # print(view.GetDimensionDisplayString)

            while dispDim:

                number = None
                dispText  = None
                for i in SWDIMENSIONTEXT_TYPES:
                    try:
                        dispText = dispDim.GetText(i)
                    except:
                        continue
                    ballNo_text = BALLROLE.search(dispText)
                    if ballNo_text is not None:
                        number = str(ballNo_text.group(1))
                        break

                if number is not None:
                    if number not in BALLNO_TABLE.keys():
                        Table.extraBallNo_list.append(number)
                        dispDim = dispDim.GetNext
                        continue

                    Table.ballNo_list.append(number)
                    if PHIROLE.search(dispText) is not None:
                        Table.hasPhi_list.append(True)
                    else:
                        Table.hasPhi_list.append(False)
                    
                    dim = dispDim.GetDimension
                    val = dim.GetSystemValue2("")
                    Table.standardValue_list.append(val)

                    tol = dim.GetToleranceValues
                    tol_type = dim.GetToleranceType
                    Table.toleranceType_list.append(tol_type)

                    if tol_type == SWTOLSYMMETRIC:   # 對稱公差
                        tol = (tol[1]*-1, tol[1])
                    elif tol_type == SWTOLBILAT: # 雙向公差
                        tol = (tol[0], tol[1])
                    else:
                        tol = (0, 0)
                    Table.toleranceValueTuple_list.append(tol)

                    item = BALLNO_TABLE.get(number, None)
                    if item is not None:
                        Table.characteristic_list.append(item.get(CHARACTERISTIC_KEY, ""))
                        Table.cnc_list.append(item.get(CNC_KEY, CNC_TURNING))
                        for d in DESCRIPTION_KEY_LIST:
                            if Table.desciptionList_dict.get(d) is not None:
                                Table.desciptionList_dict.get(d).append(item.get(d, ""))
                        for m in MEASUREMENT_KEY_LIST:
                            if Table.measurementList_dict.get(m) is not None:
                                Table.measurementList_dict.get(m).append(item.get(m, ""))
                    if dispDim.GetOverride:
                        index = len(Table.ballNo_list) - 1
                        replace = dispDim.GetOverrideValue
                        Table.replaceValueCheck_list.append((index, replace))
                        error_signal.emit(REPLACE_VALUE_WARNING.format(file, number, cm_to_mm(val)+UNIT_MM, cm_to_mm(replace)+UNIT_MM), REPLACE_VALUE_WARNING_TYPE)
                dispDim = dispDim.GetNext

            
            ann = view.GetFirstAnnotation2
            while ann:
                # try:
                #     print(ann.GetSpecificAnnotation.GetText)
                # except:
                #     pass
                if ann.GetType == SWANNOTATIONTYPE_E_SWNOTE:  # swAnnotationType_e.swNote
                    note = ann.GetSpecificAnnotation
                    try:
                        noteText = note.GetText
                    except:
                        ann = ann.GetNext2
                        continue
                    ball = BALLROLE.search(noteText)
                    if ball is not None:
                        # print("註解", ball[1])
                        Table.extraBallNo_list.append(ball.group(1))
                    if note.IsBomBalloon:
                        balloonStyle = note.GetBalloonStyle
                        # swBalloonStyle_e.swBS_Circular
                        if balloonStyle == SWBALLOONSTYLE_E_SWBS_CIRCULAR:
                            # print("零件球號", note.GetText)
                            Table.extraBallNo_list.append(noteText)
                elif ann.GetType == SWANNOTATIONTYPE_E_SWGTOL:  # swAnnotationType_e.swGtol
                    gtol = ann.GetSpecificAnnotation
                    for i in SWTOLTEXT_TYPES:
                        try:
                            gtol.GetText(i)
                        except:
                            continue
                        ball = BALLROLE.search(gtol.GetText(i))
                        if ball is not None:
                            # print("幾何公差", ball[1])
                            Table.extraBallNo_list.append(ball.group(1))
                            break
                ann = ann.GetNext2
            view = view.GetNextView
        
        for i in Table.extraBallNo_list:
            item = BALLNO_TABLE.get(i, None)
            if item is not None:
                Table.extra_characteristic_list.append(item.get(CHARACTERISTIC_KEY, ""))
                Table.extra_cnc_list.append(item.get(CNC_KEY, ""))
                for d in DESCRIPTION_KEY_LIST:
                    if Table.extra_desciptionList_dict.get(d) is not None:
                        Table.extra_desciptionList_dict.get(d).append(item.get(d, ""))
                for m in MEASUREMENT_KEY_LIST:
                    if Table.extra_measurementList_dict.get(m) is not None:
                        Table.extra_measurementList_dict.get(m).append(item.get(m, ""))
            else:
                Table.extra_characteristic_list.append("")
                Table.extra_cnc_list.append("")
                for d in DESCRIPTION_KEY_LIST:
                    if Table.extra_desciptionList_dict.get(d) is not None:
                        Table.extra_desciptionList_dict.get(d).append("")
                for m in MEASUREMENT_KEY_LIST:
                    if Table.extra_measurementList_dict.get(m) is not None:
                        Table.extra_measurementList_dict.get(m).append("")
        

        return Table
    except Exception as e:
        error_signal.emit(DOC_PROCESS_ERROR.format(file), DEFAULT_ERROR_TYPE)
        error_signal.emit(repr(e), DEFAULT_ERROR_TYPE)
        return
    finally:
        sw_app.CloseDoc(model.GetTitle)
    
def cm_to_mm(cm):
    cm = float(cm)
    mm = round(cm*1000, 2)
    mm = format(Decimal(str(mm)).normalize(), 'f')
    return mm

def check_solidworks_is_running():
    try:
        win32com.client.GetActiveObject("Sldworks.Application")
        return True
    except:
        return False

def split_text_formats(text, chinese_format, english_format):
    """將字串拆成 (format, substring) 的 list，中文用標楷體，英文與數字用 Times New Roman"""
    parts = []
    current_format = None
    buffer = ""
    for ch in text:
        # 判斷是否是中文
        if '\u4e00' <= ch <= '\u9fff':
            fmt = chinese_format
        else: fmt = english_format
        # 如果格式改變，先把之前的 buffer 存起來
        if current_format is None:
            current_format = fmt
        if fmt != current_format:
            parts.append((current_format, buffer))
            buffer = ch
            current_format = fmt
        else:
            buffer += ch
    # 最後一段也要存起來
    if buffer:
        parts.append((current_format, buffer))
    return parts

def save_to_excel(data, file_path):
    # 建立 Excel 檔案
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()
    # 定義字體格式
    chinese_format = workbook.add_format({"font_name": "DFKai-SB", "font_size": 12})
    english_format = workbook.add_format({"font_name": "Times New Roman", "font_size": 12})
    cell_wrap_format = workbook.add_format({"text_wrap": True})
    for row, row_data in enumerate(data):
        for col, text in enumerate(row_data):
            rich_parts = split_text_formats(text, chinese_format, english_format)
            if len(rich_parts) == 1:
                fmt, txt = rich_parts[0]
                fmt = workbook.add_format({
                    "font_name": fmt.font_name,
                    "font_size": fmt.font_size,
                    "text_wrap": True
                })
                worksheet.write(row, col, txt, fmt)
            elif len(rich_parts) > 1:
                flat_parts = []
                for fmt, txt in rich_parts:
                    flat_parts.extend([fmt, txt])
                worksheet.write_rich_string(row, col, *flat_parts, cell_wrap_format)
    for c in range(len(data[0])):
        max_len = 0
        for row in data:
            lines = str(row[c]).splitlines() or [""]
            l = 0
            for line in lines:
                line_len = 0
                for ch in line:
                    # 判斷是否是中文
                    if '\u4e00' <= ch <= '\u9fff':
                        line_len += 3
                    else:
                        line_len += 1
                l = max(l, line_len)
            max_len = max(max_len, l)
        worksheet.set_column(c, c, max_len + 2)
    for r in range(len(data)):
        max_len = max(len(str(col).splitlines()) for col in data[r])
        worksheet.set_row(r, max_len*16)
    workbook.close()

def save_to_multiple_sheet_excel(sheet_data, file_path):
    # 建立 Excel 檔案
    workbook = xlsxwriter.Workbook(file_path)
    # 定義字體格式
    chinese_format = workbook.add_format({"font_name": "DFKai-SB", "font_size": 12})
    english_format = workbook.add_format({"font_name": "Times New Roman", "font_size": 12})
    cell_wrap_format = workbook.add_format({"text_wrap": True})
    for sheet, data in sheet_data:
        worksheet = workbook.add_worksheet(sheet)
        for row, row_data in enumerate(data):
            for col, text in enumerate(row_data):
                rich_parts = split_text_formats(text, chinese_format, english_format)
                if len(rich_parts) == 1:
                    fmt, txt = rich_parts[0]
                    fmt = workbook.add_format({
                        "font_name": fmt.font_name,
                        "font_size": fmt.font_size,
                        "text_wrap": True
                    })
                    worksheet.write(row, col, txt, fmt)
                elif len(rich_parts) > 1:
                    flat_parts = []
                    for fmt, txt in rich_parts:
                        flat_parts.extend([fmt, txt])
                    worksheet.write_rich_string(row, col, *flat_parts, cell_wrap_format)
        for c in range(len(data[0])):
            max_len = 0
            for row in data:
                lines = str(row[c]).splitlines() or [""]
                l = 0
                for line in lines:
                    line_len = 0
                    for ch in line:
                        # 判斷是否是中文
                        if '\u4e00' <= ch <= '\u9fff':
                            line_len += 3
                        else:
                            line_len += 1
                    l = max(l, line_len)
                max_len = max(max_len, l)
            worksheet.set_column(c, c, max_len + 2)
        for r in range(len(data)):
            max_len = max(len(str(col).splitlines()) for col in data[r])
            worksheet.set_row(r, max_len*16)
    workbook.close()

def get_all_solidworks_version():
    progids = []

    with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, "") as root:
        i = 0
        while True:
            try:
                key_name = winreg.EnumKey(root, i)
                m = re.fullmatch(r"SldWorks\.Application\.(\d+)", key_name)
                if m:
                    progids.append((int(m.group(1)), key_name))
                i += 1
            except OSError:
                break
    progids = sorted(progids, reverse=True) #(id, porgram_id)
    return progids