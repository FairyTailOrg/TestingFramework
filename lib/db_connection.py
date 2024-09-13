"""This file will content how to connect to dB."""
import pymssql


class DbConnection:
    """This class will establishes connection with a dB."""

    def __init__(self, user, password, dbname, host, port) -> None:
        """Process parameters.

        Args:
            user (string): user to access to dB.
            password (string): password to access to dB.
            dbname (string): db to be accesed.
            host (string): host to access to dB.
            port (int): port to conect.
        """
        self.user = user
        self.password = password
        self.dbname = dbname
        self.host = host
        self.port = port

    def connect_to_db(self):
        """Connect to database. 2 instances are needed because mngr and db."""
        self.conn = pymssql.connect(
            server=self.host,
            user=self.user,
            password=self.password,
            database=self.dbname,
            port=1433
            )
        self.cursor = self.conn.cursor(as_dict=True)

    def close_db(self):
        """Close db connections."""
        self.cursor.close()
        self.conn.close()
