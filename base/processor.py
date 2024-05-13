# TODO: Processor to Process Data and Generate Clean Data
import sys
import os
import re
from enum import Enum

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

DEFAULT_PATH = os.path.join(os.getcwd(), "data", "raw")
DEFAULT_ENCODING = "utf-8"
DEFAULT_DELIMITER = ","
DEFAULT_MODE = "r"

class DataType(Enum):
    CSV = 1
    EXCEL = 2
    JSON = 3
    XML = 4
    YAML = 5
    OTHER = 6
    

ALLOWED_EXTENSIONS = {
    DataType.CSV: '.csv',
    DataType.EXCEL: ['.xlsx', '.xls'],
    DataType.JSON: '.json',
    DataType.XML: '.xml',
    DataType.YAML : '.yaml',
    DataType.OTHER: None
}

class Processor():
    def __init__(self) -> None:
        pass
    
    
    #region Utility Methods
    def __check_file_defaults(self, file: str) -> bool:
        if not os.path.exists(path=file):
            raise FileNotFoundError(f'File Not Found: {file}')
        
        if not os.path.isfile(path=file):
            raise FileNotFoundError(f'Invalid File or Not File: {file}')
        
        return True
    
    
    # Logic: "dummy.xlsx" -> ["dummy", "xlsx"] -> len > 1 ? "xlsx" : "undefined"
    def __determine_file_type(self, file: str) -> str:
        return file.split(".")[-1] if len(file.split(".")) > 1 else 'undefined'
    
    
    def __check_file_type(file: str, datatype: DataType = DataType.OTHER) -> bool:
        _, ext = os.path.splitext(file)
        
        return ext.lower() in (ext for ext in ALLOWED_EXTENSIONS.get(datatype, []))
    #endregion
    
    
    def load_data(self, filepath: str, datatype: DataType.OTHER):
        pd_instance = None
        
        if not self.__check_file_defaults(file=filepath):
            return pd_instance