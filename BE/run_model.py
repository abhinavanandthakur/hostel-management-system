from flask import Blueprint, jsonify, request
import constants as CONST
import pandas as pd
from helper_function import *

bp = Blueprint("api", __name__)
status='status'
data='data'
#----------------boarder ROUTES----------------------#



@bp.route("/get_all_boarders", methods=["GET"])
def get_all_boarders():
    try:  
        engine, connection = make_conn()
        boarder_meta=[]
        query = "SELECT * from boarder_details ;"
        df = pd.read_sql(query, engine)   #TO FETCH

        if len(df) < 1:    #Empty boarder Data (No boarders)
            connection.close()
            return ({status:'Success',data:[]})
        else:
            for index, rows in df.iterrows():
                obj = {
                    "rollNo": int(rows.rollNo),
                    "first_name": str(rows.first_name),
                    "last_name": str(rows.last_name),
                    "phoneNumber": str(rows.phoneNumber),
                    "department": str(rows.department),
                    "programme": str(rows.programme),
                    "email": str(rows.email),
                    "dateOfBirth": str(rows.dateOfBirth),
                    "address": str(rows.address),
                    "roomNo": int(rows.roomNo)
                }
                boarder_meta.append(obj)
            connection.close()
            return ({status:'Success',data:boarder_meta})

    except Exception as e:
        return ({status:'Failed',data:str(e)})


@bp.route("/add_boarders", methods=["POST"])
def add_profile():
    try:  
            engine, connection = make_conn()
            
            rollNo=str(request.json["rollNo"])
            first_name=str(request.json["first_name"])
            last_name=str(request.json["last_name"])
            phoneNumber=str(request.json["phoneNumber"])
            department=str(request.json["department"])
            programme=str(request.json["programme"])
            email=str(request.json["email"])
            dateOfBirth=str(request.json["dateOfBirth"])
            address=str(request.json["address"])
            roomNo=str(request.json["roomNo"])

            
            query = """\
                        insert into boarder_details(rollNo,first_name,last_name,phoneNumber,department,programme,email,dateOfBirth,address,roomNo) values( ? , ?, ?, ?, ?, ?, ?, ?, ?, ? );
                    """
            print("Inserted",query)
            connection.execute(query,(rollNo,first_name, last_name, phoneNumber, department, programme, email, dateOfBirth, address, roomNo))   #TO INSERT
            
            query="select rollNo,first_name,last_name,phoneNumber,department,programme,email,dateOfBirth,address,roomNo from boarder_details where rollNo = "+rollNo+" ;"
            df = pd.read_sql(query, engine)    #TO FETCH

            boarder_meta = {}
            for index, rows in df.iterrows():
                    boarder_meta = {
                        "rollNo": int(rows.rollNo),
                        "first_name": str(rows.first_name),
                        "last_name": str(rows.last_name),
                        "phoneNumber": str(rows.phoneNumber),
                        "department": str(rows.department),
                        "programme": str(rows.programme),
                        "email": str(rows.email),
                        "dateOfBirth": str(rows.dateOfBirth),
                        "address": str(rows.address),
                        "roomNo": int(rows.roomNo)
                    }
            connection.close()
            return({status:'Success',data:boarder_meta})
    
    except Exception as e:
        return ({status:'Failed',data:str(e)})


@bp.route("/update_boarder", methods=["POST"])
def boarder_update():

    try:
        engine, connection = make_conn()
        rollNo=str(request.json["rollNo"])
        first_name=str(request.json["first_name"])
        last_name=str(request.json["last_name"])
        phoneNumber=str(request.json["phoneNumber"])
        department=str(request.json["department"])
        programme=str(request.json["programme"])
        email=str(request.json["email"])
        dateOfBirth=str(request.json["dateOfBirth"])
        address=str(request.json["address"])
        roomNo=str(request.json["roomNo"])
        #updateString = "UPDATE boarder_details SET first_name = "+first_name+", last_name = "+last_name+", phoneNumber="+phoneNumber+",department="+department+",programme="+programme+",email="+email+",dateOfBirth="+dateOfBirth+",address="+address+",roomNo="+roomNo+" WHERE rollNo = "+rollNo+" ;"
        updateString  = """\
                        UPDATE boarder_details SET first_name=?,last_name=?,phoneNumber=?,department=?,programme=?,email=?,dateOfBirth=?,address=?,roomNo=? WHERE rollNo=? ;
                    """
        connection.execute(updateString,(first_name, last_name, phoneNumber, department, programme, email, dateOfBirth, address, roomNo, rollNo))  #TO UPDATE

        query = "SELECT rollNo,first_name,last_name,phoneNumber,department,programme,email,dateOfBirth,address,roomNo from boarder_details where rollNo = "+rollNo+" ;"
        df = pd.read_sql(query, engine)

        boarder_meta = {}
        for index, rows in df.iterrows():
            boarder_meta = {
                    "rollNo": int(rows.rollNo),
                    "first_name": str(rows.first_name),
                    "last_name": str(rows.last_name),
                    "phoneNumber": str(rows.phoneNumber),
                    "department": str(rows.department),
                    "programme": str(rows.programme),
                    "email": str(rows.email),
                    "dateOfBirth": str(rows.dateOfBirth),
                    "address": str(rows.address),
                    "roomNo": int(rows.roomNo)
            }

        connection.close()
        return({status:'Success',data:boarder_meta})

    except Exception as e:
        return ({status:'Failed',data:str(e)})


@bp.route("/delete_boarder", methods=["POST"])
def boarder_delete():

    try:
        engine, connection = make_conn()
        rollNo=str(request.json["rollNo"])
        query = "DELETE FROM boarder_details WHERE rollNo = "+rollNo+";"
        connection.execute(query)
        connection.close()
        return({status:'Success',data:{}})

    except Exception as e:
        return ({status:'Failed',data:str(e)})


#----------------rooms ROUTES----------------------#


@bp.route("/get_all_rooms", methods=["GET"])
def get_all_rooms():
    try:  
        engine, connection = make_conn()
        room_meta=[]
        query = "SELECT * from rooms ;"
        df = pd.read_sql(query, engine)   #TO FETCH

        if len(df) < 1:    #Empty room Data (No room)
            connection.close()
            return ({status:'Success',data:[]})
        else:
            for index, rows in df.iterrows():
                obj = {
                    "roomNo": int(rows.roomNo),
                    "floor": int(rows.floor)
                }
                room_meta.append(obj)
            connection.close()
            return ({status:'Success',data:room_meta})

    except Exception as e:
        return ({status:'Failed',data:str(e)})


@bp.route("/add_rooms", methods=["POST"])
def add_room():
    try:  
            engine, connection = make_conn()
            
            roomNo=str(request.json["roomNo"])
            floor=str(request.json["floor"])

            query="insert into rooms(roomNo,floor) values("+roomNo+","+floor+");"
            print(query)
            connection.execute(query)   #TO INSERT

            query="select roomNo,floor from rooms where roomNo = "+roomNo+" ;"
            df = pd.read_sql(query, engine)    #TO FETCH

            room_meta = {}
            for index, rows in df.iterrows():
                    room_meta = {
                        "roomNo": int(rows.roomNo),
                        "floor": int(rows.floor)
                    }
            connection.close()
            return({status:'Success',data:room_meta})
    
    except Exception as e:
        return ({status:'Failed',data:str(e)})


@bp.route("/update_room", methods=["POST"])
def room_update():

    try:
        engine, connection = make_conn()
        roomNo=str(request.json["roomNo"])
        floor=str(request.json["floor"])

        updateString = "UPDATE rooms SET roomNo = "+roomNo+", floor = "+floor+" ;"
        connection.execute(updateString)  #TO UPDATE

        query = "SELECT roomNo,floor from rooms where roomNo = "+roomNo+" ;"
        df = pd.read_sql(query, engine)

        room_meta = {}
        for index, rows in df.iterrows():
            room_meta = {
                "roomNo": int(rows.roomNo),
                "floor": int(rows.floor)
            }

        connection.close()
        return({status:'Success',data:room_meta})

    except Exception as e:
        return ({status:'Failed',data:str(e)})


@bp.route("/delete_room", methods=["POST"])
def room_delete():

    try:
        engine, connection = make_conn()
        roomNo=str(request.json["roomNo"])
        query = "DELETE FROM rooms WHERE roomNo = "+roomNo+";"
        connection.execute(query)
        connection.close()
        return({status:'Success',data:{}})

    except Exception as e:
        return ({status:'Failed',data:str(e)})


#----------------representatives ROUTES----------------------#


@bp.route("/get_all_representatives", methods=["GET"])
def get_all_representatives():
    try:  
        engine, connection = make_conn()
        representatives_meta=[]
        query = "SELECT * from representatives ;"
        df = pd.read_sql(query, engine)   #TO FETCH

        if len(df) < 1:    #Empty representatives Data
            connection.close()
            return ({status:'Success',data:[]})
        else:
            for index, rows in df.iterrows():
                obj = {
                    "role": str(rows.role),
                    "rollNo": int(rows.rollNo)
                }
                representatives_meta.append(obj)
            connection.close()
            return ({status:'Success',data:representatives_meta})

    except Exception as e:
        return ({status:'Failed',data:str(e)})

@bp.route("/add_representatives", methods=["POST"])
def add_representatives():
    try:  
            engine, connection = make_conn()
            
            rollNo=str(request.json["rollNo"])
            role=str(request.json["role"])

            query = """\
                        insert into representatives(role,rollNo) values( ? , ? );
                    """
            connection.execute(query,(role,rollNo))   #TO INSERT

            query="select role,rollNo from representatives where role = "+role+" ;"
            df = pd.read_sql(query, engine)    #TO FETCH

            representatives_meta = {}
            for index, rows in df.iterrows():
                    representatives_meta = {
                        "role": str(rows.role),
                        "rollNo": int(rows.rollNo)
                    }
            connection.close()
            return({status:'Success',data:representatives_meta})
    
    except Exception as e:
        return ({status:'Failed',data:str(e)})


@bp.route("/update_representative", methods=["POST"])
def representatives_update():

    try:
        engine, connection = make_conn()
        rollNo=str(request.json["rollNo"])
        role=str(request.json["role"])
        updateString = """\
                        UPDATE rooms SET rollNo = ? WHERE role = ? ;
                    """
        connection.execute(query,(rollNo,role))   #TO UPDATE

        query ="select (role,rollNo) from representatives where role = "+rollNo+" ;"
        df = pd.read_sql(query, engine)

        representatives_meta = {}
        for index, rows in df.iterrows():
            representatives_meta = {
                "role": str(rows.role),
                "rollNo": int(rows.rollNo)
            }

        connection.close()
        return({status:'Success',data:representatives_meta})

    except Exception as e:
        return ({status:'Failed',data:str(e)})


@bp.route("/delete_representative", methods=["POST"])
def representative_delete():
    try:
        engine, connection = make_conn()
        role=str(request.json["role"])
        query = "DELETE FROM representatives WHERE role = ? ;"
        connection.execute(query,(role))
        connection.close()
        return({status:'Success',data:{}})

    except Exception as e:
        return ({status:'Failed',data:str(e)})

