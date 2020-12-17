from flask import Blueprint, jsonify, request
import constants as CONST
import pandas as pd
from helper_function import *

bp = Blueprint("api", __name__)

#----------------boarder ROUTES----------------------#

#boarders Schema : name, boardername, first_name, last_name

@bp.route("/get_all_boarders", methods=["GET"])
def get_boarder():
    try:  
        engine, connection = make_conn()
        boarder_meta=[]
        query = "SELECT * from boarder_details ;"
        df = pd.read_sql(query, engine)   #TO FETCH

        if len(df) < 1:    #Empty boarder Data (No boarders)
            connection.close()
            return ({status:'Success',data:{}})
        else:
            for index, rows in df.iterrows():
                obj = {
                    "boarder_id": rows.boarder_id,
                    "boardername": rows.boardername,
                    "first_name": rows.first_name,
                    "last_name": rows.last_name
                }
                boarder_meta.append(obj)
            connection.close()
            return ({status:'Success',data:boarder_meta})

    except Exception as e:
        return ({status:'Failed',data:e})


@bp.route("/get_boarder", methods=["POST"])
def get_boarder():
    try:  
        engine, connection = make_conn()
        boarder_id = str(request.json["boarder_id"])
        query = "select * from boarder_details where boarder_id = "+boarder_id+" ;"
        df = pd.read_sql(query, engine)   #TO FETCH
        boarder_meta={}
        if len(df) < 1:    #Empty boarder Data (No boarder)
            ({status:'Success',data:{}})
        else:
            for index, rows in df.iterrows():
                boarder_meta = rows
            connection.close()
            return ({status:'Success',data:boarder_meta})

    except Exception as e:
        return ({status:'Failed',data:e})


@bp.route("/add_boarders", methods=["POST"])
def add_profile():
    try:  
            engine, connection = make_conn()
            boardername=str(request.json["boardername"])
            first_name=str(request.json["first_name"])
            last_name=str(request.json["last_name"])
            query="insert into boarder_details(boardername,first_name,last_name) values("+boardername+","+first_name+","+last_name+");"
            connection.execute(query)   #TO INSERT

            query="select boarder_id, boardername, first_name, last_name from boarder_details where boardername = "+boardername+" ;"
            df = pd.read_sql(query, engine)    #TO FETCH

            boarder_meta = {}
            for index, rows in df.iterrows():
                    boarder_meta = {
                        "boarder_id": rows.boarder_id,
                        "boardername": rows.boardername,
                        "first_name": rows.first_name,
                        "last_name": rows.last_name,
                    }
            connection.close()
            return({status:'Success',data:boarder_meta})
    
    except Exception as e:
        return ({status:'Failed',data:e})


@bp.route("/update_boarder", methods=["POST"])
def profile_update():

    try:
        engine, connection = make_conn()
        boarder_id=str(request.json["boarder_id"])
        boardername=str(request.json["boardername"])
        first_name=str(request.json["first_name"])
        last_name=str(request.json["last_name"])
        updateString = "UPDATE boarder_details SET first_name = "+first_name+", last_name = "+last_name+", boardername = "+boardername+" WHERE boarder_id = "+boarder_id+" ;"
        connection.execute(updateString)  #TO UPDATE

        query = "SELECT boarder_id, boardername, first_name, last_name from boarder_details where boarder_id = "+boarder_id+" ;"
        df = pd.read_sql(query, engine)

        boarder_meta = {}
        for index, rows in df.iterrows():
            boarder_meta = {
                "boarder_id": rows.boarder_id,
                "boardername": rows.boardername,
                "first_name": rows.first_name,
                "last_name": rows.last_name
            }

        connection.close()
        return({status:'Success',data:boarder_meta})

    except Exception as e:
        return ({status:'Failed',data:e})
