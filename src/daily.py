
from time import time


#SELECT last_lance from RoueDuJ where ID_User = 5
class daily:
    def CanLaunch(userID:int,cursor) -> bool:
        cursor.execute(f"SELECT last_lance from RoueDuJ where ID_User = {userID}")
        response = int(cursor.fetchall()[0])
        return int(time()) - response >= 1440

    def Launch(userID:int,conn):
        cursor = conn.cursor()
        if daily.CanLaunch(userID,cursor):
            cursor.execute(f"UPDATE RoueDuJ SET last_lance = {time()} where ID_User = {userID}")
            conn.commit()
            return True
        else:
            return False