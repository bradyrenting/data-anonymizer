import mysql.connector
import sys
import subprocess
from .ConfigReader import config
from .informationgenerator import get_anonymized_data


class Anonymize:

    def __init__(self, host='127.0.0.1', username='user',
                 password='password', database='testdatabase', configfile=None, infile=None, outfile=None):
        self.host = host
        self.user = username
        self.password = password
        self.database = database
        self.infile = infile
        self.outfile = outfile

        self.mysql_connection = self.initialise_database_connection()

        if configfile is not None:
            self.config = config(open(configfile, 'r'))
        self.cursor = self.mysql_connection.cursor(buffered=True)

        self.create_database()
        self.cursor.execute("use {}".format(self.database))

    def initialise_database_connection(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )

    def create_database(self):
        self.cursor.execute("drop database if exists {}".format(self.database))
        self.cursor.execute("create database {}".format(self.database))
        self.mysql_connection.commit()

    def populate_database(self):
        self.cursor.execute("use {}".format(self.database))

        with open(self.infile, 'r') as f:
            sql_dump = f.read()

        subprocess.run(
            ['sed', '-i', 's/DEFINER=`[^`][^`]*`@`[^`][^`]*`//g', self.infile],
            stdout=subprocess.PIPE,
        )

        subprocess.run(
            ['mysql', '-h', self.host, '-u', self.user, '-p' + self.password, self.database],
            stdout=subprocess.PIPE, input=sql_dump, encoding='utf-8'
        )

    def get_tables(self):
        self.cursor.execute("show tables")
        tables = []
        for table in self.cursor.fetchall():
            tables.append(table[0])
        return tables

    def get_columns(self, table):
        self.cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{}'".format(table))
        return self.cursor.fetchall()

    def export_database(self):
        command_output = subprocess.check_output(
            ['mysqldump', '-h', self.host, '-u', self.user, '-p' + self.password, self.database])

        with open(self.outfile, 'wb') as f:
            f.write(command_output)

    def anonymize_database(self):
        tables = self.config.tables()

        for table in tables:
            self.cursor.execute("select * from {}.{}".format(self.database, table))
            rows = self.cursor.fetchall()
            columns = self.config.columns(table)
            iterator = self.config.iterator(table)
            self.update_database(rows, iterator, columns, table)

    def update_database(self, rows, iterator, columns, table):
        for column in columns:
            for row in rows:
                column_data = columns[column]
                value = get_anonymized_data(column_data)
                sql = '''UPDATE {}.{} SET {} = '{}' where {} = '{}' '''.format(
                    self.database, table, column, value, iterator, row[0])
                try:
                    self.cursor.execute(sql)
                    self.mysql_connection.commit()
                except Exception as e:
                    print(e)
