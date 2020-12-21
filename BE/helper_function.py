import sqlalchemy as db
import urllib
import constants as CONST
import pyodbc

connection_string = CONST.connection_string

def make_conn():
    params = urllib.parse.quote_plus(connection_string)
    engine = db.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
    connection=engine.connect()
    return engine,connection

def make_pyodbc_conn():
    connection = pyodbc.connect(connection_string, autocommit=True, ansi=True)
    return connection