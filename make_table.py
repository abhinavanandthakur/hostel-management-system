import pyodbc
import constants as CONST

# For boarder_details
table1 = """IF OBJECT_ID('boarder_details', 'U') IS NULL CREATE TABLE boarder_details (\
     rollNo INT PRIMARY KEY ,\
     first_name VARCHAR(30) NOT NULL ,\
     last_name VARCHAR(30) NOT NULL, \
     phoneNumber varchar(10) NOT NULL unique,\
     department varchar(20) ,\
     programme varchar(20) ,\
     email varchar(30) unique,\
     dateOfBirth date NOT NULL,\
     address varchar(40),\
     roomNo int unique NOT NULL,\
     foreign key (roomNo) references rooms(roomNo) ); """
# For rooms
table2 ="""IF OBJECT_ID('rooms', 'U') IS NULL create table rooms ( \
     roomNo int primary key,\
     floor int); """

# For representatives
table3 ="""IF OBJECT_ID('representatives', 'U') IS NULL create table representatives ( \
     role VARCHAR(30) PRIMARY KEY,\
     rollNo int unique,\
     foreign key (rollNo) references boarder_details(rollNo) ); """


def make_table():
     try:
          connection = pyodbc.connect(CONST.connection_string,autocommit = True)
          cur = connection.cursor()
          cur.execute(table2)
          print('Room Table Created')
          cur.execute(table1)
          print('Boarder Table Created')
          cur.execute(table3)
          print('Representatives Table Created')
          connection.commit()
          connection.close()
          print('Success!')
     except Exception as e:
          print(e)


choice=int(input('Create Tables? Press 1 to create.'))
if(choice==1): 
     make_table()
