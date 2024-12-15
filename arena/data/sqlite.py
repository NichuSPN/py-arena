from .common.sqldb import SQLDB
import sqlite3

class SQLite(SQLDB):
    """
    A class to interact with a SQLite database.

    Attributes:
        db_file (str): The path to the SQLite database file.
        connection: The database connection object.
    """

    def __init__(self, db_file):
        """
        Initializes the SQLite class with the path to the database file.

        Args:
            db_file (str): The path to the SQLite database file.
        """
        self.db_file = db_file
        self.connection = None

    def create_connection(self):
        """
        Creates a connection to the SQLite database.
        """
        self.connection = sqlite3.connect(self.db_file)

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()

    def run_sql(self, query, isUpdate=False):
        """
        Executes a SQL command on the SQLite database.

        Args:
            query (str): The SQL query to execute.
            isUpdate (bool, optional): Flag indicating if the query is an update.

        Returns:
            list or int: The result of the query, or the number of affected rows for updates.
        """
        if not self.connection:
            self.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(query)
        if isUpdate:
            self.connection.commit()
        return cursor.fetchall()