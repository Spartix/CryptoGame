from time import time

class Daily:
    @staticmethod
    def can_launch(user_id: int, cursor) -> bool:
        cursor.execute("SELECT last_lance FROM RoueDuJ WHERE ID_User = ?", (user_id,))
        response = cursor.fetchone()
        if response:
            last_launch = int(response[0])
            return int(time()) - last_launch >= 1440
        else:
            return True

    @staticmethod
    def launch(user_id: int, conn):
        cursor = conn.cursor()
        try:
            if Daily.can_launch(user_id, cursor):
                cursor.execute("UPDATE RoueDuJ SET last_lance = ? WHERE ID_User = ?", (int(time()), user_id))
                conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Erreur lors du lancement de l'opération quotidienne : {e}")
            conn.rollback()
            return False
        finally:
            cursor.close()