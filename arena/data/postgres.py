from .common.sqldb import SQLDB
import psycopg2

class Postgres(SQLDB):
    """
    A class to interact with a PostgreSQL database.

    Attributes:
        config (dict): Configuration for the PostgreSQL connection.
        connection: The database connection object.
    """

    def __init__(self, config):
        """
        Initializes the Postgres class with the provided configuration.

        Args:
            config (dict): Database configuration for PostgreSQL.
        """
        self.config = config
        self.connection = None

    def create_connection(self):
        """
        Creates a connection to the PostgreSQL database.
        """
        self.connection = psycopg2.connect(**self.config)

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()

    def run_sql(self, query, isUpdate=False):
        """
        Executes a SQL command on the PostgreSQL database.

        Args:
            query (str): The SQL query to execute.
            isUpdate (bool, optional): Flag indicating if the query is an update.

        Returns:
            list or int: The result of the query, or the number of affected rows for updates.
        """
        if not self.connection:
            self.create_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            if isUpdate:
                self.connection.commit()
                return cursor.rowcount
            return cursor.fetchall()
             