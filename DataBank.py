import sqlite3

class DataBank:
    __db_name = "configs.db"
    __db = None

    def close(self):
        self.__db.close()

    def __Create_or_Connect(self):
        try:
            sql = "create table if not exists Tconfig ( "
            sql += " token text , active_code1 text, active_code2 text ) ;"
            self.__db = sqlite3.connect(self.__db_name, check_same_thread=False)
            self.__db.execute(sql)
            self.__db.commit()
            return True
        except Exception as ex:
            print(ex)
            return False

    def __init__(self):
        self.__Create_or_Connect()

    def insertToken_and_ActiveCode(self, Token, ActiveCode1, ActiveCode2):
        try:
            sql = "insert into Tconfig ( token , active_code1, active_code2 ) values ( ? , ? , ? ) ;"
            crs = self.__db.cursor()


            import Cryptography
            Token = Cryptography.BigAss().encode(Token)


            crs.execute(sql, (Token, ActiveCode1, ActiveCode2, ))
            self.__db.commit()
            return True
        except Exception as ex:
            print(ex)
            return False

    def getTokenAndActiveCode(self):
        sql = "select * from Tconfig"
        crs = self.__db.cursor()
        crs.execute(sql)
        temp = crs.fetchone()
        import Cryptography
        a = Cryptography.BigAss().text_decode(temp[0])
        b = Cryptography.BigAss().decode(temp[1])
        c = Cryptography.BigAss().decode(temp[2])
        temp = (a, b, c)
        return temp

    def edit(self, Token, ActiveCode1, ActiveCode2):
        try:
            sql = "update Tconfig set token = ? , active_code1 = ? , active_code2 = ? "
            crs = self.__db.cursor()
            import Cryptography
            Token = Cryptography.BigAss().encode(Token)
            crs.execute(sql, (Token, ActiveCode1, ActiveCode2, ))
            self.__db.commit()
            return True
        except Exception as ex:
            print(ex)
            return False
