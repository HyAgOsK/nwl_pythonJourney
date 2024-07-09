from sqlite3 import Connection
from typing import Dict, Tuple, List

class LinksToTrip:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_link(self, link_info: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute('''
            INSERT INTO links 
                (id, trip_id, link, title)
            VALUES ( ?, ?, ?, ?) ''', 
                (
                    link_info["id"],
                    link_info["trip_id"],
                    link_info["link"],
                    link_info["title"]
                )
            )
        self.__conn.commit()
    
    def find_link_info(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM links WHERE trip_id = ?''', (trip_id,)
        )
        trip = cursor.fetchone()
        return trip