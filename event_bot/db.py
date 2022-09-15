import sqlite3


class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def add_record(self, name, date, time, place):
        self.cursor.execute("INSERT INTO `events` (`name`, `date`, `time`,`place`) VALUES (?,?,?,?)",
                            (name, date, time, place,))
        return self.conn.commit()

    def close(self):
        self.conn.close()
