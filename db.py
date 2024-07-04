class MySQL:
    def __init__(self, host, user, password, database):
        import mysql.connector
        
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()


    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.conn.commit()


    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()


    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()


    def close(self):
        self.cursor.close()
        self.conn.close()

