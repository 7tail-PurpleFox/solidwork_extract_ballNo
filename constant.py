import os
import sys
import re
import csv

def get_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.normpath(os.path.join(base_path, relative_path))

def read_csv_to_2d_dict(filename: str, primary_key_field: str):
    """
    Reads a CSV file into a 2D dictionary using a specified column as the primary key.
    """
    data_dict = {}
    with open(filename, mode='r', newline='', encoding='utf-8') as csv_file:
        # DictReader uses the first row as keys by default
        reader = csv.DictReader(csv_file)
        for row in reader:
            # The primary key for the outer dictionary
            primary_key_value = row[primary_key_field]
            # Remove the primary key from the inner dictionary
            del row[primary_key_field]
            # Store the rest of the row as the inner dictionary
            data_dict[primary_key_value] = row
    return data_dict


ICON_PATH = get_path("resource/icon.png")
BALLNO_TABLE_PATH = get_path("resource/BallNo_Table.csv")
LOADING_GIF_PATH = get_path("resource/loading.gif")
BALLNO_TABLE_PRIMARY_KEY_FIELD = 'BallNo'
BALLNO_TABLE = read_csv_to_2d_dict(BALLNO_TABLE_PATH, BALLNO_TABLE_PRIMARY_KEY_FIELD)
DESCRIPTION_KEY_LIST = ["Description_1", "Description_2", "Description_3", "Description_4"]
MEASUREMENT_KEY_LIST = ["Measurement_1", "Measurement_2", "Measurement_3", "Measurement_NO"]
DESCRIPTION_COMBOBOX_ITEMS = [("中文", DESCRIPTION_KEY_LIST[0]), ("英文", DESCRIPTION_KEY_LIST[1]), ("球號+中文", DESCRIPTION_KEY_LIST[2]), ("中文+英文", DESCRIPTION_KEY_LIST[3]), ("不顯示", None)]
MEASUREMENT_COMBOBOX_ITEMS = [("中文", MEASUREMENT_KEY_LIST[0]), ("英文", MEASUREMENT_KEY_LIST[1]), ("中文+英文", MEASUREMENT_KEY_LIST[2]), ("編號", MEASUREMENT_KEY_LIST[3]), ("不顯示", None)]
EXTRA_BALL_USE = 0
EXTRA_BALL_UNUSE = 1
EXTRA_BALL_ONLY = 2
EXTRABALL_COMBOBOX_ITEMS = [("顯示無尺寸球號選項", EXTRA_BALL_USE), ("不顯示無尺寸球號選項", EXTRA_BALL_UNUSE), ("僅顯示無尺寸球號選項", EXTRA_BALL_ONLY)]
REPLACE_VALUE_USE = 0
REPLACE_VALUE_UNUSE = 1
REPLACE_VALUE_DONT_SHOW = 2
REPLACE_VALUE_ONLY_USE = 3
REPLACE_VALUE_ONLY_UNUSE = 4
REPLACE_VALUE_COMBOBOX_ITEMS = [("顯示取代值選項並使用取代值", REPLACE_VALUE_USE), ("顯示取代值選項但使用原尺寸", REPLACE_VALUE_UNUSE), ("不顯示取代值選項", REPLACE_VALUE_DONT_SHOW), ("僅顯示取代值選項並使用取代值", REPLACE_VALUE_ONLY_USE), ("僅顯示取代值選項但使用原尺寸", REPLACE_VALUE_ONLY_UNUSE)]

CHARACTERISTIC_KEY = "Characteristic"
CHARACTERISTIC_SC = "SC"
CHARACTERISTIC_CC = "CC"
CNC_KEY = "CNC"
CNC_TURNING = "車床"
CNC_MILLING = "銑床"
PHI = "Ø"
UNIT_MM = " mm"

TABLE_BALLNO = "球號"
TABLE_DESCRIPTION = "描述"
TABLE_MEASUREMENT = "檢測"
TABLE_STANDARDVALUE = "標準值"
TABLE_LOWERBOUND = "下限"
TABLE_UPPERBOUND = "上限"
TABLE_TOLERANCE = "公差"
TABLE_CHARACTERISTIC = "管制特性"
TABLE_CNC = "車銑床"
TABLE_KEYS = [TABLE_BALLNO, TABLE_DESCRIPTION, TABLE_MEASUREMENT, TABLE_STANDARDVALUE, TABLE_LOWERBOUND, TABLE_UPPERBOUND, TABLE_TOLERANCE, TABLE_CHARACTERISTIC, TABLE_CNC]
INFO_KEYS = [TABLE_BALLNO, TABLE_DESCRIPTION, TABLE_MEASUREMENT, TABLE_CHARACTERISTIC, TABLE_CNC]


BALLROLE = re.compile(r'<\s*C#-(\d+)>')   # <+空白*(0~infinite)+C#-+數字+>
PHIROLE = re.compile(r'<\s*MOD-DIAM>') # <+空白*(0~infinite)+MOD-DIAM+>
SWDOCDRAWING = 3
SWOPENDOCOPTIONS_SILENT = 1
SW_OPEN_READONLY = 2
SWTOLSYMMETRIC = 4
SWTOLBILAT = 2

# swDimensionTextAll            =0          # from enum swDimensionTextParts_e
# swDimensionTextCalloutAbove   =3          # from enum swDimensionTextParts_e
# swDimensionTextCalloutAboveDefinition=7          # from enum swDimensionTextParts_e
# swDimensionTextCalloutBelow   =4          # from enum swDimensionTextParts_e
# swDimensionTextCalloutBelowDefinition=8          # from enum swDimensionTextParts_e
# swDimensionTextPrefix         =1          # from enum swDimensionTextParts_e
# swDimensionTextPrefixDefinition=5          # from enum swDimensionTextParts_e
# swDimensionTextSuffix         =2          # from enum swDimensionTextParts_e
# swDimensionTextSuffixDefinition=6          # from enum swDimensionTextParts_e
SWDIMENSIONTEXT_TYPES = [0, 1, 2, 3, 4, 5, 6, 7, 8]

SWANNOTATIONTYPE_E_SWNOTE = 6
SWANNOTATIONTYPE_E_SWGTOL = 5
SWBALLOONSTYLE_E_SWBS_CIRCULAR = 1
# swGTolTextCalloutAbove        =3          # from enum swGTolTextParts_e
# swGTolTextCalloutBelow        =4          # from enum swGTolTextParts_e
# swGTolTextPrefix              =1          # from enum swGTolTextParts_e
# swGTolTextSuffix              =2          # from enum swGTolTextParts_e
SWTOLTEXT_TYPES = [1, 2, 3, 4]

TOLERANCE_BILAT_STRING = "{0} {1}/{2}"
TOLERANCE_SYMMETRIC_STRING = "{0} ± {1}"


SLDWORKS_OPEN_ERROR = "SOLIDWORKS開啟失敗"
FILE_NOT_FOUND_ERROR = "{0}\n找不到檔案"
DOC_OPEN_ERROR = "{0}\n無法開啟檔案"
DOC_PROCESS_ERROR = "{0}\n檔案處理時發生錯誤"
FILE_SAVE_ERROR = "儲存檔案時發生錯誤"
FILE_PERMISSION_ERROR = "{0}\n可能正在被開啟或沒有寫入權限"
NO_SLDWORKS_ERROR = "找不到SOLIDWORKS"
ALL_SLDWORKS_FAIL_ERROR = "所有 SOLIDWORKS COM 都啟動失敗"

REPLACE_VALUE_WARNING = "{0}\n發現球號{1}有取代值\n原尺寸: {2}  取代值: {3}"
EXTRA_BALLNO_WARNING = "{0}\n發現球號{1}無法抓取尺寸"
SLDWORKS_OPENING_WARNING = "發現您正在使用SOLIDWORKS，為了避免編輯中檔案遺失，請關閉SOLIDWORKS後再使用"
SLDWORKS_VERSION_LOWER_THAN_2025_WARNING = "您正在使用的SOLIDWORKS版本為{0}\n較舊的版本可能會出錯"
SLDWORKS_OPEN_ERROR_WITH_VERSION = "SOLIDWORKS{0}開啟失敗"

WARNING_TITLE = "警告"
DEFAULT_ERROR_TYPE = 0
DEFAULT_WARNING_TYPE = 1
REPLACE_VALUE_WARNING_TYPE = 2
EXTRA_BALLNO_WARNING_TYPE = 3

SLDWORKS_2025_PROGID = 33
SLDWORKS_PROGID_TO_CE_DIFFERENC = 1992
