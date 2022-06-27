import sqlite3
from sqlite3 import Error


# functions
def check_file(path):
    try:
        a = open(path, 'r')
        a.close()
        return True
    except FileNotFoundError:
        return False


def create_file(path):
    if not check_file(path):
        a = open(path, "a+")
        a.close()
    else:
        return 'FileExistsError'


def write_on_file(content, path, params='w'):
    with open(path, params) as file:
        file.write(content)


def log_lines(list_of_strings, file):
    if create_file(file) == 'FileExistsError':
        pass
    else:
        for i in list_of_strings:
            write_on_file(i + '\n', list_of_strings, 'a')


class SQLiteManager:
    def __init__(self):
        #path to the default log files
        self.all_log_file = 'all_SQLite_log_file.log'
        self.successes_log_file = 'successes_SQLite_log_file.log'
        self.error_log_file = 'errors_SQLite_log_file.log'
        # database name
        self.database = ''
        # path to the database
        self.path = ''
        # the current sql script 
        self.sql = ''
        # the history of all sql 
        self.sql_history = []
        # the history of just the success queries
        self.successes = []
        # the history of just the error queries
        self.errors = []

    # cleaning all queries history
    def cls_all_history(self):
        self.sql_history = []
        self.successes = []
        self.errors = []

    # cleaning all queries history
    def cls_history(self):
        self.sql_history = []

    # cleaning all queries history
    def cls_errors(self):
        self.errors = []

    # cleaning all queries history
    def cls_successes(self):
        self.successes = []

    # logging all histories
    def log_history(self):
        log_lines(self.sql_history, self.all_log_file)

    # logging error histories
    def log_errors(self):
        log_lines(self.successes, self.successes_log_file)

    # logging success histories
    def log_sucesses(self):
        log_lines(self.errors, self.error_log_file)

    # connecting to database
    def db_connect(self, path):
        self.path = path
        self.database = self.path
        try:
            self.connection = sqlite3.connect(self.path)
            self.successes.append(f"Successfully connected on {self.path}")
            self.sql_history.append(f"Successfully connected on {self.path}")
            return self.connection
        except Error as ex:
            return ex

    # diconnecting database
    def db_disconnetc(self):
        self.database = ''
        self.successes.append(f"Successfully disconnected on {self.path}")
        self.sql_history.append(f"Successfully disconnected on {self.path}")
        return self.connection.close()

    # run SQL commands
    def any_sql(self, sql):
        self.sql = sql
        try:
            self.successes.append(self.sql)
            self.sql_history.append(self.sql)
            self.connection.cursor().execute(sql)
            self.connection.commit()
        except Error as ex:
            self.errors.append(ex)
            self.sql_history.append(self.sql)
            return ex
