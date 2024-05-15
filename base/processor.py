# TODO: Processor to Process Data and Generate Clean Data
import sys
import os
import re
from enum import Enum
from typing import Optional, Tuple

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# Rich Lib
from rich import print
from rich.console import Console
from rich.table import Table

from base.decorators import singleton

DEFAULT_PATH = os.path.join(os.getcwd(), "data", "raw")
DEFAULT_ENCODING = "utf-8"
DEFAULT_DELIMITER = ","
DEFAULT_MODE = "r"

console = Console()

class DataType(Enum):
    CSV = 1
    EXCEL = 2
    JSON = 3
    XML = 4
    YAML = 5
    OTHER = 6
    
class QueryType(Enum):
    CREATE = 1
    READ = 2
    UPDATE = 3
    DELETE = 4
    WRITE = 5
    APPEND = 6
    MERGE = 7

ALLOWED_EXTENSIONS = {
    DataType.CSV: '.csv',
    DataType.EXCEL: ['.xlsx', '.xls'],
    DataType.JSON: '.json',
    DataType.XML: '.xml',
    DataType.YAML : '.yaml',
    DataType.OTHER: None
}

@singleton
class Processor():
    def __init__(self) -> None:
        pass
    
    #region Utility Methods
    def __check_file_defaults(self, file: str) -> bool:
        '''
        Check if the file exists and if the file is a file or not.
        
        :return: True if the file exists and is indeed a file, else False.
        '''
        if not os.path.exists(path=file):
            raise FileNotFoundError(f'File Not Found: {file}')
        
        if not os.path.isfile(path=file):
            raise FileNotFoundError(f'Invalid File or Not File: {file}')
        
        return True
    
    
    # Logic: "dummy.xlsx" -> ["dummy", "xlsx"] -> len > 1 ? "xlsx" : "undefined"
    def __determine_file_type(self, file: str) -> str:
        '''
        Determine the file type ending after the . in the file name.
        
        :return: The file type ending, else undefined.
        '''
        return file.split(".")[-1] if len(file.split(".")) > 1 else 'undefined'
    
    
    def __check_file_type(file: str, datatype: DataType = DataType.OTHER) -> bool:
        '''
        Determine if the file type is allowed for the given data type, cross checking with the ALLOWED_EXTENSIONS dictionary.
        
        :return: True if the file type is allowed, else False.
        '''
        _, ext = os.path.splitext(file)
        
        return ext.lower() in (ext for ext in ALLOWED_EXTENSIONS.get(datatype, []))
    #endregion
    
    def __process_csv(self, query: str, filepath: Optional[str] = 'data/economics_classifications.csv') -> pd.DataFrame:
        with open(filepath, mode=DEFAULT_MODE) as file:
            df = pd.read_csv(file)
            df.query(query)
            
            return df 
        
    def __process_csv(self, filepath: str, *queries: str) -> pd.DataFrame:
        with open(filepath, mode=DEFAULT_MODE) as file:
            df = pd.read_csv(file)
            
            console.log(f'Processing CSV File: {filepath}')
            
            for idx, query in enumerate(queries):
                console.log(f'Processing Query {idx}: {query}')
                df.query(query)
                
                
    def __process_excel(self, filepath: str, *queries: str) -> pd.DataFrame:
        pass
    
    def __process_excel(self, filepath: str, encoding: str = DEFAULT_ENCODING):
        return pd.read_excel(filepath, encoding=encoding)
    
    def __process_json(self, filepath: str, encoding: str = DEFAULT_ENCODING):
        return pd.read_json(filepath, encoding=encoding)
    
    def __process_xml(self, filepath: str, encoding: str = DEFAULT_ENCODING):
        pass
    
    def load_data(self, filepath: str, datatype: DataType.OTHER):
        pd_instance = None
        
        if not self.__check_file_type(filepath, datatype):
            raise ValueError(f'Invalid File Type: {filepath.split(".")[-1]}')