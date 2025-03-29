import jinja2

class SQLDB:
    """
    A base class for database interactions.

    This class provides a template for creating connections and executing SQL commands
    for various database systems. Subclasses must implement the abstract methods.

    Attributes:
        connection: The database connection object.
    """

    def create_connection(self):
        """
        Creates a connection to the database.

        This method should be implemented in subclasses to establish a connection
        to the specific database type.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def close_connection(self):
        """
        Closes the database connection.

        This method should be called to ensure that the database connection is properly closed.
        """
        if self.connection:
            self.connection.close()

    def run_sql(self, query, isUpdate=False):
        """
        Executes a SQL command on the database.

        Args:
            query (str): The SQL query to execute.
            isUpdate (bool, optional): Flag indicating if the query is an update. Defaults to False.

        Returns:
            list or int: The result of the query, or the number of affected rows for updates.

        This method should be implemented in subclasses to execute the SQL command
        on the specific database type.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def resolve_template(self, query, params):
        """
        Resolves a SQL query template with parameters.

        Args:
            query (str): The SQL query template with placeholders.
            params (dict): A dictionary of parameters to substitute into the query.

        Returns:
            str: The resolved SQL query with parameters substituted.

        This method can be used to create dynamic SQL queries based on templates.
        """
        return jinja2.Template(query).render(params)
        
    def run_query(self, query, params={}, isUpdate=False, onSuccess=None, onError=None):
        """
        Runs a SQL query after resolving its template.

        Args:
            query (str): The SQL query.
            params (dict, optional): Parameters for the query.
            isUpdate (bool, optional): Flag indicating if the query is an update.

        Returns:
            list: The result of the query.
        """
        try:
            if not self.connection:
                self.create_connection()
            query = self.resolve_template(query, params)
            result = self.run_sql(query, isUpdate=isUpdate)
            if onSuccess:
                return onSuccess(result)
            else:
                return True, result
        except Exception as error:
            if onError:
                if self.connection:
                    self.close_connection()
                    self.connection = None
                return onError(error)
            else:
                return False, error
        