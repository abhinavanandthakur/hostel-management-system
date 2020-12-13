import pyodbc
import constants as CONST

# For boarder_details
table1 = """IF OBJECT_ID('boarder_details', 'U') IS NULL CREATE TABLE boarder_details (boarder_id INT PRIMARY KEY ,\
     first_name VARCHAR(30) NOT NULL ,\
     last_name VARCHAR(30) NOT NULL, \
     description VARCHAR(255),\
     is_active BIT DEFAULT 0,\
     dob DATE; """

# For rooms
table2 ="""IF OBJECT_ID('rooms', 'U') IS NULL create table rooms ( id BIGINT PRIMARY KEY IDENTITY(1,1),\
     followee_id BIGINT NOT NULL,\
     follower_id BIGINT NOT NULL,\
     date_stamp DATE NOT NULL DEFAULT CONVERT(date, getdate()),\
     time_stamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,\
     CONSTRAINT fk_ud_flrid FOREIGN KEY (follower_id) REFERENCES boarder_details(boarder_id) ON DELETE  NO ACTION ON UPDATE NO ACTION,\
     CONSTRAINT fk_ud_fleid FOREIGN KEY (followee_id) REFERENCES boarder_details(boarder_id) ON DELETE  NO ACTION ON UPDATE NO ACTION); """

# For representatives
table2 ="""IF OBJECT_ID('representatives', 'U') IS NULL create table representatives ( role VARCHAR(30) PRIMARY KEY,\
     followee_id BIGINT NOT NULL,\
     follower_id BIGINT NOT NULL,\
     date_stamp DATE NOT NULL DEFAULT CONVERT(date, getdate()),\
     time_stamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,\
     CONSTRAINT fk_ud_flrid FOREIGN KEY (follower_id) REFERENCES boarder_details(boarder_id) ON DELETE  NO ACTION ON UPDATE NO ACTION,\
     CONSTRAINT fk_ud_fleid FOREIGN KEY (followee_id) REFERENCES boarder_details(boarder_id) ON DELETE  NO ACTION ON UPDATE NO ACTION); """


def make_table():
     try:
          connection = pyodbc.connect(CONST.connection_string)
          cur = connection.cursor()
          cur.execute(table1)
          cur.execute(table2)
          connection.close()
          print('Success!')
     except Exception as e:
          print(e)


choice=int(input('Create Tables? Press 1 to create.'))
if(choice==1): 
     make_table()
