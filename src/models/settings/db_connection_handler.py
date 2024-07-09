import sqlite3
from sqlite3 import Connection
from datetime import datetime

def adapt_datetime(ts):
    return ts.isoformat()

def convert_datetime(ts):
    return datetime.fromisoformat(ts.decode('utf-8'))


# Registrar adaptador e conversor
sqlite3.register_adapter(datetime, adapt_datetime)
sqlite3.register_converter('timestamp', convert_datetime)


class DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"
        self.__conn = None

    def connect(self) -> None:
        conn = sqlite3.connect(
            self.__connection_string,
            check_same_thread=False,
            detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
        )
        self.__conn = conn
    
    def get_connection(self) -> Connection:
        return self.__conn
    

db_connetction_handler = DbConnectionHandler()